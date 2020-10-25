import os
import time
import configparser

conf = configparser.ConfigParser()
conf.read('config.cfg')
gateway_ip = conf.get('tradfri','gateway_ip')
identity = conf.get('tradfri', 'identity')
pre_shared_key = conf.get('tradfri', 'pre_shared_key')
bulb = conf.get('tradfri', 'bulb')

def set_color(color): 
    '''
    color = red : busy
    color = yellow : away
    color = green : available
    color = blue : offline
    '''
    cmd_start = f'coap-client -m put -u "{identity}" -k "{pre_shared_key}"'
    cmd_end = f'"coaps://{gateway_ip}:5684/15001/{bulb}"'
    cmd_on_bright = f'"5850":1,"5851":254'
    color_props = {
        'red': f'{{ "5709": 41406,"5710":21337, {cmd_on_bright} }}',
        'green': f'{{ "5709": 19534,"5710":38965, {cmd_on_bright} }}',
        'yellow': f'{{ "5709": 24885,"5710":28334,{cmd_on_bright} }}',
        'blue': f'{{ "5709": 9797,"5710":3936, {cmd_on_bright} }}'
    }
    cmd_props = color_props.get(color, lambda:'Not supported color')
    cmd = f'{cmd_start} -e \'{{"3311": [ {cmd_props} ] }}\' {cmd_end}'
    os.system(cmd)
