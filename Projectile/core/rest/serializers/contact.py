from rest_framework import serializers 
from phonenumber_field.serializerfields import PhoneNumberField

from ...models import Contact 
from ...choice import UserStatus

class ContactSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=300)
    contact_email = serializers.EmailField()
    Phone = PhoneNumberField()
   
    class Meta:
        model = Contact
        fields = ('uid','address', 'contact_email', 'Phone')
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        address = validated_data['address']
        contact_email = validated_data['contact_email']
        Phone = validated_data['Phone']
        contact = Contact.objects.create(
                    address=address,
                    contact_email=contact_email,
                    Phone=Phone,
                    user_created=user,
                    status=UserStatus.Active
                    ) 
        return contact
    


class ContactUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('address', 'contact_email', 'Phone', 'user_updated')