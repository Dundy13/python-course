import os

current_directory = os.getcwd()
print("Текуща работна директория:", current_directory)

directory_path = "."
file_list = os.listdir(directory_path)
print("Списък на файлове в директорията")
for file_name in file_list:
    print(file_name)

path_to_check = "path/to/check"
if os.path.exists(path_to_check):
    print('Path exist')
else:
    print('Path does not exist')


new_file_path = 'new_file.txt'
with open(new_file_path, "w") as new_file:
    new_file_path
print('Създаване на нов файл с път')


file_to_delete = "file_to_delete.txt"
os.remove('new_file.txt')
print('Файлът беше изтрит')

