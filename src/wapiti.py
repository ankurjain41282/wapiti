#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Wapiti SVN - A web application vulnerability scanner
# Wapiti Project (http://wapiti.sourceforge.net)
# Copyright (C) 2008 Nicolas Surribas
#
# David del Pozo
# Alberto Pastor
# Informatica Gesfor
# ICT Romulus (http://www.ict-romulus.eu)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import sys
import getopt
import os
import urlparse
import time

from distutils.sysconfig import get_python_lib

BASE_DIR = None
WAPITI_VERSION = "Wapiti SVN"
if '' in sys.path:
    sys.path.remove('')
for python_dir in sys.path:
    if os.path.isdir(os.path.join(python_dir, "wapiti")):
        BASE_DIR = os.path.join(python_dir, "wapiti")
        break
if not BASE_DIR:
    for lib_dir in [get_python_lib(prefix="/usr/local"), get_python_lib()]:
        if os.path.isdir(os.path.join(lib_dir, "wapiti")):
            BASE_DIR = os.path.join(lib_dir, "wapiti")
            sys.path.append(BASE_DIR)
            break
if not BASE_DIR:
    sys.path.append("")
    if "__file__" in dir():
        BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), '..'))
    else:
        BASE_DIR = os.getcwd()

CONF_DIR = BASE_DIR
if os.path.isdir("/usr/local/share/doc/packages/wapiti"):
    CONF_DIR = "/usr/local/share/doc/packages/wapiti"


from language.language import Language
lan = Language()
lan.configure()
from net import HTTP, lswww
from file.reportgeneratorsxmlparser import ReportGeneratorsXMLParser
from file.vulnerabilityxmlparser import VulnerabilityXMLParser
from file.anomalyxmlparser import AnomalyXMLParser
from net.crawlerpersister import CrawlerPersister


