# PAN-OS EDL Flask

## Synopsis

Fetch a threat intel list with python, parse/validate entries, expose in EDL format via flask

## To use these examples

`panedlflask.py --fqdn --ip <url>`

## Goals

- Ingest a published list, discard all invalid entries
- Process either IPs or FQDNs. Pipeline should be different for either one, e.g.:
  - Ingest Names + IPs as IP list. Resolve Names -> IPs and publish
  - Ingest Names + IPs as FQDN list. Resolve IPs -> Names and publish
  - Ingest URLs as URL list. Validate all URLs are correctly formatted, and publish. *(some logging should be here for un-processed URLs)*

## Testing

TBD

### Dependencies

- Python 3

## TODO

- Moved to project board

## Authors

- *Nick Schmidt*
