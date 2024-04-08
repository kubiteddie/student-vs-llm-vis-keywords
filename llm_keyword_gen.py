import pandas as pd
import spacy
import cohere
import google.generativeai as genai

def gemini_init():
    GOOGLE_API_KEY = open('gemini-api-key.txt')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    return model

def cohere_init():
    co = cohere.Client("luN4E3VyjZumWO17DsMUN43ZrFDuS81rHuPvrEk5")
    return co

def get_keywords(co, dataSubset):
   pass 

if __name__ == '__main__':
    co = cohere_init()
    classdata = pd.read_csv("datastore/class-data-collection.csv")
