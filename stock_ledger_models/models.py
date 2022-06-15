from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




LOCATION_TYPE_CHOICES = (
        ("S", "Store"),
        ("W", "Warehouse")
    )
    
class Dept(models.Model):
    class Meta:
        db_table = 'dept'

    ACC_METHOD_CHOICES = (
        (1, "Direct Cost"),
        (2, "Retail Inventory")
    )

    PURCHASE_TYPE_CHOICES = (
        (0, "Normal Merchandise"),
        (1, "Consignment Stock"),
        (2, "Concession Items")
    )

    DEPT = models.CharField(max_length=10, primary_key=True)
    DEPT_DESC = models.CharField(max_length=40, null=True)
    ACC_METHOD = models.CharField(max_length=1, choices=ACC_METHOD_CHOICES)
    PURCHASE_TYPE = models.CharField(max_length=1, choices=PURCHASE_TYPE_CHOICES)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)


class Class(models.Model):
    class Meta:
        db_table = 'class'
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.CharField(max_length=10, primary_key=True)
    CLASS_DESC = models.CharField(max_length=40, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)


class SubClass(models.Model):
    class Meta:
        db_table = 'subclass'
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.CharField(max_length=10, primary_key=True)
    SUBCLASS_DESC = models.CharField(max_length=40, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)

class Calendar(models.Model):
    class Meta:
        db_table = 'calendar'
    YEAR = models.PositiveIntegerField(null=True)
    YEAR_START = models.DateField(null=True)
    CURR_MONTH = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True)
    CURR_MONTH_START = models.DateField(null=True)
    CURR_MONTH_END = models.DateField(null=True)
    CURR_WEEK = models.PositiveIntegerField(validators=[MaxValueValidator(7)], null=True)
    CURR_WEEK_START = models.DateField(null=True)
    CURR_WEEK_END = models.DateField(null=True)
    LAST_MONTH = models.PositiveIntegerField(validators=[MaxValueValidator(12)], null=True)
    LAST_MONTH_START = models.DateField(null=True)
    LAST_MONTH_END = models.DateField(null=True)
    LAST_WEEK = models.PositiveIntegerField(validators=[MaxValueValidator(7)], null=True)
    LAST_WEEK_START = models.DateField(null=True)
    LAST_WEEK_END = models.DateField(null=True)
    SYSTEM_DATE = models.DateField(null=True)


class Currency(models.Model):
    class Meta:
        db_table = 'CURRENCY'
    CURRENCY_CODE = models.CharField(max_length=3, primary_key=True)
    CURRENCY_DESC = models.CharField(max_length=60, null=True)
    EFFECTIVE_DATE = models.DateField()
    EXCHANGE_RATE = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)

class GL_Account(models.Model):
    class Meta:
        db_table = 'gl_account'
    PRIMARY_ACCOUNT = models.PositiveIntegerField()
    SET_OF_BOOKS_ID = models.PositiveIntegerField()
    SEGMENT1 = models.CharField(max_length=5, null=True)
    SEGMENT2 = models.CharField(max_length=5, null=True)
    SEGMENT3 = models.CharField(max_length=5, null=True)
    SEGMENT4 = models.CharField(max_length=5, null=True)
    SEGMENT5 = models.CharField(max_length=5, null=True)
    SEGMENT6 = models.CharField(max_length=5, null=True)
    SEGMENT7 = models.CharField(max_length=5, null=True)
    CURRENCY = models.CharField(max_length=3, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)


