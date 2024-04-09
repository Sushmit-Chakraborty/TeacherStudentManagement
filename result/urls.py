from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage, name='homePage'),
    path('signup/',views.signupPage, name='signupPage'),
    path('login/',views.loginPage, name='loginPage'),
    #path('signup/<slug:slug>',views.slugexample, name='slugexample'),
    path('studentPage/',views.studentPage, name='studentPage'),
    path('teacherPage/',views.teacherPage, name='teacherPage'),
    path('resultPage/',views.get_result_for_student,name='resultPage'),
    path('addResult/',views.addResultPage,name='addResultPage'),
    path('viewdata/',views.viewdata,name='viewdata'),
    path('logout/',views.logoutPage,name='logoutPage'),
    path('reset/',views.resetPage,name='resetPage'),
    path('contactus/',views.contactusPage,name='contactusPage'),
    path('delete/<int:id>',views.deletepage,name='deletepage'),
    path('update/<int:id>',views.updatepage,name='updatepage'),
    path('sendmail/',views.sendmail, name='sendmail'),
]