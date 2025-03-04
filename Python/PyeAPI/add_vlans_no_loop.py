import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

#print(vlan_dict['vlans'][0])

#for switch in vlan_dict['switches']:
#    print(switch)

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1-dc1')

vlan_api = connect.api('vlans')
vlan_api.create('10')
vlan_api.set_name('10', 'DMZ')
