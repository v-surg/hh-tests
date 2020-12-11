
import requests
import asyncio
# import aiohttp


TOKEN = 'JOIN9M0LTBRLMF0S1JBLA2VUSFHAPSJF63PGT89P96D6HGNNHALD7QL2PSTKUD8P'
URL = 'https://api.hh.ru/vacancies'


def get(text):
    "get request to api.hh.ru/vacancies"
    params = {'token' : TOKEN,
            'text': text}
    return requests.get(URL, params=params)


def get_json_list_sync(lst):
    "synchronous get fot multiple text-requests"
    results = []
    params = {'token': TOKEN,
              'text': ''}
    with requests.session() as sess:
        for text in lst:
            params['text'] = text
            results.append(sess.get(URL, params=params))

    return results


def get_json_list_async(lst):
    "asynchronous get fot multiple text-requests"
    pass