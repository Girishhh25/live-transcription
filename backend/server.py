from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive transcriptions
@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.json
    print("Received:", data)
    # Process or forward JSON to another system if needed
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)


