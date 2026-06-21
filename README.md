# 🛡️ Nexus Intelligence Framework

**Nexus Intelligence** is a professional-grade Open Source Intelligence (OSINT) framework designed for rapid reconnaissance, digital footprint analysis, and infrastructure auditing. It is specifically engineered to operate within the strict resource constraints of the Render Free Tier (512MB RAM / 0.1 CPU).

## 🚀 Key Intelligence Modules

| Module | Capability | Technology |
| :--- | :--- | :--- |
| **IP Intelligence** | Geolocation, ASN lookup, and network reputation. | `ip-api` |
| **Domain Intelligence** | WHOIS registration, DNS enumeration, and tech-stack audit. | `python-whois`, `dnspython` |
| **Identity Mapping** | Cross-platform username footprinting (15+ platforms). | `Requests` (HTTP Profiling) |
| **Email Intelligence** | Domain legitimacy verification and MX record auditing. | `dnspython` |
| **Phone Intelligence** | Precision pivot link generation for public records. | Deep-link Integration |
| **System Telemetry** | Real-time RAM/CPU monitoring and memory optimization. | `psutil` |

## 🛠️ Technical Architecture

- **Backend**: Python / Flask
- **Frontend**: Tailwind CSS / Glassmorphism UI
- **Optimization**: Adaptive Garbage Collection (GC) engine to prevent OOM crashes.
- **Deployment**: Render-optimized via `Gunicorn` and `Procfile`.

## ⚡ Quick Start

### Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the framework:
   ```bash
   python run.py
   ```

### Deployment to Render
1. Push this repository to GitHub.
2. Create a new **Web Service** on Render.
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn app.main:app`

## 🛡️ Operational Security (OpSec)
*This tool is for educational and ethical security research. Always ensure your activities comply with local laws and the Terms of Service of the targeted platforms.*
