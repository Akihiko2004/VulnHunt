# VulnHunt - Red Team Cybersecurity Framework
**VulnHunt Python License Platform Version**

A comprehensive, modular red team cybersecurity framework for Kali Linux

📖 **Overview**  
VulnHunt is an all-in-one penetration testing framework that integrates multiple security tools into a unified, user-friendly interface. Designed for security professionals, it provides a centralized platform for conducting authorized security assessments across various attack vectors.

✨ **Key Features**
- 🔧 **10+ Integrated Modules** - Comprehensive coverage of all major attack vectors  
- 🔄 **Multi-Tool Selection** - Run multiple tools simultaneously or in sequence  
- ⚡ **Automated Attack Chains** - Pre-configured workflows for comprehensive assessments  
- 🎨 **Color-coded Interface** - Intuitive and visually organized user experience  
- 📊 **Comprehensive Logging** - Detailed documentation for reporting and analysis  
- 🔧 **Modular Architecture** - Easy to extend and customize  
- 🛡️ **Legal Compliance** - Built-in warnings and ethical usage reminders

---

## 🚀 Quick Start

### Prerequisites
- **Operating System:** Kali Linux (recommended) or Debian-based Linux  
- **Python:** Version 3.6 or higher  
- **Permissions:** `sudo` / root access for installation  
- **Resources:** Minimum 4GB RAM, 20GB disk space

### Installation

### # Method 1: Automated Installation (Recommended)
```bash
# Clone the repository
git clone https://github.com/akihiko2004/vulnhunt.git
cd vulnhunt

# Run the installation script
if [ -f install.sh ]; then
  sudo chmod +x install.sh
  echo "Running install.sh..."
  sudo ./install.sh || echo "install.sh finished (or returned non-zero)."
else
  echo "No install.sh found in $(pwd) — skipping installer."
fi

if [ -f vulnHunt.py ]; then
  # add executable bit
  chmod +x vulnHunt.py

  # check for shebang
  head -n1 vulnHunt.py | grep -q '^#!' || {
    echo "No shebang found in vulnHunt.py — creating wrapper instead of modifying file."
    # create wrapper at /usr/local/bin/vulnhunt that calls python3 with the script
    sudo tee /usr/local/bin/vulnhunt > /dev/null <<'EOF'
#!/usr/bin/env bash
python3 ~/vulnhunt/vulnHunt.py "$@"
EOF
    sudo chmod +x /usr/local/bin/vulnhunt
    echo "Wrapper created at /usr/local/bin/vulnhunt -> python3 ~/vulnhunt/vulnHunt.py"
  }

if [ -f vulnHunt.py ]; then
  # add executable bit
  chmod +x vulnHunt.py

  # check for shebang
  head -n1 vulnHunt.py | grep -q '^#!' || {
    echo "No shebang found in vulnHunt.py — creating wrapper instead of modifying file."
    # create wrapper at /usr/local/bin/vulnhunt that calls python3 with the script
    sudo tee /usr/local/bin/vulnhunt > /dev/null <<'EOF'
#!/usr/bin/env bash
python3 ~/vulnhunt/vulnHunt.py "$@"
EOF
    sudo chmod +x /usr/local/bin/vulnhunt
    echo "Wrapper created at /usr/local/bin/vulnhunt -> python3 ~/vulnhunt/vulnHunt.py"
  }

  # If vulnHunt.py already has shebang we create symlink directly
  head -n1 vulnHunt.py | grep -q '^#!' && {
    # create symlink pointing to the repo script (absolute path ensures it works)
    sudo ln -sf "$(pwd)/vulnHunt.py" /usr/local/bin/vulnhunt
    sudo chmod +x /usr/local/bin/vulnhunt
    echo "Symlink created: /usr/local/bin/vulnhunt -> $(pwd)/vulnHunt.py"
  }
else
  echo "vulnHunt.py not found in $(pwd). Check the repository contents."
  exit 1
fi

echo "Which vulnhunt binary will be used:"
command -v vulnhunt || true
echo "Attempting to run 'vulnhunt --help' (or run 'vulnhunt' if no --help):"
vulnhunt --help 2>/dev/null || vulnhunt 2>/dev/null || echo "Could not run 'vulnhunt' — check output above."

echo "Fallback test: run directly with python3:"
python3 "$(pwd)/vulnHunt.py" --help 2>/dev/null || python3 "$(pwd)/vulnHunt.py" || echo "Fallback run failed."
```

### # Method 2 — Manual
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install external dependencies (example list)
sudo apt install -y python3 python3-pip nmap sqlmap metasploit-framework \
  aircrack-ng hydra john wireshark burpsuite setoolkit \
  masscan dnsrecon dirb nikto wpscan hashcat crunch
