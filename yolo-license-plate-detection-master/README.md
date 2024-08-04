# yolo-license-plate-detection

License plate detection with Python and yolov3 !

Forked from [this repository](https://github.com/alitourani/yolo-license-plate-detection).

[![Watch the video](https://img.youtube.com/vi/NXjCJZxeaQA/0.jpg)](https://www.youtube.com/watch?v=NXjCJZxeaQA)

## 🔨 Environment

- Python 3.8
- You Only Look Once (YOLO) v.3
- requirements.txt

## execution

You can download the weights file from [this](https://drive.google.com/file/d/1vXjIoRWY0aIpYfhj3TnPUGdmJoHnWaOc/ "this") link.

### Test on a single image:

```
python object_detection_yolo.py --image=bird.jpg
```

### Test on an images directory:

```
python object_detection_yolo.py --image-dir=./image-directory
```

### Test on a single video file:

```
python object_detection_yolo.py --video=cars.mp4
```

### Test on the webcam:

```
python object_detection_yolo.py
```

