from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash
import json

import helpers
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__)

json_file = open("sample_comm.json")
json_data = json.load(json_file)

loyalFollowerDate = "01/01/2000"
loyalFollowerHandle = "@" + str(json_data["longest follower"])
loyalFollowerLikes = 0

interest_json = json_data["interests"]
top_interests = list(interest_json.keys())
int_list_data = []
for i in range(len(top_interests)):
    int_list_data.append((top_interests[i],interest_json[top_interests[i]] ))

lfStr = str("Your most loyal follower: " + loyalFollowerHandle)
lfDateStr = str(loyalFollowerHandle + " has followed you since " + loyalFollowerDate + ".")
lfLikeStr = str(loyalFollowerHandle + " has liked " + str(loyalFollowerLikes) + " of your tweets.")

topTweetStr = '<blockquote class="twitter-tweet"><a href="' + json_data["most popular tweet"] + '"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
leastTweetStr = '<blockquote class="twitter-tweet"><a href="' + json_data["least popular tweet"] + '"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

# MY STUFF ADDED HERE - sentiment: score between 0 and 1
sentiment = 0.74
sentiment_strings = helpers.sentiment_score(sentiment)
sentiment_percent = helpers.sentiment_breakdown(sentiment)

times = json_data["times"]

user = json_data["user"]
# -------

app.layout = html.Div([
    html.Header(f'Welcome to TwitterHawk, @{user}', style={'color': 'blue', 'background-color': 'grey', 'height': 60, 'fontSize': 20, 'text-align': 'center'}),
    
    html.Div(
        className="row",
        children = [
        html.Section([
            html.H2(lfStr),
            html.P(lfDateStr),
            html.P(lfLikeStr),
            ]),
        html.Section([
            html.H2("Your most popular topics:"),
            html.Ol(
                [
                    html.Li(str(int_list_data[0][0] + ": " + str(int_list_data[0][1]))),
                    html.Li(str(int_list_data[1][0] + ": " + str(int_list_data[1][1]))),
                    html.Li(str(int_list_data[2][0] + ": " + str(int_list_data[2][1])))
                ]
            )
        ]),
        html.Section([
            html.H2("Your most popular tweet:"),
            html.Iframe(srcDoc = topTweetStr, height = 300, width = 400)
        ]),
    ]),
    html.Div(
        className="row",
        children = [
        html.Section([
                html.H2("Your least popular tweet:"),
                html.Iframe(srcDoc = leastTweetStr, height = 300, width = 400)
        ]),
        html.Section([
            html.H2("On twitter, you tend to be " + sentiment_strings[0]),
            html.P(sentiment_strings[1]),
            dcc.Graph(id="graph", figure=helpers.generate_chart(sentiment, user))
            ]),
        html.Section([
            dcc.Graph(
                figure={
                    'data': [
                        {'x': list(times.keys()), 'y': list(times.values()), 'type': 'bar', 'name': 'Times'}
                    ],
                    'layout': {
                        'title': 'Times you Tweet',
                        'figure.layout.autosize': True,
                        # 'config.responsive': True,
                        'figure.layout.height': '300px'
                    }
                }
            )      
        ])]),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])

# @app.callback(
#     Output('out', 'children'),
#     Output("graph", "figure"), 
#     Output('err', 'children'),
#     Input('handle', 'value')
# )
# def show_handle(handle):
#     if handle is None:
#         # PreventUpdate prevents ALL outputs updating
#         raise dash.exceptions.PreventUpdate

#     # do something with twitter handle once its submitted?
#     # pass to the back end

#     return 'Your Twitter handle is @{}.'.format(handle), ''

if __name__ == '__main__':
    app.run_server(debug=True)


# app.layout = html.Div([
#     html.Div('Welcome to TwitterHawk', style={'color': 'blue', 'background-color': 'grey', 'height': 60, 'fontSize': 20, 'text-align': 'center'}),
#     # html.P('Enter your twitter handle'),
#     # debounce making sure enter is pressed
#     html.Div([
#         html.H2(lfStr),
#         html.P(lfDateStr),
#         html.P(lfLikeStr),
#         ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.Div([
#         html.H2("Your most popular topics:"),
#         html.Ol(
#             [
#                 html.Li(str(int_list_data[0][0] + ": " + str(int_list_data[0][1]))),
#                 html.Li(str(int_list_data[1][0] + ": " + str(int_list_data[1][1]))),
#                 html.Li(str(int_list_data[2][0] + ": " + str(int_list_data[2][1])))
#             ]
#         )
#     ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.Div([
#         html.H2("Your most popular tweet:"),
#         html.Iframe(srcDoc = topTweetStr, height = 300, width = 400)
#     ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.Div([
#         html.H2("Your least popular tweet:"),
#         html.Iframe(srcDoc = leastTweetStr, height = 300, width = 400)
#     ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.Div([
#         html.P('Fifth Item Title'),
#         html.P('Fifth item goes here')
#         ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.Div([
#         html.P('Sixth Item Title'),
#         html.P('Sixth item goes here')
#         ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
#     html.P(id='err', style={'color': 'red'}),
#     html.P(id='out')
# ])

# @app.callback(
#     Output('out', 'children'),
#     Output('err', 'children'),
#     Input('handle', 'value')
# )
# def show_handle(handle):
#     if handle is None:
#         # PreventUpdate prevents ALL outputs updating
#         raise dash.exceptions.PreventUpdate

#     # do something with twitter handle once its submitted?
#     # pass to the back end

#     return 'Your Twitter handle is @{}.'.format(handle), ''

if __name__ == '__main__':
    app.run_server(debug=True)