#!/bin/bash
# VulnHunt Installation Script
# Red Team Cybersecurity Framework for Kali Linux

echo -e "\033[1;36m"
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                      VulnHunt Installation                          ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo -e "\033[0m"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "\033[1;31m[!] Please run as root: sudo ./install.sh\033[0m"
    exit 1
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    echo -e "${CYAN}[*]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_error() {
    echo -e "${RED}[!]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Check if running on Kali Linux
if ! grep -q "Kali" /etc/os-release 2>/dev/null; then
    print_warning "This script is designed for Kali Linux. Continue anyway? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        exit 1
    fi
fi

# Update system
print_status "Updating system packages..."
apt update && apt upgrade -y

# Install Python dependencies
print_status "Installing Python dependencies..."
apt install -y python3 python3-pip python3-venv

# Install core penetration testing tools
print_status "Installing core penetration testing tools..."
apt install -y \
    nmap sqlmap metasploit-framework aircrack-ng \
    hydra john wireshark burpsuite setoolkit \
    masscan dnsrecon snmp dirb nikto wpscan \
    hashcat crunch wifite reaver kismet \
    git curl wget netcat-openbsd net-tools \
    tcpdump tshark dnsutils whois

# Install additional useful tools
print_status "Installing additional security tools..."
apt install -y \
    gobuster ffuf subfinder amass \
    exploitdb searchsploit \
    binwalk foremost volatility \
    autopsy sleuthkit \
    maltego recon-ng \
    theharvester sherlock

# Install Python packages
print_status "Installing Python packages..."
pip3 install colorama requests beautifulsoup4 argparse

# Create directory structure
print_status "Creating directory structure..."
mkdir -p /opt/vulnhunt
mkdir -p /opt/vulnhunt/modules
mkdir -p /opt/vulnhunt/logs
mkdir -p /opt/vulnhunt/output
mkdir -p /opt/vulnhunt/tools
mkdir -p /opt/vulnhunt/wordlists

# Copy VulnHunt files
print_status "Copying VulnHunt files..."

# Check if files exist in current directory
if [ -f "vulnhunt.py" ]; then
    cp vulnhunt.py /opt/vulnhunt/
else
    print_error "vulnhunt.py not found in current directory!"
    exit 1
fi

