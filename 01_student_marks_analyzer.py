'''1. 🎓 Student Marks Analyzer
👉 Features:
marks input lo
total, percentage nikaalo
pass/fail decide karo
topper find karo
👉 Extra add karo:
file me save karo'''

n = int(input("Enter your marks:"))

marks = []
for i in range(n):
    m = int(input(f"Enter marks of subject {i + 1}:"))
    marks.append(m)


print(marks)

total = sum(marks)
precentage  = total /  n

print("total:", total)
print("precentage:", precentage)

if precentage >= 40:
    print("pass")

else:
    print("Fail")

print("Topper Marks:", max(marks))

f = open("result.txt", "w")
f.write(f"marks: {marks}\n")
f.write(f"total: {total}\n")
f.write(f"precentage: {precentage}\n")

f.close()