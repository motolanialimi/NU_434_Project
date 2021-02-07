from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	return "Welcome to Motolani's Hello World"

@app.route('/name/<value>')
def name(value):
    val = {
        "value": value
    }
    return jsonify(val)

@app.route('/creator/')
def creator():
    val = {
        "value": "MotolaniA"
    }
    return jsonify(val)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
    
if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
	app.run(host="127.0.0.1", port=8080, debug=True)
