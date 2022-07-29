# convert all the following jl-files (json-lines) with restaurant-reviews to dataframes
# one row per review
#%%
import json
import pandas as pd


input = [
    "../restaurants_vienna7.jl"
]

newtable = []

for fn in input:
    # read the json-lines files line by line:
    with open(fn) as f:
        for line in f:
            # convert the line to a dictionary
            d = json.loads(line)
            print("-----------",d["restaurant_name"],len(d["reviews1_title_text"]),len(d["reviews1_partial_text"]),len(d["reviews1_date_of_review"]))
            if "reviews1_title_text" in d:
                for i in range(len(d["reviews1_title_text"])-1):
                    #print("####",i,d["reviews1_title_text"][i],d["reviews1_partial_text"][i],d["reviews1_date_of_review"][i])
                    try:
                        newtable.append((d["restaurant_name"],d["n_reviews"],d["restaurant_phone"],d["rating"],
                    d["restaurant_address1"],d["rank"],d["reviews1_partial_text"][i],
                     d["reviews1_title_text"][i],
                     d["reviews1_date_of_visit"][i], d["reviewer_user_name"][i], 
                     d["reviews1_date_of_review"][i]))
                    except:
                        print("Error", d["restaurant_name"])
                        pass

    df = pd.DataFrame(newtable, columns=["restaurant_name","n_reviews","restaurant_phone","rating","restaurant_address1","rank",
                                            "reviews1_partial_text","reviews1_title_text","reviews1_date_of_visit","reviewer_user_name",
                                            "reviews1_date_of_review"])
    df.to_csv(fn + ".csv", index=False)
print("Done")
        # %%
