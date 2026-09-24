import requests
import streamlit as st

st.title('Pokemon')

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_pokemon(name_or_id: str, timeout: float = 6) -> dict:
    r = requests.get(f"{BASE_URL}/{str(name_or_id).strip().lower()}", timeout=timeout)
    r.raise_for_status()
    return r.json()


pokemon = st.text_input("Enter pokemon name/id")
res = fetch_pokemon(pokemon)

if st.button("Search"):
    st.write("Id: ", res["id"])
    st.write("Name: ", res["name"])
    st.write("Weight:", res["weight"])