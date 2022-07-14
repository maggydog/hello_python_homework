# Проверить истинность логического утверждения
x=False
y=False
z=True

if not(x or y or z)==(not x and not y):
    print('True')
else:
    print('False')