class Wapiti:
    """Wapiti-SVN - A web application vulnerability scanner

Usage: python wapiti.py http://server.com/base/url/ [options]

Supported options are:
-s <url>
--start <url>
    To specify an url to start with

-x <url>
--exclude <url>
    To exclude an url from the scan (for example logout scripts)
    You can also use a wildcard (*)
    Example : -x "http://server/base/?page=*&module=test"
    or -x http://server/base/admin/* to exclude a directory

-p <url_proxy>
--proxy <url_proxy>
    To specify a proxy
    Exemple: -p http://proxy:port/

-c <cookie_file>
--cookie <cookie_file>
    To use a cookie

-t <timeout>
--timeout <timeout>
    To fix the timeout (in seconds)

-a <login%password>
--auth <login%password>
    Set credentials for HTTP authentication
    Doesn't work with Python 2.4

-r <parameter_name>
--remove <parameter_name>
    Remove a parameter from URLs

-n <limit>
--nice <limit>
    Define a limit of urls to read with the same pattern
    Use this option to prevent endless loops
    Must be greater than 0

-m <module_options>
--module <module_options>
    Set the modules and HTTP methods to use for attacks.
    Example: -m "-all,xss:get,exec:post"

-u
--underline
    Use color to highlight vulnerables parameters in output

-v <level>
--verbose <level>
    Set the verbosity level
    0: quiet (default), 1: print each url, 2: print every attack

-f <type_file>
--reportType <type_file>
    Set the type of the report
    xml: Report in XML format
    html: Report in HTML format

-o <output>
--output <output_file>
    Set the name of the report file
    If the selected report type is "html", this parameter must be a directory

-i <file>
--continue <file>
    This parameter indicates Wapiti to continue with the scan from the specified
    file, this file should contain data from a previous scan.
    The file is optional, if it is not specified, Wapiti takes the default file
    from \"scans\" folder.

-k <file>
--attack <file>
    This parameter indicates Wapiti to perform attacks without scanning again the
    website and following the data of this file.
    The file is optional, if it is not specified, Wapiti takes the default file
    from \"scans\" folder.

--verify-ssl <0|1>
    This parameter indicates whether Wapiti must check SSL certificates.
    Default is to verify certificates

-h
--help
    To print this usage message"""

    target_url = None
    target_scope = "folder"
    urls = {}
    forms = []

    color = 0
    verbose = 0

    reportGeneratorType = "html"
    REPORT_DIR = "report"
    REPORT_FILE = "vulnerabilities.xml"
    HOME_DIR = os.getenv('HOME') or os.getenv('USERPROFILE')
    COPY_REPORT_DIR = os.path.join(HOME_DIR, ".wapiti", "generated_report")
    outputFile = ""

    options = ""

    http_engine = None
    myls = None
    reportGen = None

    attacks = []

    def __init__(self, root_url):
        self.target_url = root_url
        server = urlparse.urlparse(root_url).netloc
        self.http_engine = HTTP.HTTP(server)
        self.myls = lswww.lswww(root_url, http_engine=self.http_engine)
        self.xmlRepGenParser = ReportGeneratorsXMLParser()
        self.xmlRepGenParser.parse(os.path.join(CONF_DIR, "config/reports/generators.xml"))

    def __initReport(self):
        for repGenInfo in self.xmlRepGenParser.getReportGenerators():
            if self.reportGeneratorType.lower() == repGenInfo.getKey():
                self.reportGen = repGenInfo.createInstance()
                self.reportGen.setReportInfo(target=self.target_url,
                                             scope=self.target_scope,
                                             date_string=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()),
                                             version=WAPITI_VERSION)
                break

        vulnXMLParser = VulnerabilityXMLParser()
        vulnXMLParser.parse(os.path.join(CONF_DIR, "config/vulnerabilities/vulnerabilities.xml"))
        for vul in vulnXMLParser.getVulnerabilities():
            self.reportGen.addVulnerabilityType(_(vul.getName()),
                                                (vul.getDescription()),
                                                _(vul.getSolution()),
                                                vul.getReferences())

        anomXMLParser = AnomalyXMLParser()
        anomXMLParser.parse(os.path.join(CONF_DIR, "config/vulnerabilities/anomalies.xml"))
        for anomaly in anomXMLParser.getAnomalies():
            self.reportGen.addAnomalyType(_(anomaly.getName()),
                                            (anomaly.getDescription()),
                                            _(anomaly.getSolution()),
                                            anomaly.getReferences())

    def __initAttacks(self):
        self.__initReport()

        attack = __import__("attack")

        print(_("[*] Loading modules:"))
        print(u"\t {0}".format(u", ".join(attack.modules)))
        for mod_name in attack.modules:
            mod = __import__("attack." + mod_name, fromlist=attack.modules)
            mod_instance = getattr(mod, mod_name)(self.http_engine, self.reportGen)
            if hasattr(mod_instance, "setTimeout"):
                mod_instance.setTimeout(self.http_engine.getTimeOut())
            self.attacks.append(mod_instance)

            self.attacks.sort(lambda a, b: a.PRIORITY - b.PRIORITY)

        for attack in self.attacks:
            attack.setVerbose(self.verbose)
            if self.color == 1:
                attack.setColor()

        if self.options != "":
            opts = self.options.split(",")

            for opt in opts:
                method = ""
                if opt.find(":") > 0:
                    module, method = opt.split(":", 1)
                else:
                    module = opt

                # desactivate some module options
                if module.startswith("-"):
                    module = module[1:]
                    if module == "all":
                        for x in self.attacks:
                            if method == "get" or method == "":
                                x.doGET = False
                            if method == "post" or method == "":
                                x.doPOST = False
                    else:
                        for x in self.attacks:
                            if x.name == module:
                                if method == "get" or method == "":
                                    x.doGET = False
                                if method == "post" or method == "":
                                    x.doPOST = False

                # activate some module options
                else:
                    if module.startswith("+"):
                        module = module[1:]
                    if module == "all":
                        for x in self.attacks:
                            if method == "get" or method == "":
                                x.doGET = True
                            if method == "post" or method == "":
                                x.doPOST = True
                    else:
                        for x in self.attacks:
                            if x.name == module:
                                if method == "get" or method == "":
                                    x.doGET = True
                                if method == "post" or method == "":
                                    x.doPOST = True

    def browse(self, crawlerFile):
        "Extract hyperlinks and forms from the webpages found on the website"
        #self.urls, self.forms = self.myls.go(crawlerFile)
        self.myls.go(crawlerFile)
        self.urls = self.myls.getLinks()
        self.forms = self.myls.getForms()

    def attack(self):
        "Launch the attacks based on the preferences set by the command line"
        if self.urls == {} and self.forms == []:
            print(_("No links or forms found in this page !"))
            print(_("Make sure the url is correct."))
            sys.exit(1)

        self.__initAttacks()

        for x in self.attacks:
            if x.doGET is False and x.doPOST is False:
                continue
            print('')
            if x.require != []:
                t = [y.name for y in self.attacks if y.name in x.require and (y.doGET or y.doPOST)]
                if x.require != t:
                    print(_("[!] Missing dependecies for module {0}:").format(x.name))
                    print(u"  {0}".format(",".join([y for y in x.require if y not in t])))
                    continue
                else:
                    x.loadRequire([y for y in self.attacks if y.name in x.require])

            x.logG(_("[+] Launching module {0}"), x.name)
            x.attack(self.urls, self.forms)

        if self.myls.getUploads() != []:
            print('')
            print(_("Upload scripts found:"))
            print("----------------------")
            for upload_form in self.myls.getUploads():
                print(upload_form)
        if not self.outputFile:
            if self.reportGeneratorType == "html":
                self.outputFile = self.COPY_REPORT_DIR
            else:
                self.outputFile = self.REPORT_FILE
        self.reportGen.generateReport(self.outputFile)
        print('')
        print(_("Report"))
        print("------")
        print(_("A report has been generated in the file {0}").format(self.outputFile))
        if self.reportGeneratorType == "html":
            print(_("Open {0}/index.html with a browser to see this report.").format(self.outputFile))

    def setTimeOut(self, timeout=6.0):
        "Set the timeout for the time waiting for a HTTP response"
        self.http_engine.setTimeOut(timeout)

    def setVerifySsl(self, verify=True):
        "Set whether SSL must be verified."
        self.http_engine.setVerifySsl(verify)

    def setProxy(self, proxy=""):
        "Set a proxy to use for HTTP requests."
        self.http_engine.setProxy(proxy)

    def addStartURL(self, url):
        "Specify an URL to start the scan with. Can be called several times."
        self.myls.addStartURL(url)

    def addExcludedURL(self, url):
        "Specify an URL to exclude from the scan. Can be called several times."
        self.myls.addExcludedURL(url)

    def setCookieFile(self, cookie):
        "Load session data from a cookie file"
        self.http_engine.setCookieFile(cookie)

    def setAuthCredentials(self, auth_basic):
        "Set credentials to use if the website require an authentification."
        self.http_engine.setAuthCredentials(auth_basic)

    def addBadParam(self, bad_param):
        """Exclude a parameter from an url (urls with this parameter will be
        modified. This function can be call several times"""
        self.myls.addBadParam(bad_param)

    def setNice(self, nice):
        """Define how many tuples of parameters / values must be sent for a
        given URL. Use it to prevent infinite loops."""
        self.myls.setNice(nice)

    def setScope(self, scope):
        """Set the scope of the crawler for the analysis of the web pages"""
        self.target_scope = scope
        self.myls.setScope(scope)

    def setColor(self):
        "Put colors in the console output (terminal must support colors)"
        self.color = 1

    def verbosity(self, vb):
        "Define the level of verbosity of the output."
        self.verbose = vb
        self.myls.verbosity(vb)

    def setModules(self, options=""):
        """Activate or desactivate (default) all attacks"""
        self.options = options

    def setReportGeneratorType(self, repGentype="xml"):
        "Set the format of the generated report. Can be xml, html of txt"
        self.reportGeneratorType = repGentype

    def setOutputFile(self, outputFile):
        "Set the filename where the report will be written"
        self.outputFile = outputFile

