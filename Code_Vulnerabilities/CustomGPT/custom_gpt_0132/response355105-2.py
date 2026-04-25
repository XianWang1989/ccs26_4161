
# myapp/management/commands/collect_static.py

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Collect static files for production'

    def handle(self, *args, **options):
        self.stdout.write("Collecting static files...")
        call_command('collectstatic', '--noinput')
        self.stdout.write(self.style.SUCCESS("Static files collected successfully!"))
