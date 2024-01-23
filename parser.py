import requests


def get_names_champions() -> list[str]:
    response = requests.get('https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion.json',
                            headers={"User-Agent": "Mozilla/5.0"})
    names = list(response.json()['data'].keys())
    return names


def champions_kd() -> dict:
    dict_kd = {}
    for name in get_names_champions():
        response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/14.1.1/data/en_US/champion/{name}.json',
                                headers={"User-Agent": "Mozilla/5.0"})
        kd_champ = []
        for abilities in range(0, 4):
            kd_champ.append(response.json()['data'][name]['spells'][abilities]['cooldown'])

        dict_kd[name] = kd_champ

    return dict_kd



