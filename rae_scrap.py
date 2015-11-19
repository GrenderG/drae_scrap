#coding: utf-8

import dryscrape
import codecs
import time

def saveAsHtml(responseBody, fileName):
	
with codecs.open(fileName + ".html", "w", "utf_8") as fileToSave:
	fileToSave.write(responseBody)

if __name__ == "__main__":
	session = dryscrape.Session()		
	word_count = 1
	wait_count = 1
	with open("lemario.txt", "r") as lemario:
		for line in lemario:
			word = line.strip()
			url = ("http://lema.rae.es/drae/srv/search?type=3&val=%s&origen=APP" % word)
			session.visit(url)
			responseBody = session.body()

			while "Solicitud rechazada" in responseBody:
				session.visit(url)
				responseBody = session.body()
				#time.sleep(0.1)
				print "Esperando" + ("." * wait_count)
				wait_count += 1
		
			saveAsHtml(responseBody, line.strip())
			#time.sleep(0.1)
			print "Palabra número: " + str(word_count) + " -> " + line.strip()
			word_count += 1
			if (wait_count > 1):
				wait_count = 1
