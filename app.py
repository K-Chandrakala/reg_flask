from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None
    error_messages = []

    if request.method == 'POST':
        # Extract form data
        fullname = request.form.get('fullname')
        email = request.form.get('mail')
        password = request.form.get('pass')
        confirm_pass = request.form.get('confirm_pass')
        username = request.form.get('username')
        phone = request.form.get('phone')
        gender = request.form.get('gender')

        # Form validation logic
        if not fullname or not email or not password or not confirm_pass or not username or not phone or not gender:
            error_messages.append('All fields are required.')
        
        if password != confirm_pass:
            error_messages.append('Passwords do not match.')

        # If no errors, display success message
        if not error_messages:
            success_message = "Registration Successful!"
        
    return render_template('index.html', success_message=success_message, error_messages=error_messages)

if __name__ == '__main__':
    app.run(debug=True)