# modules/report_writer.py

import json
from datetime import datetime

def save_report(results):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_data = {
        'scan_date': now,
        'vulnerabilities': results
    }
    report_filename = f"reports/vulnhunt_report_{now}.json"
    with open(report_filename, 'w') as json_file:
        json.dump(report_data, json_file, indent=4)
    return report_filename
