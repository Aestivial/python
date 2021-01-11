reg=["10188","20788","10992"]
name=["Nayan","Aestivial","Dhiman"]
for i in  range(len(name)):
    print(reg[i]+name[i])
print("\n")
while True:
    print("Registration No.s:",reg)
    print("Names:",name)
    res=int(input('''Choose:
    1. Insert new data
    2. Delete existing data
    3. Update data\n'''))
    if res==1:
        r1=input("Enter new name:")
        name.append(r1)
        r2=input("Enter new registration number:")
        reg.append(r2)
    elif res==2:
        r1=int(input("Which index number to delete?\n"))
        name.remove(name[r1])
        reg.remove(reg[r1])
    elif res==3:
        r1=int(input("Which index number to update?\n"))
        r2=input("Enter new name:")
        r3=input("Enter new reg no.")
        reg[r1]=r3
        name[r1]=r2
    else:
        print("Invalid Input")
        break
