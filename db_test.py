from flask import Flask,render_template,request,redirect,url_for
import re
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
#from MySQLdb import _mysql

app = Flask(__name__)
#db connections
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:shreyas4603@localhost/login_info"
db=SQLAlchemy(app)
CORS(app)

class data(db.Model):
    Email = db.Column(db.String(255),primary_key=True, nullable=False)
    Username = db.Column(db.String(255),primary_key=True, nullable=False)
    Password = db.Column(db.String(255),primary_key=True, nullable=False)
    Mobile = db.Column(db.BIGINT,primary_key=True, nullable=True)
###db connection end
d_info={}# loads the required data
dis_name=["default"] #global list which store username to print in main page

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

@app.route('/')
def login_main():
    return render_template('login_school.html',info="WELCOME")

@app.route('/login',methods=["POST"])
def login():
    try:
        global umail
        umail=request.form['user']
        psw=request.form['pass']
        record=data.query.filter_by(Email=umail).all()
        if record==[]:
          return render_template('login_school.html', info="No User Found")
        else:
          print(record)
          pass_check=record[0].Password
          if psw == pass_check:
            dis_name[0] = (data.query.filter_by(Email=umail).all())[0].Username
            return redirect(url_for("main_app"))
          else:
            print("wrong")
            return render_template('login_school.html', info="Incorrect password")
    except BaseException as error:
        raise error

@app.route('/registrations',methods=["POST"])
def register_startup():
    return render_template("register.html",info="")

@app.route('/registrations_write',methods=["POST"])
def register_write():
    ruser=request.form['r_user']
    rpass =request.form['r_pass']
    rpass_c = request.form['r_pass_c']
    rmail= request.form['r_email']
    rphone= request.form['r_phone']
    print("r pass ",rpass)
    print("r pass con ", rpass_c)
    if( ruser!="" and rpass!="" and rpass_c!="" and rpass==rpass_c and rmail!="" and rphone!="") :
        print("entered")
        if (re.search(regex, rmail)) :#email validation
             check = data.query.filter_by(Email=rmail).all()
             print(check)
             if check ==[]:
                # writing data to the database
                 write = data(Email=rmail, Username=ruser,Mobile=rphone,Password=rpass)
                 db.session.add(write)
                 db.session.commit()
                 dis_name[0]=(data.query.filter_by(Email=rmail).all())[0].Username
                 print(dis_name[0])
                 return redirect(url_for("main_app"))
             else:
                 return render_template("register.html", pass_match="User Exists")
        else:
            return render_template("register.html", pass_match="Invalid mail id")
    elif(rpass!=rpass_c):
        return render_template("register.html", pass_match="Password mismatch")
    elif str(rphone).strip().isnumeric() == False :
        write = data(Email=rmail, Username=ruser, Mobile=0, Password=rpass)
        db.session.add(write)
        db.session.commit()
        dis_name[0] = (data.query.filter_by(Email=rmail).all())[0].Username
        return redirect(url_for("main_app"))
    elif str(ruser).strip().isalnum()==False:
        return render_template("register.html", pass_match="Username Mandatory")
    elif str(rpass).strip().isalnum()==False:
        return render_template("register.html", pass_match="Password Mandatory")
    elif str(rmail).strip().isalnum()==False:
        return render_template("register.html", pass_match="Email Mandatory")
    else:
        return "No conditions satisfied"

@app.route('/forgot_render',methods=["POST"])
def forgot_render():
    return render_template("forgot.html")

@app.route('/main')
def main_app ():
    return render_template("main_app.html",name=dis_name[0])
    
app.run(debug=True)
