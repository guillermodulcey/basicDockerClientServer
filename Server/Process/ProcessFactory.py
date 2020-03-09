from E.ExtractorFactory import ExtractorFactory
from T.TransformFactory import TransformFactory
from L.LoadFactory import LoadFactory

class ProcessFactory():
    def __init__(self):
        pass

    def getProcess(self, nombreProcess, tipoProcess, servers, parametros, espera):
        if nombreProcess == "E":
            return ExtractorFactory().getExtractor(tipoProcess, servers, parametros, espera)
        if nombreProcess == "T":
            return TransformFactory().getTransform(tipoProcess, servers, parametros, espera)
        if nombreProcess == "L":
            return LoadFactory().getLoad(tipoProcess, servers, parametros, espera)