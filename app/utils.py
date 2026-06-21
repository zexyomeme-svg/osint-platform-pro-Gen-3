import requests
import whois
import socket
import dns.resolver
import os
from datetime import datetime

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "emails": w.emails,
            "name_servers": w.name_servers
        }
    except Exception as e:
        return {"error": str(e)}

def get_dns_records(domain):
    records = {}
    for rtype in ['A', 'MX', 'NS', 'TXT', 'AAAA', 'CNAME', 'SOA']:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(rdata) for rdata in answers]
        except Exception:
            records[rtype] = []
    
    try:
        g_dns = requests.get(f"https://dns.google/resolve?name={domain}&type=A", timeout=5).json()
        if 'Answer' in g_dns:
            records['Google_A'] = [ans['data'] for ans in g_dns['Answer']]
    except Exception:
        pass

    return records

def search_username(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "YouTube": f"https://youtube.com/@{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "Medium": f"https://medium.com/@{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Behance": f"https://behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
    }
    results = {}
    for name, url in platforms.items():
        try:
            res = requests.get(url, timeout=3)
            if res.status_code == 200:
                results[name] = {"status": "Found", "url": url}
            else:
                results[name] = {"status": "Not Found", "url": url}
        except Exception:
            results[name] = {"status": "Error", "url": url}
    return results

def analyze_website(url):
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        res = requests.get(url, timeout=5)
        headers = res.headers
        tech = []
        server = headers.get('Server', '').lower()
        if 'nginx' in server: tech.append('Nginx')
        if 'apache' in server: tech.append('Apache')
        if 'cloudflare' in server: tech.append('Cloudflare')
        x_powered_by = headers.get('X-Powered-By', '').lower()
        if 'php' in x_powered_by: tech.append('PHP')
        if 'asp.net' in x_powered_by: tech.append('ASP.NET')
        if 'express' in x_powered_by: tech.append('Node.js/Express')
        return {
            "status_code": res.status_code,
            "server": headers.get('Server', 'Unknown'),
            "tech_stack": tech if tech else ["Unknown/Custom"],
            "content_type": headers.get('Content-Type', 'Unknown'),
            "headers": dict(headers)
        }
    except Exception as e:
        return {"error": str(e)}

def verify_email(email):
    try:
        domain = email.split('@')[1]
        answers = dns.resolver.resolve(domain, 'MX')
        return {
            "valid_domain": True,
            "mx_records": [str(rdata) for rdata in answers],
            "status": "Domain accepts email"
        }
    except Exception as e:
        return {"valid_domain": False, "status": f"Domain does not accept email or error: {str(e)}"}

def get_phone_search_links(phone):
    return {
        "Google": f"https://www.google.com/search?q=\"{phone}\"",
        "Facebook": f"https://www.facebook.com/search/top/?q={phone}",
        "TrueCaller": f"https://www.truecaller.com/search/{phone}",
        "Sync.me": f"https://sync.me/search?q={phone}",
    }

def scan_file_kicom(file_storage, server_url):
    """Scans file using KicomAV REST API"""
    # KicomAV default port is 8311
    url = f"{server_url.rstrip('/')}/scan/file"
    files = {"file": (file_storage.filename, file_storage.stream, file_storage.content_type)}
    try:
        response = requests.post(url, files=files, timeout=30)
        if response.status_code == 200:
            return response.json() # Returns scan results directly
        return {"error": f"KicomAV API Error: {response.status_code} - {response.text}"}
    except Exception as e:
        return {"error": str(e)}
