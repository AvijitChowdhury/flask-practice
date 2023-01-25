###jinga2 template engine
'''
{% ... %} conditions for loops
{{ }} expressiong to print output
{# #} for comment
'''
from flask import Flask,render_template,redirect,url_for,request

app =Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if(score<33):
        res='Failed'
    else:
        res='Passed'

    return render_template('result1.html',result=res)

@app.route('/aftersub/<int:score>')
def aftersub(score):
    res=''
    if(score<33):
        res='Failed'
    else:
        res='Passed'
    dict={'result':res,'score':score}
    return render_template('result2.html',result=dict)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_marks=0
    if request.method=='POST':
        science=int(request.form['science'])
        maths=int(request.form['maths'])
        c=int(request.form['c'])
        datascience=int(request.form['datascience'])
        total_marks=science+maths+c+datascience
    # return redirect(url_for('success',score=total_marks))
    return redirect(url_for('aftersub',score=total_marks))

@app.route('/fail/<int:number>')
def fail(number):
    return 'you are failed by ' + str(number)

@app.route('/passing/<int:number>')
def passing(number):
    return '<h1>you are passed by </h1>' + str(number)

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if(marks<33):
        result="fail"
    else:
        result='passing'
    return redirect(url_for(result,number=marks))

if __name__=='___main__':
    app.run(debug=True)