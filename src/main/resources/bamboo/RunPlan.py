#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
