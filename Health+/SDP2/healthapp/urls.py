from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage ,name='home'),
    path('signup/', views.registerPage, name='register'),
	#path('user/register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('contact/',views.contactPage,name="contact"),
    path('about/',views.aboutPage,name="about"),
    path('mid/',views.midPage,name="mid"),
    path('appointment/',views.appointmentPage,name="appointment"),
    path('medicine/',views.medicinePage,name="medicine"),
    path('medicine/Successful/',views.SuccessfulPage,name="Successful"),
    path('new/',views.newPage,name="new"),
    path('service/',views.servicePage,name="service"),
    path('new/doctors/',views.DoctorsPage,name="doctors"),
    path('pay/',views.payPage,name="pay"),
    path('pay/Success/',views.successPage,name="success"),
    path('logout/', views.logoutUser, name="logout"),
   # path('appointment/',views.appointmentPage,name="appointment"),

]