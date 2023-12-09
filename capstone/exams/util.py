import random
from .models import Question, Exam
from django.contrib.auth.models import User

def generate_exam(user, num_questions, exam_time):
    # Get all questions
    all_questions = Question.objects.all()

    # Ensure that there are enough questions available
    if num_questions > len(all_questions):
        raise ValueError("Not enough questions available")

    # Get random questions
    random_questions = random.sample(list(all_questions), num_questions)

    # Create Exam instance
    exam_size = num_questions  # Set the exam size equal to the number of questions
    exam = Exam(user=user, size=exam_size, time=exam_time)
    exam.save()

    # Add random questions to the exam
    exam.questions.set(random_questions)

    return exam