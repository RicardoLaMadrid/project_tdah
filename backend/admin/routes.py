from flask import Blueprint, render_template, session, redirect

admin_bp = Blueprint('admin', __name__, template_folder='../../frontend/templates/admin')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('logueado'):
        return redirect('/auth/login')
    return render_template('admin_dashboard.html')