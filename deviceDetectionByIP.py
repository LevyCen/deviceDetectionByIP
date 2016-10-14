import os
from os import listdir
from string import *

diccAP = {} #diccionario vacio
#Variables para conocer la fecha del registro
apACtivos = int(0)
apInactivos = int(0)
ffileCSV = open("apInfo.csv","r")

#Se extrae linea por linea del archivo csv
for lineaDeCSV in ffileCSV:
	#se acomoda en un arreglo, dividido por las comas
    lineaLeidaCSV = split(lineaDeCSV,',')

    columnaNameAP =  strip(lineaLeidaCSV[0])
    columnaMACAP =  strip(lineaLeidaCSV[1])
    columnaIPAP =  strip(lineaLeidaCSV[2])

    ipPorRevisar= columnaIPAP
    
    #hostname = "google.com" #example
    print "\n\n"
    print '#############' + columnaNameAP +' - '+ columnaIPAP + '#############'
    hostname = str(columnaIPAP) 
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
    	print '\n'+ columnaNameAP + ' is up!'
    	apACtivos=apACtivos + 1
    else:
    	print '\n'+ columnaNameAP + ' is down!'
    	apInactivos = apInactivos + 1

print '------------- Resultados -------------'
print '------------- AP Activos = '+str(apACtivos) + '-------------'
print '------------- AP Inactivos = '+str(apInactivos) + '-------------'
