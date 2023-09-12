num_students = 1
while(num_students<=40):
    total = 0
    subject = 1
    while(subject<=2):
        marks = int(input("Enter marks for subject "+ str(subject) +" : "))
        total = total + marks
        subject+=1
    avr = total/5
    if(avr>= 50):
        print("Student",num_students,"has passed")
    else:
        print("Student",num_students,"has failed")
    num_students+=1