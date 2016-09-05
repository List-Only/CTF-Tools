import socket
import base64



def recvline(req):
    buf = b""
    while not buf.endswith(b"\n"):
        buf += req.recv(1)
    return buf

def pad(num):
    out = ""
    for i in range(num):
        out += 'a'
    return out

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("flagstaff.vuln.icec.tf", 6003))
    return s
iv_base = b'\x95B\r\xa0\xcb\xba\xae1\xd3\n\xe3\xb00\x1d,\x13'
text = b'aaaaaaaaaaaaaaaa'
s = connect()
print(recvline(s))
s.send(b'decrypt\n')
#s.send(base64.b64encode(iv_base + text) + b'\n')
s.send(b'tdJV5W9b/Tx2OCg6YTZaHgM6ZtJ5bzegXUbjz4Dh3o7QPQ+LkbG7H42WDmBLh40408xTCJJTGNQgKb5yqIifs/LXCm7JeXj+qPWIeBz8Xoc=\n')
print(recvline(s))
#print(recvline(s))
s.shutdown(1)
s.close()
