***

# pyscan-core

**A minimal Python tool for understanding TCP connect scanning and basic service interaction.**

> *Note: This is a basic learning tool, not a production-grade scanner.*

## Overview

pyscan-core is a lightweight Python script designed to demonstrate fundamental network reconnaissance concepts using standard socket operations. It provides:

- **DNS Resolution**: Converts domain names to IP addresses
- **TCP Port Scanning**: Identifies open TCP ports via connect scans
- **Banner Grabbing**: Captures service identification banners from open ports

The tool intentionally prioritizes clarity and correctness over speed or coverage.

## How It Works

### DNS Resolution
Utilizes `socket.gethostbyname()` for domain-to-IP resolution with graceful error handling for invalid domains.
IPv4-only resolution is used intentionally to keep behavior explicit and predictable.

### TCP Port Scanning
Implements TCP Connect Scanning using `socket.connect_ex()`:
- Completes full TCP three-way handshake
- Returns success (0) for open ports
- Configurable timeouts prevent indefinite blocking
- Sequential scanning is used to keep execution flow simple and avoid masking network behavior with concurrency

### Banner Grabbing
- Reads initial service responses from open ports
- Sends minimal HTTP HEAD request for port 80 services
- Limitation: Does not support encrypted protocols (HTTPS/TLS)
- Banner grabbing is inherently unreliable and depends on server-side behavior

## Usage

```bash
python scanner.py <target-ip-or-domain>
```

## Example

```bash
$ python scanner.py example.com
```

Output may vary depending on target configuration; absence of banners does not imply closed or inactive services.

## Limitations

| Feature | Status |
|---------|--------|
| UDP Scanning | Not supported |
| TLS/SSL Handling | Cleartext only |
| OS Fingerprinting | Not implemented |
| Parallel Scanning | Sequential only |
| Stealth Capabilities | Not a design goal |

## Legal and Ethical Notice

- **Educational Purpose Only**: Designed for protocol learning and authorized testing
- **Authorization Mandatory**: Only scan networks you own or have explicit written permission to test
- **Legal Compliance**: Unauthorized scanning may violate computer fraud laws

This tool is provided for educational purposes. The author assumes no liability for misuse. Users are responsible for ensuring compliance with all applicable laws and obtaining proper authorization before use.
