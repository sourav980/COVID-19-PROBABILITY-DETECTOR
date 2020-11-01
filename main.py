from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

file=open('project','rb')
clf=pickle.load(file)
file.close()

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        Mydict= request.form
        Age=int(Mydict['age'])
        fever=int(Mydict['fever'])
        bodypain=int(Mydict['bodypain'])
        difficulty_in_breath=int(Mydict['difficulty_in_breath'])
        chest_pain=int(Mydict['chest_pain'])
        Comorbidity=int(Mydict['Comorbidity'])
        cough=int(Mydict['cough'])
        running_nose=int(Mydict['running_nose'])
        tiredness=int(Mydict['tiredness'])
        blurring_of_speech=int(Mydict['blurring_of_speech'])
        loss_of_taste_or_smell=int(Mydict['loss_of_taste_or_smell'])
        #test code
        inputfeature=[Age,fever,bodypain,difficulty_in_breath,chest_pain,Comorbidity,cough,running_nose,tiredness,blurring_of_speech,loss_of_taste_or_smell]
        infprob=clf.predict_proba([inputfeature])[0][1]
        print(infprob)
        return render_template('show.html',inf=round(infprob*100))
    return render_template('index.html')
    #return 'Hello, World!' +str(infprob)

if __name__ == '__main__':
    app.run(debug=True)
        