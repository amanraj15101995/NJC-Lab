from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='amankumar'
app.config['MYSQL_DB']='project1'

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])

def index():
     if request.method=='POST':
        userDetails=request.form
        roll=userDetails['roll']
        name=userDetails['name']
        address=userDetails['address']
        
        cur=mysql.connection.cursor()
        cur.execute("insert into register1(roll,name,address) VALUES(%s,%s,%s)",(roll,name,address))
        mysql.connection.commit()
        cur.close()
        return redirect('/user')
     return render_template('index.html')
     
@app.route('/user')
def register1():
    cur=mysql.connection.cursor()
    resultValue=cur.execute("select * from register1")
    if resultValue > 0:
        userDetails=cur.fetchall()
        return render_template('user.html',userDetails = userDetails)

if __name__== '__main__':
    app.run(debug=True)
