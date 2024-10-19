from flask import Flask, request, render_template, redirect, url_for
import csv
from collections import defaultdict

app = Flask(__name__)

CSV_FILE_PATH = 'C:/Users/Thanusree/OneDrive/Desktop/hi/Best_Performing_Student_Dataset.csv'

# Function to read student data from CSV
def read_student_data():
    student_data = defaultdict(list)
    with open(CSV_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data[row['Batch_Year']].append({
                "Student_ID": row['Student_ID'],
                "Name": row['Name'],
                "GPA": float(row['GPA']) if row['GPA'] else 0.0,
                "Consistency_Score": int(float(row['Consistency_Score'])) if row['Consistency_Score'] else 0,
                "Core_Course_Excellence": int(float(row['Core_Course_Excellence'])) if row['Core_Course_Excellence'] else 0,
                "Hackathons_Participated": int(float(row['Hackathons_Participated'])) if row['Hackathons_Participated'] else 0,
                "Papers_Presented": int(float(row['Papers_Presented'])) if row['Papers_Presented'] else 0,
                "Course_Assistance": int(float(row['Course_Assistance'])) if row['Course_Assistance'] else 0,
                "Overall_Ranking_Score": float(row['Overall_Ranking_Score']) if row['Overall_Ranking_Score'] else 0.0
            })
    return student_data

# Function to add a new student to the CSV file
def add_student_to_csv(student):
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student)

# Load student data initially
student_data = read_student_data()

@app.route('/')
def index():
    # Fetch top 3 students for the default batch (you can change this as needed)
    top_students = get_top_students('2022')  # Default to batch 2022
    return render_template('index.html', top_students=top_students)

@app.route('/calculate', methods=['POST'])
def calculate():
    batch = request.form['batch']
    top_students = get_top_students(batch)
    return render_template('index.html', top_students=top_students)

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    name = request.form['name']
    batch_year = request.form['batch_year']
    gpa = request.form['gpa']
    consistency_score = request.form['consistency_score']
    core_course_excellence = request.form['core_course_excellence']
    hackathons_participated = request.form['hackathons_participated']
    papers_presented = request.form['papers_presented']
    course_assistance = request.form['course_assistance']
    overall_ranking_score = request.form['overall_ranking_score']

    # Create a new student record
    new_student = [
        student_id, name, batch_year, gpa, consistency_score,
        core_course_excellence, hackathons_participated,
        papers_presented, course_assistance, overall_ranking_score
    ]
    
    # Add new student to CSV
    add_student_to_csv(new_student)

    # Redirect to the index to show updated top students
    return redirect(url_for('index'))

def get_top_students(batch):
    # Fetch students for the selected batch and sort by Overall Ranking Score
    if batch in student_data:
        return sorted(student_data[batch], key=lambda x: x['Overall_Ranking_Score'], reverse=True)[:3]
    return []

if __name__ == '__main__':
    app.run(debug=True)
