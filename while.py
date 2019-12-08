# run = 'y'
# while run == 'y':
#     print ('hey!')
#     run = input('keep going (y/n)?')

numberchain = 0
response = 'y'
while response == 'y':
    num = int(input("How many numbers: "))
    
    for i in range(numberchain, numberchain+num):
        print(i)

    numberchain += num
    response = input("continue? (y/n)")
