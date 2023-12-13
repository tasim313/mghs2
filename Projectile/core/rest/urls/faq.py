from django.urls import path
from core.rest.views import faq

urlpatterns = [
    path('',
         faq.FrequentAskedQuestionCreate.as_view(),
         name='faq-list-create'),
    path('<uuid:uid>/', faq.FrequentAskedQuestionRetrieveUpdate.as_view(),
         name='faq-update'),
    path('list/',
         faq.FrequentAskedQuestionList.as_view(),
         name='faq-list'),
    path("sub_content/list/", 
         faq.FrequentAskedQuestionSubContentList.as_view(),
         name='sub_content_list'),
    path("sub_content/<uuid:uid>/", 
         faq.FrequentAskedQuestionSubContentRetrieveUpdate.as_view(),
         name='sub_content_update'),
    path("sub_content/<uuid:frequent_asked_question_info__uid>/create", 
         faq.FrequentAskedQuestionSubContentCreate.as_view(),
         name='sub_content_create'),
]