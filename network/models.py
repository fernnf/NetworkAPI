from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length = 255, blank = False, unique = True)
    subnet = models.GenericIPAddressField(protocol='ipv4', max_length = 255, blank = False, unique = True)
    gateway = models.GenericIPAddressField(protocol='ipv4', max_length = 255, blank = False, unique = True)
    cidr = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(32)], blank = False, default = 1)
    vlan  =  models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(4094)], blank = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'network'

class Node(models.Model):
    SERVER = 'SRV'
    HOST = 'HT'

    TYPE_NODES_CHOICE = [
        (SERVER, 'Server'),
        (HOST, 'Host')
    ]

    class Meta:
        db_table = 'node'

    network = models.ForeignKey(Network, related_name='nodes',blank = True, null=True, on_delete=models.CASCADE)
    name =  models.CharField(max_length = 255, blank = False, unique = True)
    address = models.GenericIPAddressField(protocol='ipv4', max_length = 255, blank = False, unique = True)
    type = models.CharField(max_length = 3, blank = False, choices = TYPE_NODES_CHOICE, default = HOST)