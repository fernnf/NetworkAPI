import ipaddress

from rest_framework import serializers

from .models import Network, Node


def check_node_address(network, cidr, host):
    net = ipaddress.IPv4Network("{}/{}".format(network, cidr))
    addr = ipaddress.IPv4Address(host)
    if addr in net.hosts():
        return True
    return False


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

    def validate(self, data):
        net = data.get('network', None)

        network = net.subnet
        cidr = net.cidr
        host = data.get('address')
        errors = {}

        if check_node_address(network, cidr, host):
            return data
        else:
            errors['error'] = 'the host ip ({}) is not valid on subnet ({}/{})'.format(host, network, cidr)
            raise serializers.ValidationError(errors)


class NetworkSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True)

    class Meta:
        model = Network
        fields = '__all__'

    def create(self, validated_data):
        nodes_data = validated_data.pop('nodes')
        network = Network.objects.create(**validated_data)
        for node_data in nodes_data:
            Node.objects.create(network=network, **node_data)
        return network
