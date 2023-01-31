# **Python Detector**
![Mediapipe](https://mediapipe.dev/images/mobile/pose_tracking_example.gif)

---
# **Important information📌:**

This program cannot run on linux subsystem terminals, such as WSL2, or WSL. It can be done, but it's many more complicated steps. I leave more information obtained in [Stackoverflow](https://stackoverflow.com/questions/65939167/problem-using-opencv-in-wsl-when-opening-windows) in case you want to try.

---
<details><summary>FACE DETECTOR APP: 🧔</summary>

# **Face Analyzer**
Face Analyzer. It recognizes faces shown on camera, analyzing features and coloring a box when it has detected a face. This program was made with [OpenCV](https://docs.opencv.org/4.x/)

[![example-img](https://pbs.twimg.com/media/FnmrU-MWAAEjm8U?format=jpg&name=large)](https://twitter.com/AndyDollin21)

---
## First Steps:

* Created Virtual environment

<details><summary>FOR LINUX DISTRO:</summary>


```
python3 -m venv venv 
```
* Activate Virtual Environment:

```
source venv/bin/activate
```
* Install Requirements via PIP:

```
pip install -r requirements.txt
```
</details>

---

<details><summary>FOR WINDOWS DISTRO:</summary>


```
python -m virtualenv venv 
```
* Activate Virtual Environment:

```
.\venv\Scripts\activate
```
* Install Requirements via PIP:

```
pip install -r requirements.txt
```
</details>

---

## Start the App:


```
python3 face-view.py
```
</details>

---
<details><summary>HANDS DETECTOR APP: 🖖</summary>

# **Hands Detector**
Hands Detector is a program that uses a machine learning model to analyze the camera frames and detect hands. This program was made with [OpenCV](https://docs.opencv.org/4.x/) and [MediaPipe](https://mediapipe.dev/)

[![example2-img](https://pbs.twimg.com/media/Fn1dbXUXEAQW60y?format=jpg&name=large)](https://twitter.com/AndyDollin21)

---
## First Steps:

* Created Virtual environment

<details><summary>FOR LINUX DISTRO:</summary>


```
python3 -m venv venv 
```
* Activate Virtual Environment:

```
source venv/bin/activate
```
* Install Requirements via PIP:

```
pip install -r requirements.txt
```
</details>

---

<details><summary>FOR WINDOWS DISTRO:</summary>


```
python -m virtualenv venv 
```
* Activate Virtual Environment:

```
.\venv\Scripts\activate
```
* Install Requirements via PIP:

```
pip install -r requirements.txt
```
</details>

---

## Start the App:


```
python3 hands_detector.py
```
</details>


--- 

## PROBLEMS?

> If you have issues, please init [issues](https://github.com/Cervantes21/Face-Analyzer/issues) with all detail for examine. Thanks.
