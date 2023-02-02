from django.db import models
from django.contrib.auth.models import User
import uuid, os, re
from django.core.exceptions import ValidationError
# Create your models here.



class Profile(models.Model):

    roles = (
        ('HOD', 'HOD'),
        ('Other', 'Other')
    )

    gender = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=10, choices=roles)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=60, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='user-default.png')
    FacultyId = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=gender)
    departmentName = models.CharField(max_length=20)
    FacultyPhone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self):
        return str(self.user.username)


def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if ext not in valid_extensions:
        raise ValidationError("File should be in pdf format")

class Conference(models.Model):
    listed = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    conferenceId = models.CharField(max_length=200, unique=True)
    conferenceName = models.CharField(max_length=200)
    conferenceDoi = models.CharField(max_length=200)
    conferenceArticle = models.FileField(upload_to='files/', validators=[validate_pdf])
    ugcListed = models.CharField(max_length=10, choices=listed)
    conferenceNationality = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.conferenceName)
    


class Journal(models.Model):
    listed = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    JournalId = models.CharField(max_length=200, unique=True)
    journalName = models.CharField(max_length=200)
    journalDoi = models.CharField(max_length=200)
    journalArticle = models.FileField(upload_to='files/', validators=[validate_pdf])
    ugcListed = models.CharField(max_length=10, choices=listed)
    journalNationality = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.journalName)
    

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created']