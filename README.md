# Prepare speech

Transliterates data from english to russian language. Also provides transliterated values of numbers.

## Getting Started

Clone content of repository to separate directory, install dependencies, run script providing data for transliteration
to stdin or file. Output will be placed to sys.stdout or file.  

Example: 
```bash
python3 prepare_speech.py -f speech.txt -o transliterated_speech.txt
```

### Prerequisites

```
python3
pip3
```

### Installing
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r dependencies.txt
```
## Running the tests

```bash
python3 tests.py
```

## License

This project is licensed under the MIT License.
