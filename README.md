# WebScanner

[![License](https://img.shields.io/github/license/anonwincy/webscanner)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/anonwincy/webscanner)](https://github.com/anonwincy/webscanner/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/anonwincy/webscanner)](https://github.com/anonwincy/webscanner/network)

## Introduction

WebScanner is an advanced and professional tool designed for security professionals and enthusiasts. It offers a comprehensive suite of features, including a web vulnerability scanner, subdomain finder, admin panel finder, and brute force attack capabilities. WebScanner is user-friendly and highly responsive, making it an essential tool for anyone looking to enhance their web security assessments.

## Features

1. **Web Vulnerability Scanner**: Scan websites for common vulnerabilities and weaknesses.
2. **Subdomain Finder**: Discover subdomains associated with a target domain.
3. **Admin Panel Finder**: Locate admin panels on a target website.
4. **Brute Force Attack (Admin Login)**: Perform brute force attacks on admin login pages.
5. **Help & Usage**: Get detailed help and usage instructions.
6. **Exit**: Exit the application.

## Installation

To install WebScanner, clone the repository and install the required dependencies:

```bash
git clone https://github.com/anonwincy/webscanner.git
cd webscanner
pip install -r requirements.txt
```

## Usage

To use WebScanner, run the following command:

```bash
python webscanner.py
```

### Menu Options

Upon running the command, you will be presented with a menu of options:

1. **Web Vulnerability Scanner**: 
    - Scan a website for vulnerabilities:
      ```bash
      python webscanner.py --target http://example.com --mode scan
      ```

2. **Subdomain Finder**: 
    - Find subdomains associated with a target domain:
      ```bash
      python webscanner.py --target example.com --mode subdomain
      ```

3. **Admin Panel Finder**:
    - Locate admin panels on a target website:
      ```bash
      python webscanner.py --target http://example.com --mode find-admin
      ```

4. **Brute Force Attack (Admin Login)**:
    - Perform brute force attacks on admin login pages:
      ```bash
      python webscanner.py --target http://example.com/admin --mode brute-force --threads 10
      ```

5. **Help & Usage**:
    - Get detailed help and usage instructions:
      ```bash
      python webscanner.py --help
      ```

6. **Exit**:
    - Exit the application:
      ```bash
      python webscanner.py --exit
      ```

### Options

- `--target` or `-t`: Specify the target URL or domain.
- `--mode` or `-m`: Specify the mode to use (scan, subdomain, find-admin, brute-force).
- `--path-file` or `-p`: Specify a custom path file for finding admin panels.
- `--threads` or `-th`: Specify the number of threads to use for the operation.
- `--verbose` or `-v`: Enable verbose output.

### Example Commands

Scan a website for vulnerabilities:
```bash
python webscanner.py --target http://example.com --mode scan
```

Find subdomains associated with a target domain:
```bash
python webscanner.py --target example.com --mode subdomain
```

Locate admin panels using a custom path file:
```bash
python webscanner.py --target http://example.com --mode find-admin --path-file paths.txt
```

Perform a brute force attack on an admin login page:
```bash
python webscanner.py --target http://example.com/admin --mode brute-force --threads 10
```

## Contributing

We welcome contributions from the community. Please create a pull request with a detailed description of your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please open an issue on the [GitHub repository](https://github.com/anonwincy/webscanner/issues).

---

Thank you for using WebScanner! If you find this tool useful, please consider giving it a star on GitHub.
```` ▋
