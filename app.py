from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'origins_ivf_secret_key'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/lead-form')
def lead_form():
    return render_template('lead_form.html')

@app.route('/admin/dashboard')
def admin():
    return render_template('admin/base_layout.html')

# Route to preview the clean Staff Dashboard module
@app.route('/staff/dashboard')
def staff_dashboard():
    return render_template('staff/staff_dashboard_module.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
