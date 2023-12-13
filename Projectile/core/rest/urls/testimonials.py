from django.urls import path
from core.rest.views import testimonials

urlpatterns = [
    path('',
         testimonials.TestimonialAPIView.as_view(),
         name='testimonial-list'),
    path('<uuid:uid>/', testimonials.TestimonialRetrieveUpdate.as_view(),
         name='testimonial-update'),
    path('create/',
         testimonials.TestimonialCreate.as_view(),
         name='testimonial-create'),
]