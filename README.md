# **VulnHunt - Web Vulnerability Scanner with Flask Dashboard**

**VulnHunt** is a simple yet powerful tool for scanning web applications for common vulnerabilities such as **SQL Injection**, **XSS**, **Missing Security Headers**, and **Directory Bruteforce**. This tool is built using **Python** and is integrated with a **Flask-based web dashboard** to monitor the progress of your vulnerability scan in real time.

## **Features**

- **SQL Injection** detection with advanced payloads.
- **Cross-Site Scripting (XSS)** vulnerability detection.
- **Security Header Checker** to detect missing security headers like `Strict-Transport-Security`, `Content-Security-Policy`, etc.
- **Directory Brute-Forcing** to uncover hidden directories or files.
- **Flask Dashboard** to track and display scan progress and results.

---

## **Requirements**

Before using the project, ensure you have the following dependencies installed:

### **Software Requirements:**

- **Python 3.x** (preferably **Python 3.8+**)

### **Required Python Libraries:**

- `requests`
- `flask`
- `colorama`

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

Or manually install the libraries with:

```bash
pip install requests flask colorama
```

## **Project Structure**

```
VulnHunt/
├── app.py                  # Flask web server for scan progress dashboard
├── vulnHunt.py             # Main scan logic
├── modules/                # Vulnerability check modules
│   ├── sql_injection.py    # SQL Injection module
│   ├── xss_scanner.py      # XSS module
│   ├── header_checker.py   # Security header checker module
│   └── dir_bruteforce.py   # Directory brute-forcing module
├── reports/                # Directory to save scan results (JSON format)
├── wordlists/              # Wordlists for brute-force (e.g., directories, files)
├── templates/
│   └── index.html          # HTML template for Flask dashboard
├── requirements.txt        # List of required Python dependencies
└── README.md               # This README file
```

## **Setup & Configuration**

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/VulnHunt.git
cd VulnHunt
```

### 2. Flask Dashboard Setup
The Flask web server (`app.py`) allows you to monitor the progress of your scan in real-time.

The `index.html` template renders a simple web page where you can start the scan and view the progress in a progress bar.

Ensure that the following files are in place:
- `app.py`: Runs the Flask web server.
- `templates/index.html`: Contains the front-end HTML to visualize the scan progress.

## **Usage**

### 1. Running the Flask Dashboard
To start the Flask dashboard, run:

```bash
python app.py
```

This will start the server at `http://127.0.0.1:5000/`. Open this URL in your browser to access the dashboard.

### 2. Scan Process via Dashboard

#### Starting the Scan
Click the **"Start Scan"** button on the Flask dashboard. The scan will begin, and the progress bar will fill up as the scan progresses.

#### Monitor the Scan
As the scan progresses, the status and progress bar will be updated in real-time. Once the scan is completed, the scan results will be saved in the `reports` directory in JSON format.

#### View Scan Results
After completion, you will see a message with the file path of the generated report (e.g., `reports/vulnhunt_report_2025-05-03_14-30-00.json`). You can open this JSON file to view the detailed results of the vulnerabilities found.

### Running the VulnHunt Scanner (Without Flask)
If you prefer to run the scan via the command line without the Flask dashboard, you can use `vulnHunt.py` directly:

```bash
python vulnHunt.py --url http://example.com --brute --skip-sqli --skip-xss
```

**Options:**
- `--url`: The target URL to scan.
- `--brute`: Enable directory brute-forcing.
- `--skip-sqli`: Skip SQL Injection testing.
- `--skip-xss`: Skip XSS testing.
- `--skip-headers`: Skip security header checks.

## **Customizing the Wordlists and Payloads**
You can customize the wordlists and payloads used by the scanner:
- The directory brute-forcing module uses a wordlist (`wordlists/common.txt`) that you can replace with your own custom list.
- You can add or modify the payloads used in the SQL Injection and XSS detection modules by editing the respective Python files in the `modules/` folder.

## **Vulnerability Scan Modules**

### 1. SQL Injection (`sql_injection.py`)
Detects SQL injection vulnerabilities by testing common SQL payloads.

### 2. Cross-Site Scripting (XSS) (`xss_scanner.py`)
Detects Cross-Site Scripting (XSS) vulnerabilities by testing common XSS payloads.

### 3. Header Checker (`header_checker.py`)
Checks for the presence of important security headers like `Strict-Transport-Security`, `Content-Security-Policy`, etc.

### 4. Directory Bruteforce (`dir_bruteforce.py`)
Attempts to brute-force common directories or files on the target server to find hidden paths.