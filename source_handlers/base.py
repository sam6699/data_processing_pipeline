import requests
import xml.etree.ElementTree as ET

class XMLDataReader:
    def __init__(self,process_func=None, params=None):
        self._params = params
        self._process_func = process_func

    @property
    def process_func(self):
        return self._process_func
    
    @process_func.setter
    def process_func(self,process_func):
        self._process_func = process_func

    @property
    def params(self):
        return self._params
    
    @params.setter
    def params(self,params):
        self._params = params

    def run(self,uri):
        return self._process_func(uri,self._params)
