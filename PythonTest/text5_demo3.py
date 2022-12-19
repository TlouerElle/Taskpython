names = [['Tom ', 'Billy ', 'Jefferson ', ' Andrew ', 'Wesley ', 'Steven ', 'Joe '],
         ['Alice ', 'Jill ', 'Ana ', 'Wendy ', ' Jennifer ', 'Sherry ', 'Eva ']]
alter_names = names[0] + names[1]
print([alter_names[i] for i in range(0,len(alter_names)) if alter_names[i].count('e') == 2])


