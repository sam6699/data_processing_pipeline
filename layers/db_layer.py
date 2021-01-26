from abc import ABC

from layers.base import PipelineLayerInterface
from data_objects.pipeline_data_object import PipeLineDataObject
import abc
from db.mysql_db import MySqlService


class DbLayer(PipelineLayerInterface):
    def __init__(self, connector: MySqlService, read=True, query: str = None):
        self.connector = connector
        self.query = query
        self.read = read

    def run(self, data: PipeLineDataObject) -> PipeLineDataObject:
        if self.read:
            return PipeLineDataObject(
                self.connector.get_query(data.content, self.read))
        else:
            self.connector.insert_query(self.query, data.content)
