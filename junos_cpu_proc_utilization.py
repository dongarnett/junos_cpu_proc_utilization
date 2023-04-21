import argparse, paramiko, os, re, sys, time
from pprint import pprint
from lib_ssh_connectivity import Device
from lib_junos_sys_chassis import get_cpu_proc_use
from lib_junos_sys_chassis import parse_re_cpu_output
from lib_backend_functions import determine_list_average
from lib_backend_functions import determine_list_highest_value



'''The following code can be used to execute this script file on 1 device under test.'''
cli_args = sys.argv[1:]
dut_ip = cli_args[0]
dut_user = cli_args[1]
dut_pass = cli_args[2]
interval_max = int(cli_args[3])


'''DUT Login parameters'''
host_ip = dut_ip
user = dut_user
passwd = dut_pass
timeout = 30


def main():
    dut_host = Device(host_ip, user, passwd)
    dict_proc_data = parse_re_cpu_output(dut_host, interval_max)
    '''A dictionary is returned with process names, average process utilization,
    and peak process utilization'''
    #print(dict_proc_data)



if __name__ == '__main__':
    main()
