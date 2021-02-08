class Pipeline:
    def __init__(self, layers=list(),verbose=None):
        self._verbose = verbose
        self._layers = layers

    @property
    def steps(self) -> list:
        return self._layers

    @steps.setter
    def steps(self, layers: list) -> None:
        self._layers = layers

    def run(self, dataset: list) -> list:
        result: list = []
        for raw in dataset:
            if self._verbose is not None:
                self._verbose(raw)
            temp = raw
            for layer in self._layers:
                temp = layer.run(temp)
            result.append(temp)
        return result
