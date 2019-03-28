"""
- Creates the admin user when openwisp2 is installed
- Additionally creates the default organization if no organization is present
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openwisp2.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
changed = False

if User.objects.filter(is_superuser=True).count() < 1:
    admin = User.objects.create_superuser(username='admin',
                                          password='admin',
                                          email='')
    print('superuser created')
