# PPE Detection System using YOLO

A real-time Personal Protective Equipment (PPE) detection system designed to enhance workplace safety by monitoring compliance with safety gear requirements. This application uses computer vision to detect whether workers are wearing the required safety equipment.

## Features

- Real-time video feed processing
- Detection of multiple PPE items (hard hats, safety vests, etc.)
- Violation alerts and logging
- Simple web interface

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Webcam or video source
- Modern web browser (Chrome, Firefox, Edge, or Safari)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/PPE-Detection-using-YOLO.git
   cd PPE-Detection-using-YOLO
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # OR
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install required packages**
   ```bash
   pip install flask opencv-python numpy
   ```

## Usage

1. **Start the application**
   ```bash
   python backend.py
   ```

2. **Open the application**
   - Open your web browser and navigate to `http://127.0.0.1:5000/`
   - Grant camera access when prompted

3. **Using the application**
   - The system will automatically start detecting PPE compliance
   - Violations will be highlighted in the video feed

## Project Structure

```
PPE-detection/
├── backend.py         # Flask backend server
├── frontend.html      # HTML/JavaScript frontend
├── images/            # Directory for sample/test images
│   └── iocl.jpg      
└── README.md          # This file
```

## Configuration

You can modify the following settings in `backend.py`:
- Camera source (default is 0 for webcam)
- Detection confidence thresholds
- Port number (default: 5000)

## Deployment

For production deployment, consider using:
- Waitress or Gunicorn as the WSGI server
- Nginx as the reverse proxy
- Environment variables for configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/your-username/PPE-Detection-using-YOLO/blob/main/LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [YOLO](https://pjreddie.com/darknet/yolo/)

## Support

For support, please open an issue in the repository or contact the maintainers.
