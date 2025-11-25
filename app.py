from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from tripAI_core import generate_trip_plan, secure_store_data

app = Flask(__name__)
CORS(app)

os.makedirs("user_data", exist_ok=True)

@app.route("/api/plan_trip", methods=["POST"])
def plan_trip():
    try:
        data = request.get_json()
        plan = generate_trip_plan(data)
        secure_store_data(plan)
        return jsonify(plan)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return "TripAI Planner API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
