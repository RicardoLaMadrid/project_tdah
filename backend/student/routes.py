from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__, template_folder='../../frontend/templates/student')

@student_bp.route('/dashboard')
def dashboard():
    return render_template('student_dashboard.html')