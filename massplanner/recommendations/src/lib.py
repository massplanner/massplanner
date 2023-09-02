from aiohttp.web_request import FileField

import base64


def encode(message):
    return base64.b64encode(message.encode('ascii')).decode('ascii')


def set_files(function):
    async def wrapper(*args):
        try:
            request = args[1]  # class based handler
        except IndexError:
            request = args[0]  # function based handler

        files = {}
        form_data = await request.post()
        for field_name, field_value in form_data.items():
            if isinstance(field_value, FileField):
                files[field_name] = field_value
        request.files = files
        return await function(*args)

    return wrapper


class GptFunctionParameterProperty:

    def __init__(self, name, type, description, example) -> None:
        self.name = name
        self.type = type
        self.description = description
        self.example = example

    def get_serialized(self):
        return {
            self.name: {
                "type": self.type,
                "description": self.description,
                "example": self.example
            }
        }
        

class GptFunctionParameter:

    def __init__(self, type):
        self.type = type
        self.properties = {}

    def add_property(self, property: GptFunctionParameterProperty):
        prop = property.get_serialized()
        self.properties[property.name] = prop[property.name]


class GptFunction:

    def __init__(self, name, description, parameter: GptFunctionParameter) -> None:
        self.name = name
        self.description = description
        self.parameter = parameter
        
    def get_serialized(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": self.parameter.type,
                "properties": self.parameter.properties
            }
        }



