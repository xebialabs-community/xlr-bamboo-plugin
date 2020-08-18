#
#Copyright 2020 XEBIALABS
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.#
#

import sys
import time
import com.xhaus.jyson.JysonCodec as json

print "Executing triggerBambooDeployment.py\n"

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

def getEnvironmentId(projectId, environmentName):
  print "Executing getEnvironmentId() with projectId %s and environmentName %s\n" % (projectId, environmentName)
  response = request.get('rest/api/latest/deploy/project/%s' % projectId, contentType=contentType, headers=headers)
  for item in json.loads(response.response)['environments']:
    if item['name'] == environmentName:
        print "Environment ID for %s is %s\n" % (environmentName, item['id'])
        return item['id']
  print "Error:  environment not found for %s, %s\n" % (projectId, environmentName)
  sys.exit(1)

def getVersionId(projectId, versionName):
  print "Executing getVersionId() with projectId %s and versionName %s\n" % (projectId, versionName)
  response = request.get('rest/api/latest/deploy/project/%s/versions' % projectId, contentType=contentType, headers=headers)
  for item in json.loads(response.response)['versions']:
    if item['name'] == versionName:
        print "Version ID for %s is %s\n" % (versionName, item['id'])
        return item['id']
  #print "Error:  version not found for %s, %s\n" % (projectId, versionName)
  print "Error:  version not found for %s, %s, %s\n" % (projectName, environmentName, versionName)
  sys.exit(1)

def getPlanKey(projectName):
  print "Executing getPlanKey() with projectName %s\n" % projectName
  response = request.get('rest/api/latest/deploy/project/all', contentType=contentType, headers=headers)
  #print "response: %s " % response
  for item in json.loads(response.response):
    if item['name'] == projectName:
        print "planKey for %s is %s\n" % (projectName, item['planKey'])
        print "planKey.key for %s is %s\n" % (projectName, item['planKey']['key'])
        return item['planKey']['key']
  print "Error:  project not found for %s\n" % projectName
  sys.exit(1)

def getPlanKeyResult(planKey, versionName):
  #e.g. SER-AR-139, planKey = SER-AR, versionName = 3.1.0-139
  print "in getPlanKeyResult- planKey: %s, versionName: %s" % (planKey,versionName)
  planKeyRslt = planKey + versionName[versionName.index("-"):]
  print "planKey: %s, versionName: %s, planKeyResult: %s\n" % (planKey, versionName, planKeyRslt)
  return planKeyRslt

def createDeploymentVersion(projectId, planKeyResult, versionName):
  print "Executing createDeploymentVersion() with projectId %s and versionName %s\n" % (projectId, versionName)
  response = request.post('rest/api/latest/deploy/project/%s/version' % (projectId), '{"planResultKey" : "%s", "name" : "%s"}' % (planKeyResult, versionName), contentType=contentType, headers=headers)
  result = json.loads(response.response)
  print (result['id'])
  return result['id']

def getDeploymentVersion(projectId, planKeyResult, versionName):
  print "Executing getDeploymentVersion() with projectId %s and versionName %s\n" % (projectId, versionName)
  response = request.get('rest/api/latest/deploy/project/%s/versions' % (projectId), contentType=contentType, headers=headers)
  for item in json.loads(response.response)['versions']:
    if item['name'] == versionName:
        print "versionId for %s is %s\n" % (versionName, item['id'])
        return item['id']
  return None

def triggerDeployment(environmentId, versionId):
  print "Executing triggerDeployment() with environmentId %s and versionId %s\n" % (environmentId, versionId)
  response = request.post('rest/api/latest/queue/deployment/?environmentId=%s&versionId=%s' % (environmentId, versionId), '{}', contentType=contentType, headers=headers)
  result = json.loads(response.response)
  print (result['deploymentResultId'], result['link']['href'])
  return result['deploymentResultId'], result['link']['href']

credentials = CredentialsFallback(bambooServer, username, password).getCredentials()
print "1) credentials: no value"

request = HttpRequest(bambooServer, credentials['username'], credentials['password'])
print "2) request: %s" % request

projectId = getProjectId(projectName)
print "3) projectId: %s" % projectId

environmentId = getEnvironmentId(projectId, environmentName)
print "4) environmentId: %s" % environmentId

#versionId = getVersionId(projectId, versionName)

print "4a) before getPlanKey with projectName: %s" % projectName
planKey = getPlanKey(projectName)
print "5) planKey: %s" % planKey

planKeyResult = getPlanKeyResult(planKey, versionName)
print "6) planKeyResult: %s" % planKeyResult

versionId = getDeploymentVersion(projectId, planKeyResult, versionName)
print "7) versionId: %s" % versionId

if versionId is None:
    versionId = createDeploymentVersion(projectId, planKeyResult, versionName)
print "8) versionId: %s" % versionId

(deploymentResultId, href) = triggerDeployment(environmentId, versionId)
