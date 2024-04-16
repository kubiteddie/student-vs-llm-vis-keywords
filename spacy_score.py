import spacy
import pandas as pd
import json

def read_data():
    llmkeywords = pd.read_csv("datastore/llm_answers_clean.csv")
    wordcounts = []
    wordcounts.append(pd.read_csv("datastore/group1_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group2_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group3_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group4_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group5_student_wordcounts.csv"))
    return llmkeywords, wordcounts

def calculate_scores(llmkeywords, wordcounts, nlp):
    enddata = dict()
    for idx, llmdata in llmkeywords.iterrows():
        wordpairs = []
        keywords = list(llmdata[['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10']])
        currcounts = wordcounts[idx]
        for idx2, wordcount in currcounts.iterrows():
            for word in keywords:
                wordpairdata = dict()
                llmword = nlp(word)
                studentword = nlp(str(wordcount[0]))
                sim = llmword.similarity(studentword)
                wordpairdata['llm_keyword'] = word
                wordpairdata['student_term'] = wordcount[0]
                wordpairdata['similiarity'] = sim
                wordpairdata['count'] = wordcount[1]
                wordpairs.append(wordpairdata)
        enddata[idx+1] = wordpairs
    return enddata

if __name__ == "__main__":
    llmkeywords, wordcounts = read_data()
    nlp = spacy.load("en_core_web_lg")
    enddata = calculate_scores(llmkeywords, wordcounts, nlp)
    with open('datastore/finalsimscores_stem.json', 'w') as file:
        json.dump(enddata, file, indent=4)
    