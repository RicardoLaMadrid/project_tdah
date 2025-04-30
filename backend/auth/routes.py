from flask import Blueprint, render_template, request, redirect, session
from backend.extensions import mysql

auth_bp = Blueprint('auth', __name__, template_folder='../../frontend/templates/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('txtemail')
        password = request.form.get('txtpassword')

        # Crear cursor y ejecutar consulta
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s AND password_hash = %s', (email, password))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['id'] = account['id']
            return redirect('/admin/dashboard')
        else:
            return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/auth/login')