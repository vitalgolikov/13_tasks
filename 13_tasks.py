# 1. Дано целое число (int). Определить сколько нулей в этом числе.
#value = 4343230534535230
#str_value = str(value)
#print(str_value.count('0'))

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
value = 1002000
str_value = str(value)
zero_collection = []
for symbol in str_value[::-1]:
    if symbol == "0":
        zero_collection.append(symbol)
    else:
        break
print(len(zero_collection))

#3. Даны списки my_list_1 и my_list_2.
#Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1,3,6,"t",24,2]
my_list_2 = [5,6,5,3,5,3,5]
my_result = []
my_result.extend(my_list_1[1::2])
my_result.extend(my_list_2[::2])
print(my_result)

#4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
#стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1,2,3,4]
new_list = my_list[1:]+my_list[:1]
print(new_list)

#5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
#[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1,2,3,4]
my_list.append(my_list[0])
my_list.pop(0)
print(my_list, id(my_list))

#6. Дана строка в которой есть числа (разделяются пробелами).
#Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
#Для данного примера ответ - 133. (используйте split и проверку isdigit)

my_string = "43 34 56"
my_digi = my_string.split()
summa = 0
for digi in my_digi:
    if digi.isdigit():
        summa += int(digi)
print(summa)

#7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
#которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
#В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
#my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)

my_str = "My long string"
l_limit = "o"
r_limit = "g"
l_limit = my_str.find(str(l_limit))
r_limit = my_str.rfind(str(r_limit))
sub_str = my_str[l_limit+1:r_limit]
print(sub_str)

#8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
#быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
#(используйте срезы длинны 2)
#my_str = "wfefwrgregregrw"
#for symbol in my_str:

my_str = "gsrgrsgrsgd"
my_str_list = []
index = 0
for _ in range(len(my_str)):
    my_str_list.append(my_str[index:index+2])
    index += 2
    if index > len(my_str) - 1:
        break
if len(my_str_list[-1]) == 1:
    my_str_list[-1] = my_str_list[-1]+"_"
print(my_str_list)


# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2,4,1,5,3,9,0,7]
counter = 0
index = 0
for num in my_list[1:-1]:
    if num > my_list[index] + my_list[index + 2]:
        counter += 1
    index += 1
print(counter)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]
my_result = []
for item in my_list:
    if type(item) == str:
        my_result.append(item)
print(my_result)


#11. Дана строка my_str. Создать список в который поместить те символы из my_str,
#которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = "vrwgvrebgerbeeeeerbfg123"
my_str_unic = []
for symbol in set(my_str) :
    if my_str.count(symbol)==1:
        my_str_unic.append(symbol)
print(my_str_unic)

#12. Даны две строки. Создать список в который поместить те символы,
#которые есть в обеих строках хотя бы раз.

my_str_1 = "gww4rgeq5r5hg5g"
my_str_2 = "rbetbetbhetbhetbnetb"
result_list = list(set(my_str_1).intersection(my_str_2))
print(result_list)

#13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
#но в каждой ТОЛЬКО ПО ОДНОМУ разу.
#Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaasdf1"
my_str_2 = "asdfff2"
count_uniq = 0
unic_my_str_1_symbols = []
unic_my_str_2_symbols = []
for symbol in my_str_1:
    if my_str_1.count(symbol)==1:
        unic_my_str_1_symbols.append(symbol)
for symbol in my_str_2:
    if my_str_2.count(symbol)==1:
        unic_my_str_2_symbols.append(symbol)
result_list = list(set(unic_my_str_1_symbols).intersection(unic_my_str_2_symbols))
print(result_list)