import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from .choice import (
    UserRole,
    UserStatus,
    ProvidedService,
    NewsEventsStatus,
)

from .utils import (
    get_appointment_slug,
    get_contact_slug,
    get_news_events_slug,
    get_news_events_image,
    get_website_logo_image,
    get_home_slider_content_slug,
    get_home_slider_content_image,
    get_product_slug,
    get_product_image,
    get_news_events_base_image,
    get_client_slug,
    get_client_logo,
    get_testimonial_image,
    get_service_slug,
    get_service_image,
    get_about_file_slug,
    get_about_file_image,
    get_why_choose_us_content_image,
    get_case_study_image,
    get_team_image,
    get_gallery_image,
    get_faq_image,
    get_product_details_image,
    get_service_details_image,
    get_product_details_slug
)


import logging

logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager):
    def create_user(self,
                    username,
                    password=None,
                    **extra_fields):
        if not username:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=self.normalize_email(username),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,
                         username,
                         password=None,
                         **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        if extra_fields.get('role') != 'Admin':
            raise ValueError('Superuser must have role of Global Admin')

        user = self.create_user(
            username=self.normalize_email(username),
            password=password, **extra_fields
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return 
       

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=False,
        verbose_name='user email address',
        max_length=255,
        blank=True,
        null=True,
    )
    username = models.EmailField(max_length=255,
                                 unique=True,
                                 verbose_name='Email')
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        db_index=True,
        default=UserRole.Manager,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.Active
    )
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
        self.email = self.username
        return super().save(*args, **kwargs)

    
class BaseModel(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=15,
        choices=UserStatus.choices,
        default=UserStatus.Active
    )
    user_created = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="User_who_created",
        verbose_name="Created Person"
        )
    user_updated = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="The_User_who_Updated",
        verbose_name="Updated Person"
    )


class Contact(BaseModel):
    address = models.TextField(max_length=555, blank=True, null=True)
    contact_email = models.EmailField(max_length=255,
                                      blank=True,
                                      null=True,
                                      verbose_name='Email')
    Phone = PhoneNumberField(blank=True,
                            null=True,
                            verbose_name="Phone Number")
    slug = AutoSlugField(populate_from=get_contact_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    
    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'


class NewsEvents(BaseModel):
    choices = models.CharField(
        max_length=100,
        choices=NewsEventsStatus.choices,
        db_index=True,
        default=NewsEventsStatus.news
    )
    slug = AutoSlugField(populate_from=get_news_events_slug,
                         unique=True,
                         null=True,
                         db_index=True)
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
        upload_to=get_news_events_base_image,
        null=True, blank=True)
    
    
    class Meta:
        ordering = ['-publish_date', '-id']

    def __str__(self):
        return self.headline 
    
    class Meta:
        verbose_name = 'News Events And Result Publication'
        verbose_name_plural = 'News Events And Result Publication'



