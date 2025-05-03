# app.py

from flask import Flask, render_template, jsonify
from threading import Thread
import time
import os
from datetime import datetime
import json

app = Flask(__name__)

# Global variable to store progress
scan_progress = {
    "status": "Not Started",
    "progress": 0,
    "report_file": ""
}

def run_scan():
    """Simulate a scan progress (replace this with your actual scan logic)"""
    global scan_progress
    scan_progress["status"] = "Running"
    for i in range(1, 101):
        time.sleep(0.1)  # Simulate work being done (replace with actual scan logic)
        scan_progress["progress"] = i
        # Simulate saving the report after scan
        if i == 100:
            scan_progress["status"] = "Completed"
            scan_progress["report_file"] = save_report()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_scan')
def start_scan():
    """Start the scan in a new thread"""
    scan_thread = Thread(target=run_scan)
    scan_thread.start()
    return jsonify({"message": "Scan started!"})

@app.route('/scan_status')
def scan_status():
    """Return the current scan status and progress"""
    return jsonify(scan_progress)

def save_report():
    """Simulate saving a scan report and return its file path"""
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_filename = f"reports/vulnhunt_report_{now}.json"
    results = {"scan_date": now, "vulnerabilities": ["SQLi", "XSS", "Headers Missing"]}  # Dummy results
    with open(report_filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    return report_filename

if __name__ == '__main__':
    app.run(debug=True)
