import pandas as pd
import pdfkit as pdf

df = pd.read_csv('results/results.csv')
df.drop('Course Result',axis=1,inplace=True)
df.to_html('results.html')
pdf.from_file('results.html','results.pdf')