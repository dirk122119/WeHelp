from urllib import response
from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector
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
        if(request.form['username'] and request.form['password']):
            mydb = mysql.connector.connect(user='root', password='dddddddd',host='127.0.0.1',port=3306,database='website')
            if mydb.is_connected():
                cursor = mydb.cursor()
                sql="SELECT name from member WHERE username=%s and password=%s"
                val=(request.form['username'],request.form['password'])
                cursor.execute(sql,val)
                result=cursor.fetchall()
                if len(result)==1:
                    session['username'] = request.form['username']
                    return redirect(url_for('member',name=result[0]))
                else:
                    return redirect(url_for('error',message="帳號或密碼錯誤"))
        elif(not request.form['username'] or not request.form['password']):
            return redirect(url_for('error',message="請輸入帳號、密碼"))
        else:
            return redirect(url_for('error',message="帳號或密碼錯誤"))

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":

        if(request.form['username'] and request.form['password']):
            mydb = mysql.connector.connect(user='root', password='dddddddd',host='127.0.0.1',port=3306,database='website')
            if mydb.is_connected():
                cursor = mydb.cursor()
                sql="SELECT * from member WHERE username=%s"
                val=(request.form['username'],)##(str,)這樣才是tuple？
                cursor.execute(sql,val)
                result=cursor.fetchall()
                if len(result):
                    return redirect(url_for('error',message="帳號已被註冊"))
                else:
                    sql = "INSERT INTO member (name,username,password) VALUES (%s, %s,%s)"
                    val = (request.form['name'], request.form['username'],request.form['password'])
                    cursor.execute(sql, val)
                    mydb.commit()

            return redirect(url_for('member'))
        elif(not request.form['username'] or not request.form['password']):
            return redirect(url_for('error',message="請輸入帳號、密碼"))
        else:
            return redirect(url_for('error',message="帳號或密碼錯誤"))
        
@app.route("/member")
def member():
    if 'username' in session:
        name = request.args.get('name')
        return render_template("memberPage.html",name=name)
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
    app.debug=True
    app.run(host="0.0.0.0", port=3000)