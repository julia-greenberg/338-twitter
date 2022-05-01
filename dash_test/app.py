from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div('Welcome to TwitterHawk', style={'color': 'blue', 'background-color': 'grey', 'height': 60, 'fontSize': 20, 'text-align': 'center'}),
    html.P('Enter your twitter handle'),
    # debounce making sure enter is pressed
    html.Div([
        html.P('@'),
        dcc.Input(id='handle', type='text', debounce=True)
        ], style={'display': 'inline-block', 'text-align': 'justify'}),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])

@app.callback(
    Output('out', 'children'),
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