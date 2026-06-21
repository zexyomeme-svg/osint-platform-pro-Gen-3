import os
import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("system_audit.log"),
        logging.StreamHandler()
    ]
)

class SystemManager:
    def __init__(self):
        self.required_files = [
            'app/main.py',
            'app/optimizer.py',
            'app/utils.py',
            'app/templates/base.html',
            'app/templates/index.html',
            'app/templates/ip_lookup.html',
            'app/templates/domain_lookup.html',
            'app/templates/identity_lookup.html',
            'app/templates/stats.html',
            'requirements.txt',
            'Procfile'
        ]
        self.required_folders = [
            'app/static/css',
            'app/static/js',
            'app/templates'
        ]

    def check_integrity(self):
        logging.info("Starting system integrity check...")
        all_ok = True
        
        # Check folders
        for folder in self.required_folders:
            if not os.path.exists(folder):
                logging.error(f"MISSING FOLDER: {folder}")
                all_ok = False
            else:
                logging.info(f"Folder OK: {folder}")

        # Check files
        for file in self.required_files:
            if not os.path.exists(file):
                logging.error(f"MISSING FILE: {file}")
                all_ok = False
            else:
                logging.info(f"File OK: {file}")

        if all_ok:
            logging.info("System integrity verified successfully.")
        else:
            logging.warning("System integrity check failed. Some files are missing.")
        
        return all_ok

    def check_for_updates(self):
        logging.info("Checking for tool updates...")
        # Simulated update check - in a real world scenario, this would hit a GitHub API
        updates = {
            "IP Module": "v1.2 (Stable)",
            "DNS Module": "v1.1 (Stable)",
            "Identity Module": "v1.0 (Update Available -> v1.1)",
            "Optimizer": "v1.0 (Stable)"
        }
        for tool, version in updates.items():
            logging.info(f"{tool}: {version}")
        
        logging.info("Update check completed.")
        return updates

    def get_live_telemetry(self):
        # This can be used by run.py to log start-up state
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=0.1)
        logging.info(f"Startup Telemetry - RAM: {mem.percent}% | CPU: {cpu}%")
        return {"ram": mem.percent, "cpu": cpu}

system_manager = SystemManager()
