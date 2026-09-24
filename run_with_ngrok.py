from pyngrok import ngrok
from app import app
import threading
import time

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

time.sleep(2)

public_url = ngrok.connect(5000).public_url
print("=" * 60)
print("✅ ORIGINS IVF SYSTEM IS LIVE!")
print("=" * 60)
print(f"Login: {public_url}/login")
print(f"Lead Form: {public_url}/lead-form")
print(f"Admin Base Layout: {public_url}/admin/dashboard")
print("=" * 60)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nServer stopped.")
