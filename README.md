# 🚀 Intervu.Ai – AI-Powered Interview Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.0%2B-green.svg)](https://djangoproject.com)
[![HTML](https://img.shields.io/badge/HTML-5.0%2B-61DAFB.svg)](https://html.spec.whatwg.org/)


---

## ✨ Overview

**Intervu.Ai** is a futuristic, AI-powered mock interview platform tailored to help job seekers master their technical and behavioral interview skills. Leveraging cutting-edge technologies like Computer Vision, NLP, and Generative AI, Intervu.Ai delivers an immersive and insightful interview simulation experience with real-time feedback.

---

## 🎥 Demo Video

▶️ **Watch the live demo here**: [Click to Watch](https://drive.google.com/file/d/1BKsurA1Q6tYVkpnISAYqpljf310xBQtc/view?usp=sharing)

---

## 🧠 Core Features

### ✅ Implemented

- 🎤 **Real-Time Feedback** – Instant insights on verbal and non-verbal behavior.
- 🧑‍💼 **Candidate Dashboard** – Track interviews, resumes, and applications.
- 📄 **Resume Management** – Upload, manage, and download your resumes easily.
- 🏢 **Company Applications** – Apply to companies directly from the platform.
- 🕐 **Interview Scheduling** – Choose dates and slots for mock interviews.
- 👁️ **Gaze Tracking** – Eye movement detection using OpenCV.
- 🤖 **AI Questioning** – Auto-generated questions tailored to your resume.

### 🔮 Upcoming Features

- 🧪 **AI Mock Interviews** – Fully automated mock interviews using LLMs.
- 📊 **Performance Analytics** – Get detailed charts and metrics after interviews.
- 📁 **Interview Templates** – Curated questions by role & industry.
- 🤝 **Peer Review System** – Get feedback from other users.
- 🔗 **Job Board Integrations** – Direct links to top hiring platforms.
- 📱 **Mobile App** – iOS and Android support.
- 📈 **Advanced Reporting** – Downloadable reports of interview performance.

---

## 🛠️ Tech Stack

### 🔙 Backend

- **Framework**: Django 4.0+
- **Database**: SQLite (Dev), PostgreSQL (Prod)
- **Authentication**: Django Auth System
- **File Handling**: Django File Storage

### 🌐 Frontend

- **Tech**: HTML5, CSS3, TailwindCSS, JavaScript (ES6+)
- **Icons**: Font Awesome 6.5.1
- **Design**: Mobile-first, responsive layout

### 🤖 AI & ML

- **Computer Vision**: OpenCV for gaze tracking
- **Machine Learning**: TensorFlow / PyTorch
- **Generative AI**: AI-driven question generation
- **Realtime**: Zoom integration for mock calls

### 🧪 Dev Tools

- **Version Control**: Git & GitHub
- **Package Manager**: pip
- **Testing**: Django Test Framework
- **Documentation**: Markdown

---

## ⚙️ Installation

### 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- Git
- Virtual Environment (`venv` recommended)

### 🚀 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/amitmore-007/Hiring-Portal-Main.git
cd intervu-ai

# 2. Create virtual environment
python -m venv venv
# For Windows
venv\Scripts\activate
# For Unix/macOS
source venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser for admin access
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
````

Now visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎮 Usage

### 👤 For Candidates

1. Register or Login
2. Upload your resume and complete your profile
3. Schedule and attend mock interviews
4. Receive real-time feedback and performance suggestions

### 🛠️ For Administrators

1. Access the admin panel via `/admin`
2. Manage candidate and company data
3. Configure interview templates and feedback logic
4. Monitor platform-wide analytics

---

## 🔐 Configuration

### 🌍 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your-api-key
```

### 🛢️ PostgreSQL Production Setup (optional)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'intervuai_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🤝 Contributing

We love collaboration! Here’s how you can help:

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "Add amazing feature"

# 4. Push and open a PR
git push origin feature/amazing-feature
```

### ✨ Coding Standards

* Follow **PEP 8** for Python
* Use meaningful variable & function names
* Include docstrings and comments
* Write tests for all new features

---

## 🙏 Acknowledgements

* 💚 Django and Python Communities
* 👁️ OpenCV team for gaze detection
* 🤖 LLM & NLP Open Source Developers
* 🎨 Font Awesome for iconography
* 🚀 All beta testers and contributors

---

**Made with 💙 by the Intervu.Ai Team**

