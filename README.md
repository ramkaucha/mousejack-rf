# MouseJack Wireless Security Analysis

This project investigates RF security in Logitech wireless devices using the Yard Stick One and RFCat. It evaluates whether MouseJack-style attacks are still possible on modern devices (2023+).

## Summary

- Was able to successfully capture encrypted RF packets
- Could not inject keystrokes.
- Modern Logitech devices us AES

## Key Scripts

- `observe.py` – RF packet capture
- `channel_check.py` - Checks mice frequency
- `jammer.py` – RF jamming attempts
- `observe_entropy.py` – Entropy analysis
- `detect_packet_repetition.py` – Checks for packet repetition

## Requirements

- Yard Stick One
- Python 3
- Linux (Fedora tested)

## .env

Use the provided env

```bash
source rfcat-env/bin/activate`
```
