from resteasy import RESTEasy, json

import sys

def get_city_from_cep( cep: str ) -> str:
    cep = cep.replace('-', '')
    api = RESTEasy(endpoint=f'https://viacep.com.br/ws/{cep}/json',
               verify=True, cert=None, timeout=60,
               allow_redirects=True,
               encoder=json.dumps, decoder=json.loads, debug=False)
    return api.get()['localidade'].encode('iso-8859-1').decode('utf-8')
