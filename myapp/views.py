from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from myapp.models import Agriculture_Universities
from myapp.models import Agriculture_News
from myapp.models import Agriculture_Videos
from myapp.models import Agriculture_Crop
from myapp.models import Agriculture_Call_centre
from myapp.models import Agriculture_Farmer_Scheme
from myapp.models import Latest_Technology
from myapp.models import Indian_Agriculture_University
from myapp.models import myreview
from myapp.models import contact
from myapp.models import register
from myapp.models import agri_crops_details
from myapp.models import disease_solution
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model




# Create your views here.
def footer(request):
     return render (request,'footer.html')

def contactus(request):
     if request.method == "POST":
          x=contact()
          x.name=request.POST.get('name')
          x.email=request.POST.get('mail')
          x.message=request.POST.get('comment')
          x.save()
          return render (request,'contactus.html',{'msg':1})
     else:
          return render (request,'contactus.html')

def index(request):
     return render (request,'index.html')

def login(request):
     if request.method=="POST" :
          em=request.POST.get("email")
          pw=request.POST.get("password")
          
          user=register.objects.filter(email=em,password=pw)
          k=len(user)
          if k>0:
               request.session['email']=em
               return redirect('/userprofile_s')
          else:
               return render(request,'login.html',{'msg':1})
          
     else:
          return render (request,'login.html')

def userprofile(request):
     user=register.objects.get(email=request.session['email'])
     return render(request,'userprofile_s.html',{'user':user})

def navbar(request):
     return render (request,'navbar.html')

def registration(request):
     if request.method == "POST":
          n=request.POST.get("name")
          e=request.POST.get("email")
          p=request.POST.get("password")
          c=request.POST.get("cpass")
          if register.objects.filter(email=e).exists():
             
               return render (request,'registration.html',{'msg' : 1})
          else: 
               if p == c:
                    x=register()
                    x.name=n
                    x.email=e
                    x.password=p
                    x.save()
                    
                    return render (request,'registration.html',{'msg' : 2})
               else:
                
                    return render (request,'registration.html',{'msg' : 3})
     else:
          return render (request,'registration.html')
          
                    

def base(request):
     return render(request,'base.html')

def e503(request):
     return render(request,'error503.html')

def base2(request):
     return render(request,'base2.html')

def Agri_call_center(request):
     x=Agriculture_Call_centre.objects.all()
     return  render(request, 'Agri_call_center.html',{'data':x})
def Agri_crops(request):
     x=Agriculture_Crop.objects.all()
     return  render(request, 'Agri_crops.html',{'data':x})

def crop_detail(request,name):
     
     x=agri_crops_details.objects.filter(crop_identity=name)
     return  render(request, 'Agri_crops_detail1.html',{'data':x})

def crop_detail2(request,name):
     
     x=agri_crops_details.objects.filter(crop_head=name)
     return  render(request, 'Agri_crops_detail2.html',{'data':x})

def Agri_farmer_scheme(request):
     x=Agriculture_Farmer_Scheme.objects.all()
     return  render(request, 'Agri_farmer_scheme.html',{'data':x})
def Agri_indian_uni(request):
     x=Indian_Agriculture_University.objects.all()
     return  render(request, 'Agri_indian_uni.html',{'data':x})
def Agri_latest_technology(request):
     x=Latest_Technology.objects.all()
     return  render(request, 'Agri_latest_technology.html',{'data':x})
def Agri_news(request):
     x=Agriculture_News.objects.all()
     return  render(request, 'Agri_news.html',{'data':x})

def news_detail(request,name):
     x=Agriculture_News.objects.filter(title=name)
     return  render(request, 'news_detail.html',{'data':x})
def Agri_uni(request):
     x=Agriculture_Universities.objects.all()
     return  render(request, 'Agri_uni.html',{'data':x})
def Agri_videos(request):
     x=Agriculture_Videos.objects.all()
     return  render(request, 'Agri_videos.html',{'data':x})

def review(request):
     
     if request.method == "POST":
          x=myreview()
          x.title=request.POST.get('ti')
          x.message=request.POST.get('msg')
          x.save()
          return render(request,'review.html',{'msg':1})
     else:
          return render(request,'review.html')

def sidebar(request):
     return render(request,'sidebar.html')
     
def change_password(request):
     return render(request,'change_password.html')

def help_support(request):
     return render(request,'help_support.html')

def handle_uploaded_file(f,name):
     destination = open(name, 'wb+')
     for chunk in f.chunks():
          destination.write(chunk)
     destination.close()

