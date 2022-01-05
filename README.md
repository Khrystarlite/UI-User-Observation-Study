# UI-User-Observation-Study
A basic User Interface project. A user observation study was done comparing to variations of the same interface to observe the potential difference in usability between discrete and integrated visual feedback. 


### Setup
```
# if using pipenv
pipenv install
# pipenv - for exact versions in pipfile
pipenv sync

# pip - requirements
pip install -r requirements.txt
```

### Dependency Versions
```
OS=Windows 10
python=3.9
tk=

```

### Manual Pyaudio install
If you are  on Windows, you will need to download a different wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install it manually.
```
# Example for Windows 10, python=3.6
pip install PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl

# Example for Ubuntu 20-04
sudo apt install portaudio19-dev  # This is a depenency for pyaudio
pip install pyaudio
```
