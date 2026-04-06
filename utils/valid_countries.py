from rapidfuzz import process
import pandas as pd

valid_countries = [
    'united_kingdom','france','germany','usa','australia','spain','italy',
    'netherlands','belgium','switzerland','portugal','japan','canada',
    'sweden','norway','finland','austria','denmark','ireland'
]

def normalize_country(country):
    if pd.isna(country):
        return country

    match, score, _ = process.extractOne(country, valid_countries)

    if score >= 60:  # umbral
        return match
    return country