def disease_detection(request):
     if request.method=='POST':
    

          # Load the model from HDF5 file
          model = load_model("save1.h5")  # Replace this with the path to your model

          f = request.FILES['file1'] # here you get the files needed
          handle_uploaded_file(f,'STATIC/'+f.name)
          # Load the image you want to classify
          image_path = 'STATIC/'+f.name  # Replace this with the path to your image
          print('image_path',image_path)
          img = image.load_img(image_path, target_size=(256, 256))

          # Preprocess the image
          img_array = image.img_to_array(img)
          img_array = np.expand_dims(img_array, axis=0)
          img_array /= 255.  # Rescale to [0, 1] as done during training

          # Make predictions
          predictions = model.predict(img_array)
          classes=['Apple_Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

          # Get the predicted class
          predicted_class_index = np.argmax(predictions)
          predicted_class = classes[predicted_class_index]
      

          # # Make predictions
          # predictions = model.predict(img_array)
          # classes=['Apple_Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

          # # Get the predicted class
          # predicted_class_index = np.argmax(predictions)
          # predicted_class = classes[predicted_class_index]

          # Get the exact class name
          # class_labels = train_generator.class_indices
          # exact_class_name = list(class_labels.keys())[predicted_class_index]

          print("Predicted class:", predicted_class)
          # print("Exact class name:", exact_class_name)
          
          if predicted_class == 'Apple_Apple_scab':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___Black_rot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___Cedar_apple_rust':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Apple___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Blueberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Cherry_(including_sour)___Powdery_mildew':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Cherry_(including_sour)___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Common_rust_':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___Northern_Leaf_Blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Corn_(maize)___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Black_rot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Esca_(Black_Measles)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Grape___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Orange___Haunglongbing_(Citrus_greening)':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Peach___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Peach___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Pepper,_bell___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Pepper,_bell___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___Early_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___Late_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Potato___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Raspberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Soybean___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Squash___Powdery_mildew':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Strawberry___Leaf_scorch':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Strawberry___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Bacterial_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Early_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Late_blight':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Leaf_Mold':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Septoria_leaf_spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Spider_mites Two-spotted_spider_mite':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Target_Spot':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___Tomato_mosaic_virus':
               o=disease_solution.objects.filter(description=predicted_class)
          elif predicted_class == 'Tomato___healthy':
               o=disease_solution.objects.filter(description=predicted_class)
          else:
               o="No Disease Detection"
          
          

          return render(request,'detection_result.html',{'data':o})
          
     else:
          return render(request,'disease_detection.html')
     
# def detection_result(request):
#      return render(request,'detection_result.html')
     
     
def change_password(request):
     if request.method=='POST':
          o=request.POST.get('op')
          n=request.POST.get('np')
          c=request.POST.get('cp')
          
          if n==c:
               user=register.objects.get(email=request.session['email'])
               p=user.password
               
               if p==o:
                    user.password=n
                    user.save()
                    msg='Password successfully changed'
                    return render(request,'change_password.html',{'msg':1})
               else:
                    msg='old password not correct'
                    return render(request,'change_password.html',{'msg':2})
          else:
               msg='New pass and confirm pass not match'
               return render(request,'change_password.html',{'msg':3})
     else:
          return render(request,'change_password.html')
               

def edit_profile_s(request):
     user=register.objects.get(email=request.session['email'])
     if request.method=='POST':
          user.name=request.POST.get("nm")
          user.email=request.POST.get("em")
          user.contact=request.POST.get("ph")
          user.address=request.POST.get("ad")
          user.gender=request.POST.get("gn")
          user.age=request.POST.get("ag")
          user.save()
          
          
          return redirect('/userprofile_s')
     else:
          return render (request,'edit_profile_s.html',{'user':user})
          

def forget(request):
     if (request.method == 'POST'):
          em=request.POST.get('email')
          user=register.objects.filter(email=em)
          if(len(user)>0):
               password=user[0].password
               subject="Password"
               message="Hi your password is '"+ password +"'"
               email_from=settings.EMAIL_HOST_USER
               recipient_list=[em]  
               send_mail(subject,message,email_from,recipient_list)
               return render(request,'login.html')
          else:
               return render(request,'forget.html',{'msg':2}) 
     else:
          return render(request,"forget.html")   


def logout(request):
     if not request.session.has_key('email'):
          return redirect('/login')
     del request.session['email']
     return redirect('/login')

def live(request):
     import datetime
     from datetime import date
     from newsapi import NewsApiClient
     newsapi = NewsApiClient(api_key='b5bebd12136d4ecf8878f2060de6d277')

     json_data = newsapi.get_everything(q='Agriculture',language= 'en',from_param=str(date. today() - datetime. timedelta(days=29)),to=str (date.today()),page_size=21,page = 1,sort_by='relevancy')
     k=json_data['articles']
     return render (request,'live_news.html',{'k':k})
     

# add def fuction to the urls
#copy from admin.py the import lines
#then we have to make dictionary for the data in each table in views.py
#and then pass that dict into template file
