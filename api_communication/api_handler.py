from api_communication import walmart_api
from typing import Dict

func_dict = {'walmart': lambda search_term: walmart_api.search(search_term)}


def handle_request(search_term: str, api: str) -> Dict:
    for key in func_dict:
        if key == api.lower():
            return func_dict[key](search_term)

#http://127.0.0.1:5000/search?search_term=pencil&api=walmart

