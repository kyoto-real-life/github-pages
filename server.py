from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'client.html')

@app.route('/api/create-room', methods=['POST'])
def create_room():
    # Wherebyへのリクエストをプロキシする
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmFwcGVhci5pbiIsImF1ZCI6Imh0dHBzOi8vYXBpLmFwcGVhci5pbi92MSIsImV4cCI6OTAwNzE5OTI1NDc0MDk5MSwiaWF0IjoxNzQ1NjE4Mjg3LCJvcmdhbml6YXRpb25JZCI6MzE0ODQ2LCJqdGkiOiJjZjhlNmFmMi1iYTViLTQ3NzgtODZjYS1mNTlmNzlmZDA4YWUifQ.v3OU-ynzq7-CoNIkMo_g0zpzRNJ5h3PCZIrsbV_lwe4"
    
    response = requests.post(
        'https://api.whereby.dev/v1/meetings',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'roomNamePrefix': 'customer-service',
            'endDate': request.json.get('endDate')
        }
    )
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=8000) 