import streamlit as st
st.set_page_config(page_title="Language Translator")

st.title('Nigeria translator')
st.write("English words into nigeria languages")

translations = {
    "Yoruba": {
        "hello": "bawo",
        "water": "omi",
        "food": "ounje",
        "house": "ile",
        "book": "iwe",
        "man": "okunrin",
        "woman": "obinrin",
        "child": "omo",
        "sun": "oorun",
        "moon": "osupa",
        "school": "ile-iwe",
        "go": "lo",
        "come": "wa",
        "sit": "joko",
        "stand": "dide",
        "love": "ife",
        "run": "sa",
        "walk": "rin",
        "fire": "ina",
        "earth": "aye"
    },

    "Igbo": {
        "hello": "ndewo",
        "water": "mmiri",
        "food": "nri",
        "house": "ulo",
        "book": "akwukwo",
        "man": "nwoke",
        "woman": "nwanyi",
        "child": "nwa",
        "sun": "anyanwu",
        "moon": "onwa",
        "school": "ulo akwukwo",
        "go": "gaa",
        "come": "bia",
        "sit": "nodo",
        "stand": "guzo",
        "love": "ihunanya",
        "run": "gba oso",
        "walk": "ga ije",
        "fire": "oku",
        "earth": "uwa"
    },

    "Hausa": {
        "hello": "sannu",
        "water": "ruwa",
        "food": "abinci",
        "house": "gida",
        "book": "littafi",
        "man": "namiji",
        "woman": "mace",
        "child": "yaro",
        "sun": "rana",
        "moon": "wata",
        "school": "makaranta",
        "go": "tafi",
        "come": "zo",
        "sit": "zauna",
        "stand": "tashi",
        "love": "so",
        "run": "gudu",
        "walk": "tafiya",
        "fire": "wuta",
        "earth": "kasa"
    },

    "Edo": {
        "hello": "obokhian",
        "water": "amen",
        "food": "ukpoke",
        "house": "ugie",
        "book": "iwe",
        "man": "okpia",
        "woman": "okhuo",
        "child": "omo",
        "sun": "orhion",
        "moon": "okhuo-orhion",
        "school": "egbe",
        "go": "ghe",
        "come": "wa",
        "sit": "gbe",
        "stand": "ghogho",
        "love": "iyen",
        "run": "gba",
        "walk": "goke",
        "fire": "ekha",
        "earth": "agbon"
    },

    "Tiv": {
        "hello": "mngu",
        "water": "mku",
        "food": "wa",
        "house": "iv",
        "book": "kwagh",
        "man": "or",
        "woman": "nyor",
        "child": "kpam",
        "sun": "kohol",
        "moon": "ihemba",
        "school": "ishim",
        "go": "kwagh",
        "come": "nyi ",
        "sit": "tsô",
        "stand": "va",
        "love": "un",
        "run": "yem",
        "walk": "tyô",
        "fire": "mba",
        "earth": "tar"
    }
}

language = st.selectbox("Choose language:", list(translations.keys()))
word = st.text_input("Enter an english word")

if st.button("Translate"):
    if word in translations[language]:
        st.success(f"Translation: {translations[language][word]}")
    else:
        st.error("Word not found in dictionary")

