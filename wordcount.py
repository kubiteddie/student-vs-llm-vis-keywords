import pandas as pd
from collections import defaultdict

outfile = "datastore/group{}_student_wordcounts.csv"

def rollup_group(category, subset):
    counts = defaultdict(int)
    corpuslist = list(subset.split(" "))
    for term in corpuslist:
        counts[term] += 1
    countsDF = pd.DataFrame.from_dict(counts.items())
    countsDF.to_csv(outfile.format(category), index=False)

if __name__ == "__main__":
    classdata = pd.read_csv("datastore/intermediate_categories.csv")
    answers_group = classdata.groupby(by=['Category'])
    categories = classdata['Category'].unique()
    for category in categories:
        stringdata = ' '.join(answers_group.get_group(category)['Task1Naming'].tolist()).lower()
        rollup_group(category, stringdata)

