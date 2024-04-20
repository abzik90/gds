from flask import Flask, jsonify, request, render_template
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/route')
def get_route_coordinates():
    # Replace this with logic to fetch dynamic coordinates from your database or another data source
    route_coordinates = [
        [51.128187, 71.430472],
        [51.126579, 71.471865],
        [51.115546, 71.532250],  # метро "Кунцевская"
    ]
    return jsonify(route_coordinates)


@app.route('/chat', methods=['POST'])
def chat():
    # Get the message from the request
    data = request.get_json()
    message = data.get('message')

    # Your logic to process the message and generate a response
    # This is just a placeholder, replace it with your actual logic
    response = gemini_response(message)

    return jsonify({'answer': response})


def gemini_response(message):
    # Your logic to generate a response based on the message
    # This is just a placeholder, replace it with your actual logic
    if message.lower() == 'hello':
        return "Hi there!"
    elif message.lower() == 'how are you?':
        return "I'm fine, thank you!"
    else:
        return "I'm sorry, I didn't understand that."


if __name__ == '__main__':
    app.run(debug=True)
