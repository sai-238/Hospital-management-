import os
import csv
print("-"*60)
print("\t\t\t\tWELCOME TO SRET HOSPITAL")
print("-"*60)
class LoginError(Exception):
    def Wrong(self):
        print("\n\n----------------wrong Username or password----------------")
while True:
    try:
        user=input("\n\t\t\t\tUserName: ")
        password=input("\n\t\t\t\tpassword: ")
        if(user=="admin" and password=="SRET"):
            print("\n\n----------------login sucessful-----------------\n\n\t\t\t\tWELCOME DOCTOR")
            break
        else:
            raise LoginError

    except LoginError as s:
        s.Wrong()
while True:    
    print("\n\t\tMENU\n")
    print("1.ADD PATIENT DEITAILS \n2.DISPLAY THE FULL TABLE\n3.SEARCH THE PATIENT DETAILS\n4.DELETE THE PATIENT DETAILS\n5.EXIT")
    ch=int(input("\nEnter The  choice:"))
    if(ch==1):
        class Patient:
        # constructor to initialize instance variables
            def __init__(self,pid, name, age,gen, bg, ht, wt,cn):
                self.setDetails(pid,name, age,gen, bg, ht, wt,cn)
            def Setpid(self,pid):
                self.pid=pid
            # setter for the name
            def setName(self, name):
                self.name = name

            # setter for the age
            def setAge(self, age):
                self.age = age
            # setter for the Gender
            def setGender(self,gen):
                self.gen = gen

            # setter for the blood group
            def setBloodGroup(self, bg):
                self.bg = bg

            # setter for the height
            def setHeight(self, ht):
                self.ht = ht

            # setter for the weight
            def setWeight(self, wt):
                self.wt = wt
            # setter for the Contact no
            def setCN(self,cn):
                self.cn=cn
            #setter for disease
            def setDisease(self,dis):
                self.dis=dis
            # setter for all instance variables
            def setDetails(self,pid, name, age, gen,bg, ht, wt,cn):
                self.Setpid(pid)
                self.setName(name)
                self.setAge(age)
                self.setGender(gen)
                self.setBloodGroup(bg)
                self.setHeight(ht)
                self.setWeight(wt)
                self.setCN(cn)
            # getter for all instance variables
            def getDetails(self):
                return (self.pid,self.name, self.age,self.gen, self.bg, self.ht, self.wt,self.cn,dis,tst,sym)


        # driver code
        if __name__ == "__main__":
        # take user input for patient info
            print("\nEnter patient details\n")
            patient_pid = int(input("Enter Patient ID:"))
            patient_name = input("Enter Name: ")
            patient_age = int(input("Enter Age: "))
            patient_gen=input("Enter Gender:")
            patient_bg = input("Enter blood group: ")
            patient_ht = int(input("Enter Height: "))
            patient_wt = int(input("Enter Weight: "))
            patient_cn=int(input("Enter Contact No:"))
            p = Patient(patient_pid,patient_name, patient_age,patient_gen, patient_bg, patient_ht, patient_wt,patient_cn)


        print("\n\tChoose The Symptoms Of The Patient From The Following\n")
        print("\n\tGeneral: \n\n01)	Breathlessness or difficulty in breathing \n02)	Dyspnea(shortness of breath)  \n03)	High pitched breathing\n04)	Fever\n05)	Weakness\n06)	extreme tiredness\n07)	Weight loss\n08)	Chills\n09)	Lowering of blood pressure\n10)	Sudden drop in blood pressure\n11)	Severe pain\n12)	Low cholesterol level\n13)	Nausea and vomiting\n14)	Loss of consciousness\n15)	Altered level of consciousness\n16)	Altered mental state\n17)	Loss of sensation\n18)	Back pain\n19)	Internal bleeding\n20)	Flank pain and tenderness\n21)	Numbness\n22)	Seizures\n23)	Stroke\n24)	Sudden growth\n25)	Clammy skin or sweaty skin\n26)	Melanomas\n27)	Clot bursting\n28)	Thrombosis\n29)	Tear in inner line of the vessel\n30)	Blood leak in between layers of walls\n31)	Signs of hypovolemic shock\n32)	Sense of impending doom\n33)	Painful mass in an extremity\n34)	Constant pain\n35)	Fainting\n\n\tHead:\n\n36)	Head ache\n37)	Pain in jaw\n38)	Pain above and behind eye\n39)	Blurred/Double vision\n40)	Sudden loss of vision(focal paralysis)\n41)	Focal neurological deficits\n42)	Sub hyaloid retinal haemorrhage\n43)	Anisocoria(eye)\n44)	Nystagmus(eye)\n45)	Trouble speaking\n46)	Intracerebral haemorrhage\n\n\tNeck:\n\n47)	pain in neck\n48)	Coughing\n49)	Swelling in neck\n50)	Hoarseness( harsh, raspy, or strained voice)\n51)	Nuchal rigidity\n\n\tUpper body:\n\n52)	Chest pain\n53)	Rapid heart rate\n54)	frequent palpitation(heart beat)\n55)	Hypertension (heart)\n56)	Cardiac arrhythmia\n57)	Pain in upper back\n58)	Pain in abdomen\n59)	Abdominal heart Rhythm\n60)	Pulse near belly pain\n61)	Swelling in  abdomen\n\n\tLower body:\n\n62)	Pain in pelvis/legs/buttock\n63)	Pain behind the knees\n64)	Edema in low leg\n65)	Reduced kidney function\n66)	Haematuria\n67)	Foot pain\n68)	Swelling in ankle and legs\n69)	Discoloured toe\n70)	Ulcer on the skin of the feet that don’t heal")
        possible_test=["none","MRI","MRA","BLOOD TEST","DSA","ECHOCARDIOGRAM","CT","X-RAY","ULTRASOUND","ANGIOGRAM"]
        symptoms_list = [[68 ,59, 61, 54], [52, 54, 14 ,2], [52, 1], [37, 47, 57, 48], [49, 50, 13, 3], [18, 60, 53,14], [21, 38, 45, 39], [30, 36], [57, 23, 40], [46, 23, 40, 17], [4, 16, 22, 33], [63, 64, 67, 70], [20, 55, 65, 27], [51, 56, 44, 41], [28, 24, 26], [35, 67, 68, 69], [11, 19, 10], [29]]
        disease = ["Ventricular aneurysm", "Aneurysm of sinus of Valsalva", "Aneurysm following cardiac surgery", "Aortic aneurysm", "Thoracic aneurysm", "Abdominal aneurysm", "Berry aneurysm", "Fusiform aneurysm", "Dissecting aneurysm", "Charcot–Bouchard aneurysms", "Mycotic aneurysm", "Popliteal aneurysm", "Renal aneurysm", "Intraparenchymal aneurysm", "Capillary aneurysm", "Peripheral aneurysm", "Visceral aneurysm", "Pseudo aneurysm"]
        symptoms = []
        while True:
                    inp = input("\nEnter the symptoms (exit to end): ")
                    if inp.lower() == "exit":
                        break
                    else:
                        symptoms.append(int(inp))
        possible_symptoms=["NONE",
                    "Breathlessness or difficulty in breathing",
                    "Dyspnea(shortness of breath)",
                    "High pitched breathing",
                    "Fever",
                    "Weakness",
                    "extreme tiredness",
                    "Weight loss",
                    "Chills",
                    "Lowering of blood pressure",
                    "Sudden drop in blood pressure",
                    "Severe pain",
                    "Low cholesterol level",
                    "Nausea and vomiting",
                    "Loss of consciousness",
                    "Altered level of consciousness",
                    "Altered mental state",
                    "Loss of sensation",
                    "Back pain",
                    "Internal bleeding",
                    "Flank pain and tenderness",
                    "Numbness",
                    "Seizures",
                    "Stroke",
                    "Sudden growth",
                    "Clammy skin or sweaty skin",
                    "Melanomas",
                    "Clot bursting",
                    "Thrombosis",
                    "Tear in inner line of the vessel",
                    "Blood leak in between layers of walls",
                    "Signs of hypovolemic shock",
                    "Sense of impending doom",
                    "Painful mass in an extremity",
                    "Constant pain",
                    "Fainting",
                    "Head ache",
                    "Pain in jaw",
                    "Pain above and behind eye",
                    "Blurred/Double vision",
                    "Sudden loss of vision(focal paralysis)",
                    "Focal neurological deficits",
                    "Sub hyaloid retinal haemorrhage",
                    "Anisocoria(eye)",
                    "Nystagmus(eye)",
                    "Trouble speaking",
                    "Intracerebral haemorrhage",
                    "pain in neck",
                    "Coughing",
                    "Swelling in neck",
                    "Hoarseness( harsh, raspy, or strained voice)",
                    "Nuchal rigidity",
                    "Chest pain",
                    "Rapid heart rate",
                    "frequent palpitation(heart beat)",
                    "Hypertension (heart)",
                    "Cardiac arrhythmia",
                    "Pain in upper back",
                    "Pain in abdomen",
                    "Abdominal heart Rhythm",
                    "Pulse near belly pain",
                    "Swelling in  abdomen",
                    "Pain in pelvis/legs/buttock",
                    "Pain behind the knees",
                    "Edema in low leg",
                    "Reduced kidney function",
                    "Haematuria",
                    "Foot pain",
                    "Swelling in ankle and legs",
                    "Discoloured toe",
                    "Ulcer on the skin of the feet that don’t heal"]
        for i in range(18):
          if(all(x in symptoms for x in symptoms_list[i])):
                    print("\n\tDISEASE OF THE PATIENT")
                    print("\nThe Patient May Have -->", disease[i])
                    dis = disease[i]
                    sym = []
                    print("\n\tSYMPTOMS OF THE PATIENT\n")
                    for i in symptoms_list[i]: 
                        print(possible_symptoms[i])
                        sym.append(possible_symptoms[i])
                    break
          else:
                      print("\n\tDISEASE OF THE PATIENT")
                      print("\nthe patient don't have any of the aneurysm")    
                      dis="the patient don't have any of the aneurysm"
                      sym=[]
                      print("\n\tSYMPTOMS OF THE PATIENT:\n")
                      for i in symptoms: 
                        print(possible_symptoms[i])
                        sym.append(possible_symptoms[i])
                      break
        test = []
        print("\n\tChoose The Tests For The Patient From The Following\n")
        print("1.MRI\n2.MRA\n3.BLOOD TEST\n4.DSA\n5.ECHOCARDIOGRAM\n6.CT\n7.X-RAY\n8.ULTRASOUND\n9.ANGIOGRAM")
        while True:
                        inp = input("\nEnter the tests to be taken (exit to end): ")
                        if inp.lower() == "exit":
                            break
                        else:
                            test.append(int(inp))
        tst=[]
        print("\n\tTESTS TO BE TAKEN:\n")
        for j in test:
                        print(possible_test[j])
                        tst.append(possible_test[j])
        filename = "patient.csv"
        info_fields = ["ID","Name", "Age","Gender","Blood Group", "Height", "Weight","Disease","Test To be Taken","Symptoms"]
        with open(filename, "a+") as patient_file:
                    csv_writer = csv.writer(patient_file, delimiter=",")
                    # check if first character is empty
                    if os.path.exists(filename) and os.stat(filename).st_size == 0:
                        csv_writer.writerow(info_fields)
                    csv_writer.writerow(p.getDetails())
    elif(ch==2):
      import csv
      with open("patient.csv","r+") as file:
          reader=csv.reader(file)
          for row in reader:
              print(row)
    elif(ch==3):
      sea = []
      while True:
            search = input("\nEnter The ID To Search (exit to end):")
            if search.lower()=="exit":
              break
            else:
                sea.append(str(search))
            from csv import DictReader
            with open('patient.csv', 'r') as read_obj:
                csv_dict_reader = DictReader(read_obj)
                for row in csv_dict_reader:
                  if all(x in sea for x in row['ID']):
                    print(row)
    elif(ch==4):
        pn = []
        lines = list()
        while True:
          n = input("\nPlease enter a patient ID to be deleted:")
          if n.lower()=="exit":
              break
          else:
              pn.append(str(n))
        with open('patient.csv', 'r') as readFile:
          reader = csv.reader(readFile)
          for row in reader:
            lines.append(row)
            if all(x in pn for x in row[0]):
              lines.remove(row)
        with open('patient.csv', 'w') as writeFile:
              writer = csv.writer(writeFile)
              writer.writerows(lines)
    elif(ch==5):
      break  
    else: 
      print("\nEnter Correct choice") 