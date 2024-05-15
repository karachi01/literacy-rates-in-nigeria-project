import pandas as pd
import plotly.express as px

# going to read the nothes.csv file
lwd = pd.read_csv("notes.csv")

# this is for plotting
categories = ['Total', 'Male', 'Female']
values = [lwd['literacy_rate_total'][0], lwd['literacy_rate_male'][0], lwd['literacy_rate_female'][0]]
data = pd.DataFrame({'Category': categories, 'Literacy Rate': values})

# making the bar interactive
fig = px.bar(data, x='Category', y='Literacy Rate', color='Category', title='Literacy Rates in Nigeria (2023)')

fig.show()
