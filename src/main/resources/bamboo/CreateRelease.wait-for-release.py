#
# Copyright 2020 XEBIALABS
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

print "Executing CreateRelease.wait-for-release.py\n"

contentType = 'application/json'
headers = {'accept' : 'application/json'}

credentials = CredentialsFallback(bambooServer, username, password).getCredentials()
request = HttpRequest(bambooServer, credentials['username'], credentials['password'])

def getReleaseStatus(projectId, planResultKey, versionName, releaseId):
  print "Executing getReleaseStatus() with projectId %s, planResultKey %s, versionName %s, releaseId %s\n" % (projectId, planResultKey, versionName, releaseId)
  # Configure query string and request body to get the release status
  # reqBody = '{"planResultKey" : "%s", "name" : "%s"}' % (planResultKey, versionName)
  # response = request.post('rest/api/latest/deploy/project/%s/version' % projectId, reqBody, contentType=contentType, headers=headers)
  # result = json.loads(response.response)
  result = "Undetermined"
  return str(result)

try:
    status = getReleaseStatus(projectId, planResultKey, versionName, releaseId)

    if status = "successful":
        print "Release %s has completed successfully." % releaseId
    elif status = "in-progress":
        task.schedule("bamboo/CreateRelease.wait-for-release.py")
    else:
        task.schedule)"bamboo/CreateRelease.fail.py"
except IOException as error:
    print "\nFailed to check the release status due to connection problems. Will retry in the next polling run. Error details: `%s`" % error
    task.schedule("bamboo/CreateRelease.wait-for-release.py")
