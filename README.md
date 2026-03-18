📦 Inventory Management System V1
<div align="center">
https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django&logoColor=white
https://img.shields.io/badge/TailwindCSS-3.x-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white
https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge
A modern, full-stack inventory solution for small to medium businesses
🚀 Live Demo • 📖 Documentation • 🐛 Report Bug • ✨ Request Feature
</div>
✨ Key Features
Table
Feature	Description
📦 Product Management	Add, edit, delete products with detailed information
📊 Real-time Stock Tracking	Monitor inventory levels with automatic low-stock alerts
🏷️ Category Organization	Organize products into customizable categories
📈 Analytics Dashboard	Visual reports on inventory status and trends
🔐 Secure Authentication	Role-based user access control
📱 Responsive Design	Fully mobile-optimized interface
🔔 Smart Notifications	Alerts for stock thresholds and expirations
🛠️ Technology Stack
plain
Copy
Backend:     Django 4.x (Python)
Frontend:    TailwindCSS 3.x + Django Templates
Database:    SQLite (Development) / MySQL (Production)
Authentication: Django Auth System + Sessions
⚡ Quick Start
Prerequisites
Python 3.10 or higher
pip (Python package manager)
Node.js & npm (for TailwindCSS)
Installation Steps
bash
Copy
# 1. Clone the repository
git clone https://github.com/faridi-nayunda/Inventory-Management-System-V1.git
cd Inventory-Management-System-V1

# 2. Create virtual environment & install dependencies
pipenv install
pipenv shell

# 3. Install frontend dependencies
npm install

# 4. Setup database
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver

# 7. Access the application
# Open http://127.0.0.1:8000 in your browser
🖥️ Usage Guide
Login with your superuser credentials at /admin or the main login page
Dashboard - View inventory overview and key metrics
Products - Manage your product catalog
Categories - Organize products into groups
Reports - Generate stock level and transaction reports
📸 Screenshots
Add screenshots of your dashboard, product list, and mobile view here
Table
Dashboard	Product Management	Mobile View
screenshots/dashboard.png	screenshots/products.png	screenshots/mobile.png
🗂️ Project Structure
plain
Copy
Inventory-Management-System-V1/
├── inventory/                 # Main Django app
│   ├── models.py             # Product, Category, Stock models
│   ├── views.py              # Business logic
│   ├── urls.py               # URL routing
│   └── templates/            # HTML templates
├── static/                   # CSS, JS, images
├── templates/                # Base templates
├── manage.py
├── requirements.txt
└── README.md
🔧 Configuration
Environment Variables
Create a .env file in the root directory:
env
Copy
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
Production Setup
Switch to MySQL/PostgreSQL database
Set DEBUG=False
Configure static files with WhiteNoise
Set up proper ALLOWED_HOSTS
🤝 Contributing
Contributions are what make the open source community amazing! Any contributions you make are greatly appreciated.
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 Roadmap
[ ] Multi-warehouse support
[ ] Barcode/QR code integration
[ ] Email notifications for low stock
[ ] REST API for mobile apps
[ ] Advanced analytics with charts
[ ] Multi-language support
📄 License
Distributed under the MIT License. See LICENSE for more information.
👤 Author
Faridi Nayunda
GitHub: @faridi-nayunda
Project Link: https://github.com/faridi-nayunda/Inventory-Management-System-V1
🙏 Acknowledgments
Django Documentation
TailwindCSS
Django-Tailwind
<div align="center">
⭐ Star this repository if you found it helpful! ⭐
</div>
