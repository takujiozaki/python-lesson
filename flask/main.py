from flask import *

# Flask Object
app = Flask(__name__)


# route'/'
@app.route('/')
def root():
    # start html
    return render_template('index.html')


@app.route('/', methods=['post'])
def calc():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    answer = num1 * num2
    return render_template('result.html', answer=answer)


# server build
if __name__ == "__main__":
    app.run(debug=True, port=8888)
