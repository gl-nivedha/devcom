from rest_framework import serializers
from . models import booking
class booking_ser(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['Contact','Reason','Council','Room','start_date','end_date','status']

