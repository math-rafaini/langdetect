import pandas as pd
from langdetect import detect

# Language detection

df = pd.read_excel('texts.xlsx')

langs = []
words = []

for index, row in df.iterrows():
    lang = detect(row['Words'])
    if(lang == "dt"):
        lang = "German"

    elif(lang == "en"):
        lang = "English"

    elif(lang == "pt"):
        lang = "Portuguese"

    else:
        lang = lang + " - ISO 639-1"

    langs.append(lang)
    words.append(row['Words'])

df = pd.DataFrame({'Words': words, 'Languages detected': langs})
print(df)
