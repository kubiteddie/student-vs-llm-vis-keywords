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

def keyword_query(co, query):
    response = co.chat(
        message = query,
        model="command",
        temperature=1
    )
    return response

def get_keywords(co, dataSubset, numKeywords):
    query = "The following array holds tuples that represent the type of a data visualization and a caption for that visualization in the form of (Type, Caption). Can you generate {} keywords that describe them? {}."
    keyword_responses = []
    vis_tuples = []
    for category, subset in dataSubset.items():        
        vis_tuples.append((subset['VisType'], subset['Caption']))
    keyword_responses = [keyword_query(co, query.format(numKeywords, tuples)) for tuples in vis_tuples]
    return keyword_responses

def get_vis_groups(dataframe):
    groupDict = dict()
    dataframe = dataframe.groupby(by=['Category'])
    for value in dataframe['Category'].unique():
        groupDict[value[0]] = dataframe.get_group(value[0]).to_dict(orient='index')
    return groupDict, dataframe['Category'].unique()

if __name__ == '__main__':
    co = cohere_init()
    groundDF = pd.read_csv("datastore/vis-ground-truth.csv").drop(columns=['VisualizationLink', 'ImageLink', 'Image'])
    groundGroups, categories = get_vis_groups(groundDF)
    keywordSets = [{category[0]: get_keywords(1, groundGroups[category[0]], 10)} for category in categories]
    print(keywordSets)
