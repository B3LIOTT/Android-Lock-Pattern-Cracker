# Motivation
I developped this script in order to solve a Root Me challenge.

# Usage
1 - Find the `gesture.key` file in your android system. It might be in `android/data/system`.
2 - Use `attack.py` to crack the lock pattern:
```txt
attack.py [-v] [-p hash ] or [-f file.key ]
-v : verbose mode
-p : hash value in hex
-f : file path, like gesture.key
```

# Example
In this repo, you will find a `gesture.key` file to try this script:
```bash
python attack.py -v -f path/to/android/data/system/gesture.key
```
or without verbose:
```bash
python attack.py -f path/to/android/data/system/gesture.key
```
