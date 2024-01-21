# TCIdirbuster.py

`TCIdirbuster.py` is a simple command-line tool for performing directory brute-force enumeration on a specified base URL using a provided wordlist. The script uses the `requests` library to send HTTP GET requests to different paths formed by combining the base URL and words from the wordlist. It then prints whether each path is found (HTTP status code 200) or if the path is not found along with the corresponding status code.

## Features

- **Base URL Enumeration:** The script forms URLs by combining the base URL with paths from the wordlist.
- **HTTP Status Code Handling:** It prints whether a path is found (HTTP status code 200) or if the path is not found.
- **Silent Mode:** Optionally, the script can run in silent mode to suppress 'not found' messages.

## Usage

```bash
python TCIdirbuster.py http://example.com --wordlist wordlist.txt [-s]
```

- `http://example.com`: The base URL to perform enumeration on.
- `--wordlist wordlist.txt`: Path to the wordlist file containing paths or filenames.
- `[-s]` or `[--silent]`: Optional flag for silent mode (suppress 'not found' messages).

## Example

```bash
python TCIdirbuster.py http://example.com --wordlist wordlist.txt
```

This command will perform directory brute-force enumeration on `http://example.com` using the wordlist from `wordlist.txt`.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)

## Acknowledgments

- The script utilizes the `requests` library for HTTP requests.

## Contribution

Contributions are welcome! Please feel free to open issues or submit pull requests.
