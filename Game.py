import random
game=True
moves=10
tutorial=False
starts_stats=[]
stage_tutorial=0
tutorial_try=0
B=[[25],[11],[20],[6],[0]]
chapter=0
def m (n,m):
    return matrix[n][m]
def p (b):
    yelow(b)
def ammo (am,f):
    if m(2,am)!=0:
        matrix[2][am]-=1
        p(f)
        if am==1:
            if B[1][0]>=5:
                B[1][0]-=5
            else:
                change=random. randint(1,10)
                if change==1 and tutorial==False:
                    red('CRIT!')
                    B[0][0]-=15-int(B[1][0])
                    B[1][0]=0
                else:
                    B[0][0]-=5-int(B[1][0])
                    B[1][0]=0
        elif am==0:
            if B[1][0]>=1:
                B[1][0]-=1
            else:
                change=random. randint(1,10)
                if change==1 and tutorial==False:
                    red('CRIT!')
                    B[0][0]-=30
                else:
                    B[0][0]-=10
    else:
        p('not ammo')
def new_item (j,i): 
    matrix[j][i]+=1
def weapon_n (nomber):
    for i in '1','2':
        if nomber==i:
            if m(2,2)!=i:
                if i=='1':
                    p(f'you equip a bow')
                    i='bow'
                if i=='2':
                    p(f'you equip a gun')
                    i='gun'
            return i
    return m(2,2)
def unit ():
    B=[[],[],[],[],[]]
    n=3
    while n==3:
        n=random. randint(1,4)
        if n==1:
            write('Heavy fighter')
            hp= random. randint(30,50)
            arm= random. randint(4,6)
            atk= random. randint(25,40)
            rng= random. randint(2,4)
            B=[[hp],[arm],[atk],[rng],[n],[0]]
        elif n==2:
            write('Medium fighter')
            hp= random. randint(15,25)
            arm= random. randint(2,4)
            atk= random. randint(15,20)
            rng= random. randint(5,6)
            B=[[hp],[arm],[atk],[rng],[n],[0]]
        elif n==4:
            write('light  fighter')
            hp= random. randint(10,15)
            arm= random. randint(0,1)
            atk= random. randint(5,10)
            rng= random. randint(7,9)
            B=[[hp],[arm],[atk],[rng],[n],[0]]
    return B
def difficult (dif):
    if dif=='0':
        return 1
    elif dif=='1':
        return 2
    elif dif=='2':
        return 3
    else:
        print('No difficult')
        return 'not'
def red (text):
    print('\033[31m{}'.format(text))
def blue (text):
    print('\033[34m{}'.format(text))
def green (text):
    print('\033[32m{}'.format(text))
def yelow (text):
    print('\033[33m{}'.format(text))
def write (text):
    print('\033[36m{}'.format(text))
def texts (text):
    return ('\033[34m{}'.format(text))
def Boss():
    B=[[],[],[],[],[],[]]
    n=random. randint(1,3)
    if n==1:
        red('Dragon!')
        B=[[250],[50],[100],[10],[2],[1]]
    elif n==2:
        blue('Ogr!')
        B=[[500], [100], [150], [0], [1],[2]]
    elif n==3:
        green('Army!')
        B=[[150], [5], [50], [15], [4],[3]]
    return B
damage=0
move=0
yelow('no-tutorial, 0-easy, 1-medium, 2-hard, Boss')
Difference=input(texts('input difficulty:'))
if Difference == 'no':
    game=False
    tutorial=True
    green('You start tutorial about attack and defense')
elif Difference=='Boss':
    moves=20
    differ=1
    B=Boss()
    information_unit=f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range'
    red(information_unit)
    defence_damage=B[4][0]
else:
    differ= difficult(Difference)
    if differ=='not':
        game=False
    else:
        B= unit()
        defence_damage=B[4][0]
        B=[[int(B[0][0])*differ],[int(B[1][0])*differ],[int(B[2][0])*differ],[B[3][0]]]
        information_unit=f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range'
        green(information_unit)
