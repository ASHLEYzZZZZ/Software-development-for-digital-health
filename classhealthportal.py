
class Health_Portal:

    def __init__(self):
        self.Medications = ("from", "a", "to", "z")
        self.LabResults = {patient1:"x", patinet2:"y", patient3:"z"}
        self.Diagnosis = {patient1:"x", patient2:"y", patient3:"z"}



    def storeInfoAboutPatientsMedicalRecord(self, medications, lab_results, diagnosis):
        self.Medications = medications
        self.LabResults = lab_results
        self.Diagnosis = diagnosis



    from classdoctor import classdoctor

    def verifyLogin(username, password):
         if username == "doctoridxxx" and password == "password":
            self.logged_in_to_Health_Portal = True
            print("Logged in successfully.")
         else:
            print("Login failed. Please try again.")
    #example
    login("","")



    def provideInfoAboutPatient(self):
        if not self.logged_in_to_Health_Portal:
            print("Access denied. Please log in.")
            return
        return {'Medications': self.Medications, 'LabResults': self.LabResults, 'Diagnosis': self.Diagnosis}
