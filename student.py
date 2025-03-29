import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json
import os

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        
        # Initialize students list
        self.students = []
        self.current_user = None
        
        # Create login screen first
        self.create_login_screen()
    
    def create_login_screen(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Styling
        self.bg_color = "#f5f5f5"
        self.button_color = "#4a7a8c"
        self.text_color = "#333333"
        
        self.root.config(bg=self.bg_color)
        
        # Login Frame
        login_frame = tk.Frame(self.root, bg=self.bg_color)
        login_frame.pack(pady=100)
        
        # Title
        tk.Label(
            login_frame,
            text="Student Management System",
            font=("Helvetica", 20, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Username
        tk.Label(
            login_frame,
            text="Username:",
            bg=self.bg_color,
            font=("Helvetica", 12)
        ).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        self.username_entry = tk.Entry(
            login_frame,
            width=25,
            font=("Helvetica", 12)
        )
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Password
        tk.Label(
            login_frame,
            text="Password:",
            bg=self.bg_color,
            font=("Helvetica", 12)
        ).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        
        self.password_entry = tk.Entry(
            login_frame,
            width=25,
            font=("Helvetica", 12),
            show="*"
        )
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Login Button
        login_button = tk.Button(
            login_frame,
            text="Login",
            command=self.authenticate,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=10
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=20)
    
    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Simple authentication (in real app, use proper authentication)
        if username == "admin" and password == "admin123":
            self.current_user = username
            self.create_main_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def create_main_interface(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        self.header = tk.Label(
            self.root,
            text=f"Student Management System | Logged in as: {self.current_user}",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.header.pack(pady=10)
        
        # Input Frame
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(pady=10)
        
        # Student ID
        tk.Label(
            self.input_frame,
            text="Student ID:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        self.id_entry = tk.Entry(
            self.input_frame,
            width=15,
            font=("Helvetica", 10)
        )
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Name
        tk.Label(
            self.input_frame,
            text="Full Name:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        
        self.name_entry = tk.Entry(
            self.input_frame,
            width=25,
            font=("Helvetica", 10)
        )
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Grade
        tk.Label(
            self.input_frame,
            text="Grade:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        self.grade_entry = tk.Entry(
            self.input_frame,
            width=15,
            font=("Helvetica", 10)
        )
        self.grade_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Email
        tk.Label(
            self.input_frame,
            text="Email:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).grid(row=1, column=2, padx=5, pady=5, sticky="e")
        
        self.email_entry = tk.Entry(
            self.input_frame,
            width=25,
            font=("Helvetica", 10)
        )
        self.email_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # Phone
        tk.Label(
            self.input_frame,
            text="Phone:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        
        self.phone_entry = tk.Entry(
            self.input_frame,
            width=15,
            font=("Helvetica", 10)
        )
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons
        self.add_button = tk.Button(
            self.input_frame,
            text="Add Student",
            command=self.add_student,
            bg="#4a8c5e",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=12
        )
        self.add_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.update_button = tk.Button(
            self.input_frame,
            text="Update",
            command=self.update_student,
            bg="#4a7a8c",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=12
        )
        self.update_button.grid(row=2, column=3, padx=5, pady=5)
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg=self.bg_color)
        search_frame.pack(pady=10)
        
        tk.Label(
            search_frame,
            text="Search:",
            bg=self.bg_color,
            font=("Helvetica", 10)
        ).pack(side="left", padx=5)
        
        self.search_entry = tk.Entry(
            search_frame,
            width=40,
            font=("Helvetica", 10)
        )
        self.search_entry.pack(side="left", padx=5)
        
        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_students,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=10
        )
        search_button.pack(side="left", padx=5)
        
        show_all_button = tk.Button(
            search_frame,
            text="Show All",
            command=self.load_students,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=10
        )
        show_all_button.pack(side="left", padx=5)
        
        # Student Table (Treeview)
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10)
        
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Name", "Grade", "Email", "Phone"),
            show="headings",
            height=15
        )
        
        # Define columns
        self.tree.heading("ID", text="Student ID", anchor="center")
        self.tree.heading("Name", text="Full Name", anchor="center")
        self.tree.heading("Grade", text="Grade", anchor="center")
        self.tree.heading("Email", text="Email", anchor="center")
        self.tree.heading("Phone", text="Phone", anchor="center")
        
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Name", width=200, anchor="center")
        self.tree.column("Grade", width=100, anchor="center")
        self.tree.column("Email", width=200, anchor="center")
        self.tree.column("Phone", width=150, anchor="center")
        
        self.tree.pack(side="left")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Bind selection
        self.tree.bind("<ButtonRelease-1>", self.select_student)
        
        # Action Buttons Frame
        action_frame = tk.Frame(self.root, bg=self.bg_color)
        action_frame.pack(pady=10)
        
        # Delete Button
        delete_button = tk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_student,
            bg="#8c4a4a",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=15
        )
        delete_button.pack(side="left", padx=10)
        
        # Export CSV
        export_csv_button = tk.Button(
            action_frame,
            text="Export to CSV",
            command=self.export_to_csv,
            bg="#4a7a8c",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=15
        )
        export_csv_button.pack(side="left", padx=10)
        
        # Export JSON
        export_json_button = tk.Button(
            action_frame,
            text="Export to JSON",
            command=self.export_to_json,
            bg="#4a7a8c",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=15
        )
        export_json_button.pack(side="left", padx=10)
        
        # Import Button
        import_button = tk.Button(
            action_frame,
            text="Import Data",
            command=self.import_data,
            bg="#4a8c5e",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=15
        )
        import_button.pack(side="left", padx=10)
        
        # Logout Button
        logout_button = tk.Button(
            action_frame,
            text="Logout",
            command=self.create_login_screen,
            bg="#8c7a4a",
            fg="white",
            font=("Helvetica", 10, "bold"),
            width=15
        )
        logout_button.pack(side="left", padx=10)
        
        # Load initial data
        self.load_students()
    
    def add_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        if not student_id or not name:
            messagebox.showerror("Error", "Student ID and Name are required!")
            return
        
        # Check if ID already exists
        for student in self.students:
            if student["id"] == student_id:
                messagebox.showerror("Error", "Student ID already exists!")
                return
        
        student = {
            "id": student_id,
            "name": name,
            "grade": grade,
            "email": email,
            "phone": phone
        }
        
        self.students.append(student)
        self.load_students()
        self.clear_entries()
        messagebox.showinfo("Success", "Student added successfully!")
    
    def select_student(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            student = self.tree.item(selected_item)["values"]
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, student[0])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, student[1])
            self.grade_entry.delete(0, tk.END)
            self.grade_entry.insert(0, student[2])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, student[3])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, student[4])
    
    def update_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected!")
            return
        
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        if not student_id or not name:
            messagebox.showerror("Error", "Student ID and Name are required!")
            return
        
        # Find and update student
        for student in self.students:
            if student["id"] == student_id:
                student["name"] = name
                student["grade"] = grade
                student["email"] = email
                student["phone"] = phone
                break
        
        self.load_students()
        self.clear_entries()
        messagebox.showinfo("Success", "Student updated successfully!")
    
    def delete_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No student selected!")
            return
        
        student_id = self.tree.item(selected_item)["values"][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            self.students = [s for s in self.students if s["id"] != student_id]
            self.load_students()
            self.clear_entries()
    
    def search_students(self):
        query = self.search_entry.get().lower()
        if not query:
            self.load_students()
            return
        
        filtered_students = []
        for student in self.students:
            if (query in student["id"].lower() or 
                query in student["name"].lower() or 
                query in student["grade"].lower() or 
                query in student["email"].lower() or 
                query in student["phone"].lower()):
                filtered_students.append(student)
        
        self.display_students(filtered_students)
    
    def load_students(self):
        self.display_students(self.students)
    
    def display_students(self, students):
        self.tree.delete(*self.tree.get_children())
        for student in students:
            self.tree.insert("", "end", values=(
                student["id"],
                student["name"],
                student["grade"],
                student["email"],
                student["phone"]
            ))
    
    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
    
    def export_to_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Export to CSV"
        )
        
        if file_path:
            try:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Grade", "Email", "Phone"])
                    for student in self.students:
                        writer.writerow([
                            student["id"],
                            student["name"],
                            student["grade"],
                            student["email"],
                            student["phone"]
                        ])
                messagebox.showinfo("Success", "Data exported to CSV successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def export_to_json(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Export to JSON"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    json.dump(self.students, file, indent=4)
                messagebox.showinfo("Success", "Data exported to JSON successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def import_data(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json")],
            title="Import Data"
        )
        
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    with open(file_path, mode='r') as file:
                        reader = csv.DictReader(file)
                        self.students = [row for row in reader]
                elif file_path.endswith('.json'):
                    with open(file_path, 'r') as file:
                        self.students = json.load(file)
                
                self.load_students()
                messagebox.showinfo("Success", "Data imported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
