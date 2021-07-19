#PHARMACY MANAGEMENT PROJECT
#-By SAURABH GUHA (18012011096) 
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import pymysql

con = pymysql.connect(host = "localhost", user = "root", passwd = "saurabh1309", database = "saurabh1234")
cur = con.cursor()

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("PHARMACY MANAGEMENT SYSTEM")
        self.master.geometry("1218x596+0+0")
        self.frame = Frame(self.master, background = "black")
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()
        
        self.LabelTitle = Label(self.frame, text = "PHARMACY MANAGEMENT SYSTEM", font = ("Arial", 50, "bold"), bd = 20, background = "black", fg = "white")        
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)       
        
        self.Loginframe1 = Frame(self.frame, width = 1010, height = 300, bd = 20, relief = "ridge", background = "black")
        self.Loginframe1.grid(row = 1, column = 0)
        
        self.Loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 20, relief = "ridge", background = "black")
        self.Loginframe2.grid(row = 2, column = 0)        
        
        self.Loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 20, relief = "ridge", background = "black")
        self.Loginframe3.grid(row = 3, column = 0, pady = 2) 
        
        self.lblUsername = Label(self.Loginframe1, text = "USERNAME", width = 14, font = ("Arial", 30, "bold"), bd = 22)
        self.lblUsername.grid(row = 0, column = 0)
        self.txtUsername = Entry(self.Loginframe1, font = ("Arial", 30, "bold"), bd = 20, textvariable = self.Username)
        self.txtUsername.grid(row = 0, column = 1)        
        
        self.lblPassword = Label(self.Loginframe1, text = "PASSWORD", width = 14,font = ("Arial", 30, "bold"), bd = 22)
        self.lblPassword.grid(row = 1, column = 0)
        self.txtPassword = Entry(self.Loginframe1, font = ("Arial", 30, "bold"), bd = 20, textvariable = self.Password, show = "*")
        self.txtPassword.grid(row = 1, column = 1, padx = 60)
        
        self.btnLogin = Button(self.Loginframe2, text = "LOGIN", width = 20, font = ("Arial", 20, "bold"), command = self.Login_System)
        self.btnLogin.grid(row = 0, column = 0)      
        self.btnReset = Button(self.Loginframe2, text = "RESET", width = 19,  font = ("Arial", 20, "bold"), command = self.Reset)
        self.btnReset.grid(row = 0, column = 1)  
        self.btnExit = Button(self.Loginframe2, text = "EXIT", width = 18,  font = ("Arial", 20, "bold"), command = self.iExit)
        self.btnExit.grid(row = 0, column = 2)
         
        self.btnRegistration = Button(self.Loginframe3, text = "PATIENT'S REGISTRATION SYSTEM",  font = ("Arial", 20, "bold"), state = DISABLED, command = self.Registration_window)
        self.btnRegistration.grid(row = 0, column = 0)
        self.btnHospital = Button(self.Loginframe3, text = "HOSPITAL REGISTRATION SYSTEM",  font = ("Arial", 20, "bold"), state = DISABLED, command = self.Hospital_window)
        self.btnHospital.grid(row = 0, column = 1, pady = 8)
        
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if (user == str("saurabh13")) and (pas == str("13092000")):
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("PHARMACY MANAGEMENT SYSTEM", "YOU'VE ENTERED AN INVALID LOGIN DETAILS")
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
            
    def Reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
            
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("PHARMACY MANAGEMENT SYSTEM", "CONFIRM IF YOU WANT TO EXIT")
        if self.iExit>0:
            self.master.destroy()
            return          
    
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
        
    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)         
        
