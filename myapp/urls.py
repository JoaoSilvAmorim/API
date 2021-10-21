from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [ 
    path('casos/', views.Casos.as_view()),
    path('casos/<id>/', views.Casos.as_view())
    
]
urlpatterns = format_suffix_patterns(urlpatterns)