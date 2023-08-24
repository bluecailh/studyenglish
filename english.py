import easygui
import pyttsx3
import csv
import time
import random
ld = pyttsx3.init()
def random_list(input_list):
    
    output_list = input_list.copy()
    
    random.shuffle(output_list)
    # 返回打乱后的列表
    return output_list

def study():
    with open('yydc.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            english = [val for val in row]
    first = int(easygui.enterbox("你要学习的首个单词（数字）"))
    nofirst = int(easygui.enterbox("你要学习的最后一个单词（数字）"))
    studyenglish = english[first-1:nofirst]
    for item in studyenglish:
        xyg = True
        while xyg == True:
            englishword = easygui.buttonbox(item, choices=["朗读", "下一个"])
            if englishword == "朗读":
                ld.say(item)
                ld.runAndWait()
            elif englishword == "下一个":
                xyg = False
        
            
            



def listenenglish():
    with open('yydc.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            english = [val for val in row]
    first = int(easygui.enterbox("你要听写的首个单词（数字）"))
    nofirst = int(easygui.enterbox("你要听写的最后一个单词（数字）"))
    studyenglish = english[first-1:nofirst]
    listenword = random_list(studyenglish)
    nanbow =1
    for item in listenword:
        easygui.msgbox("开始听写")
        ld.say(item)
        ld.runAndWait()
        time.sleep(3)
        ld.say(item)
        ld.runAndWait()
        time.sleep(2)
        nanbow+=1
    
            
            
button_choices = ["学习单词", "听写单词"]
button_choice = easygui.buttonbox("请选择一个模式", choices=button_choices)
if button_choice == "学习单词":
    study()
elif button_choice == "听写单词":
    listenenglish()


