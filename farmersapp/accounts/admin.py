from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth import get_user_model
from django.db import models
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Officer, Farmer, District, Subcounty, Village, Session, Report, Parish

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    #forms to add and change user instances
    form = UserAdminChangeForm #update view
    add_form = UserAdminCreationForm #create view
    
    #the fields to be used in displaying the user model.
  
    #reference specific fields on auth.user.
    list_display = ('email', 'admin')
    list_filter = ('admin', 'officer', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Details', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'officer', 'active',)}),
    )
   
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(User, UserAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ( 'name', )
admin.site.register(District, DistrictAdmin)

class SubcountyAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'district')
admin.site.register(Subcounty, SubcountyAdmin)

class ParishAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_county')
admin.site.register(Parish, ParishAdmin)

class VillageAdmin(admin.ModelAdmin):
     list_display = ('name', 'parish')
admin.site.register(Village, VillageAdmin)

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'login_id', 'password',  'phone_number', 'district_id', 'subcounty_id')
admin.site.register(Officer, OfficerAdmin)
   

class FarmerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'parish', 'village', 'phone_number', 'gender',
                     'birth_year', 'marriage', 'language', 'phone_number', 'photo', 'community_status', 
                     'instructor_possibility', 'crop_type',
                     )
admin.site.register(Farmer, FarmerAdmin)
 

class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'area', 'harvest')
admin.site.register(Session, SessionAdmin)


class ReportAdmiin(admin.ModelAdmin):
    list_display = ('session_id', 'farm_area', 'rice_type', 'sowing_type', 'planting_type',
                     'levelling', 'rigde', 'watercourse_state', 'fertilizer', 'fertilizer_1_type',
                     'fertilizer_1_amount', 'fertilizer_2_type', 'fertilizer_2_amount', 'weed_condition',
                     'harvest_date', 
                    )
admin.site.register(Report, ReportAdmiin) 

admin.site.site_header='JICA PRIDE'



    