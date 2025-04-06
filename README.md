# 🔍 Network and Port Scanner

A lightweight and effective Python-based tool to scan for live hosts and detect open or closed TCP ports using `nmap`. This tool helps security professionals and network administrators perform essential reconnaissance for network security assessments.

---

## 📌 Project Overview

This project is designed to:
- ✅ Detect **live hosts** on a network.
- 🔓 Identify **open or closed ports**.
- ⚙️ Detect **services** running on open ports.

---

## 🚀 Features

- **Host Detection** – Check if the target host is reachable.
- **Port Scanning** – Analyze specific TCP ports on a target host.
- **Service Detection** – Discover services running on open ports.
- **Command-line Interface** – Accepts dynamic host and port inputs using `argparse`.
- **Robust Error Handling** – Ensures the script gracefully handles invalid inputs or unreachable hosts.

---

## 🛠️ Technologies Used

- **Python** – Simplicity and wide library support.
- **Nmap** – Powerful network scanning tool (via `python-nmap`).
- **Argparse** – For parsing command-line arguments.
- **Requests** – To verify host availability.

---

## 💻 How to Run

1. Install dependencies:
   ```bash
   pip install python-nmap requests
   ```

2. Run the script:
   ```bash
   python3 main.py -H 192.168.1.1 -p 22,80,443
   ```

3. Output:
   - Displays whether the target host is reachable.
   - Indicates if each specified port is open or closed.

---

## 📈 Example Output

```
Scanning host: 192.168.1.1
Port 22: OPEN
Port 80: OPEN
Port 443: CLOSED
```

---

## 🌐 Real-World Applications

- 🔐 Network security auditing.
- 🧪 Educational tool for students learning about port scanning.
- 🔧 Troubleshooting network services and firewall configurations.

---

## 📬 Contact

**Aditya Rajendra Talwatkar**  
📧 [adityatalwatkar@gmail.com](mailto:adityatalwatkar@gmail.com)  

---

## 📅 Last Updated

**September 21, 2024**

---

## ✅ Conclusion

This Network and Port Scanner is a practical and efficient tool for identifying potential vulnerabilities in a network. Its simplicity and effectiveness make it an ideal choice for both beginners and professionals in cybersecurity.
