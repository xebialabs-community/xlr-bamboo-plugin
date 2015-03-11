import datetime
import sys
import time

import com.xhaus.jyson.JysonCodec as json

print "Executing RunPlan.py\n"

if bambooServer is None:
	print "No server provided."
	sys.exit(1)
	
contentType = 'application/json'
headers = {'accept' : 'application/json'}

def checkFinished(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['finished']

def checkSuccessful(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['successful']

print "Starting Bamboo job at " + str(datetime.datetime.isoformat(datetime.datetime.now())) + "\n"
request = HttpRequest(bambooServer)
response = request.post('/rest/api/latest/queue/' + projPlanKey, '{}', contentType=contentType, headers=headers)
result = json.loads(response.response)
buildNumber = result['buildNumber']
print 'Build number is ' + str(buildNumber) + '\n'

brkey = result['buildResultKey']
while (not checkFinished(brkey)):
	#print "Sleeping for 5 seconds at " + str(datetime.datetime.isoformat(datetime.datetime.now())) + "\n"
	time.sleep(5)
	
if checkSuccessful(brkey):
	print "Build job completed successfully at " + str(datetime.datetime.isoformat(datetime.datetime.now())) + "\n"
else:
	print "Build job failed at " + str(datetime.datetime.isoformat(datetime.datetime.now())) + "\n"

