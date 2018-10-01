# load additional Python modules
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(local_hostname)
server_address = (ip_address, 8875)
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

data = {
    'app': 'asaf',
    'throw': 1
}
sock.sendall(json.dumps(data))
newData = sock.recv(1024)
sock.close()
print 'Received', repr(newData)

