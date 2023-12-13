from django.urls import path
from career.rest.views import message

urlpatterns = [
    path('', 
         message.LeaveMessageCreate.as_view(),
         name='message-create'),
    path('list/',
         message.LeaveMessageList.as_view(),
         name='message-list'),
]