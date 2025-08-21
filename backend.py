import os
from django.http import HttpResponse
import sys
import numpy as np

# It's assumed you are using TensorFlow/Keras. If not, adjust the model loading.
try:
    import tensorflow as tf
except ImportError:
    print("TensorFlow not found. Please install it using: pip install tensorflow")
    sys.exit(1)

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.wsgi import get_wsgi_application

# 1. Minimal Django Settings Configuration
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='a-secret-key-for-development-change-me',
        ROOT_URLCONF=__name__,  # This file will act as the URLconf
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                # Tell Django to look for templates in a 'templates' subdirectory
                'DIRS': [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')],
                'APP_DIRS': True,
            },
        ],
    )

# 2. Model Loading
# Place your trained model file (e.g., 'ppe_model.h5') in the same directory as this script.
MODEL_PATH = 'ppe_model.h5'  # <-- IMPORTANT: Update this to your model's filename
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print(f"Model '{MODEL_PATH}' loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("The application will run, but predictions will fail.")
else:
    print(f"Model file not found at '{MODEL_PATH}'.")
    print("Please place your model file in the same directory as this script.")

# 3. Views (Application Logic)

# View to render the main HTML page
def index(request):
    with open(os.path.join(os.path.dirname(__file__), 'frontend.html'), encoding='utf-8') as f:
        return HttpResponse(f.read())


# 4. URL Patterns
urlpatterns = [
    path('', index, name='index'),
]

# 5. WSGI Application for deployment
application = get_wsgi_application()

# 6. Main execution block to run the development server
if __name__ == "__main__":
    # Allows running the server with `python backend.py runserver`
    execute_from_command_line(sys.argv)