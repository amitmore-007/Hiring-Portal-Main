# InsightHire - AI-Powered Interview Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.0%2B-green.svg)](https://djangoproject.com)
[![Html](https://img.shields.io/badge/Html-5.0%2B-61DAFB.svg)](https://html.org)

## 🚀 Overview

InsightHire is an innovative AI-powered mock interview platform designed to help job seekers prepare for technical and behavioral interviews. The platform leverages advanced AI technologies including computer vision, natural language processing, and machine learning to provide comprehensive interview preparation and feedback.

## ✨ Features

### 🎯 Core Features (Implemented)

- **Real-time Feedback**: Instant analysis of verbal and non-verbal communication
- **Candidate Dashboard**: Comprehensive user interface for interview management
- **Resume Management**: Upload, manage, and download resume functionality
- **Company Applications**: Apply to various companies directly through the platform
- **Interview Scheduling**: Schedule and manage upcoming interviews
- **Gaze Tracking**: Eye movement analysis during interviews using computer vision
- **AI Integration**: Advanced AI questioning and evaluation system

### 🔮 Future Features 
- **AI Mock Interviews**: Interactive mock interview sessions with AI-powered questioning
- **Performance Analytics**: Detailed performance metrics and improvement suggestions
- **Interview Templates**: Industry-specific interview question sets
- **Peer Review System**: Community-based feedback and review system
- **Integration with Job Boards**: Direct connection to popular job platforms
- **Mobile Application**: iOS and Android companion apps
- **Advanced Reporting**: Comprehensive interview performance reports


## 🛠️ Technology Stack

### Backend
- **Framework**: Django 4.0+
- **Database**: SQLite (development) 
- **Authentication**: Django Authentication System
- **File Storage**: Django File Storage

### Frontend
- **Framework**: HTML5, CSS3, Tailwind, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Variables
- **Icons**: Font Awesome 6.5.1
- **Responsive Design**: Mobile-first approach

### AI & Machine Learning
- **Computer Vision**: OpenCV for gaze tracking
- **Machine Learning**: TensorFlow/PyTorch for model training
- **Generative AI**: Generative AI for question generation
- **Real-time Processing**: Zoom Integration for meetings

### Development Tools
- **Version Control**: Git
- **Package Management**: pip
- **Testing**: Django Test Framework
- **Documentation**: Markdown

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 14+ (for frontend development)
- Git
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aimockinterview2.git
   cd aimockinterview2
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: `http://127.0.0.1:8000/`



## 🎮 Usage

### For Candidates
1. **Register/Login**: Create an account or log in to existing account
2. **Complete Profile**: Upload resume and complete profile information
3. **Schedule Interview**: Select company and schedule mock interview

### For Administrators
1. **Access Admin Panel**: Login to Django admin interface
2. **Manage Users**: Add, edit, or remove candidate profiles
3. **Configure Companies**: Set up company-specific interview questions
4. **Monitor Performance**: View system analytics and user statistics

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1

GROQ_API_KEY=your-api-key


```

### Database Configuration
For production, update `settings.py` to use PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insighthire_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```


## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Write unit tests for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Django and React communities for excellent documentation
- OpenCV team for computer vision capabilities
- Font Awesome for beautiful icons
- All contributors and beta testers

## 📞 Support

For support, please contact:
- Email: support@insighthire.com
- GitHub Issues: [Create an issue](https://github.com/yourusername/aimockinterview2/issues)
- Documentation: [Wiki](https://github.com/yourusername/aimockinterview2/wiki)



**Made with ❤️ by the InsightHire Team**
