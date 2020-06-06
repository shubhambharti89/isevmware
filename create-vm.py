#!/usr/bin/python
import vm_include
import take_input as ti
import getpass
import keystroke as key
import time

#Increase Disk Size to 2400 GB for Production - Currently 200GB for Testing

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

    print("Waiting for Devices to Power-On")

    time.sleep(20)

    boot = ['KEY_1', 'KEY_ENTER']

    for i in range(0, vmcount):
        vm = key.keystrokes(host, user, pw, guest_name[i])
        key.sendKeyStrokes(vm, boot)

    print ("All the devices are installing : Will go into wait state for 3 hours")

    ti.countdown(10800)

    mgmt_ip = ti.getmgmtip(sheet, vmcount)
    mgmt_mask = ti.getmgmtmask(sheet, vmcount)
    mgmt_gateway = ti.getmgmtgateway(sheet, vmcount)
    def_domain = ti.getdomain(sheet, vmcount)
    name_server1 = ti.getnameserver1(sheet, vmcount)
    name_server2 = ti.getnameserver2(sheet, vmcount)
    ntp_server1 = ti.getntpserver1(sheet, vmcount)
    ntp_server2 = ti.getntpserver2(sheet, vmcount)

    setup = ['KEY_S', 'KEY_E', 'KEY_T', 'KEY_U', 'KEY_P', 'KEY_ENTER']
    yes = ['KEY_Y', 'KEY_ENTER']
    no = ['KEY_N', 'KEY_ENTER']
    enter = ['KEY_ENTER']
    password = ["KEY_CAPSLOCK", 'KEY_C', "KEY_CAPSLOCK", 'KEY_1', 'KEY_S', 'KEY_C', 'KEY_O', 'KEY_V', 'KEY_P', 'KEY_N','KEY_1', 'KEY_2', 'KEY_3', 'KEY_ENTER']

    for i in range(0, vmcount):
        vm = key.keystrokes(host, user, pw, guest_name[i])
        key.sendKeyStrokes(vm, setup)
        hostname = ti.strtokey(guest_name[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, hostname)
        mgmtip = ti.strtokey(mgmt_ip[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, mgmtip)
        mgmtmask = ti.strtokey(mgmt_mask[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, mgmtmask)
        mgmtgateway = ti.strtokey(mgmt_gateway[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, mgmtgateway)
        key.sendKeyStrokes(vm, no)
        domain = ti.strtokey(def_domain[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, domain)
        nameserver1 = ti.strtokey(name_server1[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, nameserver1)
        key.sendKeyStrokes(vm, no)
        ntpserver1 = ti.strtokey(ntp_server1[i])
        time.sleep(1)
        key.sendKeyStrokes(vm, ntpserver1)
        key.sendKeyStrokes(vm, no)
        time.sleep(1)
        key.sendKeyStrokes(vm, enter)
        key.sendKeyStrokes(vm, yes)
        time.sleep(1)
        key.sendKeyStrokes(vm, enter)
        time.sleep(1)
        key.sendKeyStrokes(vm, password)
        time.sleep(1)
        key.sendKeyStrokes(vm, password)

# For Lab purpose as Gateway, NTP, Nameserver wont be reachable
        time.sleep(5)
        key.sendKeyStrokes(vm, no)
        time.sleep(5)
        key.sendKeyStrokes(vm, no)
        time.sleep(5)
        key.sendKeyStrokes(vm, no)
        time.sleep(5)
        key.sendKeyStrokes(vm, no)
        time.sleep(5)



    print("Devices have been successfully configured : Wait for 15 minutes for Application Server to come up")





if __name__ == '__main__':
    main()

