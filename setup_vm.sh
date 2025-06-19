#!/bin/bash

# Update and install basic tools
sudo dnf update -y && \
sudo dnf install nano -y && \
sudo dnf install wget -y

# Install EPEL release and tmate/screen
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
sudo dnf install -y tmate && \
sudo dnf install screen -y

# Start tmate (consider if this should be interactive or daemonized)
# tmate # This command will likely block cloud-init, reconsider if it's needed this way during provisioning

# Install Python and Selenium dependencies
sudo dnf install python3-pip -y && \
pip3 install selenium && \
pip3 install selenium-wire && \
pip3 install blinker==1.4 && \
sudo dnf install unzip -y && \
sudo dnf install libvulkan1 alsa-lib -y

# Install ChromeDriver
wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.119/linux64/chromedriver-linux64.zip && \
unzip chromedriver-linux64.zip && \
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
sudo chmod +x /usr/local/bin/chromedriver

# Install Google Chrome
wget -O /tmp/chrome.rpm https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
sudo dnf localinstall /tmp/chrome.rpm -y

# Download rosak1.py
wget https://raw.githubusercontent.com/sentosamemet/tuwir/refs/heads/main/rosak1.py

# Start screen session (this will also likely block cloud-init,
# consider running the Python script in a detached screen session or as a service)
# screen -R 220219 # This command will likely block cloud-init
