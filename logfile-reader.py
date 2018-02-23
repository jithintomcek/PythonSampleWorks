
# 
# Sample script to read log file line-by-line
#

LogFile = '/path/to/logfile'


with open(LogFile) as fh:
	for logline in fh:
		print(logline)
