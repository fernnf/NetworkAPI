from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/networks/', views.NetworkListCreateView.as_view(), name='network-list-create'),
    path('api/v1/network/<int:pk>', views.NetworkListUpdateDeleteView.as_view(), name='network-list-update-delete'),
    path('api/v1/nodes/', views.NodeListCreateView.as_view(), name='node-list-create'),
    path('api/v1/node/<int:pk>', views.NodeListUpdateDeleteView.as_view(), name='node-list-update-delete' )

]