import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")

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
