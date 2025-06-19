#!/bin/bash

# Update and install basic tools
echo "Starting system update and installing basic tools..."
sudo dnf update -y && \
sudo dnf install nano -y && \
sudo dnf install wget -y
echo "Basic tools installed."

# Install EPEL release and tmate/screen
echo "Installing EPEL release, tmate, and screen..."
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
sudo dnf install -y tmate && \
sudo dnf install screen -y
echo "EPEL, tmate, and screen installed."

# Tmate: Consider if this needs to be daemonized or run only on demand.
# For now, it's just installed. If you want it to start automatically on boot,
# you might need a systemd service for it.

# Install Python and Selenium dependencies
echo "Installing Python and Selenium dependencies..."
sudo dnf install python3-pip -y && \
pip3 install selenium && \
pip3 install selenium-wire && \
pip3 install blinker==1.4 && \
sudo dnf install unzip -y && \
sudo dnf install libvulkan1 alsa-lib -y
echo "Python and Selenium dependencies installed."

# Install ChromeDriver
echo "Installing ChromeDriver..."
wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.119/linux64/chromedriver-linux64.zip && \
unzip chromedriver-linux64.zip && \
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
sudo chmod +x /usr/local/bin/chromedriver
echo "ChromeDriver installed."

# Install Google Chrome
echo "Installing Google Chrome..."
wget -O /tmp/chrome.rpm https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
sudo dnf localinstall /tmp/chrome.rpm -y
echo "Google Chrome installed."
