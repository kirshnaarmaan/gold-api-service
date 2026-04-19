# gold-api-service
import os
from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/')
def get_gold():
    url = "https://www.google.com/search?q=gold+price+india+24k"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        # Gold rate nikalne ka formula
        match = re.search(r'(\d{2,3},\d{3})', response.text)
        price = match.group(1) if match else "Wait..."
        return jsonify({"status": "success", "gold_24k_10g": price, "unit": "INR"})
    except:
        return jsonify({"status": "error", "message": "Server Busy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
