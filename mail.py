from flask import Flask
from flask_mail import Mail,Message
app=Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 34
app.config['MAIL_USERNAME']='xyz@gmail.com'
app.config['MAIL_PASSWORD']='xyz@gmail.com'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USER_SSL']=True
mail =Mail(app)

@app.route('/')
def index():
    msg=Message('hello',sender='xyz@gmail.com',recipients=['abc@gmail.com'])
    msg.body="Hello flask! This message is sent from flask-mail"
    mail.send(msg)
    return "Message Sent"

if __name__=="__main__":
    app.run(debug=True)