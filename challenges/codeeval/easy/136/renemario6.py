import sys

archivo = open(sys.argv[1], 'r')

for i in archivo:
	line = i.strip()
	if line:
		
archivo.close()
