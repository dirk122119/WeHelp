from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hompage():
    if 'username' in session:
        return redirect(url_for('member'))
    return render_template("homPage.html")

@app.route("/signin",methods=['POST'])
def signin():
    if request.method == "POST":
        if(request.form['username']=="test" and request.form['password']=="test"):
            session['username'] = request.form['username']
            return redirect(url_for('member'))
        elif(not request.form['username'] or not request.form['password']):
            return redirect(url_for('error',message="請輸入帳號、密碼"))
        else:
            return redirect(url_for('error',message="帳號或密碼錯誤"))

        
@app.route("/member")
def member():
    if 'username' in session:
        return render_template("memberPage.html")
    else:
        return redirect(url_for('hompage'))

@app.route("/error",methods=['GET'])
def error():
    message = request.args.get('message')
    return render_template("errorPage.html",message=message)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('hompage'))

@app.route("/square/<number>",methods=['GET','POST'])
def square(number):
    answer=str(int(number)*int(number))
    return render_template("squarePage.html",output=answer)

if __name__ == '__main__':
    app.debug=False
    app.run(host="0.0.0.0", port=3000)