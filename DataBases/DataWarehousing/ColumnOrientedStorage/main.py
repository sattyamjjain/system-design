import pandas as pd

data = {'id': [1, 2], 'name': ['John Doe', 'Jane Smith'], 'email': ['john.doe@example.com', 'jane.smith@example.com']}
df = pd.DataFrame(data)
df.to_csv('example.csv', index=False)
df = pd.read_csv('example.csv')
result = df[['id', 'name']]
print(result)
