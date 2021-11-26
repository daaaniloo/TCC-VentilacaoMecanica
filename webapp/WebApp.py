from flask import Flask, redirect, url_for, render_template, request, flash
import pandas as pd 

#Create Flash app
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main_page():
    return redirect(url_for('home'))


@app.route("/home", methods=['GET', 'POST'])
def home():

    columns = ['Info_%s'% x for x in range(0,15) ]
    nrows = int(len(columns) / 5 ) 
    if len(columns) %5 != 0: 
        nrows +=1

    if request.method=="GET":
        return render_template('home.html', data=columns)

    elif request.method=="POST":
        for cols in columns:
            answer = request.form[cols] 
            print(answer)
        return render_template('home.html', data=columns)


if __name__ == "__main__":
    app.run(debug=True)
