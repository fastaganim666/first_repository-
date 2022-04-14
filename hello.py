any_list = ['2018-01-01', 'yandex', 'cpc', 100, 1, 23234444232]
size_list = len(any_list)
if size_list == 1:
    any_dict = {any_list[0]: None}
else:
        any_dict = {any_list[-2]: any_list[-1]}
i = 2
while i < size_list:
    i+=1
    any_dict = {any_list[-i]: any_dict}
print(any_dict)