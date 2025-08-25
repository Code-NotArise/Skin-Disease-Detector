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

<<<<<<< HEAD
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

4. **Database Setup**
   - Create a MySQL database named `skin_db`
   - Update database credentials in `skindetector/settings.py` if needed:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'skin_db',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply Migrations**
=======
### Cloning Repository
   ```bash
   git clone https://github.com/arslan548/Skin_detector.git
   cd Skin_detector
   ```

### Database setup
1. Go to the MySql site (https://dev.mysql.com/downloads/installer/) and download the installer. Make sure to download the full setup:
![image](https://github.com/user-attachments/assets/8eb80d79-1f24-4be2-a2b3-ff51a2839cb6)

2. Then install the MySql

3. You will create a username (By default its "root") and a password during installation make sure to remember that.

4. After installation go to the folder "skindetector" in the repository you just cloned.

5. Now open settings.py in it and go to line 94, 95 and enter you usernaame and password.

6. Open terminal and give command:
   ```bash
   mysql -u root -p
   ```
   
7. Enter your Mysql password.

8. Now enter this:
   ```MySql
   CREATE DATABASE skin_db;
   ```
   
9. Database setup complete.

### Installation Steps
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Apply database migrations:
>>>>>>> 152d82eb01739cd35909ff407e8738c7c933e519
   ```bash
   python manage.py migrate
   ```

<<<<<<< HEAD
6. **Create Superuser (Optional)**
=======
4. Create a superuser (optional, for admin access):
>>>>>>> 152d82eb01739cd35909ff407e8738c7c933e519
   ```bash
   python manage.py createsuperuser
   ```

<<<<<<< HEAD
7. **Run Development Server**
=======
5. Run the development server:
>>>>>>> 152d82eb01739cd35909ff407e8738c7c933e519
   ```bash
   python manage.py runserver
   ```

<<<<<<< HEAD
8. **Access Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`
=======
6. Access the application at `http://127.0.0.1:8000/`
>>>>>>> 152d82eb01739cd35909ff407e8738c7c933e519

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
├── media/                  # User-uploaded files
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
├── roboflow_response.json    # Sample prediction response
└── roboflow_first_prediction.json # Initial prediction sample
```

## 🔧 Technical Details

### Models
- **Profile**: Extends Django User model with profile picture support
- **SkinImage**: Stores uploaded skin images with metadata
- **SkinPrediction**: Records prediction results with confidence scores

### API Integration
- **Roboflow API**: Used for machine learning predictions
- **API Key**: Configured in `detection/views.py` (replace with your own key)
- **Model**: "poxclassification" version 1

### Security Features
- Password hashing and validation
- CSRF protection
- User authentication requirements
- Secure file upload handling

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

2. **API Key**: The current Roboflow API key is for demonstration. Replace it with your own key for production use.

3. **Database**: Requires MySQL. Ensure the database server is running before starting the application.

4. **File Storage**: Media files are stored locally. Consider cloud storage for production deployments.

5. **Security**: Change the SECRET_KEY in production and set DEBUG=False.

## 🚀 Deployment Considerations

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Use a proper web server (nginx + gunicorn)
3. Configure a production database
4. Set up proper static file serving
5. Use environment variables for sensitive data
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

<<<<<<< HEAD
## 📞 Support

For questions or issues:
- Check the existing documentation
- Review the code comments
- Create an issue in the repository
- Contact the development team

---

**Remember**: This application is a prototype designed for educational and demonstration purposes. It should not be used for actual medical diagnosis without proper validation and clinical oversight.
=======
## Contact
For questions or support, please contact the project maintainer at: [arslansajjad548@gmail.com]

---

# Additional Notes
- The project uses Roboflow API for skin disease prediction.
- Media files are stored in the `media/` directory.
- User authentication is handled by Django's built-in auth system.
### Made By Arslan Sajjad as a Collage Project. 
>>>>>>> 152d82eb01739cd35909ff407e8738c7c933e519
#   S k i n D i s e a s e D e t e c t o r  
 