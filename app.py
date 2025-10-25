from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Optional: store data, but SQLite won't persist on Vercel
    print(name, email, phone, message)

    flash("✅ Booking submitted successfully!")
    return redirect('/')

# ✅ expose app (no app.run() here)
app = app
