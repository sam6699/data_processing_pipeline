from layers.base import PipelineLayerInterface
from data_objects.pipeline_data_object import PipeLineDataObject
import abc
from bs4 import BeautifulSoup


class DataProcessLayer(PipelineLayerInterface, metaclass=abc.ABCMeta):

    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        """Load in the data set"""
        pass


class HtmlProcessor(DataProcessLayer):
    def __init__(self, func, is_raw=False):
        self._process_func = func
        self._is_raw = is_raw

    def run(self, raw_data: PipeLineDataObject) -> PipeLineDataObject:
        processed = []
        if self._is_raw:
            for item in raw_data.content:
                processed += self._process_func(BeautifulSoup(item, "html.parser"))
        else:
            for item in raw_data.content:
                processed += self._process_func(item)
        return PipeLineDataObject(processed)


class DataProcessor(DataProcessLayer):
    def __init__(self, func, func_params=tuple()):
        self._process_func = func
        self._func_params = func_params

    def run(self, raw_data: PipeLineDataObject) -> PipeLineDataObject:
        processed = []

        for key, value in raw_data.content:
            processed.append(
                [key, self._process_func(*((value,) + self._func_params))]
            )
        return PipeLineDataObject(processed)
