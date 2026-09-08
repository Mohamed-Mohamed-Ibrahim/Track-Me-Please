# Track Me Please

### Project Decription

Real-time object tracker that can follow a specific object in a live webcam feed.

### How to install

#### Install Dependencies

###### Global Dependencies

you must have `python` and `pip` available
```bash
pip install -e .
```

###### Virtual Environment (pip)
If you have `venv` available, this is the command to use.

```bash
python -m venv .venv

source .venv/bin/activate       # Linux
.venv\Scripts\activate.bat      # Windows

pip install -e .
```
###### Virtual Environment (uv)

If you have `uv` available, this is the command to use.

```bash
uv sync
```

#### Start Application

```python
python main.py 
```

### References

1. [Main Source](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Intermediate/objectTracking.py)