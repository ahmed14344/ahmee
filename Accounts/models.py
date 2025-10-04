from django.db import models

class Customer(models.Model):
    full_name = models.CharField("الاسم الكامل", max_length=100)
    email = models.EmailField("البريد الإلكتروني", unique=True)
    phone = models.CharField("رقم الجوال", max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField("تاريخ التسجيل", auto_now_add=True)

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"

    def __str__(self):
        return self.full_name
