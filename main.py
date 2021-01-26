import re
from bs4 import BeautifulSoup

from data_objects.pipeline_data_object import PipeLineDataObject
from layers.data_loader_layer import HttpDataLoader
from layers.processing_layer import HtmlProcessor, DataProcessor
from models.sequential import Pipeline
from layers.db_layer import DbLayer
from layers.base import DefaultLayer
from db.mysql_db import MySqlService


def clean_data(data: str):
    t = str.maketrans("\n\t\r", "   ")
    return data.translate(t)


def regex_clean(data: str, pattern: re.Pattern):
    return pattern.sub(' ', data)

def extract_data(body: BeautifulSoup):
    links = body.find_all("a")
    results = []
    for link in links:
        results.append(
            [link.string,link['href']]
        )
    return results

host = ""
user = ""
password = ""
db = ""
pattern = re.compile('<.*?>')
db_out_query = "INSERT INTO mytable (name,value) values (%s, %s)"
db_in_query = "SELECT url FROM links"



if __name__ == "__main__":
    connector = MySqlService(host, user, password, db)


    dataset = [
        PipeLineDataObject(db_in_query)
    ]

    layers = [
        DbLayer(connector, read=True),
        HtmlProcessor(extract_data, is_raw=True),
        DataProcessor(regex_clean, func_params=(pattern,)),
        DataProcessor(clean_data),
        DbLayer(connector, read=False, query=db_out_query)
    ]

    pipeline = Pipeline(layers)

    result = pipeline.run(dataset)

