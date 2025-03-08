import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to PostgreSQL
dbSql = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="sKaxECGNkgUrrmHnsXcPqjIFfzsWpvzE",
    port="40949"
)
cursorSql = dbSql.cursor()

@app.route('/police', methods=['GET', 'POST'])
def police():
    if request.method == 'POST':
        stationId = request.form['stationId']
        stationName = request.form['stationName']
        location = request.form['location']
        officerName = request.form['officer']
        
        # Insert data into PostgreSQL
        cursorSql.execute(
            "INSERT INTO police_info (station_id, station_name, location, officer_name) VALUES (%s, %s, %s, %s)",
            (stationId, stationName, location, officerName)
        )
        dbSql.commit()
        
        return render_template('police.html')
    return render_template('police.html')

@app.route('/')
def index():
    return render_template('police.html')

if __name__ == '__main__':
    app.run(debug=True)
