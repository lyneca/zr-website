# Zero Robotics Website
The Zero Robotics Australia website. Written in Django.

## Dependencies

- [Django](https://djangoproject.com): Python web server
  - `python3 -m pip install django`

## Installation and Testing
    # Clone repo 
    $ git clone https://github.com/lyneca/zr-website/
    $ cd zr-website

    # Switch to development branch
    $ git checkout develop

    # Create database
    $ python3 manage.py migrate

    # Create local database admin
    $ python3 manage.py createsuperuser

    # Run development server
    $ python3 manage.py runserver 0.0.0.0:8000

Navigate to [localhost:8000](https://localhost:8000), and you should see the website.
