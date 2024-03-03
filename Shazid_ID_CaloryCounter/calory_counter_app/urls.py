from django.urls import path
from calory_counter_app.views import signup

urlpatterns = [
    path('',signup,name="signup"),
]
