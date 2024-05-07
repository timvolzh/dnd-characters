
import json
import asyncpg

from aiohttp import web

app = web.Application()


class CharView(web.View):

    async def get(self):
        char_name = str(self.request.match_info['char_name'])






