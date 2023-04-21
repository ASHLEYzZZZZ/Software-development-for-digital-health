
class Doctor:
    def __init__(self, specialty):
        self.specialty = specialty
        self.logged_in_to_Health_Portal = False



    # potential_symptoms: ("x", "y", "z", "and", "so", "on")

    def diagnosePatient(symptoms):
        if "x" in symptoms:
            print("I believe you suffer from: <insert illness>")
        elif "y" in symptoms:
            print("I thin you have: <insert whatever is the right illness>")
        elif "z" in symptoms:
            print(f"Based on your symptoms being {symptoms}, you seem to suffer from <insert illness>.")
        else:
            print("Luckily, I don't see any signs of serious illness.")

    # example of what to activate the program
    diagnosePatient("x")



    # poential_diagnosis: ("a", "b", "c", "and", "so", "on")

    def prescribeMedication(diagnosis):
        if diagnosis == "a":
            print("You should take some over-the-counter <medication type1> medication.")
        elif diagnosis == "b":
            print("You need to take <medication type2> to treat the infection")
        elif diagnosis == "c":
            print(
                "Go home, make sure to stay warm, and on the way home, stop by the farmacy and get some <medication type3>")
        else:
            print("I'm not sure what the diagnosis is, so I can't prescribe medication yet.")
    # example
    prescribeMedication("b")



    # username is "doctoridxxx"
    # password is "password"

    def login(username, password):
        if username == "doctoridxxx" and password == "password":
            self.logged_in_to_Health_Portal = True
            print("I'm in.")
        else:
            print("Hmm wrong password. I could try again")
    # example
    login("Hopefully the correct username", "aswell as the right password")



    def viewMedicalRecord(patient):
        if self.logged_in_to_Health_Portal:
            print(f"Viewing medical record for {patient}...")
        else:
            print("Please log in first to view medical records.")
    # example
    viewMedicalRecord("patientx")



    def logout(self):
        self.logged_in_to_Health_Portal = False
        print("You have logged out and it was done successfully")