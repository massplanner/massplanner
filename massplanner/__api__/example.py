#!/usr/local/bin/python3.9
from aiohttp import web
import sys

async def default(request):
    headers = { "content_type": "text/html" }
    return web.json_response({ "message": "ExampleApi" }, headers=headers)

app = web.Application()

base_path = sys.argv[2] if len(sys.argv) > 2 else ''
app.add_routes([
    web.get(base_path + "/api", default),
])

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
web.run_app(app, port=port)