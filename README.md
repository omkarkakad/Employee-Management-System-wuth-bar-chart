# Employee-Management-System-wuth-bar-chart
This is a GUI-based Employee Management System built using Python’s Tkinter library for the frontend and MongoDB for the backend database. The application allows users to add, view, update, delete, and visualize employee records, making it a complete CRUD-based desktop system ideal for small to mid-level HR management workflows.
🚀 Features
🔹 Add Employee
Takes Employee ID, Name, Email, Position, and Salary.

Validates all fields including email format and salary constraints.

Prevents duplicate ID entries using MongoDB lookups.

🔹 View Employees
Displays all employee records in a neatly formatted scrollable text area.

Pulls real-time data from the MongoDB database.

🔹 Update Records
Allows editing employee details by ID.

Performs field-wise validation before update.

Checks for valid IDs before processing.

🔹 Delete Employee
Deletes a specific employee based on the entered ID.

Confirmation messages on success or failure.

📊 Charts
Uses Matplotlib to display a bar chart of Top 5 Highest Salaried Employees.

Visual representation includes value labels, colors, and styling for better insights.

📂 Tech Stack
Frontend: Python Tkinter

Backend: MongoDB (Localhost)

Libraries: Pymongo, Matplotlib, Pandas, Regex, ScrolledText

✅ Validations & UX
Email Validation using regex

Salary Check (must be positive)

Duplicate ID Prevention

Error Messages for invalid inputs and exceptions

Proper Exception Handling for database and input errors

Safe window closing protocols for all sub-windows

🧠 Learning Outcome
This project strengthened my skills in GUI development, NoSQL databases, data validation, and data visualization. I understood the importance of user-friendly interfaces and robust backend interaction in real-world applications.

📎 Note
To run this project, ensure MongoDB is installed and running locally at localhost:27017. The database name used is emp_22june25.

