age_alowed = True
def yes():
    age_alowed = True
def no():
    print('not alowed')
    quit()
def _():
    print(" do not valid try again")
    quit()

match input("are you above 18 ?, answer by yes or no : "):
    case 'yes':
       yes() 
    case "no":
        no()
    case _:
        _()

if age_alowed:
    print("alowed")

print('hi welcome')
print('my name is alie' )
name = input('do u mind sharing your name?: ')
print('hiiii ' + name + ', today im traying to make my data the biggest holding place of infotmation' )
print('can u help with that ?')
print('if u can please enter your age , hight , birth of year , and what countrie you live in ')
date_of_birth = input('date of birth: ')
age = 2024 - int(date_of_birth)
print(age)
hight = input("what's your hight in cm ?: ")
print( hight + ' CM')
location = input('where do you live?: ')
print('ohhhh ' + location + ' we have about 3.095% of morocan people on our webcite welcom with them ')
def yes():
    print('ohhhh glad that you like it in here, ither way thank you for all the information ')
def no():
    print('ohhh im sorry for your experince with us ')
    input("what u didn't like ?: ")
def _():
    print('ply ansewr by yes or no ')
match input('do you like your experience in our setup , ansewr by yes or no : '):
    case 'yes':
        yes()
    case 'no':
        no()
    case _:
        _()









