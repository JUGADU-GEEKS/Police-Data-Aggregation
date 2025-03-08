from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

dbSql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kunal1234",
    database="Police"
)
cursorSql = dbSql.cursor()

@app.route('/police', methods=['GET','POST'])
def police():
    if request.method=='POST':
        stationId = request.form['stationId']
        stationName = request.form['stationName']
        location = request.form['location'],
        officerName = request.form['officer']
        cursorSql.execute("INSERT INTO police_info(station_id, station_name, location, officer_name) VALUES (%s, %s, %s, %s)",(stationId, stationName, location, officerName))
        dbSql.commit()
        return render_template('police.html')
    return render_template('police.html')

@app.route('/')
def index():
    return render_template('police.html')

if __name__ == '__main__':
    app.run(debug=True)