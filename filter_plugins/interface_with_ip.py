from __future__ import (absolute_import, print_function)
import json
from ipaddress import IPv4Interface

def interface_with_ip(data):
    ip_interfaces = []
    for item in data:
        if 'ipv4' in item.keys():
            ip_interfaces.append(item)
    return ip_interfaces

def interface_networks(data):
    data = interface_with_ip(data)
    for item in data:
        # TODO: Add IPv6 support
        ip = item['ipv4'][0]['address'].replace(' ', '/')
        network = IPv4Interface(ip).network.exploded
        item['ipv4'][0]['network'] = network
    return data


class FilterModule(object):
    '''Filter, removes interfaces without IP Address configured'''

    def filters(self):
        return {
            'interface_with_ip': interface_with_ip,
            'interface_networks': interface_networks,
        }