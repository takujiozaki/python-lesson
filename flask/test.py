from flask import Flask

# Flask Object
app = Flask(__name__)


# url '/'

@app.route("/")
def root():
    return 'Hello Flask!'


# server build
if __name__ == "__main__":
    app.run(debug=True, port=8888)
