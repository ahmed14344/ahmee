from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView   # عشان نعرض الصفحة مباشرة بدون view مخصص

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),  # الصفحة الرئيسية
    path('admin/', admin.site.urls),                 # لوحة التحكم
    path('accounts/', include('Accounts.urls')),     # روابط تطبيق الحسابات
    path('courses/', include('Courses.urls')),       # روابط تطبيق الدورات
    path('booking/', include('Booking.urls')),       # روابط تطبيق الحجز
]

# ✅ إضافة دعم الملفات الثابتة والمرفوعة أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
