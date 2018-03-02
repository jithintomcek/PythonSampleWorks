
import re
import collections
import argparse
import requests



parser = argparse.ArgumentParser()
parser.add_argument('-l',help='LogFile Path',dest='LOGFILE',required=True )
parser.add_argument('-c',help='Count',dest='COUNT',default='5')
parser.add_argument('-i',help='Ignore Ips',nargs='+',dest='IGNORE')
parser.add_argument('-v',help='Enable Country Code',dest='CC_Enable',action='store_true')

args = parser.parse_args()

logFile = args.LOGFILE
count = int(args.COUNT)
ignoreList = args.IGNORE
showCountryCode = args.CC_Enable


def getCountryCode(ip):
	response = requests.get('http://freegeoip.net/json/'+ip)
	code = response.json()['country_code']
	return code


hitCounter = collections.Counter()


with open(logFile) as fh:
	regexPattern = '(?P<IP>.+?)\s'
	for logLine in fh:
		resutl = re.match(regexPattern,logLine)
		ip = resutl.group('IP')
		if ip not in ignoreList:
			hitCounter.update((ip,))

for ip,count in  hitCounter.most_common(count):
	if showCountryCode:
		print('{:15} : {}[{}]'.format(ip,count,getCountryCode(ip)))
	else:
		print('{:15} : {}'.format(ip,count))
