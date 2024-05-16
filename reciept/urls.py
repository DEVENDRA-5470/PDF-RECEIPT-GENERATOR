
from django.contrib import admin
from django.urls import path
from newapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400,handler403,handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path('new_reg',views.new_reg,name='new_reg'),
    path('recents',views.recents,name='recents'),
    path('stu_pdf/<pk>/',views.student_pdf,name='student-pdf'),
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