# Copy modules if they exist
if [ -d "modules" ]; then
    cp -r modules/* /opt/vulnhunt/modules/
else
    print_warning "modules directory not found, creating basic structure..."
    # Create basic module structure
    cat > /opt/vulnhunt/modules/network_recon.py << 'EOF'
#!/usr/bin/env python3
def run():
    print("Network Reconnaissance Module - Placeholder")
EOF
fi

# Copy README if exists
if [ -f "README.md" ]; then
    cp README.md /opt/vulnhunt/
fi

# Copy this install script
cp install.sh /opt/vulnhunt/

# Set permissions
print_status "Setting permissions..."
chmod +x /opt/vulnhunt/vulnhunt.py
chmod +x /opt/vulnhunt/install.sh
chmod -R +x /opt/vulnhunt/modules/
chown -R root:root /opt/vulnhunt/

# Create symlink for easy access
print_status "Creating symlink..."
ln -sf /opt/vulnhunt/vulnhunt.py /usr/local/bin/vulnhunt

# Create configuration file
print_status "Creating configuration..."
cat > /opt/vulnhunt/config.json << 'EOF'
{
    "version": "1.0.0",
    "author": "VulnHunt Team",
    "output_dir": "/opt/vulnhunt/output",
    "log_dir": "/opt/vulnhunt/logs",
    "tools_dir": "/opt/vulnhunt/tools",
    "wordlists": {
        "common": "/usr/share/wordlists/dirb/common.txt",
        "rockyou": "/usr/share/wordlists/rockyou.txt",
        "seclists": "/usr/share/seclists"
    },
    "settings": {
        "auto_update": true,
        "log_level": "INFO",
        "color_output": true,
        "default_wordlist": "/usr/share/wordlists/rockyou.txt"
    }
}
EOF

# Download additional wordlists if not present
print_status "Checking for wordlists..."
if [ ! -f "/usr/share/wordlists/rockyou.txt" ]; then
    print_warning "rockyou.txt not found, downloading..."
    cd /usr/share/wordlists/
    wget -q https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
    gunzip rockyou.txt.gz 2>/dev/null || true
fi

if [ ! -d "/usr/share/seclists" ]; then
    print_status "Installing SecLists..."
    git clone https://github.com/danielmiessler/SecLists.git /usr/share/seclists
fi

# Create desktop entry (optional)
print_status "Creating desktop entry..."
cat > /usr/share/applications/vulnhunt.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=VulnHunt
Comment=Red Team Cybersecurity Framework
Exec=/usr/local/bin/vulnhunt
Icon=utilities-terminal
Categories=System;Security;
Terminal=true
StartupNotify=false
EOF

# Create update script
print_status "Creating update script..."
cat > /opt/vulnhunt/update.sh << 'EOF'
#!/bin/bash
# VulnHunt Update Script

echo "Updating VulnHunt..."
cd /opt/vulnhunt
git pull origin main 2>/dev/null || echo "Manual installation detected"
sudo apt update && sudo apt upgrade -y
sudo pip3 install --upgrade colorama requests beautifulsoup4
echo "VulnHunt update completed!"
EOF

chmod +x /opt/vulnhunt/update.sh

# Create uninstall script
print_status "Creating uninstall script..."
cat > /opt/vulnhunt/uninstall.sh << 'EOF'
#!/bin/bash
# VulnHunt Uninstall Script

echo "Uninstalling VulnHunt..."
rm -f /usr/local/bin/vulnhunt
rm -f /usr/share/applications/vulnhunt.desktop
rm -rf /opt/vulnhunt
echo "VulnHunt has been uninstalled!"
EOF

chmod +x /opt/vulnhunt/uninstall.sh

# Final setup
print_status "Finalizing installation..."

# Create log file
touch /opt/vulnhunt/logs/vulnhunt.log

# Test installation
print_status "Testing installation..."
if [ -f "/usr/local/bin/vulnhunt" ] && [ -x "/opt/vulnhunt/vulnhunt.py" ]; then
    print_success "VulnHunt installation completed successfully!"
else
    print_error "Installation may have issues. Please check manually."
fi

# Display completion message
echo -e "\033[1;36m"
echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                    Installation Complete!                           ║"
echo "╠══════════════════════════════════════════════════════════════════════╣"
echo "║                                                                      ║"
echo "║ Usage: vulnhunt                                                     ║"
echo "║                                                                      ║"
echo "║ Quick Start:                                                        ║"
echo "║   $ vulnhunt                                                        ║"
echo "║                                                                      ║"
echo "║ Update:                                                             ║"
echo "║   $ sudo /opt/vulnhunt/update.sh                                    ║"
echo "║                                                                      ║"
echo "║ Uninstall:                                                          ║"
echo "║   $ sudo /opt/vulnhunt/uninstall.sh                                 ║"
echo "║                                                                      ║"
echo "║ Location: /opt/vulnhunt/                                            ║"
echo "║                                                                      ║"
echo "║ Available Modules:                                                  ║"
echo "║   • Network Reconnaissance                                          ║"
echo "║   • Web Application Testing                                         ║"
echo "║   • Vulnerability Scanning                                          ║"
echo "║   • Password Attacks                                                ║"
echo "║   • Wireless Attacks                                                ║"
echo "║   • Social Engineering                                              ║"
echo "║   • Post-Exploitation                                               ║"
echo "║   • Forensic Analysis                                               ║"
echo "║   • Custom Tool Integration                                         ║"
echo "║   • Automated Attack Chains                                         ║"
echo "║                                                                      ║"
echo "║ Legal Notice:                                                       ║"
echo "║   Use only on systems you own or have explicit permission to test.  ║"
echo "║   The authors are not responsible for any misuse of this tool.      ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo -e "\033[0m"

print_success "VulnHunt is ready to use! Run 'vulnhunt' to start."
print_warning "Remember: Always ensure you have proper authorization before testing!"
```](streamdown:incomplete-link)