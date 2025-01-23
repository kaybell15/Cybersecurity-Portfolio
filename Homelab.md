# Homelab Project

## Overview
This project demonstrates my personal cybersecurity homelab, which is designed to simulate a secure and segmented network environment. The homelab allows for hands-on practice with VLANs, firewall configurations, penetration testing, and system administration.
## Features
- **Virtualized Environment**: Created using VirtualBox to isolate and control network traffic.
- **Network Segmentation**: Implemented VLANs to separate traffic between different virtual machines.
- **Firewall Management**: Configured pfSense to control and monitor network communication.
- **Vulnerability Testing**: Deployed bWAPP on VLAN 20 for web application vulnerability testing.
- **Secure Workstation**: Used Linux Mint as a daily-use secure operating system.

## Components
- **pfSense**: Configured as the core router/firewall.
  - Role: Network segmentation and traffic management.
  - Features: VLAN tagging, firewall rules, and traffic monitoring.
- **Kali Linux**: Used for penetration testing and ethical hacking.
  - Role: Network scanning and vulnerability testing.
- **Linux Mint**: Secure workstation for general-purpose use.
  - Role: Demonstrates system hardening and secure configurations.
- **bWAPP**: Vulnerable web application for testing web security.
  - Role: Web application vulnerability testing on VLAN 20.

## Network Diagram
![Network Diagram](./network_diagram.png)

## Skills Demonstrated
- Network segmentation using VLANs.
- Firewall configuration and traffic control with pfSense.
- Penetration testing using Kali Linux tools (e.g., Nmap, Wireshark).
- Vulnerability scanning and analysis using bWAPP.
- System hardening and secure workstation setup on Linux Mint.
