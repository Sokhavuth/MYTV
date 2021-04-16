import os
import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import include, path
from django.utils.crypto import get_random_string
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(
    #(os.environ.get("DEBUG", "") == "1")
    DEBUG= True,
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY=get_random_string(50),
)

import django
django.setup()

urlpatterns = [
    path("", include('mysite.urls')),
]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)