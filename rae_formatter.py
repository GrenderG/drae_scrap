import re
import os
 
for i in os.listdir(os.getcwd()):
 
        if (not i.endswith('.py')):
 
                f = open(i, 'r')
                texto = f.read()
 
                result = ''
                while (result != None):
                        result = re.search('<script(.*)</script>', texto)
                        if (result != None):
                                texto = texto.replace('<script' + result.group(1) + '</script>', '')
 
                result = ''
 
                while (result != None):
                        result = re.search('<a name="(.*)<hr>', texto)
                        if (result != None):
                                texto = texto.replace('<a name="' + result.group(1) + '<hr>', '')
 
                texto = texto.replace('<link rel="stylesheet" type="text/css" href="/drae/css/I.drae.css+estilosCabDrae.css,Mcc.W_CzH9ApGk.css.pagespeed.cf.w1GLVsE-IR.css">',
                        '<link rel="stylesheet" type="text/css" href="estilo.css"> <meta charset="UTF-8">')
 
                texto = texto.replace('<a href', '<a id')
 
 
                f = open(i, 'w')
                f.write(texto)