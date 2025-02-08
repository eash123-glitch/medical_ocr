Medical Records OCR Extraction and Storage System
==================================================

Overview:
----------
This script extracts text from medical records using OCR and organizes it into structured fields. 
The extracted data is stored in both JSON format and an SQLite database for further processing and analysis.

Functionalities:
-----------------
1. **OCR Processing**:
   - Uses Tesseract OCR and EAST text detection to extract text from images.
   - Cleans and processes extracted text to identify relevant medical data.

2. **Data Extraction**:
   - Extracts structured fields such as:
     - Patient Details (Name, DOB)
     - Treatment Details (Date, Injection, Exercise Therapy)
     - Difficulty Ratings (0-5) for various activities
     - Patient Changes (Since Last Treatment, Since Start, Last 3 Days)
     - Pain Symptoms (0-10) for different sensations
     - Medical Assistant (MA) Inputs (Vitals such as BP, HR, Weight, etc.)

3. **Database Storage**:
   - SQLite database is created to store extracted patient data in structured tables:
     - `patients`: Stores general patient details.
     - `treatment_details`: Stores treatment history.
     - `difficulty_ratings`: Tracks patient difficulty ratings.
     - `patient_changes`: Stores updates about patient progress.
     - `pain_symptoms`: Stores patient pain-related information.
     - `medical_assistant_inputs`: Stores medical assistant observations.
     - `forms_data`: Stores extracted JSON for flexible querying.

4. **Saving JSON Output**:
   - Extracted data is saved into `extracted_data.json` for external usage.

Usage:
------
1. Run the script and provide an image file location when prompted.
2. The script will process the image, extract relevant details, and save them.
3. The extracted data is stored in both JSON format and the SQLite database.

Prerequisites:
--------------
- Python 3.x
- Required Libraries:
  - `pytesseract`
  - `opencv-python`
  - `numpy`
  - `sqlite3`
  - `json`
  
Installation:
-------------
Ensure you have the required dependencies installed using:
```sh
pip install opencv-python numpy pytesseract
```

Execution:
----------
add the path to the image and run the script using:
```sh
python ocr_complete.py
```
