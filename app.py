from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/bot', methods=['GET', 'POST'])
def create():
    payload = request.json
    print(payload)
    description = payload['child']
    results = {"bot" : "안녕"}
    json_data = json.dumps(results)
    response = Response(json_data, content_type='application/json')
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True) 