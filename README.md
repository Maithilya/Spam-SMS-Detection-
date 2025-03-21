# Spam-SMS-Detector

A Flask-based spam detection application that classifies messages as spam or not spam. The model is trained on the Kaggle SMS Spam dataset and provides a simple web interface for predictions.

## Features
- Train a machine learning model using Kaggle's spam dataset
- Web interface to enter messages and check if they are spam
- Flask backend for handling predictions
- Preprocessing of text data for better accuracy

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Maithilya/Spam-SMS-Detector.git
   cd Spam-SMS-Detector
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download Dataset :
   ```bash
   https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
   ```
## Steps to Run the Project

1 Ensure you have Python installed (preferably Python 3.12 or later).

2 Navigate to the project directory:
 ```bash
cd Spam-SMS-Detector
 ```
3 Run the Flask app:
 ```bash
python Spam-SMS-Detector.py
 ```
4 Open http://127.0.0.1:5000 in your browser.
5 Enter a message in the provided text box and check for spam classification.

## Importance of index.html

The index.html file is crucial as it serves as the front-end interface for users to enter messages and view classification results. Flask uses Jinja2 templating, which requires index.html to be inside a templates/ directory. If the file is missing or placed incorrectly, the application will throw a TemplateNotFound error.

## Common Errors & Fixes
### 1. `TemplateNotFound: index.html`
   **Fix:** Ensure you have an `index.html` file inside a `templates/` folder:
   ```bash
   mkdir templates
   ```
   Then move your `index.html` file inside the `templates/` folder.

### 2. `SystemExit: 1` during Flask run
   **Fix:** Check if another instance of Flask is already running. Stop it using:
   ```bash
   taskkill /F /IM python.exe
   ```
   Then restart the app.

### 3. Flask Debug Mode Restarting Issues
   **Fix:** If Flask keeps restarting or crashing, run it without debug mode:
   ```bash
   python spam_detector.py --no-debug
   ```
(NOTE: everything should be in same folder)

## Future Improvements
- Deploy on a cloud platform (Heroku, Render, or AWS)
- Improve model accuracy with advanced NLP techniques
- Add user authentication for secured access

## Contributing
Feel free to fork this repo and improve the project! If you face any issues, open an issue on GitHub.

---
**Author:** Maithilya Patle 🚀

