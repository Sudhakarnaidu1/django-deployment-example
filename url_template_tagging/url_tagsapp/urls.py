from django.urls import path
from url_tagsapp import views
app_name = 'urlapp'
urlpatterns=[
    path('1',views.relative,name='relative'),
    path('2',views.other,name='other')
]