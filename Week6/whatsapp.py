from twilio.rest import Client
import requests

# account_sid = 'AC648a156ee4e8d02b8cf0704e50f7db3f'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='hello',
#   to='whatsapp:+995598247477'
# )

# print(message.sid)



# def send_alert():
#     url  = "https://inteltech.p.rapidapi.com/send.php"

#     payload = {
#         "sms": "+995598247477",
#         "message": "ALERT",
#             "senderid": "Nick", 
#         "key": "0DF6D4C5-8990-8801-441D-84BEF7D5CD48",
#         "username": "nika.gamkrelidze.1@btu.edu.ge"
#     }
#     headers = {
#         "content-type": "application/x-www-form-urlencoded",
#         "X-RapidAPI-Key": "c0be979cd8msh4bfef5909f49b03p105516jsn0792c3c189d0",
#         "X-RapidAPI-Host": "inteltech.p.rapidapi.com"
#     }

#     response = requests.post(url, data=payload, headers=headers)

#     print(response.json())  

import nmap

def get_connected_devices():
    # Create a new nmap scanner
    scanner = nmap.PortScanner()

    # Set the target IP range for scanning (replace with your network IP range)
    target_ip = "192.168.1.1"

    # Run the scan with the ARP ping scan type
    scanner.scan(hosts=target_ip, arguments='-PR')

    # Get a list of all the connected devices
    connected_devices = []
    for host in scanner.all_hosts():
        if 'mac' in scanner[host]['addresses']:
            mac_address = scanner[host]['addresses']['mac']
            ip_address = scanner[host]['addresses']['ipv4']
            connected_devices.append((mac_address, ip_address))

    return connected_devices

# Call the function to get the connected devices
devices = get_connected_devices()

# Display the connected devices
if len(devices) > 0:
    print("Connected Devices:")
    for device in devices:
        print("MAC Address: ", device[0])
        print("IP Address: ", device[1])
        print("---------------------")
else:
    print("No connected devices found.")
