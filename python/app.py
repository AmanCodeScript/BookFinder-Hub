from flask import Flask, render_template, request

app = Flask(__name__)

testDict = {}

@app.route('/', methods=['GET', 'POST'])
def testPage():
    if request.method == 'POST':
        testDict['BookName'] = request.form.get('BookName')
        testDict['Author'] = request.form.get('Author')
        testDict['Publisher'] = request.form.get('Publisher')
        print(testDict)
    return render_template(r'templates\testPage.html')


app.run(debug=True)