from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
import csv
# importing all the apps
from django.apps import apps

# Proposed command - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = 'To Import Data From A CSV File'
    
    # To Handle the python manage.py importdata file_path model_name  --arguments
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Specifies File Path')
        parser.add_argument('model_name', type=str, help='Specifies Model to Executed')
    
    def handle(self, *args, **kwargs):
        # Logic goes here
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()  # As model name is always capitalised 'Student'
        
        model = None
        # Search for model across all installed apps
        for app_config in apps.get_app_configs():
            
            # Try to search the model required in this app_config's models
            try:
                model = apps.get_model(app_config.label, model_name)
                break  # Stop searching once the model is found
            except LookupError:
                continue  # Model not found in this app i.e app_config.label, continue searching in the next app.
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app, try using correct model name!')
        
        # Now lets read the csv file
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                # Now iterate through the file to fetch each record
                for row in reader:
                    
                    # This adds each student data to database
                    model.objects.create(**row)  # **row --> makes it easy to get all column name in one go instead of writting each one.
        
        # Handles if file is not found i.e file_path is wrong
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
          
        # Handles errors if data inside the csv file not correct according to the model    
        except csv.Error as e:
            self.stderr.write(self.style.ERROR(f"CSV error: {e}"))  
         
        # Handles any other errors   
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Something went wrong: {e}"))  
        
        # This executes when there are no errors   
        else :         
            self.stdout.write(self.style.SUCCESS('Successfully Imported!'))