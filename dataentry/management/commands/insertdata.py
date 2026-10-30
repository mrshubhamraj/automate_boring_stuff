from django.core.management.base import BaseCommand
from dataentry.models import Student

# I want to add some data to the database using custom command.

class Command(BaseCommand):
    help = 'It will insert data to the database'
    
    def handle(self, *args, **kwargs):
        # Logic goes here
        
        # Inserting multiple data
        dataset = [
            {'roll_no' : 1002, 'name' : 'Raj', 'age' : 25},
            {'roll_no' : 1003, 'name' : 'Pinku', 'age' : 22},
            {'roll_no' : 1004, 'name' : 'John', 'age' : 20},
            {'roll_no' : 1005, 'name' : 'Mike', 'age' : 21},
        ]
        
        for data in dataset:
            roll_no = data['roll_no']
            exists = Student.objects.filter(roll_no=roll_no).exists()
            
            # Simple data Validation
            if not exists :
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
                self.stdout.write(self.style.SUCCESS(f'Student with roll no {roll_no} Inserted Successfully!'))
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} Already Exists!'))
        
        # Insert 1 user data in Student table
        # Student.objects.create(roll_no=10, name='Shubham', age=23)
        
        #self.stdout.write(self.style.SUCCESS('Data Inserted Successfully!')) 