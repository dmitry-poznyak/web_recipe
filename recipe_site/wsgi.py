import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_site.settings')
django.setup()


from django.core.management import call_command
call_command('migrate', interactive=False)

application = get_wsgi_application()