from rest_framework import serializers
from DRF.models import model_data

class serializer_data(serializers.ModelSerializer):
    class Meta:
        model= model_data
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
        ]
        #if DRF shows that any field is required then can be disable by defining as followed below-
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name' : {'required': False},
            'email': {'required': False},
            'username': {'required': False},
            }
        #validators = []