#
#Copyright 2022 XEBIALABS
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.#
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


error = False
credentials = CredentialsFallback(bambooServer, username, password).getCredentials()
# UNCOMMENT
# request = HttpRequest(bambooServer, credentials['username'], credentials['password'])

# TO-DO: ADD ARGUMENTS
def getDeploymentStatus():
    print "Executing getDeploymentStatus()\n"
    # response = request.get("TO-DO: ADD QUERY STRING HERE", contentType=contentType, headers=headers)
    # Add logic to parse result, Successful, Unsuccessful, In-progress, etc.
    result = "Successful"
    return str(result)

if projectId:
    if projectName:
        if projectId != getProjectId(projectName):
            print "Error: mismatch between projectId %s and projectName %s" % (projectId, projectName)
            error = True
else:
    if projectName:
        projectId = getProjectId(projectName)
    else:
        print "Error: neither projectId nor projectName was specified"
        error = True

status = getDeploymentStatus()

# if status is completed and success, fall through and exit
# if status is unsuccessful, task.schedule bamboo/TriggerDeployment.fail.py
# if status is still-in-progress, schedule this script again --
# task.schedule("bamboo/TriggerDeployment.wait-for-deployment.py")

if status == "Successful":
    print "Deployment has completed successfully." % 
elif status == "Unsuccessful":
    task.schedule("bamboo/TriggerDeployment.fail.py")
else:
    task.schedule("bamboo/TriggerDeployment.wait-for-deployment.py")
