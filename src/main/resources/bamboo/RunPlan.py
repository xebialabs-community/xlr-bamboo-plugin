#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
import time
import com.xhaus.jyson.JysonCodec as json

print "Executing RunPlan.py ver 2015Mar12-2\n"

if bambooServer is None:
	print "No server provided."
	sys.exit(1)
	
contentType = 'application/json'
headers = {'accept' : 'application/json'}

def finished(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['finished']

def successful(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['successful']

def getStatesAndTimes(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	jsonData = json.loads(response.response)
	return (jsonData['buildState'], jsonData['state'], jsonData['prettyBuildStartedTime'], jsonData['prettyBuildCompletedTime'])

request = HttpRequest(bambooServer)
response = request.post('/rest/api/latest/queue/' + projPlanKey, '{}', contentType=contentType, headers=headers)
result = json.loads(response.response)
buildNumber = result['buildNumber']
print 'Build number is ' + str(buildNumber) + '\n'
brkey = result['buildResultKey']

while (not finished(brkey)):
	time.sleep(5)
	
(buildState, state, prettyBuildStartedTime, prettyBuildCompletedTime) = getStatesAndTimes(brkey)

print "Build job started at " + prettyBuildStartedTime + "\n"

if successful(brkey):
	print "Build job completed successfully at " + prettyBuildCompletedTime + "\n"
else:
	print "Build job failed at " + prettyBuildCompletedTime + "\n"
