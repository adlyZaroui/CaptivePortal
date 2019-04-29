#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, redirect, render_template
from passlib.hash import sha256_crypt
import urllib
import os
from MySQLdb import escape_string
from dbconnect import connection

app = Flask(__name__)
app.secret_key = os.urandom(24)

def login_user(ip):
    os.system("sudo iptables -I internet 1 -t mangle -s " + ip + " -j RETURN")

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username  = request.form['lusername']
            password = request.form['lpassword']
            c, conn = connection()

            data = c.execute("SELECT * FROM users WHERE username = '%s' " % escape_string(username))
            data = c.fetchone()[2]

            if sha256_crypt.verify(password, data): # Si l'authentification est verifiée:

                login_user(request.remote_addr)

                if 'orig_url' in request.args and len(request.args['orig_url']) > 0:
                    return redirect(urllib.unquote(request.args['orig_url']))
                else:
                    return render_template('login_successful.html')

        return render_template('index.html')

    except Exception as e:
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:

        if request.method == "POST": # Si le formulaire est validé:
            username  = request.form['rusername']
            email = request.form['email']

            if request.form['rpassword'] == request.form['confirmRpassword']: # Si les mots de passe correspondent
                password = sha256_crypt.encrypt((str(request.form['rpassword'])))
            else: render_template('index.html')

            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)", [(escape_string(username))])

            if int(x) > 0:
                return render_template('index.html')

            else:
                c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                          (escape_string(username), escape_string(password), escape_string(email)))

                conn.commit()
                c.close()
                conn.close()

                login_user(request.remote_addr)

                if 'orig_url' in request.args and len(request.args['orig_url']) > 0:
                    return redirect(urllib.unquote(request.args['orig_url']))
                else:
                    return render_template('login_successful.html')

        return render_template('index.html')

    except Exception as e:
        return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("http://10.42.0.1/login?" + urllib.urlencode({'orig_url': request.url}))

if __name__ == "__main__":
    app.run('0.0.0.0', port=80)
