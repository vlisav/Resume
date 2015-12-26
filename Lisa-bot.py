print ("Hello Stranger!")

name1 = "Lisa"


print ("My name is ", name1)
name2 = input("What is your name? ")

print ("Hello", name2, "!")
mood = input("How are you today? ")

if mood == "good":
    print("Awsome!")
else:
    print("Oh, that didnt sound good")

answer1 = input("I just learned how to count to 10! Can i show you? ").lower()
if answer1 == "yes":
    for i in range(0,10):
        print (i+1)
else:
    print("Youre mean!")

cars =["volvo","audi","ford","golf","ferarri","honda","bmw","lambourgini","skoda"]


print("i have a top 9 list of my favourite cars!")
car = input("What is your favourite car?").lower()

if car in cars:
    print("That is my",cars.index(car)+1,"favourite car!")
