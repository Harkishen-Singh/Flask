from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/sys')
def system():
    return '<html><body><h1>Working</h1></body></html>'

@app.route('/')
def startUp():
    return render_template('form.html')

@app.route('/login', methods=['POST', 'GET'])
def login_system():
    if request.method == 'POST':
        print(request.form['name'] + ' is the name received in POST method')

    elif request.method == 'GET':
        print(request.args.get('name') + ' is the name received in GET method')

    return render_template('welcome.html', name = request.form['name'], password = request.form['pass'])



if __name__ == '__main__':
    app.run('0.0.0.0',9999, True)