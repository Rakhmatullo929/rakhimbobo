# Dry Fruta - Premium Dried Fruits Website

A beautiful, modern website for a dried fruits company built with Django. Features a stunning interface with vantajs fog animation and premium design elements.

## Features

- Responsive design using Bootstrap 5
- Beautiful fog animation using vantajs library
- Dynamic content management through Django admin
- Pages for home, articles and news, partners, leadership, and contacts
- Contact form for customer inquiries
- Fully customizable content through the admin panel

## Screenshots

(Add screenshots when available)

## Technologies Used

- Django 4.2.9 - Python web framework
- Bootstrap 5 - Frontend component library
- VantaJS - 3D animated backgrounds
- Font Awesome - Icon library
- Google Fonts - Web fonts
- AOS - Animate On Scroll library

## Main Color Scheme

The website uses a refreshing green color theme based on:
- Primary color: `#70ae54`

## Project Structure

- `core/` - Main Django app containing models, views, and forms
- `config/` - Project settings and configuration
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded content

## Setup and Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/dry-fruta.git
cd dry-fruta
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Create a superuser:
```
python manage.py createsuperuser
```

6. Start the development server:
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser to view the site
8. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage content

## Content Management

The website allows management of:
- Articles
- News
- Partners
- Team Members
- Contact Information

All content can be managed through the Django admin panel.

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a Pull Request

## Requirements

See `requirements.txt` for the complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Unsplash for placeholder images
- VantaJS for the beautiful fog animation # rakhimbobo
