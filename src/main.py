from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time
import random as ra

def cmdargs(args):
    while True:
        global name
        name = input("Command args: ")
        if name == '':
            print("Invalid args")

while True:
    urlinput = str(input("Input a link: "))
    sedriver = None
    if urlinput.find('www') >= 0 or urlinput.find('https://') >= 0:
        sedriver = web.Chrome("C:\Program Files (x86)\chromedriver.exe")
        print("Scanning...")
        time.sleep(5)
        print("Finishing")
        sedriver.get(urlinput)
        time.sleep(1)
        print("Title is: " + sedriver.title)
        cmdlist = ['findbyhtmlclass', 'findbyid', 'findbyname', 'getcookies', 'getsource']
        print(cmdlist)
        type = input("Input a command: ")
        if type != cmdlist.index(any):
            print("Invalid Command.")
        elif type == cmdlist.index(0):
            sedriver.find_element_by_class_name(name)
        elif type == cmdlist.index(1):
            sedriver.find_element_by_id(name)
    else:
        print("Invalid URL")