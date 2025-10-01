# NikJin CRUD Application

A comprehensive Django-based CRUD (Create, Read, Update, Delete) application with user management, task tracking, and project management features.

## Features

### 🔐 Authentication & User Management
- User registration and login
- User profiles with profile pictures
- User dashboard with statistics
- User search and filtering

### 📋 Task Management
- Create, read, update, and delete tasks
- Task priority levels (High, Medium, Low)
- Task status tracking (Pending, In Progress, Completed)
- Task assignment to users
- Due date management
- Search and filter tasks

### 🚀 Project Management
- Create and manage projects
- Assign team members to projects
- Project status tracking
- Project deadlines
- Manager and member roles

### 🎨 Modern UI/UX
- Responsive Bootstrap 5 design
- Clean and intuitive interface
- Interactive dashboard with statistics
- Mobile-friendly design
- Font Awesome icons

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (default, easily configurable)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Icons**: Font Awesome 6

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 4: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage

### Getting Started
1. **Register**: Create a new account or login with existing credentials
2. **Dashboard**: View your personalized dashboard with statistics
3. **Users**: Browse and manage users in the system
4. **Tasks**: Create, assign, and track tasks
5. **Projects**: Manage projects and team assignments

### Key URLs
- `/` - Dashboard (requires login)
- `/login/` - User login
- `/register/` - User registration
- `/users/` - User management
- `/tasks/` - Task management
- `/projects/` - Project management
- `/profile/` - User profile management
- `/admin/` - Django admin interface

## Project Structure

```
nikjin/
├── nikjin_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Main settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── main_app/               # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin configuration
│   ├── signals.py          # Django signals
│   └── tests.py            # Unit tests
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── dashboard.html      # Dashboard
│   ├── registration/       # Auth templates
│   ├── users/              # User templates
│   ├── tasks/              # Task templates
│   └── projects/           # Project templates
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── js/
│       └── main.js         # JavaScript functionality
├── media/                  # User uploads
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
└── README.md              # This file
```

## Models

### UserProfile
- Extends Django's User model
- Profile picture, phone, address
- Automatic creation via signals

### Task
- Title, description, priority, status
- Assignment and creation tracking
- Due date management

### Project
- Name, description, manager
- Team member assignments
- Deadline and status tracking

## Features in Detail

### Dashboard
- User statistics overview
- Recent tasks and projects
- Quick action buttons
- Responsive card layout

### User Management
- User listing with search
- Detailed user profiles
- Task and project associations
- Profile picture support

### Task Management
- Full CRUD operations
- Priority and status filtering
- User assignment
- Due date tracking
- Pagination support

### Project Management
- Team-based project organization
- Manager and member roles
- Project timeline tracking
- Task associations

## Customization

### Styling
- Modify `static/css/style.css` for custom styles
- Bootstrap 5 variables can be overridden
- Responsive design principles followed

### Functionality
- Extend models in `main_app/models.py`
- Add new views in `main_app/views.py`
- Create custom forms in `main_app/forms.py`

## Testing

Run the test suite:
```bash
python manage.py test
```

## Deployment

### Production Settings
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Configure static file serving
5. Set up environment variables for sensitive data

### Environment Variables
Create a `.env` file for production:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=your-database-url
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please create an issue in the repository or contact the development team.

---

**Built with ❤️ using Django and Bootstrap**
