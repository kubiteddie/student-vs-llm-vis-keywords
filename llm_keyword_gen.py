import pandas as pd
import spacy
import cohere
import google.generativeai as genai

classdata = pd.read_csv("datastore/class-data-collection.csv")
GOOGLE_API_KEY = open('gemini-api-key.txt')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Will I be able to talk to you for free or will my google account be charged")
print(response)
print(response.text)