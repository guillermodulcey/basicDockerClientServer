import sys
from Process.ProcessFactory import ProcessFactory

##config1 y config2

f = open(sys.argv[1],'r')
config = f.read().split('\n')
f.close()

servers = config[0].replace(' ','').replace('servers=','').split(';')
entrada = config[1].replace(' ','').replace('entrada=','')
salida = config[2].replace(' ','').replace('salida=','')
espera = config[3].replace(' ','').replace('espera=','')
extractor = config[4].replace(' ','').replace('extractor=','')
parametrosE = config[5].replace(' ','').replace('parametros=','').split(';')
transform = config[6].replace(' ','').replace('transform=','')
parametrosT = config[7].replace(' ','').replace('parametros=','').split(';')
load = config[8].replace(' ','').replace('load=','')
parametrosL = config[9].replace(' ','').replace('parametros=','').split(';')
gad = config[10].replace(' ','').replace('orden=','').split(';')

for process in gad:
    if process == 'E':
        E = ProcessFactory().getProcess(process,extractor,servers,parametrosE,espera).process(entrada)
    if process == 'T':
        T = ProcessFactory().getProcess(process,transform,servers,parametrosT,espera).process(E)
    if process == 'L':
        L = ProcessFactory().getProcess(process,load,servers,parametrosL,espera).process(salida)

#for li in L:
#    print(li)