
import asyncio
import datetime
import re
import lxml.html
import pandas as pd
import logging
import argparse
from aiohttp import ClientSession

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

unicode = re.compile(r'[^\x00-\x7f]')


async def fetch(url, session):        
    async with session.get(url) as response:
        return await response.text()  
        


 
async def crawler():
    url='http://db.chgk.info/'
    api_url_main='http://db.chgk.info/last'
    api_url='http://db.chgk.info{tour}'
    session = ClientSession()       
    r = await fetch(api_url_main, session)
    tree = lxml.html.fromstring(r)
    refs1 = tree.xpath('tr[@class = "odd"]/td/a/@href')
    refs2 = tree.xpath('tr[@class = "even"]/td/a/@href')
    for i in refs1:        
        r = fetch(api_url.format(tour=i), session)
        tree = lxml.html.fromstring(r)
        text = tree.xpath('//strong[@class="question"]/text()')
        text = '-Question '.join(text)
        text = tree.xpath('//strong[@class="Answer"]/text()')
        text = '-Asnwer '.join(text)
    for j in refs2:        
        r = fetch(api_url.format(tour=j), session)
        tree = lxml.html.fromstring(r)
        text = tree.xpath('//strong[@class="question"]/text()')
        text = '-Question '.join(text)
        text = tree.xpath('//strong[@class="Answer"]/text()')
        text = '-Asnwer '.join(text)
    return text

    
 
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(crawler()))
loop.close() 

 