import argparse, paramiko, os, re, sys, time
from lib_ssh_connectivity import Device
from lib_ssh_connectivity import create_handle_quiet
from lib_backend_functions import determine_list_average
from lib_backend_functions import determine_list_highest_value
from pprint import pprint



'''Get FPC values from device'''
def get_cpu_proc_use(dut_host):
    '''Command sets for device configuration'''
    command_set_1 = [f'show system process summary | except idle | find USERNAME']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(1)
        except:
            print(f"An error occurred.")
        output = dut_host_terminal.recv(1000).decode('utf-8')
    output_recv = output.split('\n')
    dut_host_terminal.send('exit\n')
    return output
    time.sleep(10)


'''Parse output from routing table data retrieved'''
def parse_re_cpu_output(dut_host, interval_max):
    proc_0_name = 'cli'
    proc_1_name = 'chassisd'
    proc_2_name = 'named-service'
    proc_3_name = 'dhcp-service'
    proc_4_name = 'eswd'
    proc_5_name = 'firewalld'
    proc_6_name = 'pfem'
    proc_7_name = 'dcd'
    proc_8_name = 'ilmi'
    proc_9_name = 'mgd'
    proc_10_name = 'rpd'
    proc_11_name = 'snmpd'
    proc_12_name = 'mib2d'
    proc_13_name = 'ppmd'
    proc_14_name = 'vrrd'
    proc_15_name = 'bfdd'
    proc_16_name = 'na-grpcd'
    proc_17_name = 'sampled'
    proc_18_name = 'jinsightd'
    proc_19_name = 'sdk_vmmd'
    proc_20_name = 'sshd'
    proc_21_name = 'bgpio-0-th'
    proc_22_name = 'license-check'
    proc_23_name = 'tracethread'
    proc_24_name = 'csh'
    proc_25_name = 'python'
    proc_0_list = []
    proc_1_list = []
    proc_2_list = []
    proc_3_list = []
    proc_4_list = []
    proc_5_list = []
    proc_6_list = []
    proc_7_list = []
    proc_8_list = []
    proc_9_list = []
    proc_10_list = []
    proc_11_list = []
    proc_12_list = []
    proc_13_list = []
    proc_14_list = []
    proc_15_list = []
    proc_16_list = []
    proc_17_list = []
    proc_18_list = []
    proc_19_list = []
    proc_20_list = []
    proc_20_list = []
    proc_21_list = []
    proc_22_list = []
    proc_23_list = []
    proc_24_list = []
    proc_25_list = []
    proc_list = [proc_0_name,
                proc_1_name,
                proc_2_name,
                proc_3_name,
                proc_4_name,
                proc_5_name,
                proc_6_name,
                proc_7_name,
                proc_8_name,
                proc_9_name,
                proc_10_name,
                proc_11_name,
                proc_12_name,
                proc_13_name,
                proc_14_name,
                proc_15_name,
                proc_16_name,
                proc_17_name,
                proc_18_name,
                proc_19_name,
                proc_20_name,
                proc_21_name,
                proc_22_name,
                proc_23_name,
                proc_24_name,
                proc_25_name
                ]
    proc_0_usage = []
    proc_1_usage = []
    proc_2_usage = []
    proc_3_usage = []
    proc_4_usage = []
    proc_5_usage = []
    proc_6_usage = []
    proc_7_usage = []
    proc_8_usage = []
    proc_9_usage = []
    proc_10_usage = []
    proc_11_usage = []
    proc_12_usage = []
    proc_13_usage = []
    proc_14_usage = []
    proc_15_usage = []
    proc_16_usage = []
    proc_17_usage = []
    proc_18_usage = []
    proc_19_usage = []
    proc_20_usage = []
    proc_21_usage = []
    proc_22_usage = []
    proc_23_usage = []
    proc_24_usage = []
    proc_25_usage = []
    proc_usage_list = [proc_0_usage,
                  proc_1_usage,
                  proc_2_usage,
                  proc_3_usage,
                  proc_4_usage,
                  proc_5_usage,
                  proc_6_usage,
                  proc_7_usage,
                  proc_8_usage,
                  proc_9_usage,
                  proc_10_usage,
                  proc_11_usage,
                  proc_12_usage,
                  proc_13_usage,
                  proc_14_usage,
                  proc_15_usage,
                  proc_16_usage,
                  proc_17_usage,
                  proc_18_usage,
                  proc_19_usage,
                  proc_20_usage,
                  proc_21_usage,
                  proc_22_usage,
                  proc_23_usage,
                  proc_24_usage,
                  proc_25_usage
                  ]

    interval_current = 1
    end_cnt = len(proc_list)
    while interval_current < interval_max:
        print('#####################################################################')
        print('################## AVERAGE CPU PROCESS UTILIZATION ##################')
        print('#####################################################################')
        print(f'Interval {interval_current} of {interval_max}')
        input = get_cpu_proc_use(dut_host)
        input = input.split('\r\n')
        i = 0
        while i < end_cnt:
            for line in input:
                init_pattern = proc_list[i]
                pattern = fr'{init_pattern}'
                init_proc_data = re.findall(pattern, line)
                if len(init_proc_data) >= 1:
                    t = len(init_proc_data) - 1
                    if init_proc_data[t] in line:
                        init_proc_data_list = line.split()
                        init_pct_use = init_proc_data_list[-2].replace('%', '')
                        init_pct_use = float(init_pct_use)
                        print(f'{init_proc_data[t]} CPU Usage: {init_pct_use}')
                        proc_usage_list[i].append(init_pct_use)
            i += 1
        interval_current += 1
        time.sleep(5)
    dict_proc_data = {
                    "proc_list" : proc_list,
                    "proc_usage_list" : proc_usage_list
                    }
    dict_returned_data =process_re_cpu_output(dict_proc_data)
    return dict_returned_data


