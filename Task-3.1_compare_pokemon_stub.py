"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
class pokemon:
    def __init__(self, name):
        self.name=name.lower()
        url="https://pokeapi.co/api/v2/pokemon/{self.name}"
        response=htpx.get(url)
        if response.status_code != 200:
            print("Pokemon not found!")
        indivi=resdponse.json()
        ini_attack=ini_defense=ini_speed=ini_hp=None
        for num in indivi["stats"]:
            if num["name"]["stat"]=="attack":
                ini_attack=num[base_stat]
            if num["name"]["stat"]=="defense":
                ini_defense=num[base_stat]
            if num["name"]["stat"]=="speed":
                ini_speed=num[base_stat]
            if num["name"]["stat"]=="hp":
                ini_hp=num[base_stat]
        self.max_hp=measure_hp(ini_hp, level=50)
        self.now_hp=self.max_hp
        self.attack=measure_level(ini_attack, level=50)
        self.speed=measure_level(ini_speed, level=50)
        self.defense=measure_level(ini_defense, level=50)
def compare_pokemon(pokemon1, pokemon2):
    hp1=int(pokemon1.max_hp)
    hp2=int(pokemon1.max_hp)
    if hp1-hp2>0:
        print(f"On hp {pokemon1.name} win")
    elif hp1-hp2==0:
        print("On hp they are same")
    else:
        print(f"On hp {pokemon2.name} win")
    att1=int(pokemon1.attack)
    att2=int(pokemon2.attack)
    if att1-att2 >0:
        print(f"On attack {pokemon1.name} win")
    if att1-att2==0:
        print("On attack they are same")
    else:
        print(f"On attack {pokemon2.name} win")
    spe1=int(pokemon1.speed)
    spe2=int(pokemon2.speed)
    if spe1-spe2>0 :
        print(f"On speed {pokemon1.name} win")
    if spe1-spe2==0:
        print("On speed they are same")
    else:
        print(f"On speed {pokemon2.name} win")
    def1=int(pokemon1.defense)
    def2=int(pokemon2.defense)
    if def1-def2>0:
        print(f"On defense {pokemon1.name} win")
    if def1-def2==0:
        print("On defense they are same")
    else:
        print(f"On defense {pokemon2.name} win")
    """Compare the calculated stats of two Pokémon."""
    # TODO: Fetch data for both Pokémon from the PokéAPI
    
    # TODO: Extract relevant stats (HP, attack, defense, speed)
    
    # TODO: Calculate stats at level 50 for both Pokémon
    
    # TODO: Compare the calculated stats and print the results

# Example usage
if __name__ == "__main__":
    pikachu=pokemon("pikachu")
    bulbasaur=pokemon("bulbasaur")
    compare_pokemon(pikachu, bulbasaur)

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""

