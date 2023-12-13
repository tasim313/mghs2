from django.db import models
import uuid
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField 
from django.core.validators import MinLengthValidator
from core.models import (
    BaseModel,
    CaseStudy,
    NewsEvents
    )

from core.choice import UserStatus
from .utils import (
    get_case_study_details_image,
    get_news_events_details_image,
    get_curriculum_vitae_file,
)


class Career(BaseModel):
    designation = models.CharField(max_length=550, blank=True, null=True)
    education = models.CharField(max_length=550, blank=True, null=True)
    experience = models.CharField(max_length=550, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-deadline', '-id']

    def __str__(self):
        return self.designation 


class CareerDetails(BaseModel):
    career_info = models.ForeignKey(Career, on_delete=models.DO_NOTHING, related_name='career_info_details')
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(max_length=None, blank=True, null=True, verbose_name='Job Description')
    responsibilities = models.TextField(max_length=None, blank=True, null=True, verbose_name='Roles & Responsibilities')
    qualifications = models.TextField(max_length=None, blank=True, null=True, verbose_name='Qualifications')
    experience = models.TextField(max_length=None, blank=True, null=True, verbose_name='Experience Requirements')
    benefits = models.TextField(max_length=None, blank=True, null=True, verbose_name='Benefits')

    def save(self, *args, **kwargs):
        self.title = self.career_info.designation
        self.user_created = self.career_info.user_created
        self.status = UserStatus.Active
        super().save(*args, **kwargs)


class EmployeeCandidate(models.Model):
    name = models.CharField(max_length=500,db_index=True, blank=True, null=True, verbose_name="Full Name")
    email = models.EmailField(blank=True, null=True, db_index=True,)
    phone_number = PhoneNumberField(blank=True,
                                    null=True,
                                    db_index=True,
                                    verbose_name="Phone Number")
    portfolio_link = models.URLField(blank=True, null=True, verbose_name='Portfolio Link')
    linkedin_link = models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile Link')
    job_category = models.ForeignKey(Career, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='apply_job')
    comment = models.TextField(max_length=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    curriculum_vitae = models.FileField(upload_to =get_curriculum_vitae_file, null=True, blank=True)



class CaseStudyDetails(BaseModel):
    case_study = models.ForeignKey(CaseStudy, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='case_study_info_details')
    title = models.CharField(max_length=255, db_index=True, verbose_name="Title")
    introduction = models.TextField(max_length=None, blank=True, null=True)
    challenges_goals = models.TextField(max_length=None, blank=True, null=True, verbose_name="Challenges and Goals")
    result = models.TextField(max_length=None, blank=True, null=True)
    image = VersatileImageField(
        upload_to=get_case_study_details_image,
        null=True, blank=True)
    challenges_image = VersatileImageField(
        upload_to=get_case_study_details_image,
        null=True, blank=True)
    


class NewsEventsDetails(BaseModel):
    new_events = models.ForeignKey(NewsEvents, on_delete=models.DO_NOTHING, related_name="news_events_details")
    headline = models.CharField(max_length=300,
                                blank=True,
                                null=True,
                                db_index=True,
                                verbose_name='Title')
    description = models.TextField(max_length=None,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    publish_date = models.DateTimeField(blank=True, null=True)

    image = VersatileImageField(
        upload_to=get_news_events_details_image,
        null=True, blank=True)
    
    summarize_content_title = models.CharField(max_length=300,
                                blank=True,
                                null=True,
                                db_index=True,
                                verbose_name='Summarize Content Title')
    
    summarize_content_description = models.TextField(max_length=None,
                                   validators=[MinLengthValidator(1)],
                                   blank=True,
                                   null=True,
                                   )
    summarize_content_image = VersatileImageField(
        upload_to=get_news_events_details_image,
        null=True, blank=True)
    
    quotes = models.TextField(max_length=None,
                              validators=[MinLengthValidator(1)],
                              blank=True,
                              null=True,)
    
    conclusion_content = models.TextField(max_length=None,
                              validators=[MinLengthValidator(1)],
                              blank=True,
                              null=True,)
    



class IntroVideo(BaseModel):
    videoId = models.CharField(max_length=500, blank=True, null=True)


class LeaveMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True,
                                    null=True,
                                    db_index=True,
                                    verbose_name="Phone Number")
    subject = models.TextField(max_length=10000, blank=True, null=True)
    message = models.TextField(max_length=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date', '-id']
