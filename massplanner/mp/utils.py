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