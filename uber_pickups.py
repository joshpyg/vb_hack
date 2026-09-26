import requests
import streamlit as st

st.title('Pokemon')

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon(name_or_id: str, timeout: float = 6) -> dict:
    """Raise requests.HTTPError if the name/id doesn't exist (404) or on network errors."""
    r = requests.get(f"{BASE_URL}/{str(name_or_id).strip().lower()}", timeout=timeout)
    r.raise_for_status()
    return r.json()

st.title("Pokemon Search")

name = st.text_input("Name")

if st.button("Search"):
    try:
            res = fetch_pokemon(name)

            id = res["id"]
            poke_name = res["name"].capitalize()
            height = res["height"] / 10
            weight = res["weight"] / 10

            image = res["sprites"]["other"]["official-artwork"]["front_default"]
            if image is None:
                image = res["sprites"]["front_default"]

            types = []
            for t in res["types"]:
                types.append(t["type"]["name"].capitalize())

            st.image(image, width = 100)

            st.subheader("#" + str(id) + " " + poke_name)
            st.write("Type: " + " / ".join(types))
            st.write("Height:", height, "m")
            st.write("Weight:", weight, "kg")

            st.subheader("Base stats")
            hp = 0
            attack = 0
            defense = 0
            special_attack = 0
            special_defense = 0
            speed = 0

            for stat in res["stats"]:
                stat_name = stat["stat"]["name"]
                if stat_name == "hp":
                    hp = stat["base_stat"]
                if stat_name == "attack":
                    attack = stat["base_stat"]
                if stat_name == "defense":
                    defense = stat["base_stat"]
                if stat_name == "special-attack":
                    special_attack = stat["base_stat"]
                if stat_name == "special-defense":
                    special_defense = stat["base_stat"]
                if stat_name == "speed":
                    speed = stat["base_stat"]

            col1, col2, col3, col4, col5, col6 = st.columns(6)
            col1.metric("Hp", hp)
            col2.metric("Attack", attack)
            col3.metric("Defense", defense)
            col4.metric("Special Attack", special_attack)
            col5.metric("Special Defense", special_defense)
            col6.metric("Speed", speed)
    except requests.HTTPError:
            st.error("Pokémon not found!")