'''Process outputs from proc data retrieved'''
def process_re_cpu_output(dict_proc_data):
    proc_use_dict = dict_proc_data
    print('##############################################################################')
    print('################## SUMMARY: AVERAGE CPU PROCESS UTILIZATION ##################')
    print('##############################################################################')
    proc_name_list = proc_use_dict['proc_list']
    proc_usage = proc_use_dict['proc_usage_list']
    proc_0_name = proc_name_list[0]
    proc_1_name = proc_name_list[1]
    proc_2_name = proc_name_list[2]
    proc_3_name = proc_name_list[3]
    proc_4_name = proc_name_list[4]
    proc_5_name = proc_name_list[5]
    proc_6_name = proc_name_list[6]
    proc_7_name = proc_name_list[7]
    proc_8_name = proc_name_list[8]
    proc_9_name = proc_name_list[9]
    proc_10_name = proc_name_list[10]
    proc_11_name = proc_name_list[11]
    proc_12_name = proc_name_list[12]
    proc_13_name = proc_name_list[13]
    proc_14_name = proc_name_list[14]
    proc_15_name = proc_name_list[15]
    proc_16_name = proc_name_list[16]
    proc_17_name = proc_name_list[17]
    proc_18_name = proc_name_list[18]
    proc_19_name = proc_name_list[19]
    proc_20_name = proc_name_list[20]
    proc_21_name = proc_name_list[21]
    proc_22_name = proc_name_list[22]
    proc_23_name = proc_name_list[23]
    proc_24_name = proc_name_list[24]
    proc_25_name = proc_name_list[25]
    proc_list_length = len(proc_usage)
    proc_usage_proc_0 = proc_use_dict['proc_usage_list'][0]
    proc_usage_proc_1 = proc_use_dict['proc_usage_list'][1]
    proc_usage_proc_2 = proc_use_dict['proc_usage_list'][2]
    proc_usage_proc_3 = proc_use_dict['proc_usage_list'][3]
    proc_usage_proc_4 = proc_use_dict['proc_usage_list'][4]
    proc_usage_proc_5 = proc_use_dict['proc_usage_list'][5]
    proc_usage_proc_6 = proc_use_dict['proc_usage_list'][6]
    proc_usage_proc_7 = proc_use_dict['proc_usage_list'][7]
    proc_usage_proc_8 = proc_use_dict['proc_usage_list'][8]
    proc_usage_proc_9 = proc_use_dict['proc_usage_list'][9]
    proc_usage_proc_10 = proc_use_dict['proc_usage_list'][10]
    proc_usage_proc_11 = proc_use_dict['proc_usage_list'][11]
    proc_usage_proc_12 = proc_use_dict['proc_usage_list'][12]
    proc_usage_proc_13 = proc_use_dict['proc_usage_list'][13]
    proc_usage_proc_14 = proc_use_dict['proc_usage_list'][14]
    proc_usage_proc_15 = proc_use_dict['proc_usage_list'][15]
    proc_usage_proc_16 = proc_use_dict['proc_usage_list'][16]
    proc_usage_proc_17 = proc_use_dict['proc_usage_list'][17]
    proc_usage_proc_18 = proc_use_dict['proc_usage_list'][18]
    proc_usage_proc_19 = proc_use_dict['proc_usage_list'][19]
    proc_usage_proc_20 = proc_use_dict['proc_usage_list'][20]
    proc_usage_proc_21 = proc_use_dict['proc_usage_list'][21]
    proc_usage_proc_22 = proc_use_dict['proc_usage_list'][22]
    proc_usage_proc_23 = proc_use_dict['proc_usage_list'][23]
    proc_usage_proc_24 = proc_use_dict['proc_usage_list'][24]
    proc_usage_proc_25 = proc_use_dict['proc_usage_list'][25]
    avg_proc_use_0 = determine_list_average(proc_usage_proc_0)
    avg_proc_use_1 = determine_list_average(proc_usage_proc_1)
    avg_proc_use_2 = determine_list_average(proc_usage_proc_2)
    avg_proc_use_3 = determine_list_average(proc_usage_proc_3)
    avg_proc_use_4 = determine_list_average(proc_usage_proc_4)
    avg_proc_use_5 = determine_list_average(proc_usage_proc_5)
    avg_proc_use_6 = determine_list_average(proc_usage_proc_6)
    avg_proc_use_7 = determine_list_average(proc_usage_proc_7)
    avg_proc_use_8 = determine_list_average(proc_usage_proc_8)
    avg_proc_use_9 = determine_list_average(proc_usage_proc_9)
    avg_proc_use_10 = determine_list_average(proc_usage_proc_10)
    avg_proc_use_11 = determine_list_average(proc_usage_proc_11)
    avg_proc_use_12 = determine_list_average(proc_usage_proc_12)
    avg_proc_use_13 = determine_list_average(proc_usage_proc_13)
    avg_proc_use_14 = determine_list_average(proc_usage_proc_14)
    avg_proc_use_15 = determine_list_average(proc_usage_proc_15)
    avg_proc_use_16 = determine_list_average(proc_usage_proc_16)
    avg_proc_use_17 = determine_list_average(proc_usage_proc_17)
    avg_proc_use_18 = determine_list_average(proc_usage_proc_18)
    avg_proc_use_19 = determine_list_average(proc_usage_proc_19)
    avg_proc_use_20 = determine_list_average(proc_usage_proc_20)
    avg_proc_use_21 = determine_list_average(proc_usage_proc_21)
    avg_proc_use_22 = determine_list_average(proc_usage_proc_22)
    avg_proc_use_23 = determine_list_average(proc_usage_proc_23)
    avg_proc_use_24 = determine_list_average(proc_usage_proc_24)
    avg_proc_use_25 = determine_list_average(proc_usage_proc_25)
    peak_proc_use_0 = determine_list_highest_value(proc_usage_proc_0)
    peak_proc_use_1 = determine_list_highest_value(proc_usage_proc_1)
    peak_proc_use_2 = determine_list_highest_value(proc_usage_proc_2)
    peak_proc_use_3 = determine_list_highest_value(proc_usage_proc_3)
    peak_proc_use_4 = determine_list_highest_value(proc_usage_proc_4)
    peak_proc_use_5 = determine_list_highest_value(proc_usage_proc_5)
    peak_proc_use_6 = determine_list_highest_value(proc_usage_proc_6)
    peak_proc_use_7 = determine_list_highest_value(proc_usage_proc_7)
    peak_proc_use_8 = determine_list_highest_value(proc_usage_proc_8)
    peak_proc_use_9 = determine_list_highest_value(proc_usage_proc_9)
    peak_proc_use_10 = determine_list_highest_value(proc_usage_proc_10)
    peak_proc_use_11 = determine_list_highest_value(proc_usage_proc_11)
    peak_proc_use_12 = determine_list_highest_value(proc_usage_proc_12)
    peak_proc_use_13 = determine_list_highest_value(proc_usage_proc_13)
    peak_proc_use_14 = determine_list_highest_value(proc_usage_proc_14)
    peak_proc_use_15 = determine_list_highest_value(proc_usage_proc_15)
    peak_proc_use_16 = determine_list_highest_value(proc_usage_proc_16)
    peak_proc_use_17 = determine_list_highest_value(proc_usage_proc_17)
    peak_proc_use_18 = determine_list_highest_value(proc_usage_proc_18)
    peak_proc_use_19 = determine_list_highest_value(proc_usage_proc_19)
    peak_proc_use_20 = determine_list_highest_value(proc_usage_proc_20)
    peak_proc_use_21 = determine_list_highest_value(proc_usage_proc_21)
    peak_proc_use_22 = determine_list_highest_value(proc_usage_proc_22)
    peak_proc_use_23 = determine_list_highest_value(proc_usage_proc_23)
    peak_proc_use_24 = determine_list_highest_value(proc_usage_proc_24)
    peak_proc_use_25 = determine_list_highest_value(proc_usage_proc_25)
    print(f'Process {proc_0_name} average utilization: {avg_proc_use_0}%')
    print(f'Process {proc_1_name} average utilization: {avg_proc_use_1}%')
    print(f'Process {proc_2_name} average utilization: {avg_proc_use_2}%')
    print(f'Process {proc_3_name} average utilization: {avg_proc_use_3}%')
    print(f'Process {proc_4_name} average utilization: {avg_proc_use_4}%')
    print(f'Process {proc_5_name} average utilization: {avg_proc_use_5}%')
    print(f'Process {proc_6_name} average utilization: {avg_proc_use_6}%')
    print(f'Process {proc_7_name} average utilization: {avg_proc_use_7}%')
    print(f'Process {proc_8_name} average utilization: {avg_proc_use_8}%')
    print(f'Process {proc_9_name} average utilization: {avg_proc_use_9}%')
    print(f'Process {proc_10_name} average utilization: {avg_proc_use_10}%')
    print(f'Process {proc_11_name} average utilization: {avg_proc_use_11}%')
    print(f'Process {proc_12_name} average utilization: {avg_proc_use_12}%')
    print(f'Process {proc_13_name} average utilization: {avg_proc_use_13}%')
    print(f'Process {proc_14_name} average utilization: {avg_proc_use_14}%')
    print(f'Process {proc_15_name} average utilization: {avg_proc_use_15}%')
    print(f'Process {proc_16_name} average utilization: {avg_proc_use_16}%')
    print(f'Process {proc_17_name} average utilization: {avg_proc_use_17}%')
    print(f'Process {proc_18_name} average utilization: {avg_proc_use_18}%')
    print(f'Process {proc_19_name} average utilization: {avg_proc_use_19}%')
    print(f'Process {proc_20_name} average utilization: {avg_proc_use_20}%')
    print(f'Process {proc_21_name} average utilization: {avg_proc_use_21}%')
    print(f'Process {proc_22_name} average utilization: {avg_proc_use_22}%')
    print(f'Process {proc_23_name} average utilization: {avg_proc_use_23}%')
    print(f'Process {proc_24_name} average utilization: {avg_proc_use_24}%')
    print(f'Process {proc_25_name} average utilization: {avg_proc_use_25}%')
    print('###########################################################################')
    print('################## SUMMARY: PEAK CPU PROCESS UTILIZATION ##################')
    print('###########################################################################')
    print(f'Process {proc_0_name} highest utilization: {peak_proc_use_0}%')
    print(f'Process {proc_1_name} highest utilization: {peak_proc_use_1}%')
    print(f'Process {proc_2_name} highest utilization: {peak_proc_use_2}%')
    print(f'Process {proc_3_name} highest utilization: {peak_proc_use_3}%')
    print(f'Process {proc_4_name} highest utilization: {peak_proc_use_4}%')
    print(f'Process {proc_5_name} highest utilization: {peak_proc_use_5}%')
    print(f'Process {proc_6_name} highest utilization: {peak_proc_use_6}%')
    print(f'Process {proc_7_name} highest utilization: {peak_proc_use_7}%')
    print(f'Process {proc_8_name} highest utilization: {peak_proc_use_8}%')
    print(f'Process {proc_9_name} highest utilization: {peak_proc_use_9}%')
    print(f'Process {proc_10_name} highest utilization: {peak_proc_use_10}%')
    print(f'Process {proc_11_name} highest utilization: {peak_proc_use_11}%')
    print(f'Process {proc_12_name} highest utilization: {peak_proc_use_12}%')
    print(f'Process {proc_13_name} highest utilization: {peak_proc_use_13}%')
    print(f'Process {proc_14_name} highest utilization: {peak_proc_use_14}%')
    print(f'Process {proc_15_name} highest utilization: {peak_proc_use_15}%')
    print(f'Process {proc_16_name} highest utilization: {peak_proc_use_16}%')
    print(f'Process {proc_17_name} highest utilization: {peak_proc_use_17}%')
    print(f'Process {proc_18_name} highest utilization: {peak_proc_use_18}%')
    print(f'Process {proc_19_name} highest utilization: {peak_proc_use_19}%')
    print(f'Process {proc_20_name} highest utilization: {peak_proc_use_20}%')
    print(f'Process {proc_21_name} highest utilization: {peak_proc_use_21}%')
    print(f'Process {proc_22_name} highest utilization: {peak_proc_use_22}%')
    print(f'Process {proc_23_name} highest utilization: {peak_proc_use_23}%')
    print(f'Process {proc_24_name} highest utilization: {peak_proc_use_24}%')
    print(f'Process {proc_25_name} highest utilization: {peak_proc_use_25}%')
    print('##################################################################')
    proc_avg_list = []
    proc_peak_list = []
    proc_avg_list.append(avg_proc_use_0)
    proc_avg_list.append(avg_proc_use_1)
    proc_avg_list.append(avg_proc_use_2)
    proc_avg_list.append(avg_proc_use_3)
    proc_avg_list.append(avg_proc_use_4)
    proc_avg_list.append(avg_proc_use_5)
    proc_avg_list.append(avg_proc_use_6)
    proc_avg_list.append(avg_proc_use_7)
    proc_avg_list.append(avg_proc_use_8)
    proc_avg_list.append(avg_proc_use_9)
    proc_avg_list.append(avg_proc_use_10)
    proc_avg_list.append(avg_proc_use_11)
    proc_avg_list.append(avg_proc_use_12)
    proc_avg_list.append(avg_proc_use_13)
    proc_avg_list.append(avg_proc_use_14)
    proc_avg_list.append(avg_proc_use_15)
    proc_avg_list.append(avg_proc_use_16)
    proc_avg_list.append(avg_proc_use_17)
    proc_avg_list.append(avg_proc_use_18)
    proc_avg_list.append(avg_proc_use_19)
    proc_avg_list.append(avg_proc_use_20)
    proc_avg_list.append(avg_proc_use_21)
    proc_avg_list.append(avg_proc_use_22)
    proc_avg_list.append(avg_proc_use_23)
    proc_avg_list.append(avg_proc_use_24)
    proc_avg_list.append(avg_proc_use_25)
    proc_peak_list.append(peak_proc_use_0)
    proc_peak_list.append(peak_proc_use_1)
    proc_peak_list.append(peak_proc_use_2)
    proc_peak_list.append(peak_proc_use_3)
    proc_peak_list.append(peak_proc_use_4)
    proc_peak_list.append(peak_proc_use_5)
    proc_peak_list.append(peak_proc_use_6)
    proc_peak_list.append(peak_proc_use_7)
    proc_peak_list.append(peak_proc_use_8)
    proc_peak_list.append(peak_proc_use_9)
    proc_peak_list.append(peak_proc_use_10)
    proc_peak_list.append(peak_proc_use_11)
    proc_peak_list.append(peak_proc_use_12)
    proc_peak_list.append(peak_proc_use_13)
    proc_peak_list.append(peak_proc_use_14)
    proc_peak_list.append(peak_proc_use_15)
    proc_peak_list.append(peak_proc_use_16)
    proc_peak_list.append(peak_proc_use_17)
    proc_peak_list.append(peak_proc_use_18)
    proc_peak_list.append(peak_proc_use_19)
    proc_peak_list.append(peak_proc_use_20)
    proc_peak_list.append(peak_proc_use_21)
    proc_peak_list.append(peak_proc_use_22)
    proc_peak_list.append(peak_proc_use_23)
    proc_peak_list.append(peak_proc_use_24)
    proc_peak_list.append(peak_proc_use_25)
    dict_returned_data = {
                        "proc_name_list" : proc_name_list,
                        "proc_avg_list" : proc_avg_list,
                        "proc_peak_list" : proc_peak_list
                        }
    return dict_returned_data
