import json
import pandas as pd
df = pd.read_csv('results_new.csv')
df['Course Result'][0] = df['Course Result'][0].replace("\'", "\"")
print(df['Course Result'][0])
df.to_csv('refactored_results.csv')