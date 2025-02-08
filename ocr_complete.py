import json
import pytesseract
from page_detection import cleaned_image
from ocr_with_east import detect_localized_text
from word_processing import cleaned_words
import sqlite3

def wrapper(file, localize=False, min_len=3, closest_med=1):
    image = cleaned_image(file)
    
    # If needed, you can localize for scenic images where background is present
    if localize:
        text_from_image = detect_localized_text(image)[1]
    else:
        text_from_image = pytesseract.image_to_string(image)
    
    words_final = cleaned_words(text_from_image, min_len, closest_med)

    # Extract structured fields
    extracted_data = {
        "patient_details": {
            "name": "Extracted Name",  # Placeholder extraction logic
            "dob": "Extracted DOB"
        },
        "treatment_details": {
            "date": "Extracted Date",
            "injection": "Yes/No",
            "exercise_therapy": "Yes/No"
        },
        "difficulty_ratings": {
            "bending": 0,
            "putting_on_shoes": 0,
            "sleeping": 0
        },
        "patient_changes": {
            "since_last_treatment": "Extracted Data",
            "since_start_of_treatment": "Extracted Data",
            "last_3_days": "Good/Bad"
        },
        "pain_symptoms": {
            "pain": 0,
            "numbness": 0,
            "tingling": 0,
            "burning": 0,
            "tightness": 0
        },
        "medical_assistant_inputs": {
            "blood_pressure": "120/80",
            "hr": 72,
            "weight": 70,
            "height": 170,
            "spo2": 98,
            "temperature": 98.6,
            "blood_glucose": 90,
            "respirations": 16
        }
    }

    return json.dumps(extracted_data, indent=4)

def create_database():
    conn = sqlite3.connect("medical_records.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS treatment_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        date TEXT,
        injection TEXT,
        exercise_therapy TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS difficulty_ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        bending INTEGER,
        putting_on_shoes INTEGER,
        sleeping INTEGER,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patient_changes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        since_last_treatment TEXT,
        since_start_of_treatment TEXT,
        last_3_days TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pain_symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        pain INTEGER,
        numbness INTEGER,
        tingling INTEGER,
        burning INTEGER,
        tightness INTEGER,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medical_assistant_inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        blood_pressure TEXT,
        hr INTEGER,
        weight INTEGER,
        height INTEGER,
        spo2 INTEGER,
        temperature REAL,
        blood_glucose INTEGER,
        respirations INTEGER,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS forms_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        form_json TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')
    
    conn.commit()
    conn.close()

def main():
    create_database()
    file = input("Enter Location of image: ")
    json_output = wrapper(file)
    
    with open("extracted_data.json", "w") as f:
        f.write(json_output)
    
    data = json.loads(json_output)
    print(json_output)

if __name__ == '__main__':
    main()

