import spacy
import pandas as pd

#nlp = spacy.load("en_core_web_lg")

def read_data():
    llmkeywords = pd.read_csv("datastore/llm_answers_clean.csv")
    wordcounts = []
    wordcounts.append(pd.read_csv("datastore/group1_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group2_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group3_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group4_student_wordcounts.csv"))
    wordcounts.append(pd.read_csv("datastore/group5_student_wordcounts.csv"))
    return llmkeywords, wordcounts

if __name__ == "__main__":
    llmkeywords, wordcounts = read_data()
    print(wordcounts)