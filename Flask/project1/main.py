# Integrate html with flask 
# http verb get and POST

from flask import Flask, redirect, url_for, render_template, request  

# Here to enable render_template you have to follow folder structure.
# You should create 
#               template
#                       index.html 


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

### Results checker 
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0

    if request.method == "POST":
        sub1 = float(request.form["telugu"])
        sub2 = float(request.form["hindi"])
        sub3 = float(request.form["english"])
        sub4 = float(request.form["science"])
        sub5 = float(request.form['maths'])
        sub6 = float(request.form["social"])
        total_score = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 )

    subjects = [sub1, sub2, sub3, sub4, sub5, sub6]
    res = any(sub<50 for sub in subjects)

    data = [
            ["Telugu", sub1, "Pass" if sub1>=50 else "Fail"],
            ["Hindi", sub2, "Pass" if sub2>=50 else "Fail"],
            ["English", sub3, "Pass" if sub3>=50 else "Fail"],
            ["Science", sub4, "Pass" if sub4>=50 else "Fail"],
            ["Maths", sub5, "Pass" if sub5>=50 else "Fail"],
            ["Social", sub6, "Pass" if sub6>=50 else "Fail"]]

    res = ""
    if any(sub < 35 for sub in subjects):
        res = "Fail"
    else:
        res = "Pass"

    return render_template('result.html', result=data, total_score=total_score, final_res = res)

if __name__=="__main__":
    app.run(debug=True, port = 8080)