from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    CLASS_CHOICES = [
        ('Nursery A', 'Nursery A'),
        ('Nursery B', 'Nursery B'),
        ('Nursery C', 'Nursery C'),
        ('LKG A', 'LKG A'),
        ('LKG B', 'LKG B'),
        ('LKG C', 'LKG C'),
        ('UKG A', 'UKG A'),
        ('UKG B', 'UKG B'),
        ('UKG C', 'UKG C'),
        ('Class 1 A', 'Class 1 A'),
        ('Class 1 B', 'Class 1 B'),
        ('Class 1 C', 'Class 1 C'),
        ('Class 2 A', 'Class 2 A'),
        ('Class 2 B', 'Class 2 B'),
        ('Class 2 C', 'Class 2 C'),
        ('Class 3 A', 'Class 3 A'),
        ('Class 3 B', 'Class 3 B'),
        ('Class 3 C', 'Class 3 C'),
        ('Class 4 A', 'Class 4 A'),
        ('Class 4 B', 'Class 4 B'),
        ('Class 4 C', 'Class 4 C'),
        ('Class 5 A', 'Class 5 A'),
        ('Class 5 B', 'Class 5 B'),
        ('Class 5 C', 'Class 5 C'),
        ('Class 6 A', 'Class 6 A'),
        ('Class 6 B', 'Class 6 B'),
        ('Class 6 C', 'Class 6 C'),
        ('Class 7 A', 'Class 7 A'),
        ('Class 7 B', 'Class 7 B'),
        ('Class 7 C', 'Class 7 C'),
        ('Class 8 A', 'Class 8 A'),
        ('Class 8 B', 'Class 8 B'),
        ('Class 8 C', 'Class 8 C'),
        ('Class 9 A', 'Class 9 A'),
        ('Class 9 B', 'Class 9 B'),
        ('Class 9 C', 'Class 9 C'),
        ('Class 10 A', 'Class 10 A'),
        ('Class 10 B', 'Class 10 B'),
        ('Class 10 C', 'Class 10 C'),
        ('Class 11 A', 'Class 11 A'),
        ('Class 11 B', 'Class 11 B'),
        ('Class 11 C', 'Class 11 C'),
        ('Class 12 A', 'Class 12 A'),
        ('Class 12 B', 'Class 12 B'),
        ('Class 12 C', 'Class 12 C'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    class_name = models.CharField(max_length=50, choices=CLASS_CHOICES, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('resolved', 'Resolved')], default='open')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
