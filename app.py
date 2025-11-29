from flask import Flask, render_template, send_file

app = Flask(__name__)

# --- Application Routes ---

# 1. Landing Page (Root Route - /)
# Renders the main landing page (page8.html)
# This is the destination for the "Return to Home" links in other files.
@app.route('/')
def landing_page():
    # Assuming 'page8.html' is in the 'templates' folder
    return render_template('index.html')

# 2. Refund Policy Route
@app.route('/refund')
def refund_policy():
    # Renders the separate Refund Policy page
    return render_template('refund_policy.html')

# 3. Privacy Policy Route
@app.route('/privacy')
def privacy_policy():
    # Renders the separate Privacy Policy page
    return render_template('privacy_policy.html')

# 4. Terms and Conditions Route
@app.route('/terms')
def terms_conditions():
    # Renders the separate Terms and Conditions page
    return render_template('terms_conditions.html')

# 5. File Download Route (Unchanged)
@app.route('/download')
def download_file():
    path = 'static/file.pdf'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    # Ensure all HTML files are placed inside a folder named 'templates'
    # in the same directory as app.py
    app.run(debug=True)
