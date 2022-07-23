
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_show, name='add-show'),
    path('delete/<int:id>/',delete_data, name='deletedata'),
    path('<int:id>/', edit_data, name='editdata')
]
