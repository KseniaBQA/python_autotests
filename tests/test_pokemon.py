import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
headers = {
    "Content-Type": "application/json",
    "trainer_token": "43f02dbc2d3aa62fd6a9120f0f0ccfbd",
}

def test_get_trainers():
    """
    PT-1  GET /trainers
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status'

def test_get_trainer_by_id():
   """
   PT-2  GET /trainers by id
   """
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3551}, timeout=5)
   assert response.json()['trainer_name'] == 'Kodi', ''
