import requests
from django import template
import json

register = template.Library()

@register.simple_tag()
def get_network(id):
    if id == 0:
        url = "http://127.0.0.1:8000/api/v1/networks/"
    else:
        url = "http://127.0.0.1:8000/api/v1/network/{}".format(id)


    ret = requests.get(url=url)
    ret.encoding = 'utf-8'
    data = json.loads(ret.content)
    if id > 0:
        response = {'length': list(range(1)), 'data': [data]}
    else:
        response = {'length': list(range(len(data))), 'data': data}

    if ret.status_code == 200:
        return response

    if ret.status_code == 404:
        return ''

