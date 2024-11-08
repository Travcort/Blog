from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('', views.BlogListView.as_view(), name='posts'),
    path('<slug:slug>/', views.BlogDetailedView.as_view(), name='post-view'),
]
