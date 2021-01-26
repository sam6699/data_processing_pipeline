import abc
from data_objects.pipeline_data_object import PipeLineDataObject


class PipelineLayerInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'run') and
                callable(subclass.run) or
                NotImplemented)

    @abc.abstractmethod
    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        """Load in the data set"""
        raise NotImplementedError


class DefaultLayer(PipelineLayerInterface):
    def __init__(self, exec_func, func_params):
        self.exec_func = exec_func
        self.func_params = func_params

    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        return self.exec_func(*self.func_params)
