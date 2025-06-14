#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)

# For Vercel deployment, expose the WSGI app callable as 'app' and 'handler'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

try:
    # Create the WSGI application callable for Vercel
    app = get_wsgi_application()
    handler = app
except Exception as e:
    # Handle the case where WSGI application creation fails
    app = None
    handler = None
    print(f"Error: {e}")

if __name__ == "__main__":
    main()