```

### # Install Python requirements
```bash
pip3 install -r requirements.txt
```
### # OR install selected packages individually:
```bash
pip3 install colorama requests beautifulsoup4
```

### # Create target directories
```bash
sudo mkdir -p /opt/vulnhunt/{modules,logs,output,tools}
```

### # Copy scripts and modules into /opt
```bash
sudo cp vulnhunt.py /opt/vulnhunt/
sudo cp -r modules/* /opt/vulnhunt/modules/
```

### # Make main script executable and add symlink
```bash
sudo chmod +x /opt/vulnhunt/vulnhunt.py
sudo ln -sf /opt/vulnhunt/vulnhunt.py /usr/local/bin/vulnhunt
```

## Verification
### # Check version (if supported)
```bash
vulnhunt --version
```

### # Or run the interactive UI
```bash
vulnhunt
```

## 🎯 Usage Guide
### # Starting VulnHunt (interactive)
```bash
vulnhunt
```

### # Typical interactive menu (ASCII UI):
```bash
╔══════════════════════════════════════════════════════════════════════╗
║                        AVAILABLE TOOLS                              ║
╠══════════════════════════════════════════════════════════════════════╣
║  1. Network Reconnaissance                                           ║
║  2. Web Application Testing                                          ║
║  3. Vulnerability Scanning                                           ║
║  4. Password Attacks                                                 ║
║  5. Wireless Attacks                                                 ║
║  6. Social Engineering                                               ║
║  7. Post-Exploitation                                                ║
║  8. Forensic Analysis                                                ║
║  9. Custom Tool Integration                                          ║
║ 10. Automated Attack Chains                                          ║
║ 11. Exit                                                             ║
╚══════════════════════════════════════════════════════════════════════╝
```

### # Running from CLI (non-dashboard)
```bash
python vulnHunt.py --url http://example.com --brute --skip-sqli --skip-xss
```

Options

- **url** : target URL

- **brute** : enable directory brute-forcing

- **skip-sqli** : skip SQL injection testing

- **skip-xss** : skip XSS testing

- **skip-headers** : skip security header checks

## 🔍 Module Overview
### 1. Network Reconnaissance

- **Nmap** — Network discovery and auditing

- **Masscan** — Mass IP port scanner

- **DNSRecon** — DNS enumeration

- **SNMPWalk** — SNMP enumeration

### 2. Web Application Testing

- **SQLMap** — Automatic SQL injection tool

- **Nikto** — Web server scanner

- **Dirb** — Web content scanner

- **WPScan** — WordPress security scanner

### 3. Vulnerability Scanning

- **Nmap NSE scripts** — vulnerability detection

- **OpenVAS** — optional integration for comprehensive scans

- **Custom checks** — plugin/extension friendly

### 4. Password Attacks

- **Hydra, John the Ripper, Hashcat, Crunch**

### 5. Wireless Attacks

- **Aircrack-ng, Wifite, Reaver, Kismet**

### 6. Social Engineering

- **SET (Social Engineering Toolkit), Gophish, credential harvesting scaffolds**

### 7. Post-Exploitation

- **Metasploit, Empire, Mimikatz, BloodHound**

### 8. Forensic Analysis

- **Autopsy, Volatility, Binwalk, Foremost**

### 9. Custom Tool Integration

- **Custom script runner, tool installer, GitHub downloader, payload generator**

### 10. Automated Attack Chains

- **Prebuilt chains: web full-assessment, network penetration, wireless audit, social campaign**

## 🔧 Configuration

### Configuration file location
```bash
/opt/vulnhunt/config.json
```

### Sample config.json
```bash
{
  "version": "1.0.0",
  "author": "Akihiko2004",
  "output_dir": "/opt/vulnhunt/output",
  "log_dir": "/opt/vulnhunt/logs",
  "wordlists": {
    "common": "/usr/share/wordlists/dirb/common.txt",
    "rockyou": "/usr/share/wordlists/rockyou.txt",
    "seclists": "/usr/share/seclists"
  },
  "settings": {
    "auto_update": true,
    "log_level": "INFO",
    "color_output": true
  }
}
```

## 📊 Output & Reporting

- **Logs** : /opt/vulnhunt/logs/vulnhunt.log

- **Output** : /opt/vulnhunt/output/

- **Formats** : JSON (machine), Text (human), HTML (web)

## 🛡️ Legal & Ethical Usage

- VulnHunt should only be used on systems you own or have explicit written permission to test. Unauthorized use of this tool may violate local, state, and federal laws.

## 🐛 Troubleshooting

### # Command not found
```bash
sudo ln -sf /opt/vulnhunt/vulnhunt.py /usr/local/bin/vulnhunt
```

### # Missing dependencies
```bash
# Reinstall dependencies
sudo apt install -y python3 python3-pip
pip3 install colorama requests beautifulsoup4
```

### # Permission errors
```bash
# Fix permissions
sudo chown -R root:root /opt/vulnhunt/
sudo chmod +x /opt/vulnhunt/vulnhunt.py
```

## 🤝 Contributing

We welcome contributions to VulnHunt! Please follow these guidelines:

- **1. Fork the repository**
- **2. Create a feature branch**
- **3. Make your changes**
- **4. Test thoroughly**
- **5. Submit a pull request**

## Development setup
```bash
git clone https://github.com/akihiko2004/vulnhunt.git
cd vulnhunt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ⚠️ Disclaimer: I'm not responsible for misuse. Ensure you have proper authorization before testing.
