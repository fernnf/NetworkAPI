
from rest_framework import serializers
from .models import Network, Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Node
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True)
    class Meta:
        model = Network
        fields = '__all__'

    def create(self, validated_data):
        nodes_data = validated_data.pop('nodes')
        network = Network.objects.create(**validated_data)
        for node_data in nodes_data:
            Node.objects.create(network = network, **node_data)
        return network

