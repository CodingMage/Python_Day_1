import random
rps_list = ['r', 'p', 's']
def rps_game(me, cpu):
    if (me == 'r' and cpu == 'r') or (me == 's' and cpu == 's') or (me == 'p' and cpu == 'p'):
        return 'tied'
    elif (me == 'r' and cpu == 's') or (me == 's' and cpu == 'p') or (me == 'p' and cpu == 'r'):  
        return 'win'
    else: 
        return 'lost'
for i in range(10):
    me = input('please input r/p/s: ')
    cpu = rps_list[random.randint(0,2)]
    result = rps_game(me, cpu)
    print(result)


