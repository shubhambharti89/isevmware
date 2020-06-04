#!/usr/bin/python
import vm_include
import take_input as ti
import getpass
import keystroke as key
import time

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

    # create the new VM
    res = vm_include.createGuest(host_con, guest_dc[0], esx_host[0], guest_name[0], guest_ver[0], guest_mem[0], guest_cpu[0], guest_iso, iso_ds, guest_os, guest_space[0], datastore[0], guest_network1[0], guest_network2[0], guest_enterbios)

    print(res)

    # start the new VM
    vm_include.powerOnGuest(host_con, guest_name[0])

    # disconnect from host
    host_con.disconnect()

    time.sleep(20)

    setup = ['KEY_1', 'KEY_ENTER']
    key.keystrokes(host, user, pw, guest_name[0], setup)





if __name__ == '__main__':
    main()