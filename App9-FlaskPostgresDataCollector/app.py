from flask import Flask,render_template,request
from flask_sqlalchemy  import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:test@localhost/zodiacage_gacha'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120))
    gil_=db.Column(db.String)

    def __init__(self,email_,gil_):
        self.email_=email_
        self.gil_=gil_


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email_name']
        gil=request.form['gil']
        
        # if db.session.query(Data).filter(Data.email_==email).count()==0:
        data=Data(email,gil)
        db.session.add(data)
        db.session.commit()
        # average_height=db.session.query(func.avg(Data.height_)).scalar()
        # average_height=round(average_height)
        # count=db.session.query(Data.height_).count()


        # send_email(email,height,average_height,count)
        send_email(email,gil)
        return render_template('success.html')
    # return render_template('index.html',text='That email is already inputted in our database')
    return render_template('index.html',text='Welcome back noob')



if __name__=='__main__':
    app.debug=True
    app.run()
