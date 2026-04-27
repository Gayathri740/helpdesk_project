# Help Desk Ticketing System

This project is a Docker-based help desk system that allows users to submit and view support tickets.

Technologies used:
- Flask
- Docker
- SQLite
## Features
- Submit help desk tickets
- View submitted issues
- Runs inside Docker container

## How to Run
1. Build Docker image:
   docker build -t helpdesk-app .

2. Run container:
   docker run -d -p 5000:5000 helpdesk-app

3. Open browser:
   http://localhost:5000
