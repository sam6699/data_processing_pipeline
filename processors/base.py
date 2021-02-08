class ExcelProcessor:
    def __init__(self,process_func=None,params=None):
        self._process_func = process_func
        self._params = params
    @property
    def process_func(self):
        return self._process_func
    
    @process_func.setter
    def process_func(self,process_func):
        self._process_func = process_func
    
    def run(self,doc):
        if self._params is None:
            return self._process_func(data=doc)
        else:
            return self._process_func(data=doc,params=self._params)

class XMLProcessor:
    def __init__(self,process_func=None,params=None):
        self._process_func = process_func
        self._params = params
    @property
    def process_func(self):
        return self._process_func
    
    @process_func.setter
    def process_func(self,process_func):
        self._process_func = process_func
    
    def run(self,doc):
        if self._params is None:
            return self._process_func(data=doc)
        else:
            print(doc)
            return self._process_func(document=doc,params=self._params)

