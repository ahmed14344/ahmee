from django.db import models

class Course(models.Model):
    title = models.CharField("عنوان الدورة", max_length=150)
    description = models.TextField("وصف الدورة")
    price = models.DecimalField("السعر", max_digits=8, decimal_places=2)
    duration_hours = models.PositiveIntegerField("المدة (ساعات)")
    image = models.ImageField("صورة الدورة", upload_to="courses/", blank=True, null=True)  # ✅ جديد
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "دورة"
        verbose_name_plural = "الدورات"

    def __str__(self):
        return self.title
