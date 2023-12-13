from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import(
    Career,
    CareerDetails,
    EmployeeCandidate,
    CaseStudyDetails,
    NewsEventsDetails,
    IntroVideo,
    LeaveMessage,
)



class CareerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'designation',
        'education',
        'experience',
        'deadline',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(Career, CareerAdmin)



class CareerDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'career_info',
        'title',
        'description',
        'responsibilities',
        'qualifications',
        'experience',
        'benefits',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(CareerDetails,  CareerDetailsAdmin)



class EmployeeCandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'portfolio_link',
        'linkedin_link',
        'job_category',
        'comment',
        'created_date',
        'curriculum_vitae',
        )
    
admin.site.register(EmployeeCandidate,  EmployeeCandidateAdmin)




class CaseStudyDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'title',
        'introduction',
        'challenges_goals',
        'result',
        'image',
        'challenges_image',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(CaseStudyDetails,  CaseStudyDetailsAdmin)




class NewsEventsDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'new_events',
        'headline',
        'description',
        'publish_date',
        'image',
        'summarize_content_title',
        'summarize_content_description',
        'summarize_content_image',
        'quotes',
        'conclusion_content',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(NewsEventsDetails,  NewsEventsDetailsAdmin)


class IntroVideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'uid',
        'videoId',
        'created_date',
        'updated_date',
        'status',
        'user_created',
        'user_updated',
        )
    
admin.site.register(IntroVideo,  IntroVideoAdmin)




class LeaveMessageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'subject',
        'message',
        'created_date',
        )
    
admin.site.register(LeaveMessage,  LeaveMessageAdmin)