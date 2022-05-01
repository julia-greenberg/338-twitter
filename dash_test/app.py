from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash
import json

import helpers
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

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

# sentiment - score between 0 and 1
sentiment = 0.74
sentiment_strings = helpers.sentiment_score(sentiment)
sentiment_percent = helpers.sentiment_breakdown(sentiment)

user = json_data["user"]

app.layout = html.Div([
    html.P('Enter your twitter handle'),
    # debounce making sure enter is pressed
    dcc.Input(id='handle', type='text', debounce=True),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out'),
    html.Div([
        html.H2(lfStr),
        html.P(lfDateStr),
        html.P(lfLikeStr)
    ]),
    html.Div([
        html.Ol(
            [
                html.Li(str(int_list_data[0][0] + ": " + str(int_list_data[0][1]))),
                html.Li(str(int_list_data[1][0] + ": " + str(int_list_data[1][1]))),
                html.Li(str(int_list_data[2][0] + ": " + str(int_list_data[2][1]))),
            ]
        )
    ]
    ),
    html.Div([
        html.H2("On twitter, you tend to be " + sentiment_strings[0], style={'color': 'red'}),
        html.P(sentiment_strings[1]),
        html.B(sentiment_percent)
    ]),
    html.Div([
        dcc.Graph(id="graph", figure=helpers.generate_chart(sentiment, user))
    ])
])

@app.callback(
    Output('out', 'children'),
    Output("graph", "figure"), 
    Output('err', 'children'),
    Input('handle', 'value')
)
def show_handle(handle):
    if handle is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate

    # do something with twitter handle once its submitted?
    # pass to the back end

    return 'Your Twitter handle is @{}.'.format(handle), ''

if __name__ == '__main__':
    app.run_server(debug=True)

