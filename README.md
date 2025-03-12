# Django Blog Project

A full-featured blog built with Django, MySQL, and Bootstrap.

## Features

- User authentication and authorization
- Create, read, update, and delete blog posts
- Comment system
- Responsive design using Bootstrap

## Technology Stack

- **Backend**: Django
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap
- **Version Control**: Git


## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blog-project.git
cd blog-project
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Update database configuration in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Project Structure

```
Rock_blog/
│
├──Rock_blog/
│   ├── base/                       # Core/Base App
│   │   ├── templates/              # Base app Templates
│   │   │   └── base/
│   │   │       ├── base.html       # Base template
│   │   │       ├── index.html      # Homepage
│   │   │       ├── login.html      # Login page
│   │   │       └── signup.html     # Sign up page
│   │   ├── admin.py                # Model Registration
│   │   ├── apps.py 
│   │   ├── forms.py                # Form definitions
│   │   ├── models.py               # Database Models
│   │   ├── test.py                 # Unit Tests
│   │   ├── urls.py                 # URL Configurations
│   │   └── views.py                # View Functions
│   │
|   ├── blog/                       # Blog App
│   │   ├── templates/              # Blog app template
│   │   │   └── blog/
│   │   │       ├── create.html     # New Blog template
│   │   │       └── update.html     # Update Blog template
│   │   ├── admin.py                # Model Registration
│   │   ├── apps.py                 
│   │   ├── forms.py                # Form definitions
│   │   ├── models.py               # Database Model
│   │   ├── tests.py                # Unit tests
│   │   ├── urls.py                 # URL configurations
│   │   └── views.py                # View Functions
│   │
|   ├── commenting/                 # Comment App
│   │   ├── templates/              # Comment app template
│   │   │   └── commenting/
│   │   │       ├── detail.html     # Blog Detail Page
│   │   │       └── reply.html      # Reply template
│   │   ├── admin.py                # Model Registration
│   │   ├── apps.py          
│   │   ├── forms.py                # Form definitions
│   │   ├── models.py               # Database model 
│   │   ├── tests.py                # Unit Tests
│   │   ├── urls.py                 # URL configurations
│   │   └── views.py                # View functions
│   │
│   ├── Rock_blog/
│   │   ├── asgi.py                 # ASGI configurations
│   │   ├── settings.py             # Project Settings
│   │   ├── urls.py                 # Project urls
│   │   └── wsgi.py                 # WSGI configurations
│   │
│   ├── static/                     # Static Files
│   │   └── css/                    # CSS Files
│   │       └── style.css           # Styling template
│   │
│   ├── UPLOADED_IMG/               # Image Files
│   │   └── images                  
│   │
│   └── manage.py                   # Django management script
│
├── .gitignore                      # Git Ignore File           
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## Deployment

### Production Settings

1. Update `settings.py` for production:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Set up proper static file serving
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

2. Configure a production web server (Nginx, Apache) with WSGI (Gunicorn, uWSGI).

3. Set up proper database backup procedures.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgements

- Django Documentation
- Bootstrap
- MySQL Documentation