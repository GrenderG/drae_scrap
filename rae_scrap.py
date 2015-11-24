#coding: utf-8

import dryscrape
import codecs
import time
import re

def saveAsHtml(responseBody, fileName):
    
    with codecs.open(fileName + '.html', 'w', 'utf_8') as fileToSave:
        fileToSave.write(responseBody)

if __name__ == '__main__':
    session = dryscrape.Session()        
    word_count = 1
    wait_count = 1

    with open('lemario.txt', 'r') as lemario:
        for line in lemario:
            word = line.strip()
            url = ('http://lema.rae.es/drae/srv/search?type=3&val=%s&origen=APP' % word)
            session.visit(url)
            responseBody = session.body()

            #if there are multiple choices
            if ('<li>' in responseBody):

            	#removing annoying <b>
                responseBody = responseBody.replace('<b>.</b>', '.')
                supsToRemove = re.findall('<b><sup>(.*?)</sup></b>', responseBody)
                for i, j in enumerate(supsToRemove):
                    responseBody = responseBody.replace('<b><sup>' + j + '</sup></b>', '')

                results = re.findall('<b>(.*?)</b>', responseBody)
                searchIds = re.findall('<a href="(.*?)">', responseBody)

                #choose the correct searchId depending if it's a verb or not
                if (not results[0].endswith('r') and not results[0].endswith('rse') or len(searchIds) < 2):
                    searchId = searchIds[0]
                else:
                    searchId = searchIds[1]

                url = ('http://lema.rae.es/drae/srv/%s' % searchId)
                session.visit(url)
                responseBody = session.body()

            while 'Solicitud rechazada' in responseBody:
                session.visit(url)
                responseBody = session.body()
                #time.sleep(0.1)
                print 'Esperando' + ("." * wait_count)
                wait_count += 1
        
            saveAsHtml(responseBody, line.strip())
            #time.sleep(0.1)
            print 'Palabra número: ' + str(word_count) + " -> " + line.strip()
            word_count += 1
            if (wait_count > 1):
                wait_count = 1
