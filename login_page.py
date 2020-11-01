from flask import Flask,render_template,request,redirect,url_for
import re
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string
import pickle
from datetime import datetime
import pymysql
from flask_cors import CORS

from sqlalchemy.orm import exc

#variables block {


symptoms=["Body Pain","Difficulity in breathing","Chest pain","Comorbidity","Cough","Running Nose","Tiredness","Blurring of Speech","Loss of taste or smell",'pneumonia',"Sore Throat",'Diarrhea',"Conjunctivitis","Headache","Rash"]
date=datetime.now().date()#gets current date
time=datetime.now().time()#gets current time
d_info={}# loads the required data
dis_name=["default"] #global list which store username to print in main page
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
OTP_lis=[]#stores the generated OTP
mail_lst=[] #to store tha mail id recieved from user at forget password page
ml_feed=[] #to feed to the ML model[-1,0,1....] + age n fever
mail_feed=["default"] # email id to feed to symptoms db
db_feed_sympt=[]
vals=[] #to feed to the ML model[-1,0,1....] - age n fever
report_dict={}#stores the date and the list of symtopms "date"= [list of symptoms ]


#}

#Custom functions block , to make code clean and easy to understand{

def getvalues(lst): #gets the values for each problem
    print('entered get data getvalues')
    for i in lst:
        vals.append(request.form.get(i))
    print('exited data')    
    return vals


def getsympts():
    print('entered get data getsympts')
    # print("Values sent to report",vals)
    
    
    
    for i in range(len(vals)):
    
        if vals[i]!="-1":
            db_feed_sympt.append(symptoms[i])
    # print(db_feed_sympt)
def db_feed():
    print('entered get data db_feed')
    feed=symptoms_data(Symptoms=("#".join(db_feed_sympt)),Date=date,Time=time,mail_id=data(Email=mail_feed[0]))
    db.session.add(feed)
    db.session.commit()
    print("Uploaded to symptoms table")


def get_data(lst):
    print('entered get data')
    for i in lst:
        report_dict[i.Date]=(i.Symptoms).split("#")
    
    return (report_dict)

def probabilty(lst):

    #ML Code {
    # Add extra symptoms
    # }
    return ()#return the value

#}
app = Flask(__name__)
# CORS(app)

#db connections


app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:admin@localhost/main_db"

db=SQLAlchemy(app)

class data(db.Model) : # table for login data
    Email = db.Column(db.String(255),primary_key=True)
    Username = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Mobile = db.Column(db.BIGINT)
    problems=db.relationship("symptoms_data",backref="mail_id")


class symptoms_data(db.Model) : # table for login data

    Symptoms = db.Column(db.String(255))
    Date = db.Column(db.String(255),primary_key=True)
    Time = db.Column(db.String(255),primary_key=True)
    Email=db.Column(db.String(255),db.ForeignKey('data.Email'))



###db connection end




@app.route('/')
def login_main():
    return render_template('login_school.html',info="WELCOME")
@app.route('/login',methods=["POST","GET"])
def login():
    global umail
    umail=request.form['user']
    mail_feed[0]=umail
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

@app.route('/registrations',methods=["POST","GET"])
def register_startup():
    return render_template("register.html",info="")

@app.route('/registrations_write',methods=["POST","GET"])
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

@app.route('/forgot_render',methods=["POST","GET"])
def forgot_render():
    return render_template("forgot.html")


@app.route('/send_code',methods=["POST","GET"])
def send_code():
    for_mail=request.form['f_mail']
    mail_lst.append(for_mail)
    if (re.search(regex, for_mail)) and(data.query.filter_by(Email=for_mail).all()!=[]) :
        OTP = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        OTP_lis.append(OTP)
        print(OTP_lis[0])
        message = MIMEMultipart()
        message["from"] = 'Shreyas'
        message['to'] = for_mail.strip()
        message['subject'] = ' mail for sending an OTP for conformation for forgot password'
        message.attach(MIMEText(f"An OTP has been sent for verification:{OTP}"))
        with smtplib.SMTP(host='smtp.gmail.com', port=25) as smtp :
            smtp.ehlo()
            smtp.starttls()
            smtp.login("#enter your mail here ",'#enter your email password here' )  # enter your mail id and password removed due to securrity reasons)
            smtp.send_message(message)
            print('mail succesfully sent...')
            return render_template("code.html")
    elif  (re.search(regex, for_mail))==None:
        return render_template("forgot.html", info="Invalid Email")
    else:
        if (data.query.filter_by(Email=mail_lst[0]).all() == []):
            print((re.search(regex, for_mail)))
            return render_template("forgot.html", info="No User found")



@app.route('/check_code',methods=["POST","GET"])
def code_check():
    print(OTP_lis[0])
    if(request.form["code"]!=OTP_lis[0]):
        return render_template("code.html", info="Invalid code")
    else:
        return render_template("new_password.html")
        print("update entered")


@app.route('/update_db',methods=["POST","GET"])
def update_db():
    print(mail_lst[0])
    user_mail=mail_lst[0]
    new_pass=request.form["new_pass"]
    if(request.form["new_pass"]==request.form["conf_pass"]):
        rec=(data.query.filter_by(Email=user_mail.strip()).first())
        print(rec)
        rec.Password=new_pass
        db.session.commit()
        print("Updated",flush=True)
        return render_template('login_school.html',info="WELCOME")
    else:
        return render_template("new_password.html",info="Passwords Mismatch")

#opening the ml file
file=open('project','rb')
clf=pickle.load(file)
file.close()


@app.route('/main',methods=["POST","GET"])
def main_app():
    # try:
        ml_feed = []
        if request.method == 'POST':
            valueof = request.form
            age = int(valueof["age"])
            fever = float(valueof["fever"])
            ml_feed.append(age)
            ml_feed.append(fever)
            varis = ["bpain", "breathing", "chest", "como", "cough", "rnose", "tired", "blurrsp", "tastesm",'pneumonia', "sore","dia", "conj","head","rash"]
            values = getvalues(varis)
            print(f"""values: {values} """)
            for i in values:
                    ml_feed.append(int(i))
            print(f"""ml_feed {ml_feed} """)
           
            getsympts()
            db_feed()
            
            inf1=clf.predict([ml_feed])[0]
            print(ml_feed)
            infprob=clf.predict_proba([ml_feed])[0][inf1]
            
            return render_template('prob.html',prob=round(infprob*100,2))
        # operation to be done{
        # take ml_feed list
        # feed it to the model
        # return the prob
        #
        # }
        #return ("Entered") #render prob page

        return render_template("main_app(scratch).html")
    # except BaseException as error:
    #     return str(error)

@app.route("/producereport",methods=["GET","POST"])
def produce_report():
    report_data=(data.query.filter_by(Email=mail_feed[0])).all()
    json_feed_list=get_data((report_data[0].problems))
    print(json_feed_list)
    dates=list(json_feed_list.keys())
    symptoms=list(json_feed_list.values())
    for i in range(len(dates)):
        symptoms[i]=[dates[i]]+symptoms[i]
    print(symptoms)
    # print((report_data[0].person))
    # print("Username",dis_name[0])
    # print("Symptoms he has ",db_feed_sympt)
    # print("Date",date)
    # print("Time",time)
    return render_template("report.html",sympts=symptoms)

app.run(debug=True)