from django.conf.urls import url
from basic_app import views
from django.urls import include, path


#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns =[
	path('relative/', views.relative, name='relative'),
	path('other/',views.other, name='other'),
]