class NewsEventsFile(models.Model):
    news_events = models.ForeignKey(NewsEvents, on_delete=models.DO_NOTHING, related_name='news_events_info')
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    image = VersatileImageField(
        upload_to=get_news_events_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'News Events And Result Publication File'
        verbose_name_plural = 'News Events And Result Publication File'
    
    
class LogoFile(BaseModel):
    image = VersatileImageField(
        upload_to=get_website_logo_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'School Website Logo'
        verbose_name_plural = 'School Website Logo'
    
    


class HomeSliderContent(BaseModel):
    slug = AutoSlugField(populate_from=get_home_slider_content_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    title = models.CharField(max_length=30,
                            db_index=True,
                            verbose_name='Title')
    description = models.TextField(max_length=100,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Banner or Slider Content'
        verbose_name_plural = 'Banner or Slider Content'


class HomeSliderContentFile(BaseModel):
    home_content = models.ForeignKey(
        HomeSliderContent,
        on_delete=models.DO_NOTHING,
        related_name='home_content_info')
    image = VersatileImageField(
        upload_to=get_home_slider_content_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'Banner or Slider Content File'
        verbose_name_plural = 'Banner or Slider Content File'
    

class Product(BaseModel):
    title = models.CharField(max_length=1000,
                            db_index=True,
                            unique=True,
                            verbose_name='Title')
    short_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    slug = AutoSlugField(populate_from=get_product_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    image = VersatileImageField(
        upload_to=get_product_image,
        null=True, blank=True)
    
    class Meta:
        ordering = ['created_date', 'id']
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Admission Information'
        verbose_name_plural = 'Admission Information'



class ProductDetails(BaseModel):
    products_info = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='products_details_info')
    title = models.CharField(max_length=1000, db_index=True, blank=True,
                                   null=True, verbose_name="Title")
    short_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    long_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    key_Feature = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    image = VersatileImageField(
        upload_to=get_product_details_image,
        null=True, blank=True)
    short_description_image = VersatileImageField(
        upload_to=get_product_details_image,
        null=True, blank=True)
    long_description_image = VersatileImageField(
        upload_to=get_product_details_image,
        null=True, blank=True)
    key_Feature_image = VersatileImageField(
        upload_to=get_product_details_image,
        null=True, blank=True)
    slug = AutoSlugField(populate_from=get_product_details_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    
    class Meta:
        verbose_name = 'Admission Details'
        verbose_name_plural = 'Admission Details'
    



class Clients(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    head_office = models.TextField(max_length=None, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    Phone = PhoneNumberField(blank=True,
                            null=True,
                            verbose_name="Phone Number")
    slug = AutoSlugField(populate_from=get_client_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    logo = VersatileImageField(
        upload_to=get_client_logo,
        null=True, blank=True)
    


class TESTIMONIALS(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.TextField(max_length=None, blank=True, null=True)
    comment = models.TextField(max_length=None, blank=True, null=True)
    image = VersatileImageField(
        upload_to=get_testimonial_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'



class Service(BaseModel):
    title = models.CharField(max_length=1000,
                            db_index=True,
                            verbose_name='Title')
    short_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    slug = AutoSlugField(populate_from=get_service_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    image = VersatileImageField(
        upload_to=get_service_image,
        null=True, blank=True)
    
    class Meta:
        ordering = ['created_date', 'id']
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Academic Information'
        verbose_name_plural = 'Academic Information'



class ServiceDetails(BaseModel):
    service_info = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='service_details_info')
    title = models.CharField(max_length=1000, db_index=True, blank=True,
                                   null=True, verbose_name="Title")
    short_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    long_description = models.TextField(max_length=500000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   )
    
    image = VersatileImageField(
        upload_to=get_service_details_image,
        null=True, blank=True)
    short_description_image = VersatileImageField(
        upload_to=get_service_details_image,
        null=True, blank=True)
    

    class Meta:
        verbose_name = 'Academic  Details'
        verbose_name_plural = 'Academic Information Details'





class Appointment(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    slug = AutoSlugField(populate_from=get_appointment_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,
                              blank=True,
                              null=True,
                              unique=False,
                              verbose_name="Email Address")
    phone_number = PhoneNumberField(blank=True,
                                    null=True,
                                    verbose_name="Phone Number")
    appointment_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(max_length=555,
                               blank=True,
                               null=True)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="service_info_for_appointment")

    class Meta:
        ordering = ['-appointment_date',]

    def __str__(self):
        return self.name


class AppointmentUserAdditionalInformation(models.Model):
    appointment_user = models.ForeignKey(Appointment,
                                         on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    browser = models.CharField(max_length=50, blank=True, null=True)
    operating_system = models.CharField(max_length=50, blank=True, null=True)
    online = models.CharField(max_length=6, blank=True, null=True)
    cookieEnabled = models.CharField(max_length=6, blank=True, null=True)
    user_agent = models.CharField(max_length=255)
    service = models.ForeignKey(Service,
                                on_delete=models.DO_NOTHING,
                                blank=True, null=True,
                                related_name="appointment_user_service_info")
   
    def save(self,*args, **kwargs):  
        self.service = self.appointment_user.service
        super().save(*args, **kwargs)
    


    def __str__(self):
        return self.appointment_user.name


def create_appointment_user(sender, instance, created, **kwargs):

    if created:
        import requests
        api_url = "https://api.ipify.org?format=json"
        try:
            response = requests.get(api_url)
            data = response.json()
            ip_address = data.get("ip")
        except requests.exceptions.RequestException:
            ip_address = None

        AppointmentUserAdditionalInformation.objects.create(
            appointment_user=instance,
            ip_address=ip_address,
            )


post_save.connect(create_appointment_user, sender=Appointment)





class About(BaseModel):

    title = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='Title')
    
    short_description = models.TextField(max_length=1000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   verbose_name="Company Short Description"
                                   )
    
    support_description = models.TextField(max_length=1000,
                                   validators=[MinLengthValidator(11)],
                                   blank=True,
                                   null=True,
                                   verbose_name="Customer Support Short Description"
                                   )
    
    start_year = models.DateField()
    years_of_experience = models.CharField(max_length=200, blank=True, null=True)

    vision = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Company Vision")
    mission = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Company Mission")

    def __str__(self):
        return self.title 


    def save(self, *args, **kwargs):
        import datetime
        import dateutil
        import dateutil.relativedelta
        now = datetime.datetime.utcnow()
        now = now.date()
        age = dateutil.relativedelta.relativedelta(now, self.start_year)
        experience = age.years
        self.years_of_experience = experience
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'About Information'
        verbose_name_plural = 'About Information'




class AboutFile(models.Model):
    about = models.ForeignKey(
        About,
        on_delete=models.DO_NOTHING,
        related_name='about_file_content')
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    slug = AutoSlugField(populate_from=get_about_file_slug,
                         unique=True,
                         null=True,
                         db_index=True)
    image = VersatileImageField(
        upload_to=get_about_file_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'About File'
        verbose_name_plural = 'About File'


def create_about_file_content(sender, instance, created, **kwargs):

    if created:
        AboutFile.objects.create(
            about=instance)


post_save.connect(create_about_file_content, sender=About)




class FunFactContent(BaseModel):
    about_info = models.ForeignKey(About,
                              on_delete=models.DO_NOTHING,
                              blank=True, null=True,
                              related_name="about_fun_fact_content")
    years_of_experience = models.CharField(max_length=20, blank=True, null=True)
    number_of_clients = models.CharField(max_length=50, blank=True, null=True)
    delivered_products = models.CharField(max_length=50, blank=True, null=True)
    winning_awards = models.CharField(max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.years_of_experience = self.about_info.years_of_experience
        self.user_created = self.about_info.user_created
        self.status=UserStatus.Active
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'School Other Information'
        verbose_name_plural = 'School Other Information'



def create_fun_fact_content(sender, instance, created, **kwargs):

    if created:
        FunFactContent.objects.create(
            about_info=instance)


post_save.connect(create_fun_fact_content, sender=About)



class WhyChooseUs(BaseModel):
    headline = models.CharField(max_length=255,db_index=True, verbose_name="Content Title")
    short_description = models.TextField(max_length=500, blank=True, null=True)
    image = VersatileImageField(
        upload_to=get_why_choose_us_content_image,
        null=True, blank=True)

    def __str__(self):
        return self.headline


class WhyChooseUsSubContent(BaseModel):
    content = models.ForeignKey(WhyChooseUs,
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                null=True)
    headline = models.CharField(max_length=255,db_index=True, verbose_name="Content Title")
    short_description = models.TextField(max_length=500, blank=True, null=True)



class CaseStudy(BaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Title")
    subtitle = models.CharField(max_length=100, db_index=True, verbose_name="Sub Title")
    image = VersatileImageField(
        upload_to=get_case_study_image,
        null=True, blank=True)
    
    def __str__(self):
        return self.title 
    

class Team(BaseModel):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    image = VersatileImageField(
        upload_to=get_team_image,
        null=True, blank=True)
    
    class Meta:
        verbose_name = 'School Teachers Information'
        verbose_name_plural = 'School Teachers Information'


class Gallery(BaseModel):
    image = VersatileImageField(
        upload_to=get_gallery_image,
        null=True, blank=True)



class FrequentAskedQuestion(BaseModel):
    title = models.CharField(max_length=300)
    image = VersatileImageField(
        upload_to=get_faq_image,
        null=True, blank=True)
    
    def __str__(self):
        return self.title 



class FrequentAskedQuestionSubContent(BaseModel):
    frequent_asked_question_info = models.ForeignKey(FrequentAskedQuestion,
                                                on_delete=models.DO_NOTHING,
                                                blank=True, null=True,
                                                related_name='frequent_asked_question_sub_content')
    question = models.CharField(max_length=300, blank=True, null=True)
    answer = models.CharField(max_length=300, blank=True, null=True)



class PrivacyPolicy(BaseModel):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True, null=True)



class TermsOfService(BaseModel):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True, null=True)