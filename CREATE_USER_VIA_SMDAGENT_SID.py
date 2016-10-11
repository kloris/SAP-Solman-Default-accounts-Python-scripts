#!/usr/bin/python

import sapnwrfc
import re

default_host = '192.168.181.128' ;    var_host = raw_input('Host: [%s]' % default_host) ;            var_host = var_host or default_host
default_sysnr = '00' ;          var_sysnr = raw_input('System number: [%s]' % default_sysnr) ; var_sysnr = var_sysnr or default_sysnr
default_client = '001' ;        var_client = raw_input('Client: [%s]' % default_client) ;      var_client = var_client or default_client
default_user = 'SOLMAN_BTC' ; var_user = raw_input('User: [%s]' % default_user) ;            var_user = var_user or default_user
default_pw = 'init1234' ;       var_pw = raw_input('Password: [%s]' % default_pw) ;            var_pw = var_pw or default_pw

sapnwrfc.base.load_config()
conn = sapnwrfc.base.rfc_connect({'ashost':var_host, 'sysnr':var_sysnr, 'client':var_client, 'user':var_user, 'passwd':var_pw, 'lang':'EN' })

### Create SAP user 
fa = conn.discover("SXPG_STEP_XPG_START")
a = fa.create_function_call()
a.EXTPROG("sqlcli")
a.PARAMS("-U DEFAULT INSERT INTO USR02 (MANDT,BNAME,BCODE,USTYP,CODVN) VALUES ('001','GO_IN','C76AB3A59599FE3A','S','G')")
a.STDINCNTL("R")
a.STDOUTCNTL("M")
a.STDERRCNTL("M")
a.TERMCNTL("C")
a.CONNCNTL("H")
a.invoke()
z = a.LOG.value
print z

fa = conn.discover("SXPG_STEP_XPG_START")
a = fa.create_function_call()
a.EXTPROG("sqlcli")
a.PARAMS("-U DEFAULT UPDATE USR02 set PASSCODE='CF017A9A4F1F53ED69CEDC773072B1B24A063A63' where BNAME='GO_IN' and mandt='001'")
a.STDINCNTL("R")
a.STDOUTCNTL("M")
a.STDERRCNTL("M")
a.TERMCNTL("C")
a.CONNCNTL("H")
a.invoke()
z = a.LOG.value
print z

fa = conn.discover("SXPG_STEP_XPG_START")
a = fa.create_function_call()
a.EXTPROG("sqlcli")
a.PARAMS("-U DEFAULT INSERT INTO USREFUS (MANDT,BNAME,REFUSER) VALUES ('001','GO_IN','DDIC')")
a.STDINCNTL("R")
a.STDOUTCNTL("M")
a.STDERRCNTL("M")
a.TERMCNTL("C")
a.CONNCNTL("H")
a.invoke()
z = a.LOG.value
print z

conn.close()
#when succesfully executed a user is created in the SAP system with name GO_IN and password "andinyougo"



