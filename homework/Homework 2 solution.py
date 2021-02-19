"""
Day-3:
Write a program that includes information about the grades of 5 students in a school.
- Keep these students' grades in a list. (Midterm, final, homework)
- Keep students' names in a list. (Name, surname)
- Create a dictionary named info and put all the information of students in a dictionary.
- Sort and list the students' grades here in descending order and congratulate the student with the highest score.
"""
midterm = [100,79,56,34,23]
final = [93,75,33,56,77]
homework = [78,76,45,23,30]
ortalama = [0,0,0,0,0]
names = ["Sıla Çetinkaya","Erman Yalçın","Mahmut Kaya","Murat kekilli","Rukiye ayvaz"]
info = {names[0]: [midterm[0],final[0],homework[0]], names[1]: [midterm[1],final[1],homework[1]],names[2]: [midterm[2],final[2],homework[2]],names[3]: [midterm[3],final[3],homework[3]],names[4]: [midterm[4],final[4],homework[4]]}
print("Notlar: Midterm -- Final -- Homework")
print("1. {} = {}\n2. {} = {}\n3. {} = {}\n4. {} = {}\n5. {} = {}\n".format(names[0],info[names[0]],names[1],info[names[1]],names[2],info[names[2]],names[3],info[names[3]],names[4],info[names[4]]))
for i in range(0,5):
    ortalama[i] = midterm[i] + final[i] + homework[i]
    ortalama[i] = ortalama[i]/3
print("ortalama:")
info2 = {names[0]: ortalama[0], names[1]: ortalama[1], names[2]: ortalama[2], names[3]: ortalama[3], names[4]: ortalama[4]}
print("1. {} = {}\n2. {} = {}\n3. {} = {}\n4. {} = {}\n5. {} = {}\n".format(names[0],info2[names[0]],names[1],info2[names[1]],names[2],info2[names[2]],names[3],info2[names[3]],names[4],info2[names[4]]))
ortalama.sort()
print("ortalama after sort: {}\n".format(ortalama))
print("congratulations:",names[0])

