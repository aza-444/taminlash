# TPP.uz Clone - Issiqlik Elektr Stantsiyalari

## Project Overview
A complete Django-based clone of tpp.uz (Thermal Power Plants JSC of Uzbekistan) website featuring all major sections and functionality.

## Recent Changes
- **November 13, 2024**: Initial project setup with Django 4.2.7
- Models created for News, PowerPlants, Contact, Core sections
- Admin panel configured with all models
- Multi-language support structure prepared (Uzbek, Russian, English)
- Sample data management command implemented
- Responsive templates with Bootstrap 5, Swiper.js, AOS animations
- Homepage with carousel, quick links, news, statistics
- Press center with news listing and detail pages
- Electronic reception contact form
- Online survey system
- Company history page

## Features
### Homepage
- Hero carousel slider with 4 slides
- Quick links section (6 cards)
- Press center preview
- Key indicators statistics (4 animated cards)
- Company history preview
- Government websites carousel
- Helpline statistics display

### Press Center
- News listing with pagination
- News detail pages with view counter
- Category filtering
- Related news suggestions

### Contact System
- Electronic reception form
- Survey system with multi-step forms
- Contact message management in admin

### Admin Panel
- Full CRUD for all models
- Rich text editor (CKEditor) for content
- Image upload support
- User-friendly interfaces

## Project Architecture
### Django Apps
- **core**: Homepage, quick links, carousel, government links, company history
- **news**: News articles, categories, videos, press center
- **powerplants**: Power plants information, key indicators, map data
- **contact**: Contact messages, surveys, helpline statistics

### Technology Stack
- **Backend**: Django 4.2.7, Python 3.11
- **Database**: SQLite (development), PostgreSQL-ready
- **Frontend**: Bootstrap 5, Swiper.js, Leaflet.js, AOS animations
- **Rich Text**: CKEditor
- **Server**: Gunicorn (production-ready)

### File Structure
```
├── core/               # Core app (homepage, history)
├── news/               # News & press center
├── powerplants/        # Power plants data
├── contact/            # Contact forms & surveys
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # User uploaded files
└── tpp_project/        # Django settings
```

## User Preferences
- Language: Uzbek (primary), with Russian and English support structure
- Design: Modern, clean, responsive matching tpp.uz style
- Framework: Django with class-based and function-based views

## Development Commands
```bash
# Create sample data
python manage.py create_sample_data

# Run development server (auto-configured in workflow)
python manage.py runserver 0.0.0.0:5000

# Access admin panel
# URL: /admin/
# Create superuser: python manage.py createsuperuser

# Database migrations
python manage.py makemigrations
python manage.py migrate
```

## Next Steps
- Add real images for carousel, news, power plants
- Implement interactive map with Leaflet.js
- Add more sample news articles
- Configure multi-language translation (django-modeltranslation)
- Add search functionality
- Implement email notifications for contact form
- Add PDF export for reports
- Deploy to production

## Notes
- Workflow auto-runs Django server on port 5000
- Admin panel accessible at /admin/
- Multi-language support prepared but needs translation data entry
- All models support image uploads through admin panel
