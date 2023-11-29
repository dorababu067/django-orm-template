import os
import sys

# Set the path to your custom settings module
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set the DJANGO_SETTINGS_MODULE environment variable to the custom path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Import Django after setting the environment variable
import django

django.setup()