NO=0
matrix=[[5,1,3],
        [5,100,10],
        [2,3,'no weapon']]
for i in range(0,4):
    starts_stats.append(B[i][0])
while game:
    if NO==0:
        write('--------------------------------------------------------------------------------------------')
        if -int(B[3][0])+moves-move!=0:
            blue(str(-int(B[3][0])+moves-move) + ' moves')
            fase=1
        else:
            blue('Warning')
            fase=2
        move+=1
        write('--------------------------------------------------------------------------------------------')
    NO=0
    a = input(texts('-'))
    matrix[2][2]=weapon_n(a)
    if a=="i":
        green(f'{m(0,0)} food, {m(0,1)} stones, {m(0,2)} mana potion')
        green(f'{m(1,0)} mana, {m(1,1)} helth, {m(1,2)} armor')
        green(f'{m(2,0)} arrow, {m(2,1)} bullet, {m(2,2)}')
        NO+=1
    elif a=="food":
        new_item(0,0)
        p('+ food')
    elif a=="arrow":
        new_item(2,0)
        p('+ arrow')
    elif a=="bullet":
        new_item(2,1)
        p('+ bullet')
    elif a=='shot':
        if matrix[2][2]=='bow':
            ammo(0,'shot!')
        elif matrix[2][2]=='gun':
            ammo(1,'fier!')
        else:
            print('weapon not equip')
    elif a=='eat':
        if m(0,0)>0:
            matrix[0][0]-=1
            p('Mmmmm...')
            matrix[1][1]+=10
        else:
            p('no food')
    elif a=='mana potions':
        new_item(0,2)
        p('+ mana potion')
    elif a=='stone':
        new_item(0,2)
        p('+ stone')
    elif a=='drink':
        if m(0,2)>0:
            matrix[0][2]-=1
            print('Bl-bl')
            matrix[1][0]+=20
        else:
            print('no potions')
    elif a=='healing':
        if m(1,0)>0:
            matrix[1][0]-=5
            print('mage!')
            matrix[1][1]+=20
        else:
            print('no mana')
    elif a=='armor':
        if m(0,1)>0:
            matrix[0][1]-=1
            print('stone power!')
            matrix[1][2]+=10
        else:
            print('no stones')
    elif a=='run':
        change=random. randint(1,defence_damage+differ)
        if change<=4-differ and fase==2:
            fase=1
            move=0
            yelow('Hop!')
    elif a=='end':
        print('You leave')
        game=False
    elif a=='hit':
        if B[1][0]>=3:
            B[1][0]-=3
        else:
            change=random. randint(1,5)
            if change==1:
                red('CRIT!')
                B[0][0]-=9-int(B[1][0])
                B[1][0]=0
            else:
                B[0][0]-=3-int(B[1][0])
                B[1][0]=0
        if move<-int(B[3][0])+moves-2-move:
            move+=1
        else:
            fase=2
    if B[5][0]==3:
        B[3][0]=B[0][0]/10
        B[3][0]=int(B[3][0])
        B[2][0]=B[0][0]/3
        B[2][0]=int(B[2][0])
    if B[0][0]<=0:
        write('--------------------------------------------------------------------------------------------')
        green('You win')
        game=False
        print(f'difficult {Difference}')
        write('--------------------------------------------------------------------------------------------')
        p(f'{m(0,0)} food, {m(0,1)} stones, {m(0,2)} mana potion')
        p(f'{m(1,0)} mana, {m(1,1)} helth, {m(1,2)} armor')
        p(f'{m(2,0)} arrow, {m(2,1)} bullet, {m(2,2)} weapon')
        red(f'The enemy had {starts_stats[0]} health, {starts_stats[1]} armor, {starts_stats[2]} attack power, {starts_stats[3]} range')
    if fase==2 and game==True and NO==0:
        damage=int(B[2][0])
        if matrix[1][2]>=damage*(2/defence_damage):
            matrix[1][2]-=damage*(2/defence_damage)
            matrix[1][2]=int(matrix[1][2])
        else:
            matrix[1][1]-=(damage*(2/defence_damage)-matrix[1][2])*defence_damage/2
            matrix[1][2]=0
            matrix[1][1]=int(matrix[1][1])
        move=0
        red('You were attacked!')
        if m(1,1)<=0:
            matrix[1][1]=0
        p(f'You have {m(1,1)} helth {m(1,2)} armor')
    if int(m(1,1))<=0:
        game = False
        yelow('--------------------------------------------------------------------------------------------')
        red('YOU DIE')
        yelow('--------------------------------------------------------------------------------------------')
        p(f'The enemy had {starts_stats[0]} health, {starts_stats[1]} armor, {starts_stats[2]} attack power, {starts_stats[3]} range')
        p(f'but you left {B[0][0]} health, {B[1][0]} armor')
    if game==True and NO==0:
        p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
