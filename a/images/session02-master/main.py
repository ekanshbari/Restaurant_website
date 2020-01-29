from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import sqlite3 as sql

def insertUser(username,password,email,contact):
    con = sql.connect("test.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,email,contact) VALUES (?,?,?,?)", (username,password,email,contact))
    con.commit()
    con.close()

def validUser(email,password):
    con = sql.connect("test.db")
    cur = con.cursor()
    a = cur.execute("select * from users where email = ? &  password = ?", (email,password))
    con.commit()
    
    if a.fetchall():
    	con.close()
    	return True
    else:
    	con.close()
    	return False


# Homepage
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		rd = validUser(request.form['email'], request.form['password'])
		if rd is True:
			return "Successful login"
		else:
			return "UnSucessful login"
	else:
		return render_template('index2.html')


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
    	username =  request.form['username']
    	email =  request.form['email']
    	password =  request.form['password']
    	contact =  request.form['contact']
    	# Code for db
    	insertUser(username,password,email,contact)

    	return redirect(url_for('login'))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=4000,debug=True)