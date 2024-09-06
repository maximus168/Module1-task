students={'Johny','Bilbo','Steve','Khendrik','Aaron'}
students_sort=sorted(students)
print(students_sort)
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
medium_grades=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
               sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),
               sum(grades[3])/len(grades[3])]
print(medium_grades)
class_journal=dict(zip(students_sort,medium_grades))
print('Оценки класса: ',class_journal)