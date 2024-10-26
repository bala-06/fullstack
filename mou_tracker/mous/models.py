# mous/models.py
from django.db import models
from django.utils import timezone
class Activity(models.Model):
    mou = models.ForeignKey('MOU', on_delete=models.CASCADE, related_name='activities')
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='pending'
    )

    def __str__(self):
        return f"{self.description} - {self.status}"


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Outcome(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MOU(models.Model):
    title = models.CharField(max_length=100)
    department = models.ManyToManyField(Department)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    outcomes = models.ManyToManyField(Outcome)
    start_date = models.DateField()
    end_date = models.DateField()
    pdf_file = models.FileField(upload_to='mou_pdfs/', default='path/to/default/file.pdf')

    @property
    def is_active(self):
        return self.end_date >= timezone.now().date()

    def __str__(self):
        return self.title
