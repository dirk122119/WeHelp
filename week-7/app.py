from urllib import response
from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector
from flask import jsonify

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def create_connection_pool():
    db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'dddddddd',
        'database' : 'website',
        'port' : 3306,
    }
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "website",pool_size=5, **db_config)

    return cnxpool

try:
    cnx=create_connection_pool()
except:
    print("無法建立connect pool")


@app.route("/")
def hompage():
    if 'username' in session:
        return redirect(url_for('member'))
    return render_template("homPage.html")

@app.route("/signin",methods=['POST'])
def signin():
    if(request.form['username'] and request.form['password']):
        connect_objt=cnx.get_connection()
        cursor = connect_objt.cursor()
        sql="SELECT name,id from member WHERE username=%s and password=%s"
        val=(request.form['username'],request.form['password'])
        cursor.execute(sql,val)
        result=cursor.fetchall()
        if len(result)==1:
            session['username'] = request.form['username']
            session['name'] = result[0][0]
            session['id'] = result[0][1]
            cursor.close()
            connect_objt.close()
            return redirect(url_for('member'))
        else:
            cursor.close()
            connect_objt.close()
            return redirect(url_for('error',message="帳號或密碼錯誤"))
    elif(not request.form['username'] or not request.form['password']):
        return redirect(url_for('error',message="請輸入帳號、密碼"))
    else:
        return redirect(url_for('error',message="帳號或密碼錯誤"))

@app.route("/signup",methods=['POST'])
def signup():
    if(request.form['username'] and request.form['password']):
        connect_objt=cnx.get_connection()
        cursor = connect_objt.cursor()
        sql="SELECT * from member WHERE username=%s"
        val=(request.form['username'],)##(str,)這樣才是tuple？
        cursor.execute(sql,val)
        result=cursor.fetchall()
        if len(result):
            cursor.close()
            connect_objt.close()
            return redirect(url_for('error',message="帳號已經被註冊"))
        else:
            sql = "INSERT INTO member (name,username,password) VALUES (%s, %s,%s)"
            val = (request.form['name'], request.form['username'],request.form['password'])
            cursor.execute(sql, val)
            connect_objt.commit()
            cursor.close()
            connect_objt.close()
            return redirect(url_for('member'))
    elif(not request.form['username'] or not request.form['password']):
        return redirect(url_for('error',message="請輸入帳號、密碼"))
    else:
        return redirect(url_for('error',message="帳號或密碼錯誤"))
        
@app.route("/member")
def member():
    if 'username' in session:
        name = session['name']
        
        return render_template("memberPage.html",name=name)
    else:
        return redirect(url_for('hompage'))

@app.route("/error",methods=['GET'])
def error():
    message = request.args.get('message')
    return render_template("errorPage.html",message=message)

@app.route("/signout")
def signout():
    session.pop('id', None)
    session.pop('name', None)
    session.pop('username', None)

    return redirect(url_for('hompage'))

@app.route("/message",methods=['POST'])
def message():
    connect_objt=cnx.get_connection()
    cursor = connect_objt.cursor()
    sql="insert into message(member_id,content) values(%s,%s)"
    val=(session['id'],request.get_json())
    cursor.execute(sql, val)
    connect_objt.commit()
    cursor.close()
    connect_objt.close()
    return redirect(url_for('member'))

#============================API Function============================#
@app.route("/api/member",methods=["GET","PATCH"])
def memberApi():
    
    if request.method=="GET":
        if 'username' in session:
            userName = request.args.get('username')
            connect_objt=cnx.get_connection()
            cursor = connect_objt.cursor()
            sql="SELECT id,name,username from member WHERE username=%s"
            val=(userName,)
            cursor.execute(sql,val)
            result=cursor.fetchone()
            returnStr={"data":{"id":result[0],"name":result[1],"username":result[2]}}
            cursor.close()
            connect_objt.close()
            return jsonify(returnStr)
        else:
            return jsonify({"data":None})
    elif request.method=="PATCH":
        if 'username' in session:
            print("now patch")
            print(request.get_json())
            connect_objt=cnx.get_connection()
            cursor = connect_objt.cursor()
            sql="UPDATE member SET name=%s WHERE id=%s"
            val=(request.get_json(),session["id"])
            cursor.execute(sql,val)
            connect_objt.commit()
            session['name']=request.get_json()
            cursor.close()
            connect_objt.close()
            return jsonify({"OK":True})
        else:
            return jsonify({"error":True})
    

if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0", port=3000)