# Trading Pair and Size Price Comparison Dashboard

This dashboard is designed to compare trading pair prices and visualize the $ Gain for each pair using the Dash framework in Python. It dynamically generates charts for each trading pair found in the provided JSON data, displaying both the price comparison and the $ Gain in a side-by-side format.

## Getting Started

To get this dashboard up and running on your local machine, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. This project was developed with Python 3.8, but it should be compatible with most Python 3.x versions.

### Installation

1. **Clone the repository**

   First, clone this repository to your local machine using Git.
   git clone https://github.com/elstongun/aori-data-ui.git


2. **Set up a virtual environment** (Optional but recommended)

   Navigate to the cloned project directory and create a virtual environment.
   cd path/to/cloned/repository
   python -m venv venv


   Activate the virtual environment.

   - On Windows:
   .\venv\Scripts\activate
   - On Unix or MacOS:
   source venv/bin/activate

3. **Install the required packages**

   Ensure you have the required packages installed by running the following command:
   pip install dash pandas plotly



### Running the Dashboard

With the dependencies installed, you can now run the dashboard.

1. **Start the Dash server**

   Execute the `app.py` script to start the Dash server.
   python app.py

2. **Access the dashboard**

   Once the server is running, open a web browser and navigate to `http://127.0.0.1:8050/` to view the dashboard.

## Features

- **Dynamic Chart Generation:** Automatically generates charts for each trading pair found in the `data.json` file.
- **Price Comparison:** Visualizes the price comparison between Aori Price and Binance Price for each trading pair.
- **$ Gain Visualization:** Displays the $ Gain for each trading pair alongside the price comparison charts.
- **Responsive Layout:** Charts are organized in a two-column layout for easy comparison.

## Data Structure

The dashboard expects a JSON file named `data.json` with the following structure:

Ensure your JSON data file is correctly formatted and located in the same directory as `app.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.