class ITEM_DTL(models.Model):
    class Meta:
        db_table = 'ITEM_DTL'

    PACK_IND_CHOICES = (
        ("Y", "Y"),
        ("N", "N")
    )

    STATUS_CHOICES = (
        ("A", "Active"),
        ("D", "Disabled")
    )

    ITEM = models.CharField(max_length=25)
    ITEM_PARENT = models.CharField(max_length=25, null=True)
    ITEM_GRANDPARENT = models.CharField(max_length=25, null=True)
    PACK_IND = models.CharField(max_length=1, choices=PACK_IND_CHOICES)
    ITEM_LEVEL = models.IntegerField(validators=[MaxValueValidator(9)], null=True)
    TRAN_LEVEL = models.IntegerField(validators=[MaxValueValidator(9)], null=True)
    DIFF1 = models.CharField(max_length=15, null=True)
    DIFF2 = models.CharField(max_length=15, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    STATUS = models.CharField(max_length=1, choices=STATUS_CHOICES)
    ITEM_DESC = models.CharField(max_length=100)
    SELLING_UOM = models.CharField(max_length=3, null=True)
    ORIGINAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    ORIGINAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)
    LAST_UPDATE_ID = models.CharField(max_length=25, null=True)
    UPDATE_DATETIME = models.DateTimeField(auto_now=True,null=True,blank=True)


class Location(models.Model):
    class Meta:
        db_table = 'LOCATION'

    STATUS_CHOICES = (
        ("A", "Active"),
        ("C", "Closed")
    )

    LOCATION = models.PositiveIntegerField(primary_key=True)
    LOCATION_NAME = models.CharField(max_length=50, null=True)
    LOCATION_TYPE = models.CharField(max_length=1, choices=LOCATION_TYPE_CHOICES)
    STATUS = models.CharField(max_length=1, choices=STATUS_CHOICES)
    CURRENCY_CODE = models.CharField(max_length=5, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)
    LAST_UPDATE_ID = models.CharField(max_length=25, null=True)
    UPDATE_DATETIME = models.DateTimeField(auto_now=True,null=True,blank=True)





PROCESS_IND_CHOICES = (
        ("N", "Ready to pick"),
        ("E", "Error"),
        ("P", "Processed")
    )

REF_ITEM_TYPE_CHOICES = (
        ("P", "PACK"),
        ("U", "UPC")
    )

TRN_TYPE_CHOICES = (
    ("SALES", "SALES"),
    ("RETURNS", "RETURNS"),
    ("PO", "PO"),
    ("TRANSFER", "TRANSFER")
)

class stg_trn_data(models.Model):
    class Meta:
        db_table = 'stg_trn_data'

    TRAN_SEQ_NO = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)])
    PROCESS_IND = models.CharField(max_length=1, choices=PROCESS_IND_CHOICES, null=True)
    ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.CharField(max_length=1,choices=LOCATION_TYPE_CHOICES, null=True,blank=True)
    LOCATION = models.PositiveIntegerField(null=True,blank=True,default=None)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    PACK_QTY = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999)])
    PACK_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    PACK_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    AREF = models.CharField(max_length=1, null=True)
    CURRENCY = models.CharField(max_length=3,null=True,blank=True,default=None)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    REV_NO = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    REV_TRN_NO = models.IntegerField(validators=[MaxValueValidator(99999999)], null=True)


class trn_data(models.Model):
    class Meta:
        db_table = 'trn_data'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    PROCESS_IND = models.CharField(max_length=1, choices=PROCESS_IND_CHOICES)
    ITEM = models.CharField(max_length=25, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,null=True,related_name="trn_location_type")
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,null=True,related_name="trn_location_name")
    TRN_POST_DATE = models.DateField(null=True)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField(null=True)
    SELLING_UOM = models.CharField(max_length=3)
    PACK_QTY = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999)])
    PACK_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    PACK_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.DO_NOTHING)
    CREATE_ID = models.CharField(max_length=25, null=True)
    REV_NO = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    REV_TRN_NO = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)])


class trn_data_history(models.Model):
    class Meta:
        db_table = 'trn_data_history'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    PROCESS_IND = models.CharField(max_length=1, choices=PROCESS_IND_CHOICES)
    ITEM = models.CharField(max_length=25, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,null=True,related_name="history_location_type")
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,null=True,related_name="history_location_name")
    TRN_POST_DATE = models.DateField(null=True)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField(null=True)
    SELLING_UOM = models.CharField(max_length=3)
    PACK_QTY = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999)])
    PACK_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    PACK_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.DO_NOTHING)
    CREATE_ID = models.CharField(max_length=25, null=True)
    REV_NO = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    REV_TRN_NO = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)])
    ARCHIVE_DATETIME = models.DateTimeField()


