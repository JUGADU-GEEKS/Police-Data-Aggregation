'''import sqlite3

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect("court_cases.db")
cursor = conn.cursor()

# Create "court_cases" table
cursor.execute('''
'''CREATE TABLE IF NOT EXISTS court_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    criminal_name TEXT NOT NULL,
    case_type TEXT NOT NULL,
    court_hearing_date TEXT NOT NULL,
    verdict TEXT CHECK(verdict IN ('Pending', 'Guilty', 'Not Guilty')) NOT NULL
);'''
''')

# Commit & close
conn.commit()
conn.close()

print("Database and table created successfully!")'''
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite
def get_db_connection():
    conn = sqlite3.connect("/databases/court_cases.db")
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

# Route to handle form submission
@app.route('/submit_case', methods=['POST'])
def submit_case():
    criminal_id = request.form['criminal_id']
    crime_type = request.form['crime_type']
    court_hearing_date = request.form['court_hearing_date']
    verdict = request.form['verdict']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO court_cases (criminal_name, case_type, court_hearing_date, verdict) 
            VALUES (?, ?, ?, ?)
        ''', (criminal_id, crime_type, court_hearing_date, verdict))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Court case added successfully!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
