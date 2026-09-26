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

            st.write("ID:", res["id"])
            st.write("Name:", res["name"])
            st.write("Weight:", res["weight"])
            st.write("Ability:", res["abilities"][0]["ability"]["name"])

            st.write("Base Stats:")
            for stat in res["stats"]:
                st.write(stat["stat"]["name"], ":", stat["base_stat"])
    except requests.HTTPError:
            st.error("Pokémon not found!")