import obd

obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBD-ii
ports = obd.scan_serial()
print("Ports: ")
print(ports)

connection = obd.OBD(ports[0])
print("Connection status: ")
print(connection.status())

# Require the speed info
cmd = obd.commands.SPEED

response = connection.query(cmd)

print(response.value)