import os
devices = os.popen("docker exec unms-postgres psql -U unms -c \"Select model from device\" -t -A -X").read()
devices = devices.splitlines()
device_types = {}
for device in devices:
    if device == '':
       continue
    try:
        device_types[device] += 1
    except:
        device_types[device] = 1
print device_types

