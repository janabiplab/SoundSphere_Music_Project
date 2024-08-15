from django.urls import  path

from .import  views

urlpatterns = [
    path('home/',views.index,name="index"),
    path('signup/',views.SignUp,name="signup"),
    path("login/",views.login,name="login_page"),
    path("home/<int:idd>",views.Songpage,name="Songpage"),
    path("Allsongs/",views.Allsongs,name="Allsongs"),
    path("Singer/<str:sidd>",views.Singerpage,name="Singerpage"),
    path("logout/",views.logout,name="logout")
]    