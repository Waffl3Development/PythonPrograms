def standardFunction(text):
    text = "hello world!"
    print(text)

if x < 0:
    x = 0
    print(x)


Compare = 10
hello(Compare)#hello (10)

def hello(just): #hello(10)
    match just:
        case 1:
            return "this is a " + just
        case 10:
            print("this is a 10")




HOUSE = 5 + 7 #12
print(HOUSE)

print("5" + 7) #57

something = "string"

5 + 5 #int 1
5 - 5 #int 1
5 * 5 #int 1
5 / 5 #float 1.0
5 // 5 #int 1 floor down to nearest whole number

word = "sorry"
word[0] #s
word[-1] #y
word[2:] #orry
word[:2] #so

variable = [1, 4, 5, 6] #global used in a lot of other languages
variable[0] #1

# while x < 0 statements
u = 0
while u < 10:
    u = u + 1 #u++
            #Most often used ++u
for i in variable: #i is a number
    print(i)    #1
                #4
                #5
                #6
for i in range(5): #i is 0
    print(i)
#0
#1
#2
#3
#4

u=0
r=0
while u < 5:#0
    while r < 10:#10
        print(u,r)
        #0,0
        #0,1
        #0,2

        r = r + 1
    u = u + 1
