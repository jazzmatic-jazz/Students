from django.urls import path
# from .views import  home, studentView
from .views import  home, StudentListView
# from .views import StudentCreate
urlpatterns = [
    # path('', StudentCreate.as_view(), name='HomeForm'),
    path('', home, name='home'),
    path('student/', StudentListView.as_view(), name='student'),
]