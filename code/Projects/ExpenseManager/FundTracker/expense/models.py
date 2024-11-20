from django.db import models


class Transaction(models.Model):

    title = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    amount = models.FloatField()

    CATEGORY_OPTIONS = (
        ("Food","Food"),
        ("Fuel","Fuel"),
        ("Travel","Travel"),
        ("Rent","Rent"),
        ("Bills","Bills"),
        ("Shopping","Shopping"),
        ("HealthCare","HealthCare"),
        ("Miscellaneous","Miscellaneous")
    )

    category = models.CharField(max_length=200,choices=CATEGORY_OPTIONS,default="Food")

    PAYMENT_OPTIONS = (
        ("UPI","UPI"),
        ("CASH","CASH")
    )

    payment_method = models.CharField(max_length=200,choices=PAYMENT_OPTIONS,default="CASH")

    PRIORITY_OPTIONS = (
        ("NEED","NEED"),
        ("WANT","WANT")
    )

    priority = models.CharField(max_length=200,choices=PRIORITY_OPTIONS,default="NEED")

