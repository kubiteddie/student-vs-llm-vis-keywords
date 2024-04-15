import json
import pandas as pd

score_threshold = 0.25

f = open('./datastore/finalsimscores.json', "r")
data = json.load(f)

keywords = pd.read_csv('./datastore/llm_answers_clean.csv')

out = []
header_info = []


for i, category in enumerate(data):
  category_keywords = keywords.loc[i, :].values.tolist()
  category_keywords = category_keywords[1:]
  
  for keyword in category_keywords:
    header_info.append({'keyword': keyword, 'category': category})


  category_index = 0

  while category_index < len(data[category]):

    best_resp_keyword = {"similiarity": 0}

    for i in range(10):
      if data[category][category_index]['similiarity'] > best_resp_keyword['similiarity']:
        best_resp_keyword = data[category][category_index]

      category_index += 1

    if best_resp_keyword['similiarity'] > score_threshold:
      best_resp_keyword['category'] = category
      out.append(best_resp_keyword)

json_out = {'headers': header_info, 'data': out}

with open("./datastore/filtered_sim_scores.json", "w") as outfile:
  json.dump(json_out, outfile)
