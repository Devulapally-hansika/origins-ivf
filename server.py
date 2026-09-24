from flask import Flask, render_template_string, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)

# The Login Page HTML is built directly into this file
LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Origins IVF - Login</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #E0F7FA 0%, #B2EBF2 100%); display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
        .login-container { background: white; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.1); width: 90%; max-width: 400px; padding: 40px; }
        .login-header { text-align: center; color: #08908C; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; color: #333; font-weight: 600; }
        .form-group input, .form-group select { width: 100%; padding: 12px; border: 2px solid #E0E0E0; border-radius: 10px; font-size: 15px; box-sizing: border-box; }
        .form-group input:focus, .form-group select:focus { outline: none; border-color: #0ABAB5; }
        .login-button { width: 100%; padding: 14px; background: #0ABAB5; color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: 700; cursor: pointer; }
        .login-button:hover { background: #08908C; }
        .error-message { background: #FEE; color: #C33; padding: 12px; border-radius: 8px; margin-bottom: 20px; display: none; text-align: center; font-size: 14px; }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header"><h1>Origins IVF</h1><p>Admin Control Panel</p></div>
        <div class="error-message" id="errorMessage">Invalid email or password.</div>
        <form id="loginForm">
            <div class="form-group"><label>Email</label><input type="text" id="email" value="admin@origins.com" required></div>
            <div class="form-group"><label>Password</label><input type="password" id="password" value="admin123" required></div>
            <div class="form-group"><label>Login as</label>
                <select id="role">
                    <option value="super_admin">Super Admin</option>
                    <option value="admin">Admin</option>
                    <option value="staff">Staff</option>
                </select>
            </div>
            <button type="submit" class="login-button">Log In</button>
        </form>
    </div>
    <script>
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const response = await fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: document.getElementById('email').value,
                    password: document.getElementById('password').value,
                    role: document.getElementById('role').value
                })
            });
            const result = await response.json();
            if (result.success) {
                alert('Login Successful! Redirecting to: ' + result.redirect_url);
            } else {
                const err = document.getElementById('errorMessage');
                err.innerText = result.message;
                err.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(LOGIN_HTML)

@app.route('/login', methods=['POST'])
def login_submit():
    data = request.get_json()
    if data.get('email') == 'admin@origins.com' and data.get('password') == 'admin123':
        return jsonify({'success': True, 'redirect_url': '/admin/dashboard'})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

if __name__ == '__main__':
    public_url = ngrok.connect(5000).public_url
    print("="*50)
    print(f"✅ COPY AND OPEN THIS EXACT LINK IN YOUR BROWSER:")
    print(f"   {public_url}")
    print("="*50)
    app.run(port=5000)
