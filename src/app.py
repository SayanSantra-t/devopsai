from flask import Flask, jsonify, request
import random
import time
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static info as labels
common_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)

@app.route('/')
@common_counter
def hello_world():
    return 'Hello, World!'

@app.route('/anomaly')
@common_counter
def anomaly():
    # Simulate some metrics
    cpu_usage = random.uniform(10, 50)
    memory_usage = random.uniform(200, 1024)
    response_time = random.uniform(0.1, 0.5)

    # Introduce anomalies
    cpu_usage *= random.uniform(2, 4)
    memory_usage *= random.uniform(1.5, 3)
    response_time *= random.uniform(3, 5)

    # Expose metrics to Prometheus
    metrics.gauge('cpu_usage', 'CPU Usage').set(cpu_usage)
    metrics.gauge('memory_usage', 'Memory Usage').set(memory_usage)
    metrics.gauge('response_time', 'Response Time').set(response_time)


    return jsonify({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'response_time': response_time
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
