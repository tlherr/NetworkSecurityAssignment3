#!/usr/bin/python

# Get Template
# https://gist.github.com/tlherr/ad96cf72db79efce20b4d0d35c28376f

# pip install Jinja2

import jinja2


router1 = {
        'name': 'Router 1',
        'remote_peer_ip': '10.100.100.2',
        'local_internal_network': '10.1.1.0',
        'remote_internal_network': '10.20.20.0',
        'outside_interface': 'gi0/0',
        'inside_interface': 'gi0/1',
        'map_description': 'VPN Connection to Router 3',
        'key': 'cP7YWuhfWHKLbYdS',
        'set_name': 'set_vpn_to_router_three',
        'map_name': 'map_vpn_to_router_three'
    }

router2 = {
        'name': 'Router 2',
        'remote_peer_ip': '10.100.100.2',
        'local_internal_network': '10.10.10.0',
        'remote_internal_network': '10.20.20.0',
        'outside_interface': 'gi0/1',
        'inside_interface': 'gi0/0',
        'map_description': 'VPN Connection to Router 3',
        'key': 'Fa8TRtb7BtVxQ7c5',
        'set_name': 'set_vpn_to_router_three',
        'map_name': 'map_vpn_to_router_three'
    }

router3_1 = {
        'name': 'Router 3 for Router 1',
        'remote_peer_ip': '172.16.1.1',
        'local_internal_network': '10.20.20.0',
        'remote_internal_network': '10.1.1.0',
        'outside_interface': 'gi0/2',
        'inside_interface': 'gi0/0',
        'map_description': 'VPN Connection to Router 1',
        'key': 'cP7YWuhfWHKLbYdS',
        'set_name': 'map_vpn_to_router_one',
        'map_name': 'map_vpn_to_router_one'
    }

router3_2 = {
        'name': 'Router 3 for Router 2',
        'remote_peer_ip': '10.0.0.2',
        'local_internal_network': '10.20.20.0',
        'remote_internal_network': '10.10.10.0',
        'outside_interface': 'gi0/2',
        'inside_interface': 'gi0/0',
        'map_description': 'VPN Connection to Router 2',
        'key': 'Fa8TRtb7BtVxQ7c5',
        'set_name': 'map_vpn_to_router_two',
        'map_name': 'map_vpn_to_router_one'
    }

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

print("To Disable Annoying DNS lookup: no ip domain-lookup")
print("Run Part 1 then Part 2 for each Router")

print(template.render(router=router1))
print(template.render(router=router2))
print(template.render(router=router3_1))
print(template.render(router=router3_2))

print("=========================")
print("Show Settings: show crypto ipsec sa")
print("Show Current IKE SAs: show crypto isakmp sa")
print("Debug Phase 1: debug crypto isakmp")
print("Debug Phase 2: debug crypto ipsec")

# NAT: s=10.1.1.10->10.1.1.1, d=10.100.100.2 [33]
# access-list 1 permit 10.1.1.0 0.0.0.255
# access-list 110 permit ip 10.1.1.0 0.0.0.255 10.20.20.0 0.0.0.255
# access-list 122 deny ip 10.1.1.0 0.0.0.255 10.20.20.0 0.0.0.255
# access-list 122 permit ip 10.1.1.0 0.0.0.255 any
