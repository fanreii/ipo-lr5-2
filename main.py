listt1=input("Введите первую строку:")
listt2=input("Введите вторую строку:")
sort_list1 = sorted(listt1.lower())
sort_list2 = sorted(listt2.lower())
if sort_list1 == sort_list2:
    print("Строки анаграммны")
else:
    print("Строки не анаграммны")