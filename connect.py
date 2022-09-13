from dvrip import DVRIPCam
from time import sleep
from pprint import pprint

host_ip = '10.0.250.10'

cam = DVRIPCam(host_ip, user='admin', password='')
if cam.login():
	print("Success! Connected to " + host_ip)
else:
	print("Failure. Could not connect.")

print("Camera time:", cam.get_time())

#params = cam.get_general_info()
#pprint(params)

#params = cam.get_system_info()
#pprint(params)


cam.close()
