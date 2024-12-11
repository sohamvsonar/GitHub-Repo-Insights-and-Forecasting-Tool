import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths for graph directories
LSTM_GRAPH_DIR = os.path.join(BASE_DIR, '../Forecasting/Tensorflow_LSTM/graphs/')
PROPHET_GRAPH_DIR = os.path.join(BASE_DIR, '../Forecasting/Prophet/graphs/')
STATS_GRAPH_DIR = os.path.join(BASE_DIR, '../Forecasting/StatsModel/graphs/')

# API to fetch graph names for LSTM
@app.route('/api/graphs/lstm', methods=['GET'])
def get_lstm_graphs():
    lstm_graphs = os.listdir(LSTM_GRAPH_DIR)
    return jsonify(lstm_graphs)

# API to fetch graph names for Prophet
@app.route('/api/graphs/prophet', methods=['GET'])
def get_prophet_graphs():
    prophet_graphs = os.listdir(PROPHET_GRAPH_DIR)
    return jsonify(prophet_graphs)

# API to fetch graph names for StatsModel
@app.route('/api/graphs/stats', methods=['GET'])
def get_stats_graphs():
    stats_graphs = os.listdir(STATS_GRAPH_DIR)
    return jsonify(stats_graphs)

# Serve the actual graph images
@app.route('/static/<model>/<graph_name>')
def serve_graph(model, graph_name):
    # Dynamically choose directory based on the model
    if model == "lstm":
        graph_dir = LSTM_GRAPH_DIR
    elif model == "prophet":
        graph_dir = PROPHET_GRAPH_DIR
    else:
        graph_dir = STATS_GRAPH_DIR
    return send_from_directory(graph_dir, graph_name)

if __name__ == '__main__':
    app.run(debug=True)
