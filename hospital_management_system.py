import json
import os

# ------------ MODELS ------------ #

class Doctor:
    def __init__(self, id, name, specialization, schedule):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.schedule = schedule

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "schedule": self.schedule
        }

class Patient:
    def __init__(self, id, name, age, symptoms):
        self.id = id
        self.name = name
        self.age = age
        self.symptoms = symptoms

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "symptoms": self.symptoms
        }

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date": self.date,
            "time": self.time
        }

# ------------ DATA HANDLERS ------------ #

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# ------------ CORE FUNCTIONS ------------ #

def add_doctor():
    id = input("Doctor ID: ")
    name = input("Name: ")
    specialization = input("Specialization: ")
    schedule = input("Schedule (e.g., 10AM-2PM): ")

    doctor = Doctor(id, name, specialization, schedule)
    doctors = load_data("doctors.json")
    doctors.append(doctor.to_dict())
    save_data("doctors.json", doctors)
    print("✅ Doctor added successfully!")

def view_doctors():
    doctors = load_data("doctors.json")
    if not doctors:
        print("No doctors found.")
        return
    print("\n--- Doctor List ---")
    for doc in doctors:
        print(f"ID: {doc['id']} | Name: {doc['name']} | Specialty: {doc['specialization']} | Schedule: {doc['schedule']}")

def add_patient():
    id = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    symptoms = input("Symptoms: ")

    patient = Patient(id, name, age, symptoms)
    patients = load_data("patients.json")
    patients.append(patient.to_dict())
    save_data("patients.json", patients)
    print("✅ Patient added successfully!")

def view_patients():
    patients = load_data("patients.json")
    if not patients:
        print("No patients found.")
        return
    print("\n--- Patient List ---")
    for pat in patients:
        print(f"ID: {pat['id']} | Name: {pat['name']} | Age: {pat['age']} | Symptoms: {pat['symptoms']}")

def book_appointment():
    patient_id = input("Patient ID: ")
    doctor_id = input("Doctor ID: ")
    date = input("Appointment Date (YYYY-MM-DD): ")
    time = input("Appointment Time (e.g., 11:00 AM): ")

    appointment = Appointment(patient_id, doctor_id, date, time)
    appointments = load_data("appointments.json")
    appointments.append(appointment.to_dict())
    save_data("appointments.json", appointments)
    print("✅ Appointment booked successfully!")

def view_appointments():
    appointments = load_data("appointments.json")
    if not appointments:
        print("No appointments found.")
        return
    print("\n--- Appointments ---")
    for app in appointments:
        print(f"Patient ID: {app['patient_id']} | Doctor ID: {app['doctor_id']} | Date: {app['date']} | Time: {app['time']}")

# ------------ MAIN MENU ------------ #

def main():
    while True:
        print("\n======= Hospital Management System =======")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Add Patient")
        print("4. View Patients")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_doctor()
        elif choice == "2":
            view_doctors()
        elif choice == "3":
            add_patient()
        elif choice == "4":
            view_patients()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            print("Exiting system... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
