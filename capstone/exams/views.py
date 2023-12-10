import json
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Exam, Question, User
from .forms import CreateExamForm
from .util import generate_exam
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam, UserQuestion


@login_required
def exam_summary(request, exam_id):
    exam_instance = get_object_or_404(Exam, pk=exam_id)

    # Retrieve user's questions and calculate score
    user_questions = UserQuestion.objects.filter(user=request.user, question__in=exam_instance.questions.all())
    correct_answers = user_questions.filter(is_correct=True).count()
    user_score = (correct_answers / exam_instance.size) * 100

    return render(request, 'exams/exam_summary.html', {
        'exam': exam_instance,
        'user_score': user_score,
        'user_questions': user_questions,
    })


@login_required
def take_exam(request, exam_id):
    exam_instance = get_object_or_404(Exam, pk=exam_id)

    if request.method == 'POST':
        user_answers = request.POST.dict()  # Get all form data as a dictionary
        user_answers.pop('csrfmiddlewaretoken', None)  # Remove CSRF token

        # Iterate through each question in the exam
        for index, question in enumerate(exam_instance.questions.all(), start=1):
            key = f"Question {index}"
            user_answer = user_answers.get(key, '')  # Get the user's answer for the current question

            # Determine if the user's answer is correct
            is_correct = user_answer == question.correct_response

            # Update or create UserQuestion instance
            UserQuestion.objects.update_or_create(
                user=request.user,
                question=question,
                defaults={'is_correct': is_correct}
            )

        # Calculate and set the user's score
        correct_answers = UserQuestion.objects.filter(user=request.user, is_correct=True).count()
        user_score = (correct_answers / exam_instance.size) * 100
        exam_instance.score = user_score
        exam_instance.save()

        # Redirect to the exam summary
        return redirect('exam_summary', exam_id=exam_instance.id)

    # If it's a GET request, render the exam form
    question_dict = {}
    for index, question in enumerate(exam_instance.questions.all(), start=1):
        key = f"Question {index}"
        question_dict[key] = question.content

    return render(request, 'exams/take_exam.html', {
        'exam': exam_instance,
        'question_dict': question_dict,
    })

    

@login_required
def create_exam(request):
    if request.method == 'POST':
        form = CreateExamForm(request.POST)
        if form.is_valid():
            user = request.user
            num_questions = form.cleaned_data['size']
            exam_time = form.cleaned_data['time']

            # Generate exam and get the instance
            exam_instance = generate_exam(user, num_questions, exam_time)
            exam_instance.save()

            # Redirect to the take_exam view for the new exam
            return redirect('take_exam', exam_id=exam_instance.id)

    else:
        form = CreateExamForm()

    return render(request, 'exams/create_exam.html', {'form': form})


def index(request):
    return render(request, "exams/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "exams/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "exams/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "exams/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "exams/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "exams/register.html")