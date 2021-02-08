import xml.etree.ElementTree as ET

def read_by_row(file,params):
    for evt, element in ET.iterparse(file):
        if element.tag == params['element_name'] and evt == 'end':
            yield element

def find_doc_names(documents,params):
    exceptions = ET.Element('exceptions')
    cnt = 0
    doc_names = []
    for document in documents:
        try:
            doc_names.append(document.find('name').text.strip())
        except Exception as err:
            exceptions.append(document)
            cnt +=1
    if cnt > 0:
        file_name = f"exceptions/{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.xml"
        ET.ElementTree(element=exceptions).write(file_name)
    return doc_names
