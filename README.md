# Track Me Please

---

### Project Decription

Real-time object tracker that can follow a specific object in a live webcam feed.

---

### How to install

#### Install Dependencies

###### Global Dependencies

you must have `python` and `pip` available
```bash
pip install -e .
```
---

###### Virtual Environment (pip)
If you have `venv` available, this is the command to use.

```bash
python -m venv .venv

source .venv/bin/activate       # Linux
.venv\Scripts\activate.bat      # Windows

pip install -e .
```

---

###### Virtual Environment (uv)

If you have `uv` available, this is the command to use.

```bash
uv sync
```

---

#### Start Application

Default: MOsSE

```python
python main.py 
python main.py -a mosse     # the same as above
```

KCF

```python
python main.py -a kcf     
```

CSRT

```python
python main.py -a csrt  
```

---

### Short Implementation Details

- `cv2.legacy.TrackerMOSSE_create()`: store a reference to the tracking within `tracker` 
- `selectROI`: lets the user selects the boundary box 
- `tracker.init`: initialize the tracker
- `cap.read()`: Reading frame from webcam
- `tracker.update`: update the tracker data
- `drawBox`: function to draw the box if the object is tracked successfully
- `cv2.waitKey(1) & 0xFF == ord("q")`: exit application if 


---

### References

1. [Main Source](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Intermediate/objectTracking.py)

---