class trn_data_rev(models.Model):
    class Meta:
        db_table = 'trn_data_rev'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    ITEM = models.CharField(max_length=25, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="trn_rev_location_type",null=True)
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="trn_rev_location_name",null=True)
    TRN_POST_DATE = models.DateField(null=True)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField(null=True)
    TOTAL_TRN_COST = models.PositiveIntegerField(null=True)
    TOTAL_TRN_RETAIL = models.PositiveIntegerField(null=True)
    REF_NO_1 = models.PositiveIntegerField(null=True)
    REF_NO_2 = models.PositiveIntegerField(null=True)
    REF_NO_3 = models.PositiveIntegerField(null=True)
    REF_NO_4 = models.PositiveIntegerField(null=True)
    UPDATE_DATETIME=models.DateTimeField(auto_now=True)
    CREATE_ID = models.CharField(max_length=25)
    REV_NO = models.IntegerField()
    REV_TRN_NO = models.IntegerField()


class err_trn_data(models.Model):
    class Meta:
        db_table = 'err_trn_data'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    PROCESS_IND = models.CharField(max_length=1, choices=PROCESS_IND_CHOICES)
    ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="err_location_type",null=True)
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="err_location_name",null=True)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField(null=True)
    PACK_QTY = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999)])
    PACK_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    PACK_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.DO_NOTHING)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)
    REV_TRN_NO = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)])
    ERR_MSG=models.CharField(max_length=100, choices=TRN_TYPE_CHOICES)
    ERR_SEQ_NO=models.IntegerField()


class transaction_data_expl(models.Model):
    class Meta:
        db_table = 'transaction_data_expl'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    ITEM = models.CharField(max_length=25, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL, null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    REF_ITEM = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=1, null=True, choices=REF_ITEM_TYPE_CHOICES)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="txn_location_type",null=True)
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="txn_location_name",null=True)
    TRN_DATE = models.DateField(auto_now=True)
    TRN_TYPE = models.CharField(max_length=10, null=True, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField(null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.DO_NOTHING)
    CREATE_ID = models.CharField(max_length=25)


class item_location(models.Model):
    class Meta:
        db_table = 'item_location'
    STATUS_CHOICES = (
        ("A", "Active"),
        ("I", "Inactive"),
        ("D", "Deleted"),
        ("C", "Discontinued")
    )
    ITEM = models.CharField(max_length=25)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="item_location_type",null=True)
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="item_location_name",null=True)
    ITEM_PARENT = models.CharField(max_length=25, null=True)
    ITEM_GRANDPARENT = models.CharField(max_length=25, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    SELLING_UOM = models.CharField(max_length=3, null=True)
    STATUS = models.CharField(max_length=1, choices=STATUS_CHOICES)
    STATUS_UPDATE_DATE = models.DateField(null=True)
    ITEM_SOH = models.DecimalField(max_digits=20,decimal_places=4)
    SOH_UPDATE_DATETIME = models.DateField(null=True)
    SHIPPED_QTY = models.PositiveIntegerField()
    RESERVED_QTY = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    RTV_QTY = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    EXPECTED_QTY = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    RECEIVED_QTY = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    CREATE_ID = models.CharField(max_length=25, null=True)
    CREATE_DATETIME = models.DateTimeField(auto_now_add=True)
    LAST_UPDATE_ID = models.CharField(max_length=25, null=True)
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)


class sl_control(models.Model):
    class Meta:
        db_table = 'sl_control'
    CONTROL_IND = models.CharField(max_length=1, null=True)
    PROGRAM_NAME = models.CharField(max_length=255, null=True)


