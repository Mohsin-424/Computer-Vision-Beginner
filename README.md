# Detect and Read Handwritten Words

This is a **handwritten text recognition (HTR) pipeline** that operates on **scanned pages** and applies the following
operations:

* Detect words
* Read words

![example](./doc/example.png)

## Installation

* Go to the root level of the repository (where `setup.py` is located)
* Execute `pip install .`

## Usage

### Run demo

* Additionally install matplotlib for plotting: `pip install matplotlib`
* Go to `scripts/`
* Run `python demo.py`
* The output should look like the plot shown above

### Run web demo (gradio)

* Additionally install gradio: `pip install gradio`
* Go to the root directory of the repository
* Run `python scripts/gradio_demo.py`
* Open the URL shown in the output

![example](./doc/gradio.png)

### Use Python package

Import the function `read_page` to detect and read text.

````python
import cv2
from htr_pipeline import read_page, DetectorConfig, LineClusteringConfig

# read image
img = cv2.imread('data/sample_1.png', cv2.IMREAD_GRAYSCALE)

# detect and read text
read_lines = read_page(img, 
                       DetectorConfig(scale=0.4, margin=5), 
                       line_clustering_config=LineClusteringConfig(min_words_per_line=2))

# output text
for read_line in read_lines:
    print(' '.join(read_word.text for read_word in read_line))
````

