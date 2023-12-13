from django.urls import path
from core.rest.views import why_choose_us

urlpatterns = [
    path('', 
         why_choose_us.WhyChooseUsCreate.as_view(),
         name='content-list-create'),
    path('<uuid:uid>/',
         why_choose_us.WhyChooseUsRetrieveUpdate.as_view(),
         name='content-update'),
    path('sub_content/', 
         why_choose_us.WhyChooseUsSubContentCreate.as_view(),
         name='sub-content-list-create'),
    path('list/', 
         why_choose_us.ContentList.as_view(),
         name='content-list'),
    path('sub_content/list/', 
         why_choose_us.SubContentList.as_view(),
         name='sub-content-list'),
]