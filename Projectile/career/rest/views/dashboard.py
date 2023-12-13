from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from datetime import date

from core.models import (
    Product,
    Service,
    Appointment,
    User, 
)

from career.models import(
    LeaveMessage,
    EmployeeCandidate
)

class DashboardAPIViewList(APIView):
   
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        
        today = date.today()

        product_count = Product.objects.count()
        service_count = Service.objects.count()
        message_count = LeaveMessage.objects.filter(created_date__date=today).count()
        appointment_count = Appointment.objects.filter(appointment_date__date=today).count()
        apply_job_count = EmployeeCandidate.objects.filter(created_date__date=today).count()
        user_count = User.objects.count()

        data = {
            'product_count': product_count,
            'service_count': service_count,
            'message_count_today': message_count,
            'appointment_count_today': appointment_count,
            'apply_job_count': apply_job_count,
            'user_count': user_count,
        }
        return Response(data)