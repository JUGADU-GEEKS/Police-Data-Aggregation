# Unified Data Aggregation System

## 📖 Problem Statement
Law enforcement agencies face challenges in retrieving and analyzing criminal data due to fragmented information across different databases. 

**Solution:**  
We propose a **Unified Data Aggregation System** that integrates three key databases:  
- **Criminal Records**  
- **Court Cases**  
- **Police Records**  

This system enables efficient data retrieval using structured queries or NLP-based searches, aiding law enforcement officers, legal professionals, and policymakers in decision-making and investigations.

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)  
- **Database:** PostgreSQL (hosted on Railway)  
- **Frontend:** HTML, CSS, Jinja  
- **Query Processing:** SQL (aggregate and non-aggregate queries), Natural Language Processing (Gemini API)

---

## 🚀 Key Features
- ✅ **Efficient Data Retrieval**: Seamless access to criminal records, court cases, and police station details.  
- ✅ **Integrated Query System**: Retrieve information using predefined conditions or natural language queries.  
- ✅ **Aggregated Insights**: Use aggregate and non-aggregate queries for statistics and trend analysis.  
- ✅ **Flexibility**: Adaptable to database changes or new data sources.

---

## 👤 Intended Users
- **Law Enforcement Agencies**: Police departments and investigative units  
- **Judicial System**: Lawyers, judges, and court officials  
- **Government Authorities**: Crime analysts, policymakers, and city planners  

---

## 🗂️ Data Sources and Schemas
1. **Police Station Database**  
   - `station_id` (Primary Key)  
   - `station_name`  
   - `location`  
   - `officer_name`  

2. **Criminal Records Database**  
   - `criminal_id` (Primary Key)  
   - `name`  
   - `crime_type`  
   - `status`  
   - `gender`  

3. **Court Cases Database**  
   - `court_id` (Primary Key)  
   - `criminal_id` (Foreign Key → Criminal Records)  
   - `crime_type`  
   - `court_hearing_date`  
   - `verdict`  
   - `station_id` (Foreign Key → Police Station)

---

## 🔗 Data Integration System
- **Materialized Views & Joins**: For optimized data retrieval.  
- **API-based Query Processing**: Using the Gemini API for NLP-based queries.

---

## 🔍 Query Interface
- 🎛️ **Graphical Interface**: Built using HTML and CSS for user-friendly interaction.  
- 📝 **Text-based Queries**: Structured SQL conditions.  
- 🌐 **Natural Language Search**: NLP for processing queries in plain English.

---

## 🗃️ Query Federation & Execution
- **Aggregate Queries**  
    - Total number of cases with location *Mumbai*.  
    - Count the number of criminals in each city.  

- **Non-Aggregate Queries**  
    - List all pending cases for a given criminal.  
    - Fetch details of criminals last seen in a particular location.  
    - Retrieve police station details for a specific case.

---

## ⚡ Scalability & Future Enhancements
- ➕ **Support for Additional Data Sources**: Dynamically integrate new databases.  
- 🧠 **Machine Learning Integration**: Predict crime patterns based on historical data.  
- 🔔 **Real-Time Alerts**: Notify law enforcement of status changes in cases or last-seen locations.

---

## 📈 How to Run the Project
1. **Clone the Repository**  
```bash
git clone https://github.com/JUGADU-GEEKS/Police-Data-Aggregation
