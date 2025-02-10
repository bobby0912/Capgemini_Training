import pandas as pd
data = {
    'name': ['alice', 'bob', 'carlo'],
    'age': [21, 34, 32],
    'city': ['hyderabad', 'los angles', 'ameerpet']
}

df2 = pd.read_csv("customers-100.csv")

df = pd.DataFrame(data)
# json1=df2.to_json()
# with open("customers-100.json",'w') as file:
#     file.write(json1)

df.sort_values(by='age', ascending=False)
# print(df)
# print(df2.head(10))
