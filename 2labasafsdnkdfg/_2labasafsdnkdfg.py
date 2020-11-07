import numpy as np
import sys
#Открытие файлов для чтения
alphabet=open('alphabet.txt', 'r')#Алфавит
program=open('program.txt', 'r')#Программа
task=open('task.txt', 'r')#Задача
#Открытие файлов для записи
decision=open('result.txt', 'w')#Результат'
#Считываем данные из файлов
task1=(task.read())+"_____________________________"
alphabet1=alphabet.read()
#Проверка на  соответсвие  алфавиту
result=set(task1).issubset(alphabet1)
if result==False:
     decision.write("ОШИБКА!Отсуствует введеный элемент в алфавите!")
     print("Ошибка")
     sys.exit(0)

print("Задание=",task1)
print("Алфавит",alphabet1)
#Размерность матрицы
dy=1
dx=0
dx=program.readline().split("\t")
dx=len(dx)-1
for line in program:
    dy+= 1
#Создание матрицы для правил
my_prog=np.zeros((dy,dx), dtype=object)
piz=open('program.txt', 'r')#Программа
for i in range(dy):
    z=(piz.readline().strip()).split('\t')
    for j in range(dx):
        my_prog[i][j]=z[j]
 
print("матрица правил=\n",my_prog)
     

#Получение ключа по значению
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
#Словарь алфавита 
nun_alp={a:alphabet1[a-1]  for a in range(1,6)}

#Для задания
strelka=0#Стрелка в позиции 0
sostoyanie=1#Состояние q1 (Начальное)
mytask_=list(task1)[strelka]
stroka=list(task1)
u=0

while sostoyanie!=0:
    simvol=get_key(nun_alp, list(stroka)[strelka])
    if len(list(my_prog[simvol][sostoyanie] ))==1:
        decision.write("ОШИБКА!Отсуствует переход в программе!")
        sostoyanie=0
    else:
        new_symbol=list(my_prog[simvol][sostoyanie])[0] 
        transaction=list(my_prog[simvol][sostoyanie] )[1] 
        new_sostoyanie=list(my_prog[simvol][sostoyanie] )[2] 
        xex=sostoyanie
        xex2=stroka[strelka]
        stroka[strelka]=new_symbol
        decision.write(f"{u})\nЗадача={task1}\nГоловка в положении={strelka} \n")           
        decision.write(f"q{xex} {list(task1)[strelka]} ->q{new_sostoyanie} {stroka[strelka]}\n")
        if transaction==">":
            strelka+=1
        if transaction=="<":
            strelka-=1
        sostoyanie=int(new_sostoyanie)
        u+=1
        #decision.write(f"{u})Задача={task1},\nГоловка в положении={strelka},\nТекущее состояние={sostoyanie},\nТекущий Символ={list(task1)[strelka]},\nТекущее Правило={my_prog[simvol][sostoyanie]},\nTекущая строка={''.join(stroka)} \n ")           
        decision.write(f"Tекущая строка={''.join(stroka)}\n")  
        decision.write(f"Головка в положении={strelka}\n")  
        decision.write("\n________________________________________________________\n")
 
decision.write("Разбор завершен!")
print("\n\nРазбор завершен!")
decision.close()