

# CFSS Cybersecurity Paid Internship Program

## Projects Overview

Welcome to the CFSS Cybersecurity Paid Internship Program! This repository contains the hands-on projects designed to help interns explore various cybersecurity techniques and tools. Each project has a specific objective aimed at enhancing your cybersecurity skills through practical, real-world scenarios. Below are the project descriptions, guidelines, and how to run the respective programs.

---

## Project 1: Exploring WiFi Security

**Objective:**  
This project covers WiFi hacking techniques, WiFi technologies, adapter modes, common tools, and countermeasures for securing wireless networks.

### Components:
- **WiFi Hacking Techniques**: Password cracking, WPS attacks, rogue APs, packet sniffing.
- **WiFi Technologies**: 2.4 GHz vs 5 GHz bands, modulation techniques, WiFi standards.
- **WiFi Adapter Modes**: Managed, monitor, ad-hoc, master modes.
- **Tools**: Aircrack-ng, Wireshark, Reaver, Metasploit.
- **Countermeasures**: WPA3 encryption, strong passwords, disabling WPS, MAC filtering.

### How to Run:
1. Install **Aircrack-ng** using: `sudo apt install aircrack-ng`.
2. Run the WiFi password cracking script by replacing the required parameters in the script file.
   ```bash
   sudo bash wifi_cracking.sh
   ```

---

## Project 2: MITM Attack Exploration with Bettercap

**Objective:**  
Learn how to perform a Man-in-the-Middle (MITM) attack using **Bettercap** and capture network traffic.

### How to Run:
1. Install **Bettercap** using: `sudo apt install bettercap`.
2. Enable packet forwarding:
   ```bash
   sudo sysctl -w net.ipv4.ip_forward=1
   ```
3. Run the MITM attack script:
   ```bash
   sudo bash mitm_attack.sh
   ```

---

## Project 3: Exploring Flipper Zero in Cybersecurity

**Objective:**  
Understand the **Flipper Zero** tool, its capabilities, and its applications in cybersecurity.

### How to Use:
1. Research Flipper Zero features and applications.
2. Explore real-world use cases of Flipper Zero in penetration testing and hardware hacking.

No specific script is required for this project since Flipper Zero is a hardware-based tool. Use its NFC, Bluetooth, and RFID capabilities.

---

## Project 4: Decrypting Hashed Codes

**Objective:**  
Explore hashing algorithms like **MD5**, **SHA-1**, and **SHA-256**. Decrypt provided hashed codes and understand the concept of salting.

### How to Run:
1. Ensure Python 3 is installed on your system.
2. Install the required libraries using:
   ```bash
   pip install hashlib
   ```
3. Run the hash decryption script:
   ```bash
   python hash_decrypt.py
   ```

Provide the MD5, SHA-1, or SHA-256 hash in the script and decrypt it using a wordlist.

---

## Project 5: Capture The Flag (CTF) Challenge

**Objective:**  
Participate in **Capture The Flag** (CTF) challenges to develop problem-solving skills.

### How to Play:
1. Solve challenges on platforms like **hackertest.net** and **OverTheWire's Bandit wargame**.
2. Use commands like `ssh`, `netcat`, or `curl` to connect to remote servers and retrieve flags.

---

## Project 6: Brute Force Attack with Hydra and Burp Suite

**Objective:**  
Conduct a brute force attack on the login page using **Hydra** and **Burp Suite**.

### How to Run:
1. Install **Hydra** using: `sudo apt install hydra`.
2. Run the brute force script to attack a vulnerable login page:
   ```bash
   sudo bash brute_force.sh
   ```

Replace the login parameters as needed for the target site.

---

## Requirements

- Linux-based system (recommended).
- Tools installed:
  - Aircrack-ng
  - Bettercap
  - Hydra
  - Wireshark
  - Python 3 with `hashlib` library.

---

## Documentation

Each project includes hands-on experimentation with hacking techniques, security measures, and the use of cybersecurity tools. Interns are expected to document their findings, analyze the results, and propose countermeasures where applicable. Additionally, each project should have a final presentation summarizing the learnings and techniques applied.

---

## License

This repository is for educational purposes as part of the **CFSS Cybersecurity Paid Internship Program**. Use these projects responsibly and adhere to ethical hacking practices.
