from flask import Flask, render_template, request, jsonify
from app.utils import get_ip_info, get_whois_info, get_dns_records, search_username, analyze_website, verify_email, get_phone_search_links, scan_file_kicom
from app.optimizer import optimizer
import time
import gc
import os

app = Flask(__name__)

# Memory cleanup after every request to prevent OOM on Render Free Tier
@app.after_request
def cleanup_memory(response):
    gc.collect()
    return response

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/ip-lookup')
def ip_lookup_page():
    return render_template('ip_lookup.html')

@app.route('/domain-lookup')
def domain_lookup_page():
    return render_template('domain_lookup.html')

@app.route('/identity-lookup')
def identity_lookup_page():
    return render_template('identity_lookup.html')

@app.route('/email-lookup')
def email_lookup_page():
    return render_template('email_lookup.html')

@app.route('/phone-lookup')
def phone_lookup_page():
    return render_template('phone_lookup.html')

@app.route('/kicom-av')
def kicom_av_page():
    return render_template('kicom_lookup.html')

@app.route('/stats')
def stats_page():
    return render_template('stats.html')

# API Endpoints
@app.route('/api/ip/<ip>')
def api_ip_handler(ip):
    time.sleep(1)
    return jsonify(get_ip_info(ip))

@app.route('/api/domain/<domain>')
def api_domain_handler(domain):
    time.sleep(1)
    whois_data = get_whois_info(domain)
    dns_data = get_dns_records(domain)
    return jsonify({"whois": whois_data, "dns": dns_data})

@app.route('/api/username/<username>')
def api_username_handler(username):
    time.sleep(1)
    return jsonify(search_username(username))

@app.route('/api/analyze/<url>')
def api_analyze_handler(url):
    time.sleep(1)
    return jsonify(analyze_website(url))

@app.route('/api/email/<email>')
def api_email_handler(email):
    time.sleep(1)
    return jsonify(verify_email(email))

@app.route('/api/phone/<phone>')
def api_phone_handler(phone):
    time.sleep(1)
    return jsonify(get_phone_search_links(phone))

@app.route('/api/kicom-scan', methods=['POST'])
def api_kicom_scan():
    server_url = request.form.get("server_url", "http://localhost:8311")
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
        
    file = request.files['file']
    result = scan_file_kicom(file, server_url)
    
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400
        
    return jsonify(result)

@app.route('/api/system-stats')
def api_system_stats_handler():
    return jsonify(optimizer.get_stats())

@app.route('/api/optimize', methods=['POST'])
def api_optimize_handler():
    msg = optimizer.optimize()
    return jsonify({"message": msg, "stats": optimizer.get_stats()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
