
# SEANEMA (SEA Cinema Movie Ticket Booking App)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![DaisyUI](https://img.shields.io/badge/daisyui-5A0EF8?style=for-the-badge&logo=daisyui&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)


A movie ticket booking app that allows users to effortlessly browse through a collection of movies, select showtimes, choose seats, and secure reservations in seconds. The app also features a user balance functionality for cashless transactions.


## Installation and Run the project

Clone the project repository:

```bash
  git clone https://github.com/your-username/sea-cinema.git
```

Navigate to the project directory:

```bash
  cd sea-cinema
```

Database migration

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the Django development server:

```bash
  python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/`
## Tech Stack

**Backend:** Django, Django REST Framework

**Frontend:** HTML, CSS, JavaScript

**Styling:** Tailwind CSS, DaisyUI

**Database:** PostgreSQL


## Features

- View movies: Users can see a collection of movies with details such as title, description, age rating, and ticket price.
- Ticket booking: Users can select available seats and make payments using their balance.
- User balance management: Users can top up and withdraw their balance, and view their transaction history.
- Authentication and authorization: Users can register, login, and logout. Only logged-in users can perform certain actions and access personalized features.
- Cancel ticket transactions: Logged-in users can cancel their own ticket transactions and receive refunds.


