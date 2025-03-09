import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

# Database connections
db_police = psycopg2.connect(
    host="turntable.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="sKaxECGNkgUrrmHnsXcPqjIFfzsWpvzE",
    port="40949"
)
cursor_police = db_police.cursor()

db_criminal = psycopg2.connect(
    host="yamabiko.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="ERwBkGTALKOrvPYzWKLFfZaahGsXqNgE",
    port="48760"
)
cursor_criminal = db_criminal.cursor()

db_court = psycopg2.connect(
    host="caboose.proxy.rlwy.net",
    database="railway",
    user="postgres",
    password="jSDQjKXQPNzpPhKVcMmfRjTzmxxLrIZs",
    port="25772"
)
cursor_court = db_court.cursor()

# Table schemas
police_info_columns = ["station_id", "station_name", "location", "officer_name"]
criminal_columns = ["criminalid", "name", "gender", "crimedesc", "status"]
court_columns = ["course_id", "criminal_id", "crime_type", "court_hearing_date", "verdict", "police_station_id"]

@app.route("/", methods=["GET", "POST"])
def index():
    police_info_columns_i = {}
    criminal_columns_i = {}
    court_columns_i = {}

    results = {"police_info": [], "criminal_info": [], "court_info": []}

    if request.method == "POST":
        user_inputs = {
            "station_id": request.form.get("station_id"),
            "location": request.form.get("location"),
            "officer_name": request.form.get("officer_name"),
            "station_name": request.form.get("station_name"),
            "course_id": request.form.get("course_id"),
            "crime_type": request.form.get("crime_type"),
            "criminalid": request.form.get("criminalid"),
            "name": request.form.get("name"),
            "status": request.form.get("status"),
            "verdict": request.form.get("verdict"),
            "gender": request.form.get("gender")
        }

        # Filter out None and empty values
        filtered_inputs = {k: v for k, v in user_inputs.items() if v and v.strip() != "None"}
        print("Filtered Inputs:", filtered_inputs)

        # Categorize inputs into respective tables
        for key, value in filtered_inputs.items():
            if key in police_info_columns:
                police_info_columns_i[key] = value
            elif key in criminal_columns:
                criminal_columns_i[key] = value
            elif key in court_columns:
                court_columns_i[key] = value

        print("Police Filters:", police_info_columns_i)
        print("Criminal Filters:", criminal_columns_i)
        print("Court Filters:", court_columns_i)

        # If no filters provided, fetch all data from all tables
        if not filtered_inputs:
            cursor_police.execute("SELECT * FROM police_info")
            results["police_info"] = cursor_police.fetchall()

            cursor_criminal.execute("SELECT * FROM criminal")
            results["criminal_info"] = cursor_criminal.fetchall()

            cursor_court.execute("SELECT * FROM court_info")
            results["court_info"] = cursor_court.fetchall()

        # Fetch filtered police data
        if police_info_columns_i:
            where_conditions = [f"{key} = %s" for key in police_info_columns_i]
            values = list(police_info_columns_i.values())
            query = f"SELECT * FROM police_info WHERE {' AND '.join(where_conditions)}"
            cursor_police.execute(query, tuple(values))
            results["police_info"] = cursor_police.fetchall()

        # Fetch filtered criminal data
        if criminal_columns_i:
            where_conditions = [f"{key} = %s" for key in criminal_columns_i]
            values = list(criminal_columns_i.values())
            query = f"SELECT * FROM criminal WHERE {' AND '.join(where_conditions)}"
            cursor_criminal.execute(query, tuple(values))
            results["criminal_info"] = cursor_criminal.fetchall()

        # Fetch filtered court data
        if court_columns_i:
            where_conditions = [f"{key} = %s" for key in court_columns_i]
            values = list(court_columns_i.values())
            query = f"SELECT * FROM court_info WHERE {' AND '.join(where_conditions)}"
            cursor_court.execute(query, tuple(values))
            results["court_info"] = cursor_court.fetchall()

        # 🔥 Link court cases if police data is found
        if results["police_info"]:
            station_ids = tuple(set(row[0] for row in results["police_info"]))  # Extract unique station_ids
            query = f"SELECT * FROM court_info WHERE police_station_id IN {station_ids}" if len(station_ids) > 1 else f"SELECT * FROM court_info WHERE police_station_id = %s"
            cursor_court.execute(query, station_ids if len(station_ids) > 1 else (station_ids[0],))
            results["court_info"] = cursor_court.fetchall()

        # 🔥 Link police and criminal data if court cases exist
        if results["court_info"]:
            station_ids = tuple(set(row[5] for row in results["court_info"]))  # Extract unique station_ids from court_info
            criminal_ids = tuple(set(row[1] for row in results["court_info"]))  # Extract unique criminal_ids from court_info

            if station_ids:
                query = f"SELECT * FROM police_info WHERE station_id IN {station_ids}" if len(station_ids) > 1 else f"SELECT * FROM police_info WHERE station_id = %s"
                cursor_police.execute(query, station_ids if len(station_ids) > 1 else (station_ids[0],))
                results["police_info"] = cursor_police.fetchall()

            if criminal_ids:
                query = f"SELECT * FROM criminal WHERE criminalid IN {criminal_ids}" if len(criminal_ids) > 1 else f"SELECT * FROM criminal WHERE criminalid = %s"
                cursor_criminal.execute(query, criminal_ids if len(criminal_ids) > 1 else (criminal_ids[0],))
                results["criminal_info"] = cursor_criminal.fetchall()

        print("Final Results:", results)
        return render_template("results.html", results=results)

    return render_template("query.html")

if __name__ == "__main__":
    app.run(debug=True)
