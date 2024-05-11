
from . import models
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):

	name = serializers.CharField(source="title", required=True)
	message = serializers.CharField(source="description", required=True)
	email = serializers.EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)