# BLOG-BACKEND-SYSTEM

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: MOHIT DAMLE

*INTERN ID*: CT12WSJC

*DOMAIN*: BACKEND WEB DEVELOPMENT

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH

## Description

The "BLOG BACKEND SYSTEM" is a developer blog and portfolio website built using Django, MySQL, and CSS. It includes several pages such as Home, Login, Signup, Blog, and Categories. The project features a clean and modern design that is fully responsive for any device and optimized for performance. It includes a powerful admin interface for managing the content and is easy to customize and deploy to a production environment.

## Table of Content
  * [Description](#description)
  * [Core Features](#core-features)
  * [Output/Website Screenshots](#output/website-screenshots)
  * [Pages](#pages)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployment](#deployment)

## Core Features

- **Post Creation and Management**:
    - Users (typically administrators) can create new blog posts with titles, content, and publication dates.
    - Django's models define the structure of the posts in the MySQL database.
    - The Django admin interface provides a user-friendly way to create, edit, and delete posts.

- **Post Display**:
    - Blog posts are displayed on the website, typically in a list or grid format.
    - Django's templates allow for flexible presentation of the post content.
    - Views handle the logic of retrieving posts from the database and passing them to the templates.

- **Database Integration (MySQL)**:
    - MySQL stores the blog's data, including posts, users, and comments.
    - Django's Object-Relational Mapper (ORM) simplifies database interactions, allowing you to work with Python objects instead of raw SQL queries.
    - This makes it easy to create, read, update, and delete data.

- **User Authentication**:
    - Django's built-in authentication system enables user registration, login, and logout.
    - This is essential for controlling who can create and manage blog posts.

- **Comments**:
    - Users can leave comments on blog posts.
    - Comments are stored in the MySQL database and associated with the corresponding posts.
    - Django's forms can be used to handle comment submission.

- **Admin Interface**:
    - Django's admin interface provides a powerful and customizable way to manage the blog's content and users.
    - This includes features for creating, editing, and deleting posts, managing users, and more.

- **URL Routing**:
    - Django's URL routing system maps URLs to specific views, allowing for clean and organized website structure.
    - This allows for urls such as /posts/1, for the first post, and /categories/django, for all posts in the django category.

## Output/Website Screenshot

![Image](https://github.com/user-attachments/assets/7164d97b-60a4-44c3-a03a-db93af16ea32)

![Image](https://github.com/user-attachments/assets/2bf8c708-957e-47aa-96b3-28d6e038f9c6)

![Image](https://github.com/user-attachments/assets/1220d693-f10b-4c78-abb9-3d1b250a926e)

![Image](https://github.com/user-attachments/assets/9d650f20-bf52-4d84-aa79-2daa8c84fda1)

## Pages
- `Home`: The Homepage of the website, which displays a list of blog posts with links to individual post pages and links to other pages.
- `Signup`: A page that takes your details and let you register to become user of this website.
- `Login`: A custom login page that provides proper authentication and authorization.
- `Blog Detail`: A page that displays the content of a single blog post, including the title, author, date, image, content and provides a interactive comment section.

## Technologies used

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