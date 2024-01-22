import requests

URL = 'https://api.pokemonbattle.me:9104'
headers = {
    "Content-Type": "application/json",
    "trainer_token": "43f02dbc2d3aa62fd6a9120f0f0ccfbd",
}
# 1. Создание покемона

body1 = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}



response = requests.post(url=f'{URL}/pokemons', json=body1, headers=headers, timeout=5)
print(response)



# # 2. Смена имени покемона

body2 = {
    "pokemon_id": "28332",
    "name": "Newbiese2",
    "photo": "https://dolnikov.ru/pokemons/albums/003.png"
}



requests.put(url=f'{URL}/pokemons', json=body2, headers=headers, timeout=5)
print(response)


# 3. Поймать покемона в покебол

body3 = {
    "pokemon_id": "28332"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body3, headers=headers, timeout=5)
print(response)