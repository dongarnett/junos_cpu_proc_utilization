import argparse, os, paramiko, re, sys, time
from pprint import pprint



'''Create device class to handle connectivity'''
class Device:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        #self.session_timeout = session_timeout

'''Create device handle instance'''
def create_handle(self):
    # Connection Parameters
    print(f'Connecting to host {self.hostname}')
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=self.hostname, username=self.username, password=self.password)
    return client


'''Create device handle instance'''
def create_handle_quiet(self):
    # Connection Parameters
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=self.hostname, username=self.username, password=self.password)
    return client
