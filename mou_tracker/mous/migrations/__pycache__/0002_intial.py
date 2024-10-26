# mous/migrations/0002_initial_data.py
from django.db import migrations

def create_initial_data(apps, schema_editor):
    Department = apps.get_model('mous', 'Department')
    Organization = apps.get_model('mous', 'Organization')
    Outcome = apps.get_model('mous', 'Outcome')

    # Departments
    departments = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Biotechnology"]
    for dept in departments:
        Department.objects.create(name=dept)

    # Organizations
    organizations = ["Tata Consultancy Services", "Infosys", "Wipro", "Bharat Electronics Limited", "ISRO"]
    for org in organizations:
        Organization.objects.create(name=org)

    # Outcomes
    outcomes = ["Placement", "Internship", "Research Collaboration", "Workshop", "Guest Lecture"]
    for out in outcomes:
        Outcome.objects.create(name=out)

class Migration(migrations.Migration):

    dependencies = [
        ('mous', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
