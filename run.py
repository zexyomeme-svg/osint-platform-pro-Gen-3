import os
from app.main import app
from app.system_manager import system_manager

if __name__ == "__main__":
    print("--- Nexus OSINT System Initializing ---")
    
    # 1. Integrity Check
    if not system_manager.check_integrity():
        print("[!] System integrity compromised. Please check system_audit.log")
    else:
        print("[+] System integrity verified.")

    # 2. Update Check
    updates = system_manager.check_for_updates()
    print("[+] Tool versions checked.")

    # 3. Startup Telemetry
    stats = system_manager.get_live_telemetry()
    print(f"[+] Initial Resource State: RAM {stats['ram']}% | CPU {stats['cpu']}%")

    # Render uses the PORT environment variable to assign a port to the service
    port = int(os.environ.get("PORT", 5000))
    
    print(f"--- Launching Nexus Framework on port {port} ---\n")
    # debug=False for production stability
    app.run(host='0.0.0.0', port=port, debug=False)
