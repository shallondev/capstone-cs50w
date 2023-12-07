# import necessary modules
import os
from django.core.management.base import BaseCommand
from exams.models import Question

class Command(BaseCommand):
    help = 'Import questions from text files'

    def handle(self, *args, **kwargs):
        # Specify the directory where your text files are stored
        directory_path = '/home/shallonf/capstone/capstone-cs50w/capstone/media/questions'

        # Loop through each file in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                
                # Read the content of the file
                with open(file_path, 'r') as file:
                    content = file.read()

                # Create a new Question instance and save it to the database
                question = Question(content=content)
                question.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {filename}'))
