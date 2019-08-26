import json

import requests
from django import template

register = template.Library()


@register.simple_tag()
def get_nodes(id):
    if id == 0:
        url = "http://127.0.0.1:8000/api/v1/nodes/"
    else:
        url = "http://127.0.0.1:8000/api/v1/nodes/{}".format(id)

    ret = requests.get(url=url)
    ret.encoding = 'utf-8'
    data = json.loads(ret.content)
    return data
