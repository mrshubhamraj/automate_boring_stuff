from django.core.management.base import BaseCommand


# Proposed command is python manage.py greeting name
# Proposed output  should  be "Welcome name, Good morning!"

class Command(BaseCommand):
    help = "Gives greetings to user"
    
    # Helps to  get the name from command as keyword argument
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies the user name")
    
    def handle(self, *args, **kwargs):
        
        # Write the logic here
        name = kwargs['name']
        greeting = f'Welcome {name}, Good Morning!'
        # Normal output
        self.stdout.write(greeting) 
        
        # Red output like for error
        self.stderr.write(greeting) 
        
        # Green output like for success
        self.stdout.write(self.style.SUCCESS(greeting)) 
        
        # Yellow output like for warning
        self.stdout.write(self.style.WARNING(greeting)) 
        
        # Red output like for error
        self.stdout.write(self.style.ERROR(greeting)) 