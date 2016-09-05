import hashlib

hash = "6c7f4d49729e58d7a458999b570e0151bc034ca7"

md5 = hashlib.md5()

with open("/usr/share/wordlists/rockyou.txt") as f:
	for line in f:
		line = "TMCTF{"+ line.strip() + "}"
		md5 = hashlib.md5()
		sha1 = hashlib.sha1()
		md5.update(line)
		sha1.update(md5.hexdigest())
		password = sha1.hexdigest()
		if password == hash:
			print line
			exit()
