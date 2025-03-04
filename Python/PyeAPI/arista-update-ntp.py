from netmiko import ConnectHandler

switch_ips = [
'10.60.1.44',
'10.60.1.43',
]

# NTP settings to be configured
ntp_commands = [
    'ntp server 10.26.250.34',  # Replace with your NTP server IP
    'ntp server 10.26.250.35',  # Add more servers as needed
    'ntp server 10.60.250.82',
    'ntp server 10.60.250.83',
    'no ntp server 10.60.250.36',
    #'ntp update-calendar',
    'write memory'
]

def update_ntp_settings():
    try:
       for ip in switch_ips:
            # Device information
            arista_switch = {
                'device_type': 'arista_eos',
                'host': ip,    # Replace with the IP address of your Arista switch
                'username': 'admin',
                'password': 'MzmqJ@N9NSRJJGxiHsE',
            #    'secret': 'YOUR_ENABLE_PASSWORD',  # If needed
            }

            # Establish SSH connection
            connection = ConnectHandler(**arista_switch)
            connection.enable()

            # Send NTP commands
            print(f"Updating NTP for {ip}...")
            output = connection.send_config_set(ntp_commands)
            print(output)

            # Verify NTP settings
            print("Verifying NTP settings...")
            ntp_status = connection.send_command("show ntp status")
            print(ntp_status)

            # Close the connection
            connection.disconnect()
            print("NTP settings updated and connection closed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_ntp_settings()
