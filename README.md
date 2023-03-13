# BrightnessClamp
## What's this?
A little test on how to "restore" image readability by using all of the color space up (0-255) grayscale.

## Demo
### Before
![Before (You can't see anything)](https://raw.githubusercontent.com/BillPlayzToday/BrightnessClamp/main/test.jpeg)
### After
![After (You can recognize stuff)](https://raw.githubusercontent.com/BillPlayzToday/BrightnessClamp/main/test-clamped.jpeg)
![After (with annotations)](https://raw.githubusercontent.com/BillPlayzToday/BrightnessClamp/main/test-annotated.jpeg)
By the way: image was taken from a [SurveillancePi](https://github.com/BillPlayzToday/SurveillancePi) Raspberry Pi Camera System.

## Installation
You will need to install Pillow (PIL fork) like [this](https://pillow.readthedocs.io/en/stable/installation.html) and clone the repository to your computer.

## Usage
Then execute the python script with the input image path as an argument:

    python3 main.py image.jpg

Supports all the formats that Pillow supports. Transparency should be avoided.
The output file should be available at ***image*-clamped.jpeg**.
