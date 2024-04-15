import pandas as pd
from collections import defaultdict
from nltk.stem import PorterStemmer

outfile = "datastore/group{}_student_wordcounts.csv"

def rollup_group(category, subset):
    counts = defaultdict(int)
    corpuslist = list(subset.split(" "))
    ps = PorterStemmer()
    stemmedlist = []
    # Stemming student responses
    for word in corpuslist:
        stemmedlist.append(ps.stem(word))

    for term in stemmedlist:
        counts[term] += 1
    countsDF = pd.DataFrame.from_dict(counts.items())
    countsDF.to_csv(outfile.format(category), index=False)

if __name__ == "__main__":
    
    classdata = pd.read_csv("datastore/intermediate_categories2.csv")
    answers_group = classdata.groupby(by=['Category'])
    categories = classdata['Category'].unique()
    for category in categories:
        stringdata = ' '.join(answers_group.get_group(category)['Task1Naming'].tolist()).lower()
        rollup_group(category, stringdata)

