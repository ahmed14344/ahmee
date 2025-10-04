from django.db import models
from Accounts.models import Customer
from Courses.models import Course

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="العميل")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="الدورة")
    booking_date = models.DateTimeField("تاريخ الحجز", auto_now_add=True)
    scheduled_date = models.DateTimeField("الموعد المحدد")
    is_paid = models.BooleanField("تم الدفع", default=False)

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"

    def __str__(self):
        return f"{self.customer.full_name} - {self.course.title}"
