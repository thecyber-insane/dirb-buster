# Import necessary libraries
import requests
import argparse
from urllib.parse import urlparse

# Function to ensure the URL has a scheme
def enum(url):
    if not urlparse(url).scheme:
        return "http://" + url
    return url

# Function to perform brute-force enumeration
def brute(base_url, wordlist, silent=False):
    # Ensure the base URL has a scheme and ends with '/'
    base_url = enum(base_url)
    if not base_url.endswith('/'):
        base_url += '/'

    # Iterate through each word in the wordlist
    for word in wordlist:
        # Form a URL by appending the word to the base URL
        url = base_url + word.strip()
        
        try:
            # Send an HTTP GET request to the formed URL
            response = requests.get(url, timeout=1)

            # Check if the response corresponds to an available directory
            if response.status_code == 200:
                print(f"Found: {url}")
            elif not silent:  # Print "not found" status only if not in silent mode
                print(f"Not found: {url} (Status Code: {response.status_code})")

        except requests.exceptions.Timeout:
            print(f"Timeout with {url}")

        except requests.ConnectionError:
            print(f"Failed Connection: {url}")

# Function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Simple directory brute-force enumeration tool.")
    parser.add_argument("base_url", help="The base URL to perform enumeration on")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-s", "--silent", action="store_true", help="Silent mode (suppress 'not found' messages)")
    args = parser.parse_args()

    # Read wordlist from the specified file
    with open(args.wordlist, 'r') as wordlist_file:
        wordlist = [line.strip() for line in wordlist_file]

    # Perform brute-force enumeration
    brute(args.base_url, wordlist, silent=args.silent)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
