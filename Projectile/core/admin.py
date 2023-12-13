from django.contrib import admin
from django.contrib import messages
from import_export.admin import ImportExportModelAdmin


from .models import (
    User,
    Appointment,
    AppointmentUserAdditionalInformation,
    Contact,
    NewsEvents,
    NewsEventsFile,
    LogoFile,
    HomeSliderContent,
    HomeSliderContentFile,
    Product,
    ProductDetails,
    Clients,
    TESTIMONIALS,
    Service,
    About,
    FunFactContent,
    AboutFile,
    WhyChooseUs,
    WhyChooseUsSubContent,
    CaseStudy,
    Team,
    Gallery,
    FrequentAskedQuestion,
    FrequentAskedQuestionSubContent,
    PrivacyPolicy,
    TermsOfService,
    ServiceDetails,
)


admin.site.site_header = 'Maksuda Girls High School  adminsitration'
admin.site.index_title = 'Maksuda Girls High School'
admin.site.site_title = 'Maksuda Girls High School adminsitration'


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'username',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        )
    list_filter = ('username', 'role',)
    search_fields = ("username", 'role','is_active')

    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

admin.site.register(User, UserAdmin)


# class AppointmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'slug',
#         'name',
#         'email',
#         'phone_number',
#         'appointment_date',
#         'message',
#         'service'
#         )
#     list_filter = ('name', 'email', 'appointment_date',)

# admin.site.register(Appointment, AppointmentAdmin)


# class AppointmentUserAdditionalInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'appointment_user',
#         'service',
#         'created_date',
#         'ip_address',
#         'browser',
#         'operating_system',
#         'online',
#         'cookieEnabled',
#         'user_agent',
#         )
#     list_filter = ('online', 'created_date',)


# admin.site.register(
#     AppointmentUserAdditionalInformation,
#     AppointmentUserAdditionalInformationAdmin)


class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'address',
        'contact_email',
        'Phone',
        'created_date',
        'updated_date',
        'status',
        'slug',
        'user_created',
        'user_updated',
        )
  
admin.site.register(Contact, ContactAdmin)


class NewsEventsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'choices',
        'slug',
        'headline',
        'description',
        'image',
        'publish_date',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('headline', 'publish_date', 'status',)
  
admin.site.register(NewsEvents, NewsEventsAdmin)



class NewsEventsFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'news_events',
        'image',
        )
    list_filter = ('news_events__headline', 'news_events__publish_date', 'news_events__status',)
admin.site.register(NewsEventsFile, NewsEventsFileAdmin)




class LogoFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
admin.site.register(LogoFile, LogoFileAdmin)



class HomeSliderContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'slug',
        'title',
        'description',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title','status',)
  
admin.site.register(HomeSliderContent, HomeSliderContentAdmin)



class HomeSliderContentFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'home_content',
        'image',
        )
    list_filter = ('home_content__title',)
admin.site.register(HomeSliderContentFile, HomeSliderContentFileAdmin)


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'short_description',
        'slug',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(Product, ProductAdmin)



class ProductDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'short_description',
        'long_description',
        'key_Feature',
        'slug',
        'image',
        'short_description_image',
        'long_description_image',
        'key_Feature_image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(ProductDetails, ProductDetailsAdmin)




# class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'logo',
#         'name',
#         'head_office',
#         'email',
#         'Phone',
#         'slug',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#         )
# admin.site.register(Clients, ClientAdmin)




class TestimonialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'name',
        'designation',
        'comment',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
admin.site.register(TESTIMONIALS, TestimonialAdmin)



class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'short_description',
        'slug',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(Service, ServiceAdmin)



class ServiceDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'short_description',
        'long_description',
        'image',
        'short_description_image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(ServiceDetails, ServiceDetailsAdmin)




class AboutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'short_description',
        'support_description',
        'start_year',
        'years_of_experience',
        'vision',
        'mission',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(About, AboutAdmin)



class FunFactContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'about_info',
        'years_of_experience',
        'number_of_clients',
        'delivered_products',
        'winning_awards',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
admin.site.register(FunFactContent, FunFactContentAdmin)


class AboutFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'about',
        'slug',
        'image',
    )
admin.site.register(AboutFile, AboutFileAdmin)



# class WhyChooseUsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'headline',
#         'short_description',
#         'image',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#     )
# admin.site.register(WhyChooseUs, WhyChooseUsAdmin)


# class WhyChooseUsSubContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'content',
#         'headline',
#         'short_description',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#     )
# admin.site.register(WhyChooseUsSubContent, WhyChooseUsSubContentAdmin)



class CaseStudyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'subtitle',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('title',)
    search_fields = ("title", )
admin.site.register(CaseStudy, CaseStudyAdmin)


class TeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'name',
        'designation',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    list_filter = ('name',)
    search_fields = ("name", )
admin.site.register(Team, TeamAdmin)


class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(Gallery, GalleryAdmin)



# class FrequentAskedQuestionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'title',
#         'image',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#         )
    
# admin.site.register(FrequentAskedQuestion, FrequentAskedQuestionAdmin)




# class FrequentAskedQuestionSubContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'frequent_asked_question_info',
#         'question',
#         'answer'
#         )
    
# admin.site.register(FrequentAskedQuestionSubContent, FrequentAskedQuestionSubContentAdmin)


# class PrivacyPolicyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'title',
#         'description',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#         )
    
# admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)



# class TermsOfServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = (
#         'uid',
#         'title',
#         'description',
#         'created_date',
#         'updated_date',
#         'status',
#         'user_created',
#         'user_updated',
#         )
    
# admin.site.register(TermsOfService, TermsOfServiceAdmin)
