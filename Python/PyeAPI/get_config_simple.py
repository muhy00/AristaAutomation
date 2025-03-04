import pyeapi

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1-dc1')

running_config = connect.get_config(as_string='True')
# the as_string True makes it so it prints the config out looking nice instead of as one long line

print(running_config)
