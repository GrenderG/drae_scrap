#coding: utf8

import os
 
current = 1

def decodify(old_name):
    old_name = old_name.replace('%C0', 'À')
    old_name = old_name.replace('%C1', 'Á')
    old_name = old_name.replace('%C8', 'È')
    old_name = old_name.replace('%C9', 'É')
    old_name = old_name.replace('%CC', 'Ì')
    old_name = old_name.replace('%CD', 'Í')
    old_name = old_name.replace('%D1', 'Ñ')
    old_name = old_name.replace('%D2', 'Ò')
    old_name = old_name.replace('%D3', 'Ó')
    old_name = old_name.replace('%D9', 'Ù')
    old_name = old_name.replace('%DA', 'Ú')
    old_name = old_name.replace('%E0', 'à')
    old_name = old_name.replace('%E1', 'á')
    old_name = old_name.replace('%E8', 'è')
    old_name = old_name.replace('%E9', 'é')
    old_name = old_name.replace('%EC', 'ì')
    old_name = old_name.replace('%ED', 'í')
    old_name = old_name.replace('%F1', 'ñ')
    old_name = old_name.replace('%F2', 'ò')
    old_name = old_name.replace('%F3', 'ó')
    old_name = old_name.replace('%F9', 'ù')
    old_name = old_name.replace('%FA', 'ú')
    old_name = old_name.replace('%DC', 'Ü')
    old_name = old_name.replace('%FC', 'ü')
    old_name = old_name.replace('%AD', '-')
    old_name = old_name.replace('%A1', '¡')

    return old_name
    
if __name__ == '__main__':

	for f in os.listdir(os.getcwd()):

	    new_name = decodify(f)
	    os.rename(f, new_name)
	    print str(current) + '-> ' + f + ' to ' + new_name

	    current += 1
