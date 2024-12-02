from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a simple Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the incoming POST request
    data = request.json

    # Process the data (for this example, just return it back in the response)
    print("Received Webhook Data:", data)

    # Respond with a success message
    return jsonify({
        "status": "received",
        "message": "Hello_World",
        "received_data": data
    }), 200

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
