import os
import Task1, Task2, Task3, Task4, Task5
Task = 0
List1 = ['1. Число "пи" с заданной точностью d.',
         '2. Разбить число на множители.',
         '3. Ряд уникальных чисел из списка.',
         '4. Запись многочлена в файл.',
         '5. сумма двух многочленов в результирующий файл.',
         '6. Выход']
os.system('cls')

def enter_key_to_continue():
    input("\033[0m{}".format('=================================================\nДля продолжения нажмите клавишу [ENTER]'))
    main()
def error(x):
    os.system('cls')
    print("\033[37m\033[41m{}".format('\n                                       '
                              '\n              ОШИБКА!!!                '
                              '\n  Вы ввели не существующую команду...  '
                              '\n      Выберите команду из списка.      '
                              '\n                                       '))
    enter_key_to_continue()
def inputdata(inputcomment):
    d = input("\033[0m{}".format(f'{inputcomment} ->  '))
    return d
def printres(res):
    print("\033[32m{}".format(f'==============================================================\n'
                   f'    {res}\n'
                   f'=============================================================='))
    print("\033[0m{}".format(''))

def choice(x):
    os.system('cls')
    if x <= len(List1):
        print("\033[33m{}".format(f'=================================================\n{List1[x-1]}\n================================================='))
    if x == 1:
        printres(Task1.round_pi(str(inputdata('Введите число в формате 0.001, (с любым количеством знаков после запятой)'))))
        enter_key_to_continue()
    elif x == 2:
        printres(Task2.Multiplier(int(inputdata('Введите целое число'))))
        enter_key_to_continue()
    elif x == 3:
        list1 = Task3.listgen(int(inputdata('Укажите размер генерируемого ряда чисел')))
        printres(f'исходный ряд чисел: {list1}\n    результат: {Task3.uniquelist(list1)}')
        enter_key_to_continue()
    elif x == 4:
        pol = Task4.polinom_gen(int(inputdata('Введите степень "k" (целое число)')))
        # записать певый файл для следующего задания
        Task4.save_to_file(pol, str(inputdata('Введите название файла)')))
        printres(f'Был сгенерирован многочлен, ({pol}) и записан в файл.')
        enter_key_to_continue()
    elif x == 5:
        enter_key_to_continue()
    elif x == 6:
        os.system('cls')
        print("\033[0m{}".format('Выход из программы...'))
        import sys
        sys.exit()
    else:
        error(Task)
def main():
    os.system('cls')
    print("\033[32m{}".format('================================================\n============ Г Л А В Н О Е  М Е Н Ю ============\n================================================'))
    print("\033[33m{}".format('Выберите действие...'))
    print(*List1, sep='\n')
    print("\033[32m{}".format('================================================'))
    try:
        Task = int(input("\033[0m{}".format('Введите номер операции ->  ')))
    except:
        Task = 0
    choice(Task)

main()