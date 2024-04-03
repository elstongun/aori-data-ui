import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import json

with open('data.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Amount'] = df['Amount'].astype(float)
df.sort_values('Timestamp', inplace=True)

df['Seq'] = range(1, len(df) + 1)

app = dash.Dash(__name__)

price_graphs = []
gain_graphs = []

trading_pairs = df['Binance Symbol'].unique()

sizes = [1]

for pair in trading_pairs:
    for size in sizes:
        pair_size_df = df[(df['Binance Symbol'] == pair) & (df['Amount'] == size)].copy()

        pair_size_df.reset_index(drop=True, inplace=True)

        pair_size_df['Seq'] = range(1, len(pair_size_df) + 1)

        if not pair_size_df.empty:
            trace1 = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['Aori Price'], mode='lines', name='Aori Price')

            trace2 = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['Binance Price'], mode='lines', name='Binance Price')

            fig = go.Figure(data=[trace1, trace2])

            fig.update_layout(
                title=f'{pair} Size {size} Price Comparison',
                xaxis_title='Sequential Number',
                yaxis_title='Price',
                yaxis=dict(type='linear'),
                xaxis=dict(range=[1, len(pair_size_df)]),
            )

            price_graphs.append(dcc.Graph(figure=fig))

            gain_trace = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['$ Gain'], mode='lines', name='$ Gain')

            gain_fig = go.Figure(data=[gain_trace])

            gain_fig.update_layout(
                title=f'{pair} Size {size} $ Gain',
                xaxis_title='Sequential Number',
                yaxis_title='$ Gain',
                yaxis=dict(type='linear'),
                xaxis=dict(range=[1, len(pair_size_df)]),
                shapes=[
                    dict(
                        type='line',
                        xref='paper',
                        x0=0,
                        x1=1,
                        y0=0,
                        y1=0,
                        line=dict(
                            color='black',
                            width=2
                        )
                    )
                ]
            )

            gain_graphs.append(dcc.Graph(figure=gain_fig))

app.layout = html.Div(children=[
    html.H1(children='Trading Pair and Size Price Comparison'),
    html.Div(children=[
        html.Div(children=price_graphs, style={'width': '50%', 'display': 'inline-block'}),
        html.Div(children=gain_graphs, style={'width': '50%', 'display': 'inline-block'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)