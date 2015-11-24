import re
import os
 
current = 1

if __name__ == '__main__':
        for i in os.listdir(os.getcwd()):
                

                if (not i.endswith('.py')):
                        
                        print current

                        f = open(i, 'r')
                        texto = f.read()
         
                        result = ''
                        while (result != None):
                                result = re.search('<script(.*?)</script>', texto)
                                if (result != None):
                                        texto = texto.replace('<script' + result.group(1) + '</script>', '')
         
                        result = ''
         
                        while (result != None):
                                result = re.search('<a name="(.*?)<hr>', texto)
                                if (result != None):
                                        texto = texto.replace('<a name="' + result.group(1) + '<hr>', '')
                        
                        result = re.search('<link rel="stylesheet" type="text/css" href="(.*?)">', texto)
                        if (result != None):
                                texto = texto.replace('<link rel="stylesheet" type="text/css" href="' + result.group(1) + '">', 
                                '<link rel="stylesheet" type="text/css" href="estilo.css"> <meta charset="UTF-8">')

         
                        texto = texto.replace('<a href', '<a id')
         
         
                        f = open(i, 'w')
                        f.write(texto)

                        current += 1