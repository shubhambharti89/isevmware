# isevmware
Deploy ISE ON VMware and finish up initial configuration


Create-VM : 
Creates the VM with information from Sheet.xlsx 

Take_Input :
Takes Excel sheet as input and parses the data

vm_include :
Uses Pysphere to create the vm after receiving information from Creae-VM

keystrokes :
Sends keystroke to VMware console after connecting to Vcenter using PyVmomi.
