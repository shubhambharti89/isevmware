#!/usr/bin/python
import vm_include
import take_input as ti
import getpass
import keystroke as key
import time

#Increase Disk Size to 2400 GB for Production - Curretly 200GB for Testing

def main():


    host = raw_input("Enter the vCenter IP Address : ")
    user = raw_input("Enter the vCenter Username : ")
    pw = getpass.getpass("Enter the vCenter Password : ")

    filename = raw_input("Enter the Filename : ")
    sheet = ti.Read_Onboard_Sheet(filename,2)
    vmcount = ti.numberofvm(sheet)
    guest_name = ti.gethostname(sheet,vmcount)


    guest_cpu = ti.getcpu(sheet,vmcount)
    guest_mem = ti.getmemory(sheet,vmcount)
    guest_space = ti.getdisk(vmcount)
    datastore = ti.getdsname(sheet,vmcount)

    esx_host = ti.getesxiname(sheet, vmcount)
    guest_dc = ti.getdcname(sheet, vmcount)

    guest_ver = ti.getguestver(sheet,vmcount)

    guest_iso = str(ti.getisofile(sheet))
    iso_ds = str(ti.getisods(sheet))
    guest_os = "rhel7_64Guest"

    guest_network1 = ti.getnetwork1(sheet, vmcount)
    guest_network2 = ti.getnetwork2(sheet, vmcount)
    guest_enterbios = False


    # connect to the host
    host_con = vm_include.connectToHost(host, user, pw)

    for i in range(0, vmcount) :
        res = vm_include.createGuest(host_con, guest_dc[i], esx_host[i], guest_name[i], guest_ver[i], guest_mem[i], guest_cpu[i], guest_iso, iso_ds, guest_os, guest_space[i], datastore[i], guest_network1[i], guest_network2[i], guest_enterbios)

        print(res)

    # start the new VM
        vm_include.powerOnGuest(host_con, guest_name[i])

    # disconnect from host
    host_con.disconnect()

    time.sleep(20)

    setup = ['KEY_1', 'KEY_ENTER']

    for i in range(0, vmcount):
        key.keystrokes(host, user, pw, guest_name[i], setup)

    print ("All the devices are installing")



if __name__ == '__main__':
    main()