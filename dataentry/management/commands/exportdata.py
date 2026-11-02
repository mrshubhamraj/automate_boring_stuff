import csv
from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import datetime

# Proposed command => python manage.py exportdata model_name
class Command(BaseCommand):
    help = 'Export data from the model to CSV file'
    
    # Accept the arguments
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model Name')
    
    def handle(self, *args, **kwargs):
        # logic goes here
        model_name = kwargs['model_name'].capitalize()
        
        # 1-> Search the model in our apps
        model = None
        for app_config in apps.get_app_configs():
            
            # Try to get the model_name in this app_config's models
            try:
                model = apps.get_model(app_config.label, model_name)
                break  # Stop searching once the model is found
            except LookupError:
                continue # Model not found in this app i.e app_config.label, continue searching in the next app.
        
        if not model:
                    raise CommandError(f'Model "{model_name}" not found in any app, try using correct model name!')
                
        # 2-> Fetch the data from database
        data = model.objects.all()
        
        # 3-> Generate the timestemp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        # 4-> Define the CSV file name/path
        file_path = f'{model_name}_exportedd_data_{timestamp}.csv'
        
        # 5-> Opne the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # writer first write the head which column name in first row
            # Now we are trying to get field names or column names of models that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])
            
            # Write row data now
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS('Data Exported Successfuly!'))