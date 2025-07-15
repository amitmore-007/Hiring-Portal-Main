from flask import Flask, Response, render_template, send_file
import cv2
import mediapipe as mp
import numpy as np
import os

app = Flask(__name__)

# Constants
FACE_LANDMARKS = [4, 152, 263, 33, 287, 57]
EYE_LANDMARKS = [468, 473]
MODEL_POINTS = np.array([
    (0.0, 0.0, 0.0),  # Nose tip
    (0, -63.6, -12.5),  # Chin
    (-43.3, 32.7, -26),  # Left eye outer corner
    (43.3, 32.7, -26),  # Right eye outer corner
    (-28.9, -28.9, -24.1),  # Left mouth corner
    (28.9, -28.9, -24.1)  # Right mouth corner
], dtype="double")
EYE_BALL_CENTERS = {
    "left": np.array([[29.05], [32.7], [-39.5]]),
    "right": np.array([[-29.05], [32.7], [-39.5]])
}

ALPHA = 0.2
smoothed_gaze = None

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5
)

heatmap = None

def low_pass_filter(current_gaze):
    """Apply a low-pass filter to smooth the gaze points."""
    global smoothed_gaze
    if smoothed_gaze is None:
        smoothed_gaze = current_gaze
    else:
        smoothed_gaze = ALPHA * current_gaze + (1 - ALPHA) * smoothed_gaze
    return smoothed_gaze

def relative(landmark, shape):
    """Convert normalized landmarks to image coordinates."""
    return int(landmark.x * shape[1]), int(landmark.y * shape[0])

def relativeT(landmark, shape):
    """Convert normalized landmarks to image coordinates with a third zero coordinate."""
    return (int(landmark.x * shape[1]), int(landmark.y * shape[0]), 0)

def get_image_points(landmarks, frame_shape):
    """Extract 2D image points from facial landmarks."""
    return np.array([relative(landmarks.landmark[i], frame_shape) for i in FACE_LANDMARKS], dtype="double")

def get_image_points1(landmarks, frame_shape):
    """Extract 2D image points with a third zero coordinate."""
    return np.array([relativeT(landmarks.landmark[i], frame_shape) for i in FACE_LANDMARKS], dtype="double")

def gaze(frame, points):
    """Estimate and draw gaze direction on the frame."""
    global heatmap
    # Extract 2D image points
    image_points = get_image_points(points, frame.shape)
    image_points1 = get_image_points1(points, frame.shape)

    # Camera matrix and distortion coefficients
    focal_length = frame.shape[1]
    center = (frame.shape[1] / 2, frame.shape[0] / 2)
    camera_matrix = np.array([[focal_length, 0, center[0]], [0, focal_length, center[1]], [0, 0, 1]], dtype="double")
    dist_coeffs = np.zeros((4, 1))

    # Solve PnP to get rotation and translation vectors
    (success, rotation_vector, translation_vector) = cv2.solvePnP(
        MODEL_POINTS, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE
    )

    if not success:
        return

    # Get pupil positions
    left_pupil = relative(points.landmark[EYE_LANDMARKS[0]], frame.shape)
    right_pupil = relative(points.landmark[EYE_LANDMARKS[1]], frame.shape)

    # Estimate affine transformation
    _, transformation, _ = cv2.estimateAffine3D(image_points1, MODEL_POINTS)
    if transformation is None:
        return

    # Calculate gaze direction
    pupil_world_cord = transformation @ np.array([[left_pupil[0], left_pupil[1], 0, 1]]).T
    S = EYE_BALL_CENTERS["left"] + (pupil_world_cord - EYE_BALL_CENTERS["left"]) * 10

    # Project gaze direction onto the image plane
    (eye_pupil2D, _) = cv2.projectPoints((int(S[0]), int(S[1]), int(S[2])), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
    (head_pose, _) = cv2.projectPoints((int(pupil_world_cord[0]), int(pupil_world_cord[1]), int(40)), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

    # Calculate smoothed gaze direction
    current_gaze = left_pupil + (eye_pupil2D[0][0] - left_pupil) - (head_pose[0][0] - left_pupil)
    smoothed_gaze = low_pass_filter(current_gaze)

    # Draw gaze direction (red line)
    p1 = (int(left_pupil[0]), int(left_pupil[1]))
    p2 = (int(smoothed_gaze[0]), int(smoothed_gaze[1]))
    cv2.line(frame, p1, p2, (0, 0, 255), 2)

    # Update heatmap
    if heatmap is None:
        heatmap = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.float32)
    heatmap[int(smoothed_gaze[1]), int(smoothed_gaze[0])] += 1

def generate_frames():
    """Generate frames for the live video feed."""
    global heatmap
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Process frame for gaze tracking
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            gaze(frame, results.multi_face_landmarks[0])

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Stream the live video feed."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/generate_heatmap')
def generate_heatmap():
    """Generate and download the heatmap."""
    global heatmap
    if heatmap is not None:
        # Generate heatmap
        heatmap_blur = cv2.GaussianBlur(heatmap, (15, 15), 0)
        heatmap_norm = cv2.normalize(heatmap_blur, None, 0, 255, cv2.NORM_MINMAX)
        heatmap_color = cv2.applyColorMap(np.uint8(heatmap_norm), cv2.COLORMAP_JET)

        # Save heatmap to a temporary file
        heatmap_path = "static/heatmap_temp.jpg"
        cv2.imwrite(heatmap_path, heatmap_color)

        # Reset heatmap for the next session
        heatmap = None

        return send_file(heatmap_path, mimetype='image/jpeg', as_attachment=True, download_name="heatmap.jpg")
    else:
        return "Heatmap not available", 400

if __name__ == '__main__':
    app.run(debug=True)