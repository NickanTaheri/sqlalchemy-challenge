from flask import Flask, jsonify


app = Flask(__name__)

@app.home("/")
def home():
    return (
        f"Welcome to the Hawaii Weather Station API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def jsonified():
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def jsonified():
    return jsonify(precipitation)

@app.route("/api/v1.0/tobs")
def jsonified():
    return jsonify(precipitation)

if __name__ == "__main__":
    app.run(debug=True)
