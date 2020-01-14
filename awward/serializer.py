from rest_framework import serializers
from .models import Projects,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title','post','author','caption','project_link','pub_date','project_image')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('user','profile_photo','bio')