while tutorial: 
    matrix=[[0,0,0],
            [0,100,10],
            [3,3,'no weapon']]
    if stage_tutorial==0:
        write('--------------------------------------------------------------------------------------------')
        write('Medium fighter')
        blue('you will be pposed by an opponent with the following characteristics:')
        information_unit=f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range'
        yelow(information_unit)
        write('--------------------------------------------------------------------------------------------')
        red('health')
        write('reduce this indicator to 0 to win')
        write('--------------------------------------------------------------------------------------------')
        blue('armor')
        write('break the shield so that you can reduce health')
        write('--------------------------------------------------------------------------------------------')
        yelow('attack power')
        write("opponent's damage indicator")
        write('--------------------------------------------------------------------------------------------')
        green('range')
        write("opponent's attack speed")
        write('--------------------------------------------------------------------------------------------')
        stage_tutorial+=1
    if stage_tutorial==1:
        if tutorial_try==0:
            blue(str(-int(B[3][0])+10-move) + ' moves')
            move+=1
            write("^ the nomber of moves before the opponent's attack")
            write("let's start with the attack")
            write('--------------------------------------------------------------------------------------------')
            write("enter '1' to choose a bow")
        a=input(texts('-'))
        if a=='1':
            matrix[2][2]=weapon_n(a)
            stage_tutorial+=1
            tutorial_try=0
        else:
            red("please, write '1'")
            tutorial_try+=1
    if stage_tutorial==2:
        if tutorial_try==0:
            blue(str(-int(B[3][0])+10-move) + ' moves')
            move+=1
            write("okay, now shot, fit 'shot'")
        a=input(texts('-'))
        if a=='shot':
            if matrix[2][2]=='bow':
                ammo(0,'shot!')
            elif matrix[2][2]=='gun':
                ammo(1,'fier!')
            else:
                print('weapon not equip')
            stage_tutorial=3
            tutorial_try=0
            p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
        else:
            red("please, enter 'shot'")
            tutorial_try+=1
    if stage_tutorial==3:
        write('--------------------------------------------------------------------------------------------')
        write('--------------------------------------------------------------------------------------------')
        green('against well-armored enemies, the bow is very bad')
        write('--------------------------------------------------------------------------------------------')
        stage_tutorial+=1
    if stage_tutorial==4:
        if chapter==0:
            if tutorial_try==0:
                blue(str(-int(B[3][0])+10-move) + ' moves')
                move+=1
                write('--------------------------------------------------------------------------------------------')
                yelow("now take the gun by typing '2'")
            a=input(texts('-'))
            if a=='2':
                matrix[2][2]=weapon_n(a)
                tutorial_try=0
                chapter+=1
            else:
                red("please, write '2'")
                tutorial_try+=1
        if chapter==1:
            if tutorial_try==0:
                blue(str(-int(B[3][0])+10-move) + ' moves')
                move+=1
                write("okay, now shot, fit 'shot'")
            a=input(texts('-'))
            if a=='shot':
                tutorial_try=0
                stage_tutorial+=1
                chapter=0
                if matrix[2][2]=='bow':
                    ammo(0,'shot!')
                    stage_tutorial+=1
                    chapter=0
                elif matrix[2][2]=='gun':
                    ammo(1,'fier!')
                p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
            else:
                red("please, write 'shot'")
                tutorial_try+=1
    if stage_tutorial==5:
        write('--------------------------------------------------------------------------------------------')
        write('--------------------------------------------------------------------------------------------')
        green('the gun works well against armored targets')
        write('--------------------------------------------------------------------------------------------')
        write('--------------------------------------------------------------------------------------------')
        stage_tutorial+=1
    if stage_tutorial==6:
        if tutorial_try==0:
            blue('finish off the armor')
        a=input(texts('-'))
        if a=='shot':
            ammo(1,'fier!')
            stage_tutorial+=1
            tutorial_try=0
            p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
        else:
            tutorial_try+=1
    if stage_tutorial==7:
        if tutorial_try ==0:
            write('--------------------------------------------------------------------------------------------')
            blue('Warning')
            write('--------------------------------------------------------------------------------------------')
            red('on this turn, after your actions, the enemy attact!')
            write('--------------------------------------------------------------------------------------------')
            blue("let's start taking away health")
            print(texts("enter 'shot' to attack"))
        a=input(texts('-'))
        if a=='shot':
                ammo(1,'fier!')
                tutorial_try=0
                stage_tutorial+=1
                p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
        else:
            tutorial_try+=1
            red("please, enter 'shot'")
    if stage_tutorial==8:
        damage=int(B[2][0])
        if matrix[1][2]>=damage:
            matrix[1][2]-=damage
            matrix[1][2]=int(matrix[1][1])
        else:
            matrix[1][1]-=(damage-matrix[1][2])
            matrix[1][2]=0
            matrix[1][1]=int(matrix[1][1])
        move=0
        red('You were attacked!')
        if m(1,1)<=0:
            matrix[1][1]=0
        p(f'You have {m(1,1)} helth {m(1,2)} armor')
        stage_tutorial+=1
        tutorial_try=0
    if stage_tutorial==9:
        write('--------------------------------------------------------------------------------------------')
        blue('if the opponent is "heavy", then he hits armor 2 times stronger, if "medium", then he hits armor the same way as health, if the opponent is "light", then he hits armor 2 times weaker')
        write('--------------------------------------------------------------------------------------------')
        stage_tutorial+=1
    if stage_tutorial==10:
        if chapter==0:
            if tutorial_try==0:
                yelow("enter '1' to select a bow")
            a=input(texts('-'))
            if a=='1':
                matrix[2][2]=weapon_n(a)
                tutorial_try=0
                chapter+=1
            else:
                tutorial_try+=1
        if chapter==1:
            if tutorial_try==0:
                blue("enter 'shot'")
            a=input(texts('-'))
            if a=='shot':
                ammo(0,'shot!')
                tutorial_try=0
                stage_tutorial+=1
                chapter=0
                p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
            else:
                tutorial_try+=1
    if stage_tutorial==11:
        write('--------------------------------------------------------------------------------------------')
        write('--------------------------------------------------------------------------------------------')
        blue('as result, the bow does not hit armor well, but it reduces heath well, and the cannon penetrates armor well, but is not very effective against opponents with a lot of health')
        write('--------------------------------------------------------------------------------------------')
        write('--------------------------------------------------------------------------------------------')
        stage_tutorial+=1
    if stage_tutorial==12:
        if tutorial_try==0:
            green('and finaly finish off the enemy')
        a=input(texts('-'))
        if a=='shot':
            ammo(0,'shot!')
            tutorial=False
            tutorial_try=0
            p(f'{B[0][0]} health, {B[1][0]} armor, {B[2][0]} attack power, {B[3][0]} range')
            green('you have completed tutorial in attack and defense')
        else:
            tutorial_try+=1