if __name__ == "__main__":
    doc = _("wapityDoc")
    try:
        prox = ""
        auth = []
        crawlerPersister = CrawlerPersister()
        crawlerFile = None
        attackFile = None
        if len(sys.argv) < 2:
            print(doc)
            sys.exit(0)
        if '-h' in sys.argv or '--help' in sys.argv:
            print(doc)
            sys.exit(0)

        if not os.path.isdir(crawlerPersister.CRAWLER_DATA_DIR):
            os.makedirs(crawlerPersister.CRAWLER_DATA_DIR)

        url = sys.argv[1]
        wap = Wapiti(url)
        try:
            opts, args = getopt.getopt(sys.argv[2:],
                                       "hup:s:x:c:a:r:v:t:m:o:f:n:kib:",
                                       ["help", "underline", "proxy=", "start=", "exclude=",
                                        "cookie=", "auth=", "remove=", "verbose=", "timeout=",
                                        "module=", "outputfile", "reportType", "nice=",
                                        "attack", "continue", "scope=", "verify-ssl="])
        except getopt.GetoptError, e:
            print(e)
            sys.exit(2)
        for o, a in opts:
            if o in ("-h", "--help"):
                print(doc)
                sys.exit(0)
            if o in ("-s", "--start"):
                if a.startswith("http://") or a.startswith("https://"):
                    wap.addStartURL(a)
            if o in ("-x", "--exclude"):
                if a.startswith("http://") or a.startswith("https://"):
                    wap.addExcludedURL(a)
            if o in ("-p", "--proxy"):
                if a.startswith("http://") or a.startswith("https://"):
                    wap.setProxy(a)
            if o in ("-c", "--cookie"):
                wap.setCookieFile(a)
            if o in ("-a", "--auth"):
                if a.find("%") >= 0:
                    auth = [a.split("%")[0], a.split("%")[1]]
                    wap.setAuthCredentials(auth)
            if o in ("-r", "--remove"):
                wap.addBadParam(a)
            if o in ("-n", "--nice"):
                if str.isdigit(a):
                    wap.setNice(int(a))
            if o in ("-u", "--underline"):
                wap.setColor()
            if o in ("-v", "--verbose"):
                if str.isdigit(a):
                    wap.verbosity(int(a))
            if o in ("-t", "--timeout"):
                if str.isdigit(a):
                    wap.setTimeOut(int(a))
            if o in ("-m", "--module"):
                wap.setModules(a)
            if o in ("-o", "--outputfile"):
                wap.setOutputFile(a)
            if o in ("-f", "--reportType"):
                for repGenInfo in wap.xmlRepGenParser.getReportGenerators():
                    if a == repGenInfo.getKey():
                        wap.setReportGeneratorType(a)
                        break
            if o in ("-b", "--scope"):
                wap.setScope(a)
            if o in ("-k", "--attack"):
                hostname = url.split("://")[1].split("/")[0]
                attackFile = u"{0}/{1}.xml".format(crawlerPersister.CRAWLER_DATA_DIR, hostname)
            if o in ("-i", "--continue"):
                hostname = url.split("://")[1].split("/")[0]
                crawlerFile = u"{0}/{1}.xml".format(crawlerPersister.CRAWLER_DATA_DIR, hostname)
            if o in ("--verify-ssl"):
                if str.isdigit(a):
                    wap.setVerifySsl(bool(int(a)))
        try:
            opts, args = getopt.getopt(sys.argv[2:],
                                       "hup:s:x:c:a:r:v:t:m:o:f:n:k:i:b:",
                                       ["help", "underline", "proxy=", "start=", "exclude=",
                                        "cookie=", "auth=", "remove=", "verbose=", "timeout=",
                                        "module=", "outputfile", "reportType", "nice=",
                                        "attack=", "continue=", "scope=", "verify-ssl="])
        except getopt.GetoptError, e:
            ""
        for o, a in opts:
            if o in ("-k", "--attack"):
                if a != "" and a[0] != '-':
                    attackFile = a
            if o in ("-i", "--continue"):
                if a != '' and a[0] != '-':
                    crawlerFile = a

        print(_("Wapiti-SVN (wapiti.sourceforge.net)"))
        print(_("WARNING: This is a development version. Some features may be broken."))
        if attackFile is not None:
            if crawlerPersister.isDataForUrl(attackFile) == 1:
                crawlerPersister.loadXML(attackFile)
                # TODO: xml structure
                wap.urls = crawlerPersister.getBrowsed()
                wap.forms = crawlerPersister.getForms()
                # wap.uploads = crawlerPersister.getUploads()
                print(_("File {0} loaded. Wapiti will use it to perform the attack").format(attackFile))
            else:
                print(_("File {0} not found."
                        "Wapiti will scan the web site again").format(attackFile))
                wap.browse(crawlerFile)
        else:
            wap.browse(crawlerFile)
        try:
            wap.attack()
        except KeyboardInterrupt:
            print('')
            print(_("Attack process interrupted."
                    "To perform again the attack,"
                    "lauch Wapiti with \"-i\" or \"-k\" parameter."))
            print('')
            pass
    except SystemExit:
        pass
