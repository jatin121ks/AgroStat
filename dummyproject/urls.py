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
    path('fertilizer_detection',views.fertilizer_detection,name="fertilizer_detection"),
    path('predict_crop_rice',views.predict_crop_rice,name="predict_crop_rice"),
    path('predict_crop_maize',views.predict_crop_maize,name="predict_crop_maize"),
    path('predict_population',views.predict_population,name="predict_population"),
    path('predict_crop_wheat',views.predict_crop_wheat,name="predict_crop_wheat"),
    path('register_otp',views.register_otp,name="register_otp"),
    path('predict_fruit',views.predict_fruit,name="predict_fruit"),
    path('f1',views.f1,name="f1"),
    path('f2',views.f2,name="f2"),
    path('f3',views.f3,name="f3"),
    path('f4',views.f4,name="f4"),
    path('f5',views.f5,name="f5"),
    path('f6',views.f6,name="f6"),
    path('f7',views.f7,name="f7"),
    path('f8',views.f8,name="f8"),
    path('f9',views.f9,name="f9"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('chat/',views.chat,name="chat"),
    path('chat1/',views.chat1,name="chat1"),
    path('fertilizer_link/',views.fertilizer_link,name="fertilizer_link"),
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
