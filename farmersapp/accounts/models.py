from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager
)

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('users must have an email address')
        if not password:
            raise ValueError('users must have a password')

        user_obj = self.model(
            email=self.normalize_email(email)

        )
        user_obj.set_password(password)  # user password
        user_obj.officer = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_officeruser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)  # can login
    officer = models.BooleanField(default=False)  # staff
    admin = models.BooleanField(default=False)  # superuser
    #timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # username
    # email and password are required by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.officer

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

##District Model
class District(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

	
#Subcounty Model
class Subcounty(models.Model):
    name=models.CharField(max_length=200)
	
	#Here we relate the district to the subcounty... each district has many subcounties but each subcounty belongs to only one District
    district = models.ForeignKey('District', on_delete=models.CASCADE,  # related_name='district', 
    null=True)
    def __str__(self):
        return self.name

class Parish(models.Model):
    name=models.CharField(max_length=200)
	
	#same as subcounty each parish belonngs to one subcounty but a subcounty has many parishes
    sub_county = models.ForeignKey('Subcounty', on_delete=models.CASCADE, #related_name='sub_county',
     null=True)
    def __str__(self):
        return self.name
       

class Village(models.Model):
    name = models.CharField(max_length=40, help_text='village name')
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)

    def __str__(self):
         return self.name

        


# here is the officer table
class Officer(models.Model):
    name = models.CharField(max_length=40, help_text='Enter your full name')
    login_id = models.EmailField(max_length=255, unique=True, help_text='Unique ID for every officer')
    password = models.CharField(max_length=8)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey(Subcounty, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


# here is the farmer table.

class Farmer(models.Model):
    name = models.CharField(max_length=40, help_text='enter your full name')
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey(Subcounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    # defining gender choices
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_year = models.DateField(help_text='date of birth')
    # defining marriage choices
    MARRIED = 'M'
    SINGLE = 'S'
    DIVORCED = 'D'
    MARRIAGE_CHOICES = (
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (DIVORCED, 'Divorced'),
    )
    marriage = models.CharField(
        max_length=1, choices=MARRIAGE_CHOICES, blank=True)
    # defining language choices
    LUGANDA = 'LUGANDA'
    LUSOGA = 'LUSOGA'
    ACHOLI = 'ACHOLI'
    RUNYANKOLE = 'RUNYANKOLE'
    LANGUAGE_CHOICES = (
        (LUGANDA, 'Luganda'),
        (LUSOGA, 'Lusoga'),
        (ACHOLI, 'Acholi'),
        (RUNYANKOLE, 'Runyankole'),
    )
    language = models.CharField(
        max_length=50, choices=LANGUAGE_CHOICES, blank=True)
    #phone = models.PhoneField(blank=True, help_text='contact')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    photo = models.FileField(upload_to='images/')
    # defining community status choices
    MOBILIZER = 'MOBILIZER'
    CHAIRMAN = 'CHAIRMAN'
    OTHER_ROLES = 'OTHER_ROLES'
    COMMUNITY_STATUS_CHOICES = (
        (MOBILIZER, 'Mobilizer'),
        (CHAIRMAN, 'Chairman'),
        (OTHER_ROLES, 'Other_roles'),
    )
    community_status = models.CharField(
        max_length=60, choices=COMMUNITY_STATUS_CHOICES, blank=True)
    # instructor possibility choice
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    instructor_possibility = models.BooleanField(choices=BOOL_CHOICES)
    # crop_type choice
    POTATO = 'POTATO'
    MAIZE = 'MAIZE'
    BEANS = 'BEANS'
    RICE = 'RICE'
    CROP_TYPE_CHOICES = (
        (POTATO, 'Potato'),
        (MAIZE, 'Maize'),
        (BEANS, 'Bean'),
        (RICE, 'Rice'),
    )
    crop_type = models.CharField(max_length=40, choices=CROP_TYPE_CHOICES)

    def __str__(self):
        return self.name


# session table
class Session(models.Model):
    A = '2018A'
    B = '2018B'
    C = '2018C'
    SESSION_ID_CHOICES = (
        (A, '2018A'),
        (B, '2018B'),
        (C, '2018C'),
    )
    session_id = models.AutoField(primary_key=True, choices=SESSION_ID_CHOICES)

    area = models.IntegerField('eg 2ac')

    harvest = models.IntegerField('eg 5000kg')

    def __str__(self):
        return self.session_id

# report table


class Report(models.Model):
    A = '2018A'
    B = '2018B'
    C = '2018C'
    SESSION_ID_CHOICES = (
        (A, '2018A'),
        (B, '2018B'),
        (C, '2018C'),
    )
    session_id = models.ForeignKey(
        Session, on_delete=models.CASCADE, choices=SESSION_ID_CHOICES)

    # Farm_area choices
    AC = '1-5 AC'
    AC = '2.0 AC'
    FARM_AREA_CHOICES = (
        (AC, '1-5 AC'),
        (AC, '2.0 AC'),
    )
    farm_area = models.CharField(max_length=20, choices=FARM_AREA_CHOICES)

    # Rice_type choice
    KAISO = 'K'
    SUPER = 'S'
    TILDA = 'T'
    RICE_TYPE_CHOICES = (
        (KAISO, 'Kaiso'),
        (SUPER, 'Super'),
        (TILDA, 'Tilda'),
    )
    rice_type = models.CharField(max_length=1, choices=RICE_TYPE_CHOICES)

    sowing_type = models.CharField(max_length=100)

    planting_type = models.CharField(max_length=100)

    # levelling choice
    BAD = 'B'
    FAIR = 'F'
    GOOD = 'G'
    LEVELLING_CHOICES = (
        (BAD, 'Bad'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
    )
    levelling = models.CharField(max_length=1, choices=LEVELLING_CHOICES)

    # rigde choices
    BAD = 'B'
    FAIR = 'F'
    GOOD = 'G'
    RIGDE_CHOICES = (
        (BAD, 'Bad'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
    )
    rigde = models.CharField(max_length=1, choices=RIGDE_CHOICES)

    # watercourse_state choices
    BAD = 'B'
    FAIR = 'F'
    GOOD = 'G'
    WATERCOURSE_STATE_CHOICES = (
        (BAD, 'Bad'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
    )
    watercourse_state = models.CharField(
        max_length=1, choices=WATERCOURSE_STATE_CHOICES)

    # fertilizer_choices
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    fertilizer = models.BooleanField(choices=BOOL_CHOICES)

    fertilizer_1_type = models.CharField(max_length=80)

    fertilizer_1_amount = models.IntegerField()

    fertilizer_2_type = models.CharField(max_length=80)

    fertilizer_2_amount = models.IntegerField()

    # weed_condition choices
    BAD = 'B'
    FAIR = 'F'
    GOOD = 'G'
    WEED_CONDITION_CHOICES = (
        (BAD, 'Bad'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
    )
    weed_condition = models.CharField(
        max_length=1, choices=WEED_CONDITION_CHOICES)

    harvest_date = models.DateField()
    # harvest_amount = models.IntegerField(null=True)
    # note = models.CharField(max_length=100, help_text='enter any text')
    # photo1 = models.FileField(upload_to='images/')
    # photo2 = models.FileField(upload_to='images/')
    # photo3 = models.FileField(upload_to='images/')
    # photo4 = models.FileField(upload_to='images/')
