from django.contrib import admin
from django.urls import path
from .views import frontpage,index,protection,symptoms,prevent,handwash,india,contact

urlpatterns = [
    path('', frontpage,name='home'),
    path('index/', index,name='index'),
    path('protection/', protection ,name='protection'),
    path('symptoms/',symptoms,name='symptoms'),
    path('prevent/',prevent,name='prevent'),
    path('handwash/',handwash,name='handwash'),
    path('india/',india,name='india'),
    path('contact/',contact,name='contact'),
]

