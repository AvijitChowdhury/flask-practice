#Building url dynamically
from flask import Flask,redirect,url_for

app= Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/success/<int:score>')
def success(score):
    return '<html><body><h1>NOthing than score: </h1></body></html>'+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the marks is: '+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if(marks <= 33):
        result= 'fail'
    else: 
        result= 'success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)
