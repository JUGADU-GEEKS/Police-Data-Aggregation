import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to PostgreSQL
dbSqlp = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="sKaxECGNkgUrrmHnsXcPqjIFfzsWpvzE",
    port="40949"
)
cursorSql = dbSqlp.cursor()

dbSqlc = psycopg2.connect(
    host="yamabiko.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="ERwBkGTALKOrvPYzWKLFfZaahGsXqNgE",
    port="48760"
)
cursorSqlc = dbSqlc.cursor()


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
        dbSqlp.commit()
        
        return render_template('police.html')
    return render_template('police.html')
@app.route('/criminal', methods=['GET', 'POST'])
def criminal():
    if request.method == 'POST':
        criminalId= request.form['criminalId']
        name = request.form['name']
        gender = request.form['gender']
        crimeDescription = request.form['crimeDescription']
        status = request.form['status']
        
        # Insert data into PostgreSQL
        cursorSqlc.execute(
            "INSERT INTO criminal (criminalid, name, gender, crimedesc, status) VALUES (%s, %s, %s, %s, %s)",
            (criminalId, name, gender, crimeDescription, status)
        )
        dbSqlc.commit()
        
        return render_template('criminal.html')
    return render_template('criminal.html')

@app.route('/')
def index():
    return render_template('police.html')

if __name__ == '__main__':
    app.run(debug=True)
