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
        'key': 'testkey',
        'set_name': 'testset',
        'map_name': 'testmap'
    }

router2 = {
        'name': 'Router 2',
        'remote_peer_ip': '10.100.100.2',
        'local_internal_network': '10.10.10.0',
        'remote_internal_network': '10.20.20.0',
        'outside_interface': 'gi0/1',
        'inside_interface': 'gi0/0',
        'key': 'testkey',
        'set_name': 'testset',
        'map_name': 'testmap'
    }

router3_1 = {
        'name': 'Router 3 for Router 1',
        'remote_peer_ip': '172.16.1.1',
        'local_internal_network': '10.20.20.0',
        'remote_internal_network': '10.1.1.0',
        'outside_interface': 'gi0/2',
        'inside_interface': 'gi0/0',
        'key': 'testkey',
        'set_name': 'testset',
        'map_name': 'testmap'
    }

router3_2 = {
        'name': 'Router 3 for Router 2',
        'remote_peer_ip': '10.0.0.2',
        'local_internal_network': '10.20.20.0',
        'remote_internal_network': '10.10.10.0',
        'outside_interface': 'gi0/2',
        'inside_interface': 'gi0/0',
        'key': 'testkey',
        'set_name': 'testset',
        'map_name': 'testmap'
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

