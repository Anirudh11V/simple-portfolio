from rest_framework import serializers
from cvapp.models import feedback


class feedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedback
        
        fields = ['id','Name', 'feed']
		