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

def getState(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['state']	

def getBuildState(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['buildState']	

def getPrettyBuildStartedTime(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['prettyBuildStartedTime']	

def getPrettyBuildCompletedTime(brkey):
	request = HttpRequest(bambooServer)
	response = request.get('/rest/api/latest/result/' + brkey, contentType=contentType, headers=headers)
	return json.loads(response.response)['prettyBuildCompletedTime']	

print "Executing RunPlan.py at " + "\n"
request = HttpRequest(bambooServer)
response = request.post('/rest/api/latest/queue/' + projPlanKey, '{}', contentType=contentType, headers=headers)
result = json.loads(response.response)
buildNumber = result['buildNumber']
print 'Build number is ' + str(buildNumber) + '\n'
brkey = result['buildResultKey']
print "Build job started at " + getPrettyBuildStartedTime(brkey) + "\n"

while (not checkFinished(brkey)):
	time.sleep(5)
	
prettyBuildCompletedTime = getPrettyBuildCompletedTime(brkey)
if checkSuccessful(brkey):
	print "Build job completed successfully at " + prettyBuildCompletedTime + "\n"
else:
	print "Build job failed at " + prettyBuildCompletedTime + "\n"

buildState = getBuildState(brkey)
state = getState(brkey)
