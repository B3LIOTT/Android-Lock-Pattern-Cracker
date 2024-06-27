# Motivation
I developped this script in order to solve a Root Me challenge.

# Requirements
Use `requirements.txt` to install requirements:
```txt
contourpy==1.2.1
cycler==0.12.1
fonttools==4.53.0
kiwisolver==1.4.5
matplotlib==3.9.0
networkx==3.3
numpy==2.0.0
packaging==24.1
pillow==10.3.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
six==1.16.0
tqdm==4.66.4
```
with: 
```bash
pip intall -r requirements.txt
```

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