class Window2:
    def __init__(self, root):
        self.root = root
        self.root.title("PATIENT REGISTRATION SYSTEM")
        self.root.geometry("1520x643+0+0")
        self.root.configure(background = "black")
        
        DateOfOrder = StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%Y"))
        
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()
        
        Ref = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        
        Fees = StringVar()
        Fees.set("0")
        
        #==================================================Function===================================================#
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("PATIENT REGISTRATION SYSTEM", "CONFIRM IF YOU WANT TO EXIT ?")
            if iExit>0:
                root.destroy()
                
        def iReset():
            iReset = tkinter.messagebox.askokcancel("PATIENT REGISTRATION SYSTEM", "CONFIRM IF YOU WANT TO RESET ?")
            if iReset>0:
                Ref.set("")
                Firstname.set("")
                Surname.set("")
                Address.set("")
                Postcode.set("")
                Telephone.set("")
                Fees.set("0")
                
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set(0)
                
                self.cboProve_of_ID.current(0)
                self.cboType_of_Patient.current(0)
                self.cboMethod_of_Payment.current(0)
            
            elif iReset<=0:
                Ref.set("")
                Firstname.set("")
                Surname.set("")
                Address.set("")
                Postcode.set("")
                Telephone.set("")
                Fees.set("0")
                
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set(0)
                
                self.cboProve_of_ID.current(0)
                self.cboType_of_Patient.current(0)
                self.cboMethod_of_Payment.current(0)
                self.txtReceipt.delete("1.0", END)
                return
            
        def Ref_No():
            x = random.randint(1000, 9999)
            randomRef = str(x)
            Ref.set(randomRef)
            
        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,Ref.get()+"\t\t"+Firstname.get()+"\t         "+Surname.get()+"\t\t"+Address.get()+"\t   "+DateOfOrder.get()+"\t\t"+Telephone.get()+"\t\t"+Fees.get()+"\n")
            val1 = [Ref.get(), Firstname.get(), Surname.get(), Address.get(), DateOfOrder.get(), Telephone.get(), Fees.get()]
            cur.execute("Insert Into PatientRegistration Values(%s, %s, %s, %s, %s, %s, %s)", val1);
            con.commit()
            
        def Patient_Fees():
            global paid1
            if var4.get()==1:
                self.txtMembership.configure(state = NORMAL)
                Item1 = float(500)
                Fees.set("₹"+str(Item1))
                paid1 = Fees.get()
            elif var4.get()==0:
                self.txtMembership.configure(state = DISABLED)
                Fees.set("0")
        #===================================================Frame====================================================#
        
        Mainframe = Frame(self.root)
        Mainframe.grid()
    
        TitleFrame = Frame(Mainframe, bd = 20, width = 1350, padx = 26, relief = RIDGE)
        TitleFrame.pack(side = TOP)
                
        self.lblTitle = Label(TitleFrame, font = ("Arial", 50, "bold"), text = "PATIENT REGISTRATION SYSTEM", padx = 2)
        self.lblTitle.grid()
        
        #=====================================LowerFrames===================================#
        
        PatientDetailsFrame = LabelFrame(Mainframe, width = 1350, height = 500, bd = 20, pady = 5, relief = RIDGE)
        PatientDetailsFrame.pack(side = BOTTOM)
        
        FrameDetails = LabelFrame(PatientDetailsFrame, bd = 10, width = 880, height = 400, relief = RIDGE)
        FrameDetails.pack(side = LEFT)
        
        PatientsName_F = LabelFrame(FrameDetails, bd = 10, width = 350, height = 400, font = ("Arial", 12, "bold"), text = "PATIENT NAME", relief = RIDGE)
        PatientsName_F.grid(row = 0, column = 0)
        
        Receipt_ButtonFrame = LabelFrame(PatientDetailsFrame, bd = 10, width = 1000, height = 400, relief = RIDGE)
        Receipt_ButtonFrame.pack(side = RIGHT)
        
        #=====================================LowerFrames===================================#
        
        self.lblReferenceNo = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "REFERENCE NO", bd = 7)
        self.lblReferenceNo.grid(row = 0, column = 0)      
        self.txtReferenceNo = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Ref, state = DISABLED, insertwidth = 2)
        self.txtReferenceNo.grid(row = 0, column = 1)
        
        self.lblFirstName = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "FIRST NAME", bd = 7)
        self.lblFirstName.grid(row = 1, column = 0)      
        self.txtFirstName = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Firstname, insertwidth = 2)
        self.txtFirstName.grid(row = 1, column = 1)
        
        self.lblSurname = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "SURNAME", bd = 7)
        self.lblSurname.grid(row = 2, column = 0)      
        self.txtSurname = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Surname, insertwidth = 2)
        self.txtSurname.grid(row = 2, column = 1)
        
        self.lblAddress = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "ADDRESS", bd = 7)
        self.lblAddress.grid(row = 3, column = 0)      
        self.txtAddress = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Address, insertwidth = 2)
        self.txtAddress.grid(row = 3, column = 1)
        
        self.lblPostCode = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "POST CODE", bd = 7)
        self.lblPostCode.grid(row = 4, column = 0)      
        self.txtPostCode = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Postcode, insertwidth = 2)
        self.txtPostCode.grid(row = 4, column = 1)
        
        self.lblTelephone = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "TELEPHONE", bd = 7)
        self.lblTelephone.grid(row = 5, column = 0)      
        self.txtTelephone = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = Telephone, insertwidth = 2)
        self.txtTelephone.grid(row = 5, column = 1)
        
        self.lblDate = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "DATE", bd = 7)
        self.lblDate.grid(row = 6, column = 0)      
        self.txtDate = Entry(PatientsName_F, font = ("Arial", 14, "bold"), bd = 7, textvariable = DateOfOrder, insertwidth = 2)
        self.txtDate.grid(row = 6, column = 1)
        
        #=====================================MemberInformation===================================#
        
        self.lblProve_of_ID = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "PROVE OF ID", bd = 7)
        self.lblProve_of_ID.grid(row = 7, column = 0, sticky =W)
        
        self.cboProve_of_ID = ttk.Combobox(PatientsName_F, textvariable = var1, state = "readonly", font = ("Arial", 14, "bold"), width = 19)
        self.cboProve_of_ID['value'] = ("", "Aadhar Card", "Driving License", "Passport", "Student_ID")
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row = 7, column = 1)
        
        self.lblType_of_Patient = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "TYPE OF PATIENT", bd = 7)
        self.lblType_of_Patient.grid(row = 8, column = 0, sticky = W)
        
        self.cboType_of_Patient = ttk.Combobox(PatientsName_F, textvariable = var2, state = "readonly", font = ("Arial", 14, "bold"), width = 19)
        self.cboType_of_Patient['value'] = ("", "Full Member", "Annual Membership", "Pay As You Go", "Honorary Member")
        self.cboType_of_Patient.current(0)
        self.cboType_of_Patient.grid(row = 8, column = 1)
        
        self.lblMethod_of_Payment = Label(PatientsName_F, font = ("Arial", 14, "bold"), text = "METHOD OF PAYMENT", bd = 7)
        self.lblMethod_of_Payment.grid(row = 9, column = 0, sticky = W)
        
        self.cboMethod_of_Payment = ttk.Combobox(PatientsName_F, textvariable = var3, state = "readonly", font = ("Arial", 14, "bold"), width = 19)
        self.cboMethod_of_Payment['value'] = ("", "Visa Card", "Master Card", "Debit Card", "Cash")
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row = 9, column = 1)
        
        #===========================================CheckButton========================================#
        
        self.chkMembership = Checkbutton(PatientsName_F, text = "PATIENT FEES", variable = var4, onvalue = 1, offvalue = 0, font = ("Arial", 16, "bold"), command = Patient_Fees).grid(row = 10, column = 0, sticky = W)
         
        self.txtMembership = Entry(PatientsName_F, font = ("Arial", 14, "bold"), textvariable = Fees, bd = 7, insertwidth = 2, state = DISABLED, justify = RIGHT)
        self.txtMembership.grid(row = 10, column = 1)
        
        #===========================================Receipt==============================================#
        
        self.lblReceipt = Label(Receipt_ButtonFrame, font = ("Arial", 14, "bold"), pady = 10, text = "PATIENT REF.     FIRSTNAME     SURNAME     ADDRESS     DATE REG.     TELEPHONE     PATIENT PAID", bd = 7)
        self.lblReceipt.grid(row = 0, column = 0, columnspan = 4)
        
        self.txtReceipt = Text(Receipt_ButtonFrame,width = 86, height = 16, font = ("Arial", 14, "bold"))
        self.txtReceipt.grid(row = 1, column = 0, columnspan = 4)
        
        #===========================================Buttons==============================================#
        
        self.btnReceipt = Button(Receipt_ButtonFrame, padx = 18, bd = 7, font = ("Arial", 16, "bold"), width = 18, text = "RECEIPT", command = Receipt).grid(row = 2, column = 0)
        self.btnReset = Button(Receipt_ButtonFrame, padx = 18, bd = 7, font = ("Arial", 16, "bold"), width = 18, text = "RESET",  command = iReset).grid(row = 2, column = 1)
        self.btnExit = Button(Receipt_ButtonFrame, padx = 18, bd = 7, font = ("Arial", 16, "bold"), width = 18, text = "EXIT", command = iExit).grid(row = 2, column = 2)


