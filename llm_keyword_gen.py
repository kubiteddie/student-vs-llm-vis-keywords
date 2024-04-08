import pandas as pd
import spacy
import cohere
import google.generativeai as genai

def gemini_init():
    google_api_key_file = open('gemini-api-key.txt')
    GOOGLE_API_KEY = google_api_key_file.read()
    google_api_key_file.close()
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    return model

def cohere_init():
    cohere_api_key_file = open('cohere-api-key.txt')
    COHERE_API_KEY = cohere_api_key_file.read()
    cohere_api_key_file.close()
    co = cohere.Client(COHERE_API_KEY)
    return co

def get_keywords(co, dataSubset):
   pass 

if __name__ == '__main__':
    co = cohere_init()
    classdata = pd.read_csv("datastore/class-data-collection.csv")
