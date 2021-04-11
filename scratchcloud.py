import os,json,requests,multiprocessing,scratchapi,random,string

try:
  package = json.loads(open("package-lock.json", "r").read())["dependencies"]
  if not "scratch-api" in package:
    os.system("npm install scratch-api")
except:
  os.system("npm install scratch-api")

class CloudSession:
  def __init__(self, projId, username, password):
    self.os = os
    self.username = username
    self.letters = string.ascii_lowercase
    self.password = ''.join(random.choice(self.letters)for i in range(15))
    self.os.environ[self.password] = password
    self.projId = projId
    self.log = []
    self.vars = {}
    try:
      scratch = scratchapi.ScratchUserSession(username, password)
    except:
      raise Exception('Scratch login failed.')
  def _setvar(self, projId, name, value):
    Info = [str(projId),'"'+self.username+'"','"'+self.password+'"','"☁ '+name+'"','"'+str(value)+'"']
    with open('new.js','w') as file:
      file.write('''var fs = require('fs');
var scratch = require('scratch-api');
function cloudVariable(projId, username, password, varName, varValue) {
  scratch.UserSession.create(username, process.env[password],  function (err, user) { 
    user.cloudSession(Number(projId),  function (err, cloud) {
      cloud.set(varName, varValue);
    });
  });
};
cloudVariable('''+', '.join(Info)+''')''')
    os.system('node new.js')
  def setVar(self, varName, varValue):
    if not str(self.getVar(varName)) == str(varValue):
      x = multiprocessing.Process(target=self._setvar, args=[self.projId, varName, varValue])
      x.start()
      while not str(self.getVar(varName)) == str(varValue):
        pass
      x.terminate()
      os.remove('new.js')
  def changeVar(self, varName, changeBy):
    self.setVar(varName, float(self.getVar(varName))+changeBy)
  def getVars(self, history=1000):
    oldLog = self.log
    try:
      self.log = json.loads(requests.get("https://clouddata.scratch.mit.edu/logs?projectid="+str(self.projId)+"&limit="+str(history)+"&offset=0").text)
    except:
      self.log = oldLog
    self.vars = {}
    for x in range(0, len(self.log)):
      y = self.log[x]
      if not "☁ " in str(y["value"]) and not y["name"][2:] in self.vars:
        self.vars.update({y["name"][2:]: y["value"]})
    return self.vars
  def getVar(self, varName, history=1000):
    return self.getVars(history)[varName]
  def waitUntilVar(self, varName, varValue, history=1000):
    while not str(self.getVar(varName, history)) == str(varValue):
      pass