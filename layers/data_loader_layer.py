from layers.base import PipelineLayerInterface
import requests
from data_objects.pipeline_data_object import PipeLineDataObject
import abc


class DataLoader(PipelineLayerInterface, metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data') and
                callable(subclass.load_data) or
                NotImplemented)

    @abc.abstractmethod
    def load_data(self, url: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class HttpDataLoader(DataLoader):
    def load_data(self, url: str) -> str:
        request = requests.get(url)
        return [request.text]

    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        return PipeLineDataObject(self.load_data(data.content))

