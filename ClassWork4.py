import sys

python_version = sys.version
print('Версията на Python')


platform_info = sys.platform
print('Информация за платформата')


if "sys" in sys.modules:
    print("Библиотеката sys е заредена")
else:
    print("Библиотеката sys не е заредена")


system_path = sys.path
print("Системен път")
for path in system_path:
    print(path)