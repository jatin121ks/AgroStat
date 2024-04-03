from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
import random
from myapp.models import Agriculture_Universities
from myapp.models import Agriculture_News
from myapp.models import Agriculture_Videos
from myapp.models import Agriculture_Crop
from myapp.models import Agriculture_Call_centre
from myapp.models import Agriculture_Farmer_Scheme
from myapp.models import Latest_Technology
from myapp.models import Indian_Agriculture_University
from myapp.models import myreview
from myapp.models import support
from myapp.models import contact
from myapp.models import register
from myapp.models import agri_crops_details
from myapp.models import disease_solution
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import warnings
import itertools
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
import plotly.graph_objects as go





def f1(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Entity"].drop_duplicates().tolist()
     return render(request,"md1.html",{"data":column})
def f2(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Year"].drop_duplicates().tolist()
     return render(request,"md2.html",{"data":column})
def f3(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Entity"].drop_duplicates().tolist()
     column1=data["Year"].drop_duplicates().tolist()
     return render(request,"md3.html",{"data":column,"year":column1})
def f4(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Entity"].drop_duplicates().tolist()
     return render(request,"md4.html",{"data":column})
def f5(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Entity"].drop_duplicates().tolist()
     return render(request,"md5.html",{"data":column})
def f6(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Entity"].drop_duplicates().tolist()
     column1=data["Year"].drop_duplicates().tolist()
     return render(request,"md6.html",{"data":column,"year":column1})
def f7(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Year"].drop_duplicates().tolist()
     return render(request,"md7.html",{"data":column})
def f8(request):
     data=pd.read_csv("fertilizers.csv")
     column=data["Year"].drop_duplicates().tolist()
     return render(request,"md8.html",{"data":column})



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
                    otp=random.randrange(1000,9999)
                    print(otp)

                    #mixed
                    j6="0123456789"
                    j7=random.sample(j6,6)
                    print(j7)

                    j8=""
                    for i in j7:
                         j8=j8+i
                    
                    # request.session['otp'] = j8
                         
                    subject="OTP"
                    message="Hi your OTP is '"+ j8 +"'"
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[e]  
                    send_mail(subject,message,email_from,recipient_list)
                         
                    # x=register()
                    # x.name=n
                    # x.email=e
                    # x.password=p
                 #  x.save()
                    
                    return render (request,'register_otp.html',{'msg' : 2,'name':n,'email':e,'password':p,'otp':j8})
               else:
                
                    return render (request,'registration.html',{'msg' : "3"})
     else:
          return render (request,'registration.html')
          
     
def register_otp(request):
     if request.method == "POST":
          n=request.POST.get("name")
          e=request.POST.get("email")
          p=request.POST.get("password")
          otp=request.POST.get("otp")
          generated_otp=request.POST.get("org")
          
          
          if  otp==generated_otp:
               #del request.session['otp']
               x=register()
               x.name=n
               x.email=e
               x.password=p
               x.save()
               
               return redirect('/login',{ 'msg' : 2 })
          else:
               return render(request,'register_otp.html',{ 'msg' : 4 })
     else:
          return render(request,'register_otp.html')
               
               
               
          
               
     
     
                  

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
     if not request.session.has_key('email'):
          return render(request,'/login')
     if request.method == 'POST':
          x=support()
          x.title = request.POST.get('tt')
          x.content = request.POST.get('ct')
          x.save()
          return render(request,'help_support.html',{'msg':1})
     else:
          return render(request,'help_support.html')
          
          

def handle_uploaded_file(f,name):
     destination = open(name, 'wb+')
     for chunk in f.chunks():
          destination.write(chunk)
     destination.close()

def predict_crop_rice(request):
     if request.method=='POST':
          df=pd.read_csv("rice-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Production']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Production'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Rice Production of "+country,
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'rice_prediction.html')
     

def predict_crop_maize(request):
     if request.method=='POST':
          df=pd.read_csv("maize-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Maize | 00000056 || Production | 005510 || tonnes']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Maize | 00000056 || Production | 005510 || tonnes'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Maize Production of "+country,
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'maize_prediction.html')
     

def predict_fruit(request):
     if request.method=='POST':
          fruit=request.POST.get('fruit')
          
          if fruit == 'Banana':
               address="banana-production.csv"
          elif  fruit == 'Orange':
               address="orange-production.csv"
          elif  fruit == 'Apple':
               address="apple-production.csv"
          elif  fruit == 'Avocado':
               address="avocado-production.csv"
               
          
          
          df=pd.read_csv(address,parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Production']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Production'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title= fruit+ " Production of "+country,
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'fruit_prediction.html')
     
      
     
     
def predict_population(request):
     if request.method=='POST':
          df=pd.read_csv("share_of_the_.population_in_agriculture.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','share_employed_agri']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['share_employed_agri'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          pred_uc_year = pred_uc.predicted_mean.index.year

          fig.add_trace(go.Scatter(x=pred_uc_year, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Population of "+country+" employed in Agriculture",
          xaxis_title="Year",
          yaxis_title="Production",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'population_prediction.html')
          
def predict_crop_wheat(request):
     if request.method=='POST':
          df=pd.read_csv("wheat-production.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Wheat | 00000015 || Production | 005510 || tonnes']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Wheat | 00000015 || Production | 005510 || tonnes'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Wheat Production of "+country,
          xaxis_title="Year",
          yaxis_title="Use",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'wheat_production.html')
     

def fertilizer_detection(request):
     if request.method=='POST':
          df=pd.read_csv("fertilizers.csv",parse_dates=['Year'])
          df.dtypes
          country=request.POST.get('country')
          
          print(country)
          #country='India'
          production=df[df['Entity']==country]
          production=production.loc[:,['Year','Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare']]
          production=production.sort_values('Year')
          production.isnull().sum()
          production=production.set_index('Year')
          production.index
          y=production
          p = d = q = range(0, 2)
          pdq = list(itertools.product(p, d, q))
          seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
          print('Examples of parameter combinations for Seasonal ARIMA...')
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
          print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
          print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

          min=99999999
          p1=[-1,-1,-1]
          p2=[-1,-1,-1,-1]
          for param in pdq:
               for param_seasonal in seasonal_pdq:
                    try:
                         mod = sm.tsa.statespace.SARIMAX(y,
                                                       order=param,
                                                       seasonal_order=param_seasonal,
                                                       enforce_stationarity=False,
                                                       enforce_invertibility=False)
                         results = mod.fit()
                         if results.aic<min:
                              min=results.aic
                              p1=param
                              p2=param_seasonal
                         print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                    except:
                         continue
          print(p1)
          print(min)
          print(p2)
          # 12 is the interval for 12 months
          mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(p1[0], p1[1], p1[2]),
                                        seasonal_order=(p2[0], p2[1], p2[2], 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
          results = mod.fit()
          print(results.summary().tables[1])
          steps = int(request.POST.get('steps'))
          
          print("steps are",steps)
          pred_uc = results.get_forecast(steps=steps)
               # Create traces
          fig = go.Figure()
          fig.add_trace(go.Scatter(x=y.index, y=y['Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare'],
                              mode='lines',
                              name='Actual Value'))
          type(pred_uc.predicted_mean)
          fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                              mode='lines',
                              name='Predicted Value'))
          #fig.show()
          fig.update_layout(
          title="Fertilizers Use of "+country,
          xaxis_title="Year",
          yaxis_title="Use",
          legend_title="Country",
          font=dict(
               family="Courier New, monospace",
               size=14,
               color="RebeccaPurple"))
          graph=fig.to_html()
          return render(request,'arima_result.html',{'graph':graph})

     
     else:
          return render(request,'fertilizer_prediction.html')
     
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
      

          print("Predicted class:", predicted_class)
      
          
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
