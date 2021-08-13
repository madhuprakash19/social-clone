from django.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all'),
    path('new/',view.CreateGroup.as_view(),name = 'create'),
    path('posts/in/(?P<slug>[-\w]+)/',views.SingleGroup.as_view(),name='single'),
    
]
