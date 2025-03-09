from flask import Flask, render_template, request
import psycopg2
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyDCK5KJEnq4Ri5PHX0bAS_7MG_Yb_6yFjk")  
# Connect to PostgreSQL Databases
dbSqlp = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="sKaxECGNkgUrrmHnsXcPqjIFfzsWpvzE",
    port="40949"
)
cursorSqlp = dbSqlp.cursor()

dbSqlc = psycopg2.connect(
    host="yamabiko.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="ERwBkGTALKOrvPYzWKLFfZaahGsXqNgE",
    port="48760"
)
cursorSqlc = dbSqlc.cursor()

dbSqlcc = psycopg2.connect(
    host="caboose.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="jSDQjKXQPNzpPhKVcMmfRjTzmxxLrIZs",
    port="25772"
)
cursorSqlcc = dbSqlcc.cursor()

# Route for Home Page
@app.route('/')
def index():
    return render_template('aggregated.html')

# Route to Process Query
@app.route('/query', methods=['POST'])
def process_query():
    user_query = request.form['userQuery']

    if not user_query:
        return render_template('aggregated.html', error="No query provided")

    # Gemini API Prompt
    prompt = f"""
You are an AI SQL assistant. Your task is to **ONLY** generate valid PostgreSQL SQL queries **without changing column names**.  
Strictly follow the **EXACT** schema below and do not rename any attributes.

### **Database Schema (DO NOT CHANGE COLUMN NAMES):**

1️⃣ **police_info**(This is the table 1 name)  
below are the attributes names of this table
- `station_id` (INT, PRIMARY KEY)  
- `station_name` (VARCHAR)  
- `location` (VARCHAR)  
- `officer_name` (VARCHAR)  

2️⃣ **court_info**(This is the table 2 name)   ((DO NOT CHANGE COLUMN NAMES):**)
below are the attributes names of this table

- `course_id` (INT, PRIMARY KEY) 
- `criminal_id` (INT, FOREIGN KEY → `criminal.criminalid`)  
- `crime_type` (VARCHAR)  
- `court_hearing_date` (DATE)  
- `verdict` (VARCHAR)  
- `police_station_id` (INT, FOREIGN KEY → `police_info.station_id`)  

3️⃣ **criminal** (This is the table 3 name)  (DO NOT CHANGE COLUMN NAMES):**
below are the attributes names of this table

- `criminalid` (INT, PRIMARY KEY)  
- `name` (VARCHAR)  
- `gender` (VARCHAR)  
- `crimedesc` (TEXT)  
- `status` (VARCHAR)  

### **User Query:**
'{user_query}'

### **STRICT RULES:**
✅ Use the **EXACT** column names as in the schema above.  
❌ Do NOT rename columns (e.g., `station_id` must stay `station_id`).  
❌ Do NOT add extra text like "Here is your SQL query:".  
✅ Only return the **SQL query** itself, nothing else.  
"""


    # Generate SQL Query using Gemini
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    sql_query_dash = response.text.strip()
    sql_query = sql_query_dash[7:len(sql_query_dash)-3]

    print("Generated SQL Query:", sql_query_dash)  # Debugging Output

    # Determine which database to query based on table name
    if "police_info" in sql_query:
        cursorSql = cursorSqlp
    elif "court_info" in sql_query:
        cursorSql = cursorSqlcc
    else:
        cursorSql = cursorSqlc

    # Execute SQL Query
    try:
        cursorSql.execute(sql_query)
        results = cursorSql.fetchall()
        column_names = [desc[0] for desc in cursorSql.description]

        return render_template('aggregated.html', sql_query=sql_query, results=results, column_names=column_names)

    except Exception as e:
        return render_template('aggregated.html', sql_query=sql_query, error=str(e))

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
