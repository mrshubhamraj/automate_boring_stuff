from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "print hello world"
    
    def handle(self, *args, **kwargs):
        # We write logic here
        self.stdout.write('Hello World')