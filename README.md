# AI-Based-Fire-Alarm-System

This repository contains an AI-Based Fire Detection Alarm System that uses machine learning to detect fire. The system displays the status of fire detection in real-time and alerts users accordingly.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The AI-Based Fire Detection Alarm System uses a machine learning model to detect fire through a camera feed. The system updates the status in real-time on a web interface, indicating whether fire is detected or not. This project aims to provide an early warning system to prevent fire-related accidents.

## Features

- Real-time fire detection using a machine learning model.
- Web interface displaying the status of fire detection.
- Visual and color-coded alert system (green for normal conditions, red for fire detected).
- Aesthetic and user-friendly interface.
- Footer with social media links for easy contact.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/astromanu007/AI-Based-Fire-Alarm-System.git
    cd AI-Based-Fire-Alarm-System
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the necessary machine learning model and place it in the appropriate directory.**

## Usage

1. **Start the web server:**
    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**
    ```bash
    http://localhost:5000
    ```

3. The web interface will display the status of fire detection. If fire is detected, the status box will turn red; otherwise, it will remain green.

## Project Structure

- `app.py`: Main application script to run the web server.
- `static/`: Directory containing static files (CSS, images, etc.).
- `templates/`: Directory containing HTML templates.
- `model/`: Directory for the machine learning model and related files.

```
/project-directory
├── app.py                   # Flask application file
├── templates                # HTML templates directory
│   └── index.html           # Main HTML template
└── static                   # Static assets directory
    ├── images.jpg           # Background image for the web page
    ├── linkedin.png         # LinkedIn logo (example)
    ├── 1.jpg           # GitHub logo (example)
    ├── 2.png          # Twitter logo (example)
    └── 3.jpg          # Instagram logo (example)


```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by Manish Dhatrak
