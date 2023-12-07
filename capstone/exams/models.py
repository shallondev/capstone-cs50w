from django.contrib.auth.models import AbstractUser
from django.db import models

OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
        ('E', 'Option E'),
    ]

TOPIC_CHOICES = [
        ('1','Time Value of Money'),
        ('2', 'Annuities'),
        ('3', 'Loans'),
        ('4', 'Bonds'),
        ('5', 'Other'),
]


class User(AbstractUser):
    pass


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    correct_response = models.CharField(max_length=1, choices=OPTION_CHOICES, default='A')
    topic = models.CharField(max_length=1, choices=TOPIC_CHOICES, default='Other')

    def __str__(self):
        return f"Question: {self.id}"


class Exam(models.Model):
    size = models.PositiveIntegerField(default=30)
    time = models.PositiveIntegerField(default=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Exam - Size: {self.size}, Time: {self.time} minutes, User: {self.user.username}, Score: {self.score}, Date: {self.date}"


class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
