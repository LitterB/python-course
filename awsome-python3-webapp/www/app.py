# !user/bin/env python3
# -*- coding: utf-8 -*-

import logging;logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(text='awesome')


app = web.Application()
app.add_routes([web.get("/", index)])
web.run_app(app, host='127.0.0.1', port=9000)
logging.info('server started at http://127.0.0.1：9000...')
