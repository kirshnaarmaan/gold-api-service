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
        match = re.search(r'(\d{2,3},\d{3})', response.text)
        price = match.group(1) if match else "Wait"
        return jsonify({"status": "success", "gold_price": price})
    except:
        return jsonify({"status": "error"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

