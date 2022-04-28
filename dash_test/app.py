from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

loyalFollowerDate = "01/01/2000"
loyalFollowerHandle = "@TWITTER"
loyalFollowerLikes = 0

lfStr = str("Your most loyal follower: " + loyalFollowerHandle)
lfDateStr = str(loyalFollowerHandle + " has followed you since " + loyalFollowerDate + ".")
lfLikeStr = str(loyalFollowerHandle + " has liked " + str(loyalFollowerLikes) + " of your tweets.")

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
    ])
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
