import requests
from django import template
import json
import dominate.tags as tags

register = template.Library()

@register.simple_tag()
def get_html(id):
    if id == 0:
        url = "http://127.0.0.1:8000/api/v1/networks/"
    else:
        url = "http://127.0.0.1:8000/api/v1/network/{}".format(id)

    ret = requests.get(url = url)
    ret.encoding = 'utf-8'
    data = json.loads(ret.content)

    table = tags.table()
    table.set_attribute('class', 'table table-hover')
    with table:
        with tags.thead() as thead:
            with tags.th() as th:
                th.add(tags.tr("#", scope='col'))
                th.add(tags.tr("Name", scope='col'))
                th.add(tags.tr("Subnet", scope='col'))
                th.add(tags.tr("Gateway", scope='col'))
                th.add(tags.tr("Cidr", scope='col'))
                th.add(tags.tr("Created", scope='col'))
                th.add(tags.tr("Last Modified", scope='col'))

    print(table.render())

