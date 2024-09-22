# Number Plate Recognition System

A Python-based system for recognizing number plates from video streams using OpenCV and Haar Cascade Classifier.

## Features
- Real-time number plate detection from webcam feed
- Saves detected number plate images
- Uses Haar Cascade Classifier for efficient detection

## Requirements
- Python 3.x
- OpenCV
- Haar Cascade XML file for Russian license plates

## Installation

1. Clone the repository:
   git clone: https://github.com/babulaaldon/Number_PlateRecognition_System

2. Install the required packages:
   `pip install opencv-python`

   
3. Usage

Run the script: python license_number_plate.py

- Press 's' to save a detected number plate image
- Press 'q' to quit the application

## Code Structure

- `license_number_plate.py`: Main script for number plate detection
- `model/haarcascade_russian_plate_number.xml`: Haar Cascade Classifier for Russian license plates



## Acknowledgments

This project uses the Haar Cascade Classifier from OpenCV for number plate detection. 
We acknowledge the contributions of the OpenCV community and the developers of the Haar Cascade Classifier, which were instrumental in making this project possible.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
