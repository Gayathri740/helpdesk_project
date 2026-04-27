# Help Desk Ticket System using Flask
# SQLite database added for ticket storage
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Create database
conn = sqlite3.connect('tickets.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    issue TEXT
)
''')
conn.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        issue = request.form["issue"]
        cursor.execute("INSERT INTO tickets (name, issue) VALUES (?, ?)", (name, issue))
        conn.commit()
    
    cursor.execute("SELECT name, issue FROM tickets")
    tickets = cursor.fetchall()

    return render_template_string("""
    <h2>Help Desk System</h2>
    <form method="post">
        Name: <input name="name"><br>
        Issue: <input name="issue"><br>
        <button type="submit">Submit Ticket</button>
    </form>
    <h3>Tickets:</h3>
    {% for t in tickets %}
        <p><b>{{t[0]}}</b>: {{t[1]}}</p>
    {% endfor %}
    """, tickets=tickets)

app.run(host="0.0.0.0", port=5000, debug=True)