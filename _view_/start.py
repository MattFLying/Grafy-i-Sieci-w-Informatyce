'''
Created on 27.05.2017

@author: Mateusz Mucha
'''
from enum import Enum

from _controller_ import list_one as L01
from _controller_ import list_two as L02
from _controller_ import list_three as L03


class List(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOUR = 4
    FIVE = 5
    
class Task(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOUR = 4
    FIVE = 5

def execute():
    while True:
            try:
                choosen_list = int(input(":::>> Ktore Liste wybrac? "))
                if choosen_list == List.FIRST.value:
                    choosen_task = int(input(":::>> Ktore zadanie z Listy 1 pokazac? "))
                    print("------------------")
                    if choosen_task == Task.FIRST.value:
                        print(L01.task_one())
                    elif choosen_task == Task.SECOND.value:
                        print(L01.task_two())
                    elif choosen_task == Task.THIRD.value:
                        print(L01.task_three())
                    elif choosen_task == Task.FOUR.value:
                        print(L01.task_four())
                    elif choosen_task == Task.FIVE.value:
                        print(L01.task_five())    
                    print("------------------\n")
                elif choosen_list == List.SECOND.value:
                    choosen_task = int(input(":::>> Ktore zadanie z Listy 2 pokazac? "))
                    print("------------------")
                    if choosen_task == Task.FIRST.value:
                        print(L02.task_one())
                    elif choosen_task == Task.SECOND.value:
                        print(L02.task_two())
                    elif choosen_task == Task.THIRD.value:
                        print(L02.task_three())
                    elif choosen_task == Task.FIVE.value:
                        print(L02.task_five())    
                    print("------------------\n")
                elif choosen_list == List.THIRD.value:
                    choosen_task = int(input(":::>> Ktore zadanie z Listy 3 pokazac? "))
                    print("------------------")
                    if choosen_task == Task.FIRST.value:
                        print(L03.task_one())
                    elif choosen_task == Task.SECOND.value:
                        print(L03.task_two())
                    elif choosen_task == Task.THIRD.value:
                        print(L03.task_three())
                    elif choosen_task == Task.FOUR.value:
                        print(L03.task_four())    
                    elif choosen_task == Task.FIVE.value:
                        print(L03.task_five())    
                    print("------------------\n")
            except:
                print("Podano zla wartosc! Wprowadz wylacznie liczby 1-5!")    
    
        
execute()
