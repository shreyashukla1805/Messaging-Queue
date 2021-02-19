import json
import jsonpickle
from json import JSONEncoder


class Parser:

    def serializeToJsonConvertor(self, requestObject):
        imqJson = jsonpickle.encode(requestObject, unpicklable=False)
        # print(imqJson)
        return json.dumps(imqJson, indent=4)

    def deserializeJsonFormattedData(self, responseObject):
        imqJson = jsonpickle.decode(responseObject)
        return json.loads(imqJson)