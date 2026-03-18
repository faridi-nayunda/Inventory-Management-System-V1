Inventory Management System








A web-based Inventory Management System built with Django and TailwindCSS, designed to help businesses efficiently track and manage products, stock levels, and transactions.

Table of Contents

Features

Tech Stack

Installation

Usage

Screenshots

Contributing

License

Contact

Features

Add, update, and delete products

Track stock levels in real-time

Manage product categories

Generate inventory reports

Responsive UI with TailwindCSS

User authentication with Django’s built-in system

Tech Stack

Backend: Django

Frontend: TailwindCSS

Database: MySQL

Authentication: Django’s built-in authentication system

Templates: Django Templates with TailwindCSS styling

Installation
Prerequisites

Python 3.10+

Pipenv

Node.js & npm

Steps

Clone the repository:

git clone https://github.com/faridi-nayunda/inventory-management-system-v1.git
cd inventory-management-system

Install dependencies and activate the virtual environment:

pipenv install
pipenv shell

Install TailwindCSS dependencies:

npm install

Apply Django migrations:

python manage.py migrate

Create a superuser (for admin access):

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open your browser at http://127.0.0.1:8000/

Usage

Log in with your admin credentials

Add products and categories, manage stock levels

View reports and filter inventory data

TailwindCSS ensures a modern and responsive interface across devices

Screenshots

(screenshots of my app below)

Dashboard


Add Product


Inventory List


Contributing

Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature-name)

Make your changes

Commit your changes (git commit -m "Add some feature")

Push to your branch (git push origin feature-name)

Open a Pull Request

License

This project is licensed under the MIT License. See the LICENSE
 file for details.
