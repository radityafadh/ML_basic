import pandas as pd
import json

# Function to read JS files and extract the array data
def read_js_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Extract the array portion (between [ and ])
        array_start = content.find('[')
        array_end = content.rfind(']') + 1
        array_content = content[array_start:array_end]
        # Parse as JSON
        return json.loads(array_content)

# Read all the JS files
courses = read_js_file('courses.js')
students = read_js_file('students.js')
enrollments = read_js_file('enrollments.js')
departments = read_js_file('departments.js')
faculty = read_js_file('faculty.js')

# Convert to pandas DataFrames
courses_df = pd.DataFrame(courses)
students_df = pd.DataFrame(students)
enrollments_df = pd.DataFrame(enrollments)
departments_df = pd.DataFrame(departments)
faculty_df = pd.DataFrame(faculty)

# First, merge students with their department information
students_with_dept = pd.merge(
    students_df, 
    departments_df, 
    on='department_id', 
    how='left'
).rename(columns={'department_name': 'student_department'})

# Merge faculty with their department information
faculty_with_dept = pd.merge(
    faculty_df, 
    departments_df, 
    on='department_id', 
    how='left'
).rename(columns={'department_name': 'faculty_department', 'name': 'faculty_name'})

# Merge courses with faculty information first
courses_with_faculty = pd.merge(
    courses_df,
    faculty_with_dept[['faculty_id', 'faculty_name', 'faculty_department']],
    on='faculty_id',
    how='left'
)

# Then merge with department information for the course
courses_with_info = pd.merge(
    courses_with_faculty,
    departments_df,
    left_on='department_id',
    right_on='department_id',
    how='left'
).rename(columns={'department_name': 'course_department'})

# Now merge enrollments with student information
combined = pd.merge(
    enrollments_df,
    students_with_dept,
    on='student_id',
    how='left'
)

# Finally merge with course information
combined = pd.merge(
    combined,
    courses_with_info,
    on='course_id',
    how='left'
)

# Reorder columns for better readability
column_order = [
    'enrollment_id', 'student_id', 'name', 'age', 'gender', 
    'enrollment_year', 'gpa', 'student_department',
    'course_id', 'course_name', 'credits', 'course_department',
    'faculty_id', 'faculty_name', 'faculty_department',
    'grade'
]

combined = combined[column_order]

# Display the first few rows to verify
print(combined.head())

# Optionally save to CSV
combined.to_csv('combined_data.csv', index=False)