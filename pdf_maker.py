import dash
import dash_html_components as html #if we want to include html components
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px


twitter_vis = dash.Dash()
#can add html components to twitter_vis

#Sample, but can use this for most common sentiment 
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()
