# **QuickCart**

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Setup](#setup)
- [Cloning the Repository](#cloning-the-repository)
- [Contributors](#contributors)

# **Introduction**
🚀 **QuickCart**: A Minimal E-commerce Platform
QuickCart is a lightweight, responsive e-commerce application designed to deliver a seamless shopping experience. Built with Django and HTML5, Tailwind CSS and Vanila Javascript it offers intuitive navigation, a clean interface, and modern design components.
Whether you're browsing through products, adding items to your cart, or searching for specific products, QuickCart delivers efficiency and simplicity at every step.


---
# **Prerequisites**
- Backend: Django (Python)
- Frontend: HTML5, Tailwind CSS, Javascript
- Database: SQLite (default)
- Git: Version control system to manage your codebase.

 

# **Features**
- Product Management
  - Display products with images, names, descriptions, and prices.
  - Categorize products for organized browsing.
      
- Search Functionality
  - Search for products by name or description.
  - Supports partial matches for product names and delivers accurate results.
    
- Add to Cart
  - Easily add products to the cart with a user-friendly Add to Cart button.
  - Display cart items with their details like name, price, and quantity.
    
- Stay Inspired on the Home Page
  - Scroll through your friends' posts to stay updated.
  - Easily search for and connect with new travelers.
    
- Responsive Design
  - Fully responsive with Tailwind CSS, ensuring seamless usage across mobile, tablet, and desktop devices.
  - Dynamic grid layout adapts to the screen size for an optimal experience.
  - Buttons and input fields styled to match modern design trends.
  - Features smooth transitions and hover effects for better user engagement.

# **Setup**

## Cloning the Repository

1. Open a terminal and clone the repository using Git:

```
git clone https://github.com/ShouravRakshit/Django-EcommerceShop.git
```

2. Navigate to the cloned repository:

```
cd Django-EcommerceShop
```
3. Create a virtual environment:

```
python -m venv .venv
```
4. Windows:

```
.venv\Scripts\activate
```

5. Mac/Linux:

```
source .venv/Scripts/activate
```

6. Install dependencies::

```
pip install -r requirements.txt

```

7. Navigate to the ecommercesite folder:

```
cd ecommercesite
```

8. Install Node.js Dependencies
```
npm install
```
9. Run Tailwind CSS Build
```
npm run watch:css
```
10. Load the dataset
```
python manage.py loaddata data.json
```
11. Run the Development Server
```
python manage.py makemigrations
python manage.py migrate # Apply database migrations
python manage.py runserver
```


# **Contributors**
- Shourav Rakshit Ivan, Email: shouravrakshit.ivan@ucalgary.ca 
University of Calgary
