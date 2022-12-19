persons = { '张三':30.6, '李四':23, '王五':11.2, '唐六':10.2, }
print(list(filter(lambda x: persons[x] > 18, persons)))
