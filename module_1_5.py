immutable_var = (777,'Rickitir',bool)
print(immutable_var)
print(immutable_var[1])
# immutable_var[0] = 888
# так как картеж не подерживает обращения по элементам.
mutable_list = ['лист','ручка','карандаш']
print(mutable_list)
mutable_list[2] = 'чернила'
print(mutable_list)