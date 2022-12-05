# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



class OpdPackagemaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    companycd = models.CharField(max_length=20)
    locationcd = models.CharField(max_length=20)
    packdesigncd = models.CharField(max_length=10)
    tariffcd = models.CharField(max_length=10)
    f_gtrf_tariffcd = models.CharField(max_length=20)
    pkgcd = models.CharField(max_length=20)
    pkgname = models.CharField(max_length=200)
    packagetype = models.CharField(max_length=100)
    departmentcd = models.CharField(max_length=20)
    f_getdept_departmentcd = models.CharField(max_length=100)
    isactive = models.CharField(max_length=10, blank=True, null=True)
    predays = models.IntegerField()
    postdays = models.IntegerField()
    effectfrom = models.DateField()
    effectto = models.DateField()
    pkgduration = models.IntegerField()
    pkgamount = models.BigIntegerField()
    pkgatlamount = models.BigIntegerField()
    createby = models.CharField(max_length=50)
    createdt = models.DateField()
    modifyby = models.CharField(max_length=20)
    modifydt = models.DateField(blank=True, null=True)
    equservicecd = models.CharField(max_length=20)
    includes = models.CharField(max_length=100)
    excludes = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    costcentercd = models.CharField(max_length=10)
    procedurecd = models.CharField(max_length=20)
    procedurename = models.CharField(max_length=20)
    priority1 = models.CharField(max_length=20)
    priority2 = models.CharField(max_length=20)
    priority3 = models.CharField(max_length=20)
    priority4 = models.CharField(max_length=20)
    reqdischargemedition = models.CharField(max_length=10)
    iseditdaysinpkgbilling = models.CharField(max_length=10)

    class Meta:
        # managed = False
        db_table = 'opd_packagemaster'

    def __str__(self):
        return self.companycd or ''

class OpdRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    upid = models.CharField(unique=True, max_length=20)
    registration_no = models.CharField(unique=True, max_length=20)
    title = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=50)
    patient_profile = models.CharField(max_length=100, blank=True, null=True)
    registration_type = models.CharField(max_length=20)
    is_vip = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=13)
    alt_mobile = models.CharField(max_length=13, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=10)
    passport_no = models.CharField(max_length=20, blank=True, null=True)
    patient_type = models.CharField(max_length=20)
    referral_type = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    registration_fees = models.IntegerField(blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    concession = models.IntegerField(blank=True, null=True)
    receipt_no = models.CharField(max_length=100, blank=True, null=True)
    cash_amt = models.IntegerField(blank=True, null=True)
    card_amt = models.IntegerField(blank=True, null=True)
    cheque_amt = models.IntegerField(blank=True, null=True)
    cheque_no = models.CharField(max_length=100, blank=True, null=True)
    cheque_date = models.DateTimeField(blank=True, null=True)
    cheque_bank = models.CharField(max_length=100, blank=True, null=True)
    card_no = models.CharField(max_length=100, blank=True, null=True)
    card_bank = models.CharField(max_length=100, blank=True, null=True)
    card_exp_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    registration_validity = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_time = models.TimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    canceled_by = models.CharField(max_length=100, blank=True, null=True)
    canceled_date = models.DateTimeField(blank=True, null=True)
    company_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'opd_registration'


    def __str__(self):
        return self.upid or ''

class OpdSourceofconsultationcharges(models.Model):
    id = models.BigAutoField(primary_key=True)
    companycd = models.CharField(max_length=10, blank=True, null=True)
    locationcd = models.CharField(max_length=10, blank=True, null=True)
    sofchargecd = models.CharField(max_length=10, blank=True, null=True)
    tariffcd = models.CharField(max_length=10, blank=True, null=True)
    f_gtrf_tariffcd = models.CharField(max_length=100, blank=True, null=True)
    doctorcd = models.CharField(max_length=10, blank=True, null=True)
    doctorname = models.CharField(max_length=200, blank=True, null=True)
    charge = models.IntegerField(blank=True, null=True)
    emergencycharge = models.IntegerField(blank=True, null=True)
    revisitcharge = models.IntegerField(blank=True, null=True)
    servicetype = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.CharField(max_length=100, blank=True, null=True)
    servicegroupcd = models.CharField(max_length=100, blank=True, null=True)
    f_getdept_servicegroupcd = models.CharField(max_length=100, blank=True, null=True)
    equservicecd = models.CharField(max_length=100, blank=True, null=True)
    hosppercent = models.IntegerField(blank=True, null=True)
    docpercent = models.IntegerField(blank=True, null=True)
    hospamount = models.IntegerField(blank=True, null=True)
    docamount = models.IntegerField(blank=True, null=True)
    servicefor = models.CharField(max_length=100, blank=True, null=True)
    ispackage = models.CharField(max_length=100, blank=True, null=True)
    isprocedure = models.CharField(max_length=100, blank=True, null=True)
    isoutside = models.CharField(max_length=100, blank=True, null=True)
    visits = models.CharField(max_length=100, blank=True, null=True)
    noofdays = models.IntegerField(blank=True, null=True)
    visittype = models.CharField(max_length=100, blank=True, null=True)
    emergencyhospamount = models.IntegerField(blank=True, null=True)
    revisithospamount = models.IntegerField(blank=True, null=True)
    emergencydocamount = models.IntegerField(blank=True, null=True)
    revisitdocamount = models.IntegerField(blank=True, null=True)
    createby = models.CharField(max_length=50, blank=True, null=True)
    createdt = models.DateTimeField(blank=True, null=True)
    modifyby = models.CharField(max_length=20, blank=True, null=True)
    modifydt = models.DateTimeField(blank=True, null=True)
    chargetype = models.CharField(max_length=100, blank=True, null=True)
    regfee = models.CharField(max_length=100, blank=True, null=True)
    billinghead = models.CharField(max_length=100, blank=True, null=True)
    costcentercd = models.CharField(max_length=100, blank=True, null=True)
    activationdt = models.DateTimeField(blank=True, null=True)
    reviewdt = models.CharField(max_length=100, blank=True, null=True)
    isneverexp = models.CharField(max_length=100, blank=True, null=True)
    ismanualchargesmodify = models.CharField(max_length=100, blank=True, null=True)
    opdisc = models.CharField(max_length=100, blank=True, null=True)
    ipdisc = models.CharField(max_length=100, blank=True, null=True)
    noofdaysforip = models.CharField(max_length=100, blank=True, null=True)
    ipvisits = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'opd_sourceofconsultationcharges'

    def __str__(self):
        return self.companycd or ''

class User(AbstractUser):
    user_name= None
    employee_id= models.IntegerField(unique=True)
    first_name=models.CharField(max_length=150)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects= UserManager()

    USERNAME_FIELD= 'employee_id'
    REQUIRED_FIELDS= []
    #
    # def __int__(self):
    #     return self.employee_id

    def __str__(self):
        return self.first_name or ''


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_code = models.CharField(max_length=50)
    category_code = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=50, unique=True)
    # employee_contact = models.IntegerField(unique=True)
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=50)
    relegion = models.CharField(max_length=100)
    relegion_description = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    factory_act_flag = models.CharField(max_length=100)
    designation_code = models.CharField(max_length=50)
    class_of_employee = models.CharField(max_length=100)
    weekly_off_day = models.CharField(max_length=100)
    direct_recruity_promotee = models.CharField(max_length=100)
    section_code = models.CharField(max_length=50)
    dob = models.DateField()
    initial_appointment_date = models.DateField()
    date_of_regular = models.DateField()
    date_of_last_increment_drawn = models.DateField()
    date_of_medical_examination_done = models.DateField()
    basic_pay = models.BigIntegerField()
    protected_pay = models.BigIntegerField()
    grade_pay = models.BigIntegerField()
    special_pay = models.BigIntegerField()
    family_planning_pay = models.BigIntegerField()
    telangana_incentive = models.BigIntegerField()
    graduation_increment = models.BigIntegerField()
    equalisation_allowance = models.BigIntegerField()
    special_allowance = models.BigIntegerField()
    special_allowance1 = models.BigIntegerField()
    father_spouse_name = models.CharField(max_length=50)
    caste_code = models.CharField(max_length=100)
    caste_description = models.CharField(max_length=100)
    subcast_code = models.CharField(max_length=100)
    subcast_description = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    native_place = models.CharField(max_length=100)
    native_dist_code = models.CharField(max_length=50)
    native_district = models.CharField(max_length=50)
    date_of_promotion_to_present_post = models.DateField()
    date_from_working_in_present_place = models.DateField()
    date_of_probation_declared = models.DateField()
    date_of_confirmation = models.DateField()
    date_of_splgrade_12yrs = models.DateField()
    date_of_splgrade_20yrs = models.DateField()
    opted_zone_while_appointment = models.CharField(max_length=50)
    opted_region_while_appointment = models.CharField(max_length=50)
    opted_division_while_appointment = models.CharField(max_length=50)
    physically_handicapped_falg = models.CharField(max_length=50)
    nature_of_appointment = models.CharField(max_length=50)
    nature_of_promotion = models.CharField(max_length=50)



    # def __str__(self):
    #     return str(self.name)
    class Meta:
        # managed = False
        db_table = 'employees'

    def __str__(self):
        return self.name or ''

