import time

import aiohttp
import environs
import json

env = environs.Env()
env.read_env(".env")

KINOPOISK = env.str('KP_TOKEN')
API = 'https://kinopoiskapiunofficial.tech/api/v2.1/'
headers = {"X-API-KEY": KINOPOISK}


class SEARCH:
    def __init__(self, data: dict):
        self.kp_id = data['filmId']
        self.name = data['nameRu'] if data['nameEn'] == '' else data['nameEn']
        self.ru_name = data['nameRu']
        self.year = data['year'].split('-')[0]
        self.duration = data['filmLength']
        self.genres = [genre['genre'] for genre in data['genres']]
        self.countries = [country['country'] for country in data['countries']]
        self.kp_rate = data['rating']
        self.kp_url = f'https://www.kinopoisk.ru/film/{data["filmId"]}/'
        self.poster = data['posterUrl']
        self.poster_preview = data['posterUrlPreview']


async def main(query):

    async with aiohttp.ClientSession() as session:
        for _ in range(3):
            try:
                async with session.get(API + 'films/search-by-keyword', headers=headers,
                                       params={"keyword": query, "page": 1}, ssl=False) as response:

                    request = await response.text()
                    request_json = json.loads(request)
                    output = []
                    for film in request_json['films']:
                        try:
                            if len(output) == 3:
                                continue
                            output.append(SEARCH(film))
                        except (Exception, BaseException):
                            continue
                    return output
            except json.decoder.JSONDecodeError:
                time.sleep(0.5)
                continue
