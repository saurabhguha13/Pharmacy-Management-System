from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1430x698+0+0")
        
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
    application = Hospital(root)
    root.mainloop()        