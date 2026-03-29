# XSS Payload Tester

## Description
A Python-based tool to test Cross-Site Scripting (XSS) vulnerabilities by injecting payloads into web application inputs.

## Features
- Tests multiple XSS payloads
- Detects reflected XSS vulnerabilities
- Simple and easy to use

## Tools Used
- Python
- Requests library

## Usage
1. Run the script:
   python xss_tester.py

2. Enter a URL with parameter:
   Example: http://testphp.vulnweb.com/search.php?test=

3. The tool will test for XSS vulnerabilities.

## Sample Payloads
- <script>alert(1)</script>
- <img src=x onerror=alert(1)>

## Disclaimer
This tool is for educational purposes only. Use only on authorized systems.
