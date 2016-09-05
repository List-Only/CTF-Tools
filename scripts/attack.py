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

    s.connect(("l33tcrypt.vuln.icec.tf", 6001))
    recvline(s);
    recvline(s);
    return s


base = "l33tserver please"
sol = "IceCTF{unleash_th3_Blocks_aNd_find_what"
extra = pad(78 - len(sol))
notFound = True
prev = 0

for i in range(50 - len(sol)):
    s = connect()
    s.send(base64.b64encode(bytes(base + extra, 'utf-8', 'ignore')) + b"\n")
    recvline(s);
    initial = base64.b64decode(recvline(s).strip())[:96];
    s.shutdown(1)
    s.close()
    found = False
    for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_{}":
        s = connect()
        s.send(base64.b64encode(bytes(base + extra + sol + c, 'utf-8', 'ignore')) + b"\n")
        recvline(s);
        inp = base64.b64decode(recvline(s).strip());
        test = inp[:96]
        s.shutdown(1)
        s.close()
        if test == initial:
            found = True
            sol += c
            print(sol)
            break
    if not found:
        print("error\n")
        break
    extra = extra[1:]
print(sol)
