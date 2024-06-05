from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def testPage():
    return render_template(r'testPage.html')


app.run(debug=True)