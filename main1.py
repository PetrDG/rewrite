import os

def rw_file():
    # os.chdir('sorted')
    path = os.getcwd()
    files_list = os.listdir(path)
    data = {}
    for file in files_list:
        if file.endswith('.txt'):
            with open(file, encoding='utf-8') as f:
                lines = f.read()
                with open(file, encoding='utf-8') as f:
                    f_name = f.name
                    count = sum(1 for line in f)
                data[f_name] = (count, lines)
                sorted_keys = sorted(data, key=data.get)
                sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = data[w]

    os.chdir('sorted')
    with open('Итог.txt', 'w', encoding='utf-8') as f:
        for i in sorted_dict.items():
            first = str(i[0])
            second = str(i[1][0])
            third = str(i[1][1])

            f.writelines(first + '\n')
            f.writelines(second + '\n')
            f.writelines(third + '\n')
            f.writelines('\n')

rw_file()





