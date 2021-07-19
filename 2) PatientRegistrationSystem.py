from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

class Registration:
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
        
        #=========================================================================================#
if __name__ == "__main__":
    root = Tk()
    application = Registration(root)
    root.mainloop()        