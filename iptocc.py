import sys
try:
	import requests
except ImportError:
	print('Missing Module: >> requests <<')
	print('Try : pipX install requests')
	sys.exit()

arguments = sys.argv

if len(arguments) > 1:
	ips = arguments[1:]
	for ip in ips:
		try:
			response = requests.get('http://freegeoip.net/json/'+ip)
			code = response.json()['country_code']
			print('{}:{}'.format(ip,code))
		except:
			pass
else:
	print('Usage : python3 iptocc.py x.x.x.x  y.y.y.y')
