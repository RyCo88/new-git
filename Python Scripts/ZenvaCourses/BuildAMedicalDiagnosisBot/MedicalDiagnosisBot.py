'''
Diagnose a user's state of dehydration based on a short questionnaire
    yes or no type questions
    previous responses determine next question
    severe/some/or no dehydration response

retrieve and add dehydration diagnoses
    display a list of patients and diagnoses
    store new diagnoses in the list
'''
'''
1 Run a new diagnosis and store results
2 Display a list of previout patients and diagnosis

How it will work
Text-based program that will run with the Terminal/CMD prompt
1 Display prompt/question
2 Process user text input

Diagnosis Algorithm
Assess Patients General Appearance
    Normal Appearance
        Asses Eyes
            Eyes Normal or Slightly Sunken
                No Dehydration
            Eyes Very Sunken
                Severe Dehydration
    Irratable or Lethargic
        Assess Skin Pinch
            Normal Skin Pinch
                Some Dehydration
            Slow Skin Pinch
                Severe Dehydration

Functions
    Appearance
    Eyes
    Skin
'''
#print('Welcome doctor!','What would you like to do today?')
#name=input('What is your name?\n')
#print(name)
welcome_prompt='Welcome doctor, what would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press "q"\n'
name_prompt="What is the patient's name?\n"
appearance_prompt="How is the patient's general appearance?\n - If normal: press 1\n - If irritable or lethargic: press 2\n"
skin_prompt="How does the patient's skin respond to being pinched?\n - If it reacts normally press 1\n - If it reacts slowly press 2\n"
eye_prompt="How do the patients eyes look?\n - If they look Normal or Slightly Sunken press 1\n - If they look Very Sunken press 2\n"
severe_dehydration="Severe dehydration"
some_dehydration="Some dehydration"
no_dehydration='No dehydration'
patients_and_diagnoses=['Mike - Severe dehydration','Sally - Some dehydration','Kate - No dehydration']
error_message = "Could not save patient and diagnosis due to invalid input"
def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)
def save_new_diagnosis(name,diagnosis):
    if name == '' or diagnosis == '':
        print(error_message)
        return
    final_diagnosis=name+' - '+diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:",final_diagnosis,'\n')
'''
Start a new Diagnosis
    Enter diagnosis mode and capture user information
        Implement the start-diagnosis function
        Store user's name and start questionnaire
ask for appearance
    user input 1 or 2
        if 1
            ask for eye appearance
        if 2
            ask for skin pinch
'''
def assess_eyes(eyes):
    if eyes=='1':
        return no_dehydration
    elif eyes=='2':
        return severe_dehydration
    else:
        print("I'm sorry your response was not recognized")
        return ''
def assess_skin(skin):
    if skin=='1':
        return some_dehydration
    elif skin=='2':
        return severe_dehydration
    else:
        print("I'm sorry your response was not recognized")
        return ''

def diagnose_appearance():
    appearance=input(appearance_prompt)
    if appearance=='1':
        eyes= input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance=='2':
        skin= input(skin_prompt)
        return assess_skin(skin)
    else:
        print("I'm sorry your response was not recognized")
        return ''

def start_new_diagnoses():
    name= input(name_prompt).capitalize()
    diagnosis= diagnose_appearance()
    if diagnosis is not None:
        save_new_diagnosis(name, diagnosis)
    else:
        print("Diagnosis could not be determined.")

def main():
    while True:
        selection=input(welcome_prompt)
        if selection=='1':
            list_patients()
        elif selection=='2':
            start_new_diagnoses()
        elif selection.lower()=='q':
            return False
        else:
            print("I'm sorry your response was not recongnized")
#main()

def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("3") == "")

def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("3") == "")

def test_diagnose_appearance():
    print(diagnose_appearance())

def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("", "No dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "Some dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration",
        "Nimish - Some dehydration"
    ])
#test_save_new_diagnosis()
main()