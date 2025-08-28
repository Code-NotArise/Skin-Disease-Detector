# Skin Disease Detector

## Project Overview
Skin Disease Detector is a Django-based web application that uses machine learning to help users identify various skin conditions. The application integrates with Roboflow's AI model to provide predictions on uploaded skin images, offering users insights into potential skin diseases with confidence scores.

## 🎯 Key Features
- **User Authentication**: Secure registration, login, and logout functionality
- **Image Upload**: Easy upload interface for skin condition images
- **AI-Powered Prediction**: Integration with Roboflow machine learning model
- **Disease Information**: Detailed medical information for each detected condition
- **User Profiles**: Personal profile management with profile pictures
- **Prediction History**: Track all previous predictions with timestamps
- **Responsive Design**: Clean, user-friendly interface

## 🦠 Detection Capabilities
The application can detect the following skin diseases:

| Disease | Description | Confidence Threshold |
|---------|-------------|---------------------|
| **Chickenpox** | Varicella-zoster virus infection with itchy rash and blisters | 2.2%+ |
| **Cowpox** | Animal-transmitted viral infection with pustular lesions | 2.0%+ |
| **HFMD** | Hand, Foot and Mouth Disease caused by coxsackievirus | 2.7%+ |
| **Healthy** | Normal skin with no detectable disease | 90.7%+ |
| **Measles** | Viral infection with fever, cough, and rash | 1.7%+ |
| **Monkeypox** | Viral infection transmitted through close contact | 1.8%+ |
| **Mpox** | Alternate name for Monkeypox | 2.7%+ |

*Note: Confidence scores are based on sample predictions and may vary*

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL Server 5.7+ or MySQL 8.0+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd skin-disease-detector
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration:
   # - Set your SECRET_KEY
   # - Configure database credentials
   # - Add your Roboflow API key
   ```

5. **Database Setup**
   - Create a MySQL database (default: `skin_db`)
   ```bash
   CREATE DATABASE skin_db;
   ```
   - Update database credentials in `skindetector/settings.py` file

6. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

9. **Access Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📖 Usage Guide

### For New Users
1. **Register**: Click "Register" to create a new account
2. **Login**: Use your credentials to access the application
3. **Upload Image**: Navigate to the upload page and select a skin image
4. **View Results**: See prediction results with confidence scores
5. **Explore Details**: Click on disease names for detailed information

### For Returning Users
1. **Login** with existing credentials
2. **Check History**: View your prediction history in the profile section
3. **Update Profile**: Edit your personal information and profile picture
4. **Make New Predictions**: Continue uploading images for analysis

## 🏗️ Project Structure

```
skin-disease-detector/
│
├── detection/                 # Main application
│   ├── migrations/           # Database schema migrations
│   ├── static/              # CSS, JavaScript, and images
│   ├── templates/           # HTML templates
│   ├── templatetags/        # Custom template filters
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── disease_data.py     # Medical information database
│   ├── forms.py           # User input forms
│   ├── models.py          # Database models
│   ├── signals.py         # Automated profile creation
│   ├── tests.py           # Unit tests
│   ├── urls.py           # URL routing
│   └── views.py          # Business logic
│
├── media/                  # User-uploaded files (excluded from git)
│   ├── profile_pics/      # User profile pictures
│   └── uploads/           # Skin images for prediction
│
├── skindetector/          # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL routes
│   └── wsgi.py
│
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── README.md            # This documentation
├── .gitignore           # Git ignore rules
├── .env.example         # Environment variables template
└── LICENSE              # MIT License
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file based on `.env.example`:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration
DB_NAME=skin_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306

# Roboflow API
ROBOFLOW_API_KEY=your-roboflow-api-key
```

### Database Setup
1. Install MySQL and create a database
2. Update the `.env` file with your database credentials
3. Run migrations: `python manage.py migrate`

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 📊 Sample Data

The application includes comprehensive disease information in `detection/disease_data.py` with:
- Causes and transmission methods
- Common symptoms
- Recommended medications
- Patient care instructions

## ⚠️ Important Notes

1. **Medical Disclaimer**: This is a prototype application for educational purposes only. Always consult healthcare professionals for medical diagnoses.

2. **API Key**: You need to obtain your own Roboflow API key for the application to work.

3. **Database**: Requires MySQL. Ensure the database server is running before starting the application.

4. **File Storage**: Media files are stored locally and excluded from git.

5. **Security**: Uses environment variables for sensitive data. Never commit `.env` files to version control.

## 🚀 Deployment Considerations

For production deployment:
1. Set `DEBUG = False` in environment variables
2. Use a proper web server (nginx + gunicorn)
3. Configure a production database
4. Set up proper static file serving
5. Use environment variables for all sensitive data
6. Implement SSL/TLS encryption
7. Set up proper backup procedures

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions or issues:
- Check the existing documentation
- Review the code comments
- Create an issue in the repository
- Contact the development team

---

**Remember**: This application is a prototype designed for educational and demonstration purposes. It should not be used for actual medical diagnosis without proper validation and clinical oversight.

### Made By Arslan Sajjad as a College Project.

## Contact
For questions or support, please contact the project maintainer at: [arslansajjad548@gmail.com]
