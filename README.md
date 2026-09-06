# Proxy Aggregator from GitHub Raw Lists

This project automatically collects free proxy servers from dozens of public GitHub repositories that maintain proxy lists. It parses raw text files, normalizes entries by protocol, removes duplicates, and outputs clean lists for HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.

## Features

- Aggregates proxies from 40+ GitHub raw sources per protocol.
- Supports HTTP, HTTPS, SOCKS4, and SOCKS5.
- Automatically strips protocol prefixes from raw data and adds the correct one.
- Uses randomized HTTP headers and timeouts to avoid blocking.
- Deduplicates all proxies and saves them into separate protocol files + a combined `all.txt`.
- Lightweight and easy to extend.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/just-not-google/full-free-proxy.git
   cd proxy-aggregator
   ```

2. Install required Python packages:
   ```bash
   pip install requests
   ```

## Usage

Run the main script:
```bash
python -m github_raw
```

This will:
- Fetch all proxy lists from the URLs defined in `github_raw_url_list.py`.
- Process each line, removing any existing protocol prefixes and adding the target protocol.
- Write unique proxies to `http.txt`, `https.txt`, `socks4.txt`, `socks5.txt`.
- Write all unique proxies (regardless of protocol) to `all.txt`.

## Project Structure

```
├── parsers/
│   ├── __init__.py
│   ├── github_raw_url_list.py     # Contains all GitHub raw URLs grouped by protocol
│   ├── template_requests.py       # HTTP request handler with random headers/timeouts
│   └── data/
│       ├── __init__.py            # Exports constants
│       ├── header_list.py         # List of realistic browser headers
│       ├── main_constants.py      # Timeout ranges
│       ├── protocols.py           # Protocol string constants
│       ├── protocol_names.py      # Mapping protocol -> output filename
│       └── replace_proxy.py       # Controls whether to strip prefixes (always True)
├── github_raw.py                  # Main logic: fetch and process lists
```

## Configuration

- **Add or remove sources**: Edit `github_raw_url_list.py` – each key is a protocol (`HTTP_PROTOCOL`, etc.), and the value is a list of raw GitHub URLs.
- **Change output filenames**: Modify `protocol_names.py`.
- **Adjust timeouts**: Change `MIN_TIMEOUT` and `MAX_TIMEOUT` in `main_constants.py`.
- **Disable prefix replacement**: Set `REPLACE_PROXY[protocol] = False` in `replace_proxy.py`.

## Output Files

After execution, the following files will be created in the project root:
- `http.txt`   – HTTP proxies (format: `http://ip:port`)
- `https.txt`  – HTTPS proxies (`https://ip:port`)
- `socks4.txt` – SOCKS4 proxies (`socks4://ip:port`)
- `socks5.txt` – SOCKS5 proxies (`socks5://ip:port`)
- `all.txt`    – All unique proxies from all protocols, sorted.

Each file contains one proxy per line.

## Dependencies

- Python 3.6+
- `requests` library

## License

This project is licensed under the MIT License – feel free to use and modify it for your own needs.

> **Note:** The proxy lists are fetched from third‑party repositories; availability and quality depend on those sources. The script does not validate proxy responsiveness.
