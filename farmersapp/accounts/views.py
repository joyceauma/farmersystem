from django.shortcuts import render
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
from rest_framework import viewsets
from .models import User, Officer, Farmer, Session, Report
from .serializers import OfficerSerializer, FarmerSerializer, SessionSerializer, ReportSerializer

#log a user in
# @login_required(login_url='/accounts/login')
# def my_view(request):
#      email = request.POST['email']
#      password = request.POST['password']
#      user = authenticate(email= email, password=password)
#      if user is not None:
#           if user.is_active:
#                login(request, user)
#                # redirect to a success page.
#           else:
#               'disabled account'
#      else:
#           'invalid login' 
#      if not request.user.is_authenticated():
#           return redirect('/login/?next=%s' % request.path)
#      if not request.user.is_authenticated():
#           return render(request, 'accounts/login_error.html')     
# # logout a user
# def logout_view(request):
#      logout(request)
     #redirect to the index                        




class OfficerView(viewsets.ModelViewSet):
     serializer_class = OfficerSerializer
     queryset = Officer.objects.all()
     
class FarmerView(viewsets.ModelViewSet):
     serializer_class = FarmerSerializer
     queryset = Farmer.objects.all()

class SessionView(viewsets.ModelViewSet):
     serializer_class = SessionSerializer
     queryset = Session.objects.all()

class ReportView(viewsets.ModelViewSet):
     serializer_class = ReportSerializer
     queryset = Report.objects.all()
     

def index(request):
     return render(request, 'accounts/index.html') 
     