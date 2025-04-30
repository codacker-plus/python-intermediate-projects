# flask_website.py
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect('users.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         username TEXT UNIQUE, 
                         password TEXT)''')

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            with sqlite3.connect('users.db') as conn:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                           (username, password))
                conn.commit()
                return "Registration successful!"
        except sqlite3.IntegrityError:
            return "Username already exists!"
    
    return render_template('register.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
