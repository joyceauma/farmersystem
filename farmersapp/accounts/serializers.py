from rest_framework import serializers
from .models import Officer, Farmer, Session, Report

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = "__all__"

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'



