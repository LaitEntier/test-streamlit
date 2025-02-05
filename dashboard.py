import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os


port = os.environ.get('PORT')

# Exemple de données
df = pd.DataFrame({
    "Fruit": ["Pommes", "Oranges", "Bananes", "Pommes", "Oranges", "Bananes"],
    "Quantité": [4, 1, 2, 2, 4, 5],
    "Ville": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['Ville'].unique()],
        value='SF'
    )
])

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_city):
    filtered_df = df[df['Ville'] == selected_city]
    fig = px.bar(filtered_df, x="Fruit", y="Quantité", color="Fruit", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
