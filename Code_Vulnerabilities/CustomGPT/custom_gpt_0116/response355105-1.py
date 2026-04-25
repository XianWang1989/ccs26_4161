
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Checks and applies migrations'

    def handle(self, *args, **kwargs):
        from django.core.management import call_command
        call_command('makemigrations')
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Successfully checked and applied migrations'))
