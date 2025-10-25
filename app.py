from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secretkey"

# Create database with phone column
def init_db():
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    message TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Basic validation
    if not name or not phone:
        flash("⚠️ Please enter name and phone number!")
        return redirect(url_for('home'))

    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, email, phone, message) VALUES (?, ?, ?, ?)",
              (name, email, phone, message))
    conn.commit()
    conn.close()

    flash("✅ Booking submitted successfully!")
    return redirect(url_for('home'))

# Do not run app manually in Vercel; just expose it
app = app

