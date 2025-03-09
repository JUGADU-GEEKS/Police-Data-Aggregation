Problem Statement
Law enforcement agencies face challenges in retrieving and analyzing criminal data due to the fragmentation of information across different databases. To address this, we propose a Unified Data Aggregation System that integrates three key databases: Criminal Records, Court Cases, and Police Records. Our system enables users to retrieve and analyze data efficiently using structured queries or natural language processing (NLP)-based searches. This will aid law enforcement officers, legal professionals, and policymakers in decision-making and investigation processes.
Tech Stack
•	Backend: Flask (Python)
•	Database: PostgreSQL (created on Railway)
•	Frontend: HTML , CSS , Jinja
•	Query Processing: SQL (aggregate and non-aggregate queries), Natural Language Processing (Gemini API)
The system is designed to provide:
•	Efficient Data Retrieval: Seamless access to criminal records, court cases, and police station details.
•	Integrated Query System: Users can retrieve information using predefined conditions or natural language queries.
•	Aggregated Insights: Use of aggregate and non-aggregate queries to provide meaningful statistics and trend analysis.
•	Flexibility: The system is flexible and can handle changes in database structure or add new data sources without requiring major modifications.
Intended Users
•	Law Enforcement Agencies: Police departments and investigative units
•	Judicial System: Lawyers, judges, and court officials
•	Government Authorities: Crime analysts, policymakers, and city planners
Data Sources and Schemas
The system integrates three PostgreSQL databases:
1.	Police Station Database :- station id (Primary Key), station_name, location, officer_name
2.	Criminal Records Database:- criminal id (Primary Key), name, crime_type, status, gender
3.	Court Cases Database:- court_id (Primary Key), criminal_id (Foreign Key → criminal id), crime_type, court_hearing_date, verdict, station_id (Foreign Key → station id)

Data Integration System
The system integrates these data sources using:
•	Materialized Views & Joins: Optimized retrieval of related records.
•	API-based Query Processing: Gemini API to handle queries and return structured responses.
Query Interface
•	Graphical Interface: Built using HTML and CSS 00for a user-friendly experience.
•	Text-based Queries: Users can retrieve records using structured SQL conditions.
•	Natural Language Search: NLP integration to process queries in plain English.
Query Federation & Execution
•	Aggregate Queries: 
o	Show total number of cases with location Mumbai.
o	Count the number of criminals in each city.
•	Non-Aggregate Queries: 
o	List all pending cases for a given criminal.
o	Fetch details of criminals last seen in a particular location.
o	Retrieve police station details for a specific case.
Scalability & Future Enhancements
•	Support for Additional Data Sources: System can dynamically integrate more databases such as missing persons or forensic reports.
•	Machine Learning Integration: Predict crime patterns based on historical data.
•	Real-Time Alerts: Notify law enforcement of status changes in cases or last-seen locations.

