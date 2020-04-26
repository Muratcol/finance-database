import socket
import pickle



HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))
full_msg = b''
new_msg = True
while True:
	msg = s.recv(16)
	if new_msg:
		msglen = int(msg[:HEADERSIZE])
		new_msg = False

	full_msg += msg

	if len(full_msg)-HEADERSIZE == msglen:

		content = pickle.loads(full_msg[HEADERSIZE:])
		new_msg = True
		full_msg = b''

print(full_msg)




