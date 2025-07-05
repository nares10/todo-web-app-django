# Django Todo App with Authentication

A simple, modern Todo web application built with Django.  
Each user can register, log in, and manage their own personal todo list.  
The UI uses Tailwind CSS for a clean, dark theme.

---

## Features

- User registration, login, and logout
- Each user has their own todo list
- Add new tasks (blank tasks not allowed)
- Toggle tasks as completed/incomplete
- Responsive, dark-themed UI with Tailwind CSS
- Error messages for invalid actions (e.g., blank task, duplicate username, invalid login)

---

## Screenshots

![Home Page](home.png)
![Login Page](login.png)
![Register Page](register.png)

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/<your-username>/<repo-name>.git
cd todo-app-auth
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install django
```

### 4. Apply migrations

```sh
python manage.py migrate
```

### 5. Run the development server

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Project Structure

```
todo-app-auth/
├── todo/                # Django project settings
├── todoapp/             # Main app (models, views, urls, templates)
│   ├── templates/
│   │   └── todoapp/
│   │       ├── home.html
│   │       ├── login.html
│   │       └── register.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── README.md
```

---

## Customization

- **UI**: Edit Tailwind classes in the HTML templates for your own style.
- **Features**: Add more fields (e.g., due date, priority) in `models.py`.

---

## License

This project is licensed under the MIT License.

---

## Credits

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)

---

**Happy coding!**
