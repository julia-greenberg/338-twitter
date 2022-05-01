from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div('Welcome to TwitterHawk', style={'color': 'blue', 'background-color': 'grey', 'height': 60, 'fontSize': 20, 'text-align': 'center'}),
    # html.P('Enter your twitter handle'),
    # debounce making sure enter is pressed
    html.Div([
        html.P('First Item Title'),
        html.P('First item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.Div([
        html.P('Second Item Title'),
        html.P('Second item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.Div([
        html.P('Third Item Title'),
        html.P('Third item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.Div([
        html.P('Fourth Item Title'),
        html.P('Fourth item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.Div([
        html.P('Fifth Item Title'),
        html.P('Fifth item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.Div([
        html.P('Sixth Item Title'),
        html.P('Sixth item goes here')
        ], style={'display': 'inline-block', 'text-align': 'justify', 'width': '33.1%', 'height': '300px', 'border': '1px solid red'}),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])

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