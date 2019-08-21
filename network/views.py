from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Network, Node
from .serializers import NetworkSerializer, NodeSerializer

class NetworkListCreateView(generics.ListCreateAPIView):
    '''
     1 - Using method [GET] it returns a list of all networks.
     2 - Using method [POST] it will create a new network.
    '''
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

class NetworkListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

class NodeListCreateView(generics.ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    1 - Using method [GET] it returns a list of all networks.
    2 - Using method [POST] it will create a new network.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer