"""
URL configuration for dummyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('footer',views.footer),
    path('',views.index, name="index"),
    path('contactus',views.contactus, name="contactus"),
    path('login',views.login,name="login"),
    path('navbar',views.navbar),
    path('registration',views.registration,name="registration"),
    path('base',views.base),
    path('base2',views.base2),
    path('Agri_call_center',views.Agri_call_center,name="Agri_call_center"),
    path('Agri_crops',views.Agri_crops,name="Agri_crops"),
    path('Agri_farmer_scheme',views.Agri_farmer_scheme,name="Agri_farmer_scheme"),
    path('Agri_indian_uni',views.Agri_indian_uni,name="Agri_indian_uni"),
    path('Agri_latest_technology',views.Agri_latest_technology,name="Agri_latest_technology"),
    path('Agri_news',views.Agri_news,name="Agri_news"),
    path('Agri_uni',views.Agri_uni,name="Agri_uni"),
    path('Agri_videos',views.Agri_videos,name="Agri_videos"),
    path('review',views.review,name="review"),
    path('sidebar',views.sidebar,name="sidebar"),
    path('change_password',views.change_password,name="change_password"),
    path('help_support',views.help_support,name="help_support"),
    path('userprofile_s',views.userprofile,name="userprofile_s"),
    path('edit_profile_s',views.edit_profile_s,name="edit_profile_s"),
    path('forget',views.forget,name="forget"),
    path('logout',views.logout,name="logout"),
    path('crop_detail/<str:name>',views.crop_detail,name="crop_detail"),
    path('crop_detail2/<str:name>',views.crop_detail2,name="crop_detail2"),
    path('news_detail/<str:name>',views.news_detail,name="news_detail"),
    path('live',views.live,name="live"),
    path('e503',views.e503,name="e503"),
    path('disease_detection',views.disease_detection,name="disease_detection"),
    # path('detection_result',views.detection_result,name="detection_result"),
    
    
    
    
    
    
    
    
    
    

    
    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