class Window3:
    def __init__(self, root):
        self.root = root
        self.root.title("PATIENT REGISTRATION SYSTEM")
        self.root.geometry("1430x685+0+0")
        self.root.configure(background = "black")
        
        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dosage = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        Expdate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowToUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        
         #===================================================Function Declaration===================================================#
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("HOSPITAL MANAGEMENT SYSTEM", "CONFIRM IF YOU WANT TO EXIT")
            if iExit>0:
                root.destroy()
                return
        
        def iPrescription():
            self.textPrescription.insert(END,"NAME OF TABLETS:\t\t\t\t "+cmbNameTablets.get()+"\n")
            self.textPrescription.insert(END,"REFERENCE NO.:\t\t\t\t "+Ref.get()+"\n")
            self.textPrescription.insert(END,"DOSE:\t\t\t\t "+Dosage.get()+"\n")
            self.textPrescription.insert(END,"LOT:\t\t\t\t "+NumberTablets.get()+"\n")
            self.textPrescription.insert(END,"ISSUED DATE:\t\t\t\t "+Lot.get()+"\n")
            self.textPrescription.insert(END,"EXP. DATE:\t\t\t\t "+Expdate.get()+"\n")
            self.textPrescription.insert(END,"DAILY DOSE:\t\t\t\t "+DailyDose.get()+"\n")
            self.textPrescription.insert(END,"POSSIBLE SIDE EFFECTS:\t\t\t\t "+PossibleSideEffects.get()+"\n")
            self.textPrescription.insert(END,"FURTHER INFORMATION:\t\t\t\t "+FurtherInformation.get()+"\n")
            self.textPrescription.insert(END,"STORAGE ADVICE:\t\t\t\t "+StorageAdvice.get()+"\n")
            self.textPrescription.insert(END,"DRIVING OR USING MACHINES:\t\t\t\t "+DrivingUsingMachines.get()+"\n")
            self.textPrescription.insert(END,"HOW TO USE MEDICATION:\t\t\t\t "+HowToUseMedication.get()+"\n")
            self.textPrescription.insert(END,"PATIENT ID:\t\t\t\t "+PatientID.get()+"\n")
            self.textPrescription.insert(END,"NHS NUMBER:\t\t\t\t "+PatientNHSNo.get()+"\n")
            self.textPrescription.insert(END,"PATIENT NAME:\t\t\t\t "+PatientName.get()+"\n")
            self.textPrescription.insert(END,"DATE OF BIRTH:\t\t\t\t "+DateOfBirth.get()+"\n")
            self.textPrescription.insert(END,"PATIENT ADDRESS:\t\t\t\t "+PatientAddress.get()+"\n")
            return
            
        def iReceipt():
            self.textFrameDetail.insert(END,"    "+cmbNameTablets.get()+"\t\t     "+Ref.get()+"\t\t"+Dosage.get()+"\t     "+NumberTablets.get()+"\t\t"+Lot.get()+"\t"+IssuedDate.get()+"\t"+Expdate.get()+"\t\t"+DailyDose.get()+"\t"+StorageAdvice.get()+"\t\t"+PatientNHSNo.get()+"\t"+PatientName.get()+"\t"+DateOfBirth.get()+"\t"+PatientAddress.get()+"\n")
            val2 = [cmbNameTablets.get(), Ref.get(), Dosage.get(), NumberTablets.get(), Lot.get(), IssuedDate.get(), Expdate.get(), DailyDose.get(), StorageAdvice.get(), PatientNHSNo.get(), PatientName.get(), DateOfBirth.get(), PatientAddress.get()]
            cur.execute("Insert Into HospitalRegistration Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", val2);
            con.commit()
            return
             
        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dosage.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            Expdate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.textPrescription.delete("1.0", END)
            self.textFrameDetail.delete("1.0", END)
            return
            
        def iReset(): 
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dosage.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            Expdate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.textPrescription.delete("1.0", END)
            return
         #=========================================================Frame============================================================#
        
        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame, bd = 20, width = 1350, padx = 20, relief = RIDGE)
        TitleFrame.pack(side = TOP)
        
        self.lblTitle = Label(TitleFrame, width = 42, font = ("Arial)", 40,"bold"), text = "HOSPITAL MANAGEMENT SYSTEM", padx = 2)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd = 20, width = 1350, height = 100,padx = 20, relief = RIDGE)                      
        FrameDetail.pack(side = BOTTOM)
        
        ButtonFrame = Frame(MainFrame, bd = 20, width = 1350, height = 50,padx = 20, relief = RIDGE)                      
        ButtonFrame.pack(side = BOTTOM)
        
        DataFrame = Frame(MainFrame, bd = 20, width = 1350, height = 400,padx = 20, relief = RIDGE)                      
        DataFrame.pack(side = BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd = 10, width = 800, height = 300,padx = 20, relief = RIDGE, font = ("Arial", 12, "bold"), text = "PATIENT'S INFORMATION")                      
        DataFrameLEFT.pack(side = LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd = 10, width = 450, height = 300,padx = 20, relief = RIDGE, font = ("Arial", 12, "bold"), text = "PRESCRIPTION")                      
        DataFrameRIGHT.pack(side = RIGHT)
        
        #=====================================================DataFrameLEFT=======================================================#
        
        self.lblNameTablet = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "NAME OF TABLETS:", padx = 2, pady = 4)
        self.lblNameTablet.grid(row = 0, column = 0, sticky = W)  
        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, textvariable = cmbNameTablets, state = "readonly",font = ("Arial", 12,"bold"), width = 23)
        self.cboNameTablet["value"] = ("", "Ibuprofen", "Co-codamol", "Paracetamol", "Amlodipine", "HydroChloroQueen")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row = 0, column = 1)
        
        self.lblFurtherInfo = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "FURTHER INFORMATION:", padx = 2, pady = 4)
        self.lblFurtherInfo.grid(row = 0, column = 2, sticky = W)     
        self.txtFurtherInfo = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = FurtherInformation, width = 25)
        self.txtFurtherInfo.grid(row = 0, column = 3)
        
        self.lblRef = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "REFERENCE NO.:", padx = 2, pady = 4)
        self.lblRef.grid(row = 1, column = 0, sticky = W)  
        self.txtRef = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = Ref, width = 25)
        self.txtRef.grid(row = 1, column = 1)
        
        self.lblStorage = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "STORAGE ADVICE:", padx = 2, pady = 4)
        self.lblStorage.grid(row = 1, column = 2, sticky = W)
        self.txtStorage = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = StorageAdvice, width = 25)
        self.txtStorage.grid(row = 1, column = 3)
        
        self.lblDose = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "DOSE:", padx = 2, pady = 4)
        self.lblDose.grid(row = 2, column = 0, sticky = W)
        self.txtDose = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = Dosage, width = 25)
        self.txtDose.grid(row = 2, column = 1)
        
        self.lblDUseMachine = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "DRIVING MACHINES:", padx = 2, pady = 4)
        self.lblDUseMachine.grid(row = 2, column = 2, sticky = W)
        self.txtDUseMachine = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = DrivingUsingMachines, width = 25)
        self.txtDUseMachine.grid(row = 2, column = 3)
        
        self.lblNoOfTablets = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "NO. OF TABLETS:", padx = 2, pady = 4)
        self.lblNoOfTablets.grid(row = 3, column = 0, sticky = W)
        self.txtNoOfTablets = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = NumberTablets, width = 25)
        self.txtNoOfTablets.grid(row = 3, column = 1)
        
        self.lblUseMedication = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "USE MEDICATIONS:", padx = 2, pady = 4)
        self.lblUseMedication.grid(row = 3, column = 2, sticky = W)
        self.txtUseMedication = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = HowToUseMedication, width = 25)
        self.txtUseMedication.grid(row = 3, column = 3)
        
        self.lblLot = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "LOT:", padx = 2, pady = 4)
        self.lblLot.grid(row = 4, column = 0, sticky = W)
        self.txtLot = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = Lot, width = 25)
        self.txtLot.grid(row = 4, column = 1)
        
        self.lblPatientID = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "PATIENT ID:", padx = 2, pady = 4)
        self.lblPatientID.grid(row = 4, column = 2, sticky = W)
        self.txtPatientID = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = PatientID, width = 25)
        self.txtPatientID.grid(row = 4, column = 3)
        
        self.lblIssuedDate = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "ISSUED DATE:", padx = 2, pady = 4)
        self.lblIssuedDate.grid(row = 5, column = 0, sticky = W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = IssuedDate, width = 25)
        self.txtIssuedDate.grid(row = 5, column = 1)
        
        self.lblNHSNumber = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "NHS NUMBER:", padx = 2, pady = 4)
        self.lblNHSNumber.grid(row = 5, column = 2, sticky = W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = PatientNHSNo, width = 25)
        self.txtIssuedDate.grid(row = 5, column = 3)
        
        self.lblExpDate = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "EXPIRY DATE:", padx = 2, pady = 4)
        self.lblExpDate.grid(row = 6, column = 0, sticky = W)
        self.txtExpDate = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = Expdate, width = 25)
        self.txtExpDate.grid(row = 6, column = 1)
        
        self.lblPatientName = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "PATIENT NAME:", padx = 2, pady = 4)
        self.lblPatientName.grid(row = 6, column = 2, sticky = W)
        self.txtPatientName = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = PatientName, width = 25)
        self.txtPatientName.grid(row = 6, column = 3)
        
        self.lblDailyDose = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "DAILY DOSE:", padx = 2, pady = 4)
        self.lblDailyDose.grid(row = 7, column = 0, sticky = W)
        self.txtDailyDose = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = DailyDose, width = 25)
        self.txtDailyDose.grid(row = 7, column = 1)
        
        self.lblDateOfBirth = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "DATE OF BIRTH:", padx = 2, pady = 4)
        self.lblDateOfBirth.grid(row = 7, column = 2, sticky = W)
        self.txtDateOfBirth = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = DateOfBirth, width = 25)
        self.txtDateOfBirth.grid(row = 7, column = 3)
        
        self.lblSideEffects = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "SIDE EFFECTS:", padx = 2, pady = 4)
        self.lblSideEffects.grid(row = 8, column = 0, sticky = W)
        self.txtSideEffects = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = PossibleSideEffects, width = 25)
        self.txtSideEffects.grid(row = 8, column = 1)
        
        self.lblPatientAddress = Label(DataFrameLEFT, font = ("Arial", 12,"bold"), text = "PATIENT ADDRESS:", padx = 2, pady = 4)
        self.lblPatientAddress.grid(row = 8, column = 2, sticky = W)
        self.txtPatientAddress = Entry(DataFrameLEFT, font = ("Arial", 12,"bold"), textvariable = PatientAddress, width = 25)
        self.txtPatientAddress.grid(row = 8, column = 3)
       
        #=====================================================DataFrameRIGHT=======================================================#
        
        self.textPrescription = Text(DataFrameRIGHT, font = ("Arial", 12,"bold"), width = 43, height = 14, padx = 2, pady = 4)
        self.textPrescription.grid(row = 0, column = 0)
        
        #=====================================================ButtonFrame==========================================================#
        
        self.btnPrescription = Button(ButtonFrame, text = "PRESCRIPTION", font = ("Arial", 12,"bold"), width = 26, bd = 4, command = iPrescription)
        self.btnPrescription.grid(row = 0, column = 0)
        self.btnReceipt = Button(ButtonFrame, text = "RECEIPT", font = ("Arial", 12,"bold"), width = 26, bd = 4, command = iReceipt)
        self.btnReceipt.grid(row = 0, column = 1)
        self.btnDelete = Button(ButtonFrame, text = "DELETE", font = ("Arial", 12,"bold"), width = 26, bd = 4, command = iDelete)
        self.btnDelete.grid(row = 0, column = 2)
        self.btnReset = Button(ButtonFrame, text = "RESET", font = ("Arial", 12,"bold"), width = 25, bd = 4, command = iReset)
        self.btnReset.grid(row = 0, column = 3)
        self.btnExit = Button(ButtonFrame, text = "EXIT", font = ("Arial", 12,"bold"), width = 25, bd = 4, command = iExit)
        self.btnExit.grid(row = 0, column = 4)
        
        #=====================================================FrameDetail==========================================================#
        
        self.lblLabel = Label(FrameDetail, font = ("Arial", 10,"bold"),
        text = "*NAME OF TABLETS*   *REFERENCE NO.*   *DOSAGE*   *NO. OF TABLETS*   *LOT*   *ISSUED DATE*   *EXP. DATE*\t*DAILY DOSE*\t*STORAGE ADV.*   *NHS NUMBER*\t*PATIENT NAME*\t*DOB*\t*ADDRESS*", pady = 2, padx = 2)
        self.lblLabel.grid(row = 0, column = 0)
        
        self.textFrameDetail = Text(FrameDetail, font = ("Arial", 12,"bold"), width = 148, height = 4, padx = 4, pady = 4)
        self.textFrameDetail.grid(row = 1, column = 0)
             
    
if __name__ == "__main__":
    root = Tk()
    application = Window1(root)
    root.mainloop()      