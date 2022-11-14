#
# Copyright 2022 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.#
#

import sys
import time
import com.xhaus.jyson.JysonCodec as json

print "Executing triggerBambooDeployment.wait-for-deployment.py\n"

if bambooServer is None:
  print "No server provided."
  sys.exit(1)

contentType = 'application/json'
headers = {'accept' : 'application/json'}

credentials = CredentialsFallback(bambooServer, username, password).getCredentials()
request = HttpRequest(bambooServer, credentials['username'], credentials['password'])

def getDeploymentStatus():
    print "Executing getDeploymentStatus()\n"
    response = request.get('rest/api/latest/deploy/result/%s' % str(deploymentResultId), contentType=contentType, headers=headers)
    if response.isSuccessful():
        result = json.loads(response.response)
        return (result['lifeCycleState'], result['deploymentState'], result['logFiles'][0])
    else:
        print "Error: HTTP status code %s" % str(response.getStatus())
        sys.exit(1)

projectId = projectId or foundProjectId

(lifeCycleState, deploymentState, zerothLogFileRef) = getDeploymentStatus()

if lifeCycleState == "FINISHED":
    if deploymentState == "SUCCESS":
        print "Deployment has completed successfully."
    elif deploymentState in ("FAILED", "UNKNOWN"):
        print "Error: lifeCycleState is %s and deploymentState is %s" % (lifeCycleState, deploymentState)
        sys.exit(1)
elif lifeCycleState == "IN_PROGRESS":
    task.schedule("bamboo/TriggerDeployment.wait-for-deployment.py", 30)
else:
    print "Error: Invalid lifeCycleState %s with deploymentState %s" % (lifeCycleState, deploymentState)
    sys.exit(1)
