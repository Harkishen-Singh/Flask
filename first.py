from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

def work():
    return 'This is working'

app.add_url_rule('/work',None, work)

def printing_name(name):
    l = len(name)
    rev = ''
    for i in range(l-1, -1, -1):
        rev += name[i]
    return 'Reverse name is '+rev+'\nOriginal name is '+name
app.add_url_rule('/naming/<name>',None, printing_name)

@app.route('/directing/<n>')
def directing2(n):
    if n== 'hello':
        redirect(url_for('hello_world'))
        print('Redirecting')
    elif n== 'working':
        redirect(url_for('work'))
        print('Redirecting')
    elif n== 'reverse':
        redirect(url_for('printing_name', name=n))
        print('Redirecting')



if __name__ == '__main__':
    app.run()

