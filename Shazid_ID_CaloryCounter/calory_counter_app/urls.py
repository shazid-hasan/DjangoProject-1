from django.urls import path
from calory_counter_app.views import signup,signin

urlpatterns = [
    path('',signup,name="signup"),
    path('signin',signin,name="signin")
]