class stg_fin_data(models.Model):
    class Meta:
        db_table = 'stg_fin_data'
    SET_OF_BOOKS_ID = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])    
    ACCOUNTING_DATE = models.DateField(null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.SET_NULL, null=True)
    TRN_DATE = models.DateField(null=True)
    EXCHANGE_RATE = models.DecimalField(max_digits=20,decimal_places=4)
    DEBIT_AMOUNT = models.DecimalField(max_digits=20,decimal_places=4)
    CREDIT_ACCOUNT = models.DecimalField(max_digits=20,decimal_places=4)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    PRIMARY_ACCOUNT = models.PositiveIntegerField(null=True)
    PRIMARY_CURR_CODE = models.CharField(max_length=3)
    PRIMARY_DEBIT_AMT = models.DecimalField(max_digits=20,decimal_places=4)
    PRIMARY_CREDIT_AMT = models.DecimalField(max_digits=20,decimal_places=4)


class pndg_dly_rollup(models.Model):
    class Meta:
        db_table = 'pndg_dly_rollup'
    TRAN_SEQ_NO = models.ForeignKey(to=stg_trn_data, on_delete=models.CASCADE)
    PROCESS_IND = models.CharField(max_length=1, choices=PROCESS_IND_CHOICES)
    ITEM = models.CharField(max_length=25, null=True)
    DEPT = models.ForeignKey(to=Dept, on_delete=models.SET_NULL,null=True)
    CLASS = models.ForeignKey(to=Class, on_delete=models.SET_NULL, null=True)
    SUBCLASS = models.ForeignKey(to=SubClass, on_delete=models.SET_NULL, null=True)
    REF_ITEM_NO = models.CharField(max_length=25, null=True)
    REF_ITEM_TYPE = models.CharField(max_length=10, null=True)
    LOCATION_TYPE = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="pndg_location_type",null=True)
    LOCATION = models.ForeignKey(to=Location, on_delete=models.SET_NULL,related_name="pndg_location_name",null=True)
    TRN_POST_DATE = models.DateField()
    TRN_DATE = models.DateField()
    TRN_TYPE = models.CharField(max_length=10, choices=TRN_TYPE_CHOICES)
    QTY = models.PositiveIntegerField()
    SELLING_UOM = models.CharField(max_length=3, null=True)
    UNIT_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    UNIT_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    TOTAL_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    REF_NO1 = models.CharField(max_length=10, null=True)
    REF_NO2 = models.CharField(max_length=10, null=True)
    REF_NO3 = models.CharField(max_length=10, null=True)
    REF_NO4 = models.CharField(max_length=10, null=True)
    PACK_QTY = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(9999)])
    PACK_COST = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    PACK_RETAIL = models.DecimalField(max_digits=20,decimal_places=4, null=True)
    CURRENCY = models.ForeignKey(to=Currency, on_delete=models.DO_NOTHING)
    REV_NO = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    REV_TRN_NO = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    CREATE_ID = models.CharField(max_length=25)
    ARCHIVE_DATETIME = models.DateTimeField()


class date_range(models.Model):
    class Meta:
        db_table = 'date_range'

    YEAR = models.PositiveIntegerField(null=True)
    MONTH_START = models.DateField(null=True)
    WEEK_START = models.DateField(null=True)
    MONTH_END = models.DateField(null=True)
    WEEK_END = models.DateField(null=True)
    MONTH_NO = models.PositiveIntegerField(validators=[MaxValueValidator(12)], null=True)
    WEEK_NO = models.PositiveIntegerField(validators=[MaxValueValidator(12)], null=True)
    DAILY_DATE = models.DateField(null=True)
    WEEK_CLOSE_IND = models.CharField(max_length=1)
    DAY_CLOSE_IND = models.CharField(max_length=1)
    MONTH_CLOSE_IND = models.CharField(max_length=1)


class stg_trn_data_del_records(models.Model):
    class Meta:
        db_table = 'stg_trn_data_del_records'
    DATE = models.DateField(auto_now_add=True)
    PROCESS = models.CharField(max_length=30)
    RECORDS_CLEANED = models.PositiveIntegerField()