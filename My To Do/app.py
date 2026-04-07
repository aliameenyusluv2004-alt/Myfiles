from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow all origins (for development)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})


tasks = []

@app.route("/")
def home():
    return "Backend is Running"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks.append(data["task"])
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Invalid index"}), 400

if __name__ == "__main__":
    app.run(debug=True)
