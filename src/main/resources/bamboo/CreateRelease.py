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

print "Executing CreateRelease.py\n"

if bambooServer is None:
  print "No server provided."
  sys.exit(1)

contentType = 'application/json'
headers = {'accept' : 'application/json'}

def getProjectId(projectName):
  print "Executing getProjectId() with projectName %s\n" % projectName
  response = request.get('rest/api/latest/deploy/project/all', contentType=contentType, headers=headers)
  for item in json.loads(response.response):
    if item['name'] == projectName:
        print "Project ID for %s is %s\n" % (projectName, item['id'])
        return item['id']
  print "Error:  project not found for %s\n" % projectName
  sys.exit(1)

def createRelease(projectId, planResultKey, versionName):
  print "Executing createRelease() with projectId %s and versionId %s\n" % (projectId, versionName)
  reqBody = '{"planResultKey" : "%s", "name" : "%s"}' % (planResultKey, versionName)
  response = request.post('rest/api/latest/deploy/project/%s/version' % projectId, reqBody, contentType=contentType, headers=headers)
  result = json.loads(response.response)




credentials = CredentialsFallback(bambooServer, username, password).getCredentials()
request = HttpRequest(bambooServer, credentials['username'], credentials['password'])
projectId = getProjectId(projectName)

createRelease(projectId, planResultKey, versionName)
