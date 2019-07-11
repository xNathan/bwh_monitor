# bwh_monitor

A simple Python script to get Bangwagon VPS data usage.

## Installation

Install dependencies.

```bash
$ pipenv install
```

## Usage

Set your own id and api_key to `.env` file:

```
BWH_ID=YOUR_ID
BWH_API_KEY=YOUR_API_KEY
```

Run with pipenv:

```bash
$ pipenv run python bwh_monitor.py
Loading .env environment variables…
total 1000.0 gb
used 47.72148907929659 gb
```

Fell free to modify anything you want.

## License
[MIT](https://choosealicense.com/licenses/mit/)