from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),      # لوحة التحكم
    path('accounts/', include('Accounts.urls')),  # روابط تطبيق الحسابات
    path('courses/', include('Courses.urls')),    # روابط تطبيق الدورات
    path('booking/', include('Booking.urls')),    # روابط تطبيق الحجز
]
