import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import json

# Load and prepare your data
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert Timestamp to datetime, Amount to float, and sort the DataFrame by Timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Amount'] = df['Amount'].astype(float)
df.sort_values('Timestamp', inplace=True)

# Add a sequential column to use as x-axis
df['Seq'] = range(1, len(df) + 1)

# Initialize the Dash app
app = dash.Dash(__name__)

# Prepare lists to hold the price comparison and $ Gain graphs
price_graphs = []
gain_graphs = []

# Get unique Binance Symbols (trading pairs)
trading_pairs = df['Binance Symbol'].unique()

# Define the sizes to filter by
sizes = [1]

for pair in trading_pairs:
    for size in sizes:
        # Filter the DataFrame for the current trading pair and size
        pair_size_df = df[(df['Binance Symbol'] == pair) & (df['Amount'] == size)].copy()

        # Reset index to use as a new x-axis (row number)
        pair_size_df.reset_index(drop=True, inplace=True)

        # Add a sequential column for this filtered DataFrame
        pair_size_df['Seq'] = range(1, len(pair_size_df) + 1)

        # Check if there are any rows left after filtering
        if not pair_size_df.empty:
            # Create a line chart for Aori Price using the new sequential number as x-axis
            trace1 = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['Aori Price'], mode='lines', name='Aori Price')

            # Create a line chart for Binance Price using the new sequential number as x-axis
            trace2 = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['Binance Price'], mode='lines', name='Binance Price')

            # Add the traces to a figure
            fig = go.Figure(data=[trace1, trace2])

            # Update layout for price comparison chart
            fig.update_layout(
                title=f'{pair} Size {size} Price Comparison',
                xaxis_title='Sequential Number',
                yaxis_title='Price',
                yaxis=dict(type='linear'),
                xaxis=dict(range=[1, len(pair_size_df)]),
            )

            # Append the figure to the price_graphs list
            price_graphs.append(dcc.Graph(figure=fig))

            # Create a line chart for $ Gain using the new sequential number as x-axis
            # Create a line chart for $ Gain using the new sequential number as x-axis
            gain_trace = go.Scatter(x=pair_size_df['Seq'], y=pair_size_df['$ Gain'], mode='lines', name='$ Gain')

            # Add the trace to a figure
            gain_fig = go.Figure(data=[gain_trace])

            # Update layout for $ Gain chart
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

            # Append the figure to the gain_graphs list
            gain_graphs.append(dcc.Graph(figure=gain_fig))

# Define the layout of the app with two columns of charts
app.layout = html.Div(children=[
    html.H1(children='Trading Pair and Size Price Comparison'),
    html.Div(children=[
        html.Div(children=price_graphs, style={'width': '50%', 'display': 'inline-block'}),
        html.Div(children=gain_graphs, style={'width': '50%', 'display': 'inline-block'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)