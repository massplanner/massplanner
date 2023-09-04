import openai
import os 
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
                "example": str(self.example)
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

def add_gpt_function_property(parameter, property_info):
    """Helper function to add a property to the GptFunctionParameter."""
    property = GptFunctionParameterProperty(
        name=property_info["name"], 
        type=property_info["type"], 
        description=property_info["description"], 
        example=property_info["example"]
    )
    parameter.add_property(property)

async def get_features_from_document(document, properties, model='gpt-3.5-turbo-0613'):
    try:
        parameter = GptFunctionParameter(type="object")
        for property_info in properties:
            add_gpt_function_property(parameter, property_info)

        function = GptFunction(
            name="get_information",
            description="Extracts the required information from the resume text",
            parameter=parameter
        )

        messages = [{"role": "user", "content": document }]
        functions = [function.get_serialized()]

        logger.info(functions)

        chat_response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            functions=functions,
            function_call="auto"
        )

        if "choices" in chat_response and "message" in chat_response["choices"][0]:
            chat_response_message = chat_response["choices"][0]["message"]
            if chat_response_message.get("function_call"):
                return {
                    "success": True,
                    "result": json.loads(chat_response_message["function_call"]["arguments"])
                }
            else:
                return {
                    "success": False,
                    "result": chat_response_message
                }
        else:
            return {
                "success": False,
                "result": "Error in response format"
            }
    except Exception as e:
        return {
                "success": False,
                "result": f"An error occurred while getting features from document: {str(e)}"
            }