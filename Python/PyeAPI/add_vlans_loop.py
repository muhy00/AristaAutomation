import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

#print(vlan_dict['vlans'][0])

pyeapi.load_config('eapi.conf')
# 1st Loop: Loop through list of Switches
for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}:")
    connect = pyeapi.connect_to(switch)
    for vlan in vlan_dict['vlans']:
        vlan_api = connect.api('vlans')
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} with name {vlan_name} to {switch}...")
        vlan_api.create(vlan['id'])
        vlan_api.set_name(vlan_id, vlan_name)

# 2nd Loop: Loop through VLAN IDs and configure them 


