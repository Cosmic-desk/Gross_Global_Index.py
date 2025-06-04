import mysql.connector as year

city = year.connect(host="localhost", user="root", passwd="AlphaV@3", database="gross_global_index")
y = city.cursor()
if city.connect:
    print('yes successful')


# ADDING A DATA
def adding():
    tablename = input('enter the name of the table as of format _year')
    y.execute('show tables')
    dt = y.fetchall()

    table = 'CREATE TABLE IF NOT EXISTS {} ( NAME VARCHAR(20) NOT NULL,NCODE INT(8) NOT NULL PRIMARY KEY, GDP DECIMAL(9,4), \
     GNP DECIMAL(9,4), IMPORTS DECIMAL(9,4),EXPORTS DECIMAL(9,4), LITERACY_RATE DECIMAL(9,4),LIFE_EXPECTANCY_RATE DECIMAL(9,4))'.format(
        tablename)
    y.execute(table)
    new_entry = int(input('enter the no. of data to be added'))

    for i in range(new_entry):
        print('This is entry number', i + 1)
        NAME = str(input('enter the name of the nation'))

        print(
            "the code value should be entered if that nation code value is not already present,if already present it won't be asked")
        for n in dt:
            tname = n[0]

            a = 0

            s = "SELECT NAME,NCODE FROM {}".format(tname)
            y.execute(s)
            z = y.fetchall()

            # traversing through table data & observing if ncode value is present if it is then continuing if not then asking from user
            for p in range(len(z)):
                NAME = NAME.lower()
                l = z[p][0]
                b = l.lower()
                if NAME == b:
                    a = 2
                    ncode = z[p][1]
                    print('ncode value already present.')
                    print('VALUE TAKEN')
                    break

            if a == 2:
                break
            else:
                continue

        else:
            print('no previous entry of this data so')
            ncode = int(input('enter the ncode value'))

        GDP = float(input('enter the value gross domestic product as percentage'))
        GNP = float(input('enter the value of GNP in trillion $'))
        IMPORTS = float(input('enter the value of imports as percentage'))
        EXPORTS = float(input('enter the value of  EXPORTS as percentage'))
        LITERACY_RATE = float(input('enter the value literacy rate as percentage'))
        L = float(input('enter the value of life expectancy as percentage'))
        add = "INSERT INTO {} VALUES ('{}',{},{},{},{},{},{},{})".format(tablename, NAME, ncode, GDP, GNP, IMPORTS,
                                                                         EXPORTS, LITERACY_RATE, L)
        y.execute(add)
        print('THE DATA HAS BEEN SUCCESFULLY ADDED')
        y.execute("COMMIT")
    print('~' * 148)


# GrossGlobalIndex


def dispGGI():
    tablename = input('ENTER TABLE NAME AS FORMAT _YEAR')
    y.execute('select * from {}'.format(tablename))
    d = y.fetchall()
    print("| {0:15}".format('NAME'), end="       ")  # to print column headings
    print("| {0:7}".format('NCODE'), end="             ")
    print("| {0:9}".format('GDP'), end="            ")
    print("| {0:9}".format('GNP'), end="      ")
    print("| {0:9}".format('EXPORTS'), end="         ")
    print("| {0:9}".format('IMPORTS'), end="         ")
    print("| {0:9}".format('LITERACY_RATE'), end="     ")
    print("| {0:9}".format('LIFE_EXPECT_RATE'), ' ', end="|\n")
    print('*' * 184)
    for i in d:
        '''if i==2:
         space=' '*10
        else:'''
        for p in i:
            p = str(p)
            let = ' '
            space = 10 - len(p)
            space = let * space
            print("| {0:15}".format(p), end=space)
        print('|', end='\n')

    print('*' * 184)
    print('~' * 184)


# UPDATE A DATA

def updateyear():
    tb = input("ENTER TABLE NAME FOR UPDATION OF DATA OF FORMAT '_YEAR'")
    name = input("ENTER THE NAME OF THE NATION WHOSE DATA NEEDS TO BE UPDATED ")
    print("SELECT THE DATA TO BE UPDATED")
    print('ENTER THE NO. FROM THE MENU OF YOUR INTEREST FOR UPDATION')
    print('1.GDP', '2.GNP', '3.EXPORTS', '4.IMPORTS', '5.LITERACY RATE', '6.LIFE EXPECTANCY RATE', sep='\n')
    choice = int(input())
    if choice == 1:
        val = float(input('Enter the new value'))
        sayme = 'GDP'
    if choice == 2:
        val = float(input('Enter the new value'))
        sayme = 'GNP'
    if choice == 3:
        val = float(input('Enter the new value'))
        sayme = 'EXPORTS'
    if choice == 4:
        val = float(input('Enter the new value'))
        sayme = 'IMPORTS'
    if choice == 5:
        val = float(input('Enter the new value'))
        sayme = 'LITERACY_RATE'
    if choice == 6:
        val = float(input('Enter the new value'))
        sayme = 'LIFE_EXPECTANCY_RATE'
    up = "UPDATE {} SET {}={} WHERE name='{}'".format(tb, sayme, val, name)
    y.execute(up)
    print('THE DATA HAS BEEN UPDATED SUCCESFULLY')
    y.execute("COMMIT")
    print('~' * 128)


# DISPLAYING YEARLY DATA
def onenation():
    y.execute('show tables')
    z = y.fetchall()
    k = ()
    bbc = 0
    lst = []
    for i in z:
        kbc = ''
        tname = i[0]
        y.execute('select ncode,name from {}'.format(tname))
        ami = y.fetchall()
        for j in ami:
            k = k + j
            for p in k:
                if p not in lst:
                    lst.append(p)
    space = ' '
    space = space * 30
    espace = 10 * space
    bless = space + '|'
    print("| {0:7}".format('Ncode'), end="    |     ")
    print("{0:15}".format('name'), end="|\n")
    print('-' * 39)
    for i in lst:
        if type(i) == int:
            ncode = i
            print("| {0:7}".format(ncode), end="    |     ")
        else:
            name = i
            if len(i) <= 5:
                print("{0:15}".format(name), end="      |\n")
            else:
                print("{0:15}".format(name), end="|\n")
    print('ON THE BASIS OF ABOVE NCODE VALUES SELECT YOUR PREFERENTIAL NATION FOR GROSS INDEX OVER THE PAST YEARS')
    d = int(input('enter the ncode for the nation'))
    y.execute('show tables')
    dt = y.fetchall()
    for i in dt:
        ep = i[0]
        y.execute('SELECT NAME FROM {} WHERE NCODE={}'.format(ep, d))
        yname = y.fetchall()
        if yname != []:
            print('THIS IS THE ANNUAL PERFORMANCES OF THE NATION', yname[0][0].upper(), 'OVER THE YEARS')
            break
    print("| {0:9}".format('YEAR'), end="       ")
    print("| {0:9}".format('NCODE'), end="        ")
    print("| {0:9}".format('GDP'), end="           ")
    print("| {0:9}".format('GNP'), end="       ")
    print("| {0:9}".format('EXPORTS'), end="     ")
    print("| {0:9}".format('IMPORTS'), end="      ")
    print("| {0:9}".format('LITE_RATE'), end="    ")
    print("| {0:9}".format('LIFE_EXPECTANCY'), '   ', end="|\n")
    print('*' * 220)
    for i in dt:
        ep = i[0]

        sql = 'select * from {} where ncode={}'.format(ep, d)
        y.execute(sql)
        ct = y.fetchall()
        for c in ct:
            print("| {0:9}".format(ep), end='          ')
            foe = 0
            for p in c:
                foe = foe + 1
                let = ' '
                p = str(p)
                space = 15 - len(p)
                space = let * space
                if foe > 1:
                    print("| {0:9}".format(p), end=space)
            print('             ', '|', end='\n')
    print('*' * 220)
    print('~' * 148)


# RANKLIST ON THE PREFERENCIAL CRITERIA

def ranklist():
    tablename = input('enter the name of the table as of format _year')
    print('SELECT PREFERENTIAL CRITERIA FOR RANKLIST')
    print('1.ECONOMY', '2.LITERACY', '3.HEALTH', '4.MARKET VALUE', sep='\n')
    c = int(input())
    if c == 1:
        sel = 'GDP'
    if c == 2:
        sel = 'LITERACY_RATE'
    if c == 3:
        sel = 'LIFE_EXPECTANCY_RATE'
    if c == 4:
        sel = 'EXPORTS'
    order = 'SELECT NAME,{} FROM {} ORDER BY {} desc'.format(sel, tablename, sel)
    y.execute(order)
    b = y.fetchall()
    print("| {0:9}".format('RANK'), end="           |")
    print("| {0:9}".format('NAME'), end="               |")
    print("| {0:9}".format(sel), end="               |\n")
    a = 0
    for i in b:
        a = a + 1
        print("| {0:9}".format(a), end="           |")
        for l in i:
            if type(l) == str:
                let = ' '
                l = str(l)
                space = 20 - len(l)
                space = let * space
                print("| {0:9}".format(l), end=space + "|")
            else:
                l = str(l)
                space = 20 - len(l)
                space = let * space
                print("| {0:9}".format(l), end=space + "|\n")
    print('~' * 148)


# DELETION BASED ON NCODE VALUE
def delete():
    print('this program will delete the entire row for the mentioned ncode')
    tablnam = input('ENTER NAME OF THE TABLE FOR DELETION OF THE DATA')
    y.execute('show tables')
    z = y.fetchall()
    k = ()
    lst = []
    for i in z:
        kbc = ''
        tname = i[0]
        y.execute('select ncode,name from {}'.format(tname))
        ami = y.fetchall()
        for j in ami:
            k = k + j
            for p in k:
                if p not in lst:
                    lst.append(p)
    space = ' '
    space = space * 30
    espace = 10 * space
    bless = space + '|'
    print("| {0:7}".format('Ncode'), end="    |     ")
    print("{0:15}".format('name'), end="|\n")
    print('-' * 39)
    for i in lst:
        if type(i) == int:
            ncode = i
            print("| {0:7}".format(ncode), end="    |     ")
        else:
            name = i
            if len(i) <= 5:
                print("{0:15}".format(name), end="      |\n")
            else:
                print("{0:15}".format(name), end="|\n")
    print('from the table enter the ncode value after looking for the data of your interest for deletion ')
    ncode = int(input('GIVE THE VALUE'))
    y.execute("DELETE FROM {} WHERE ncode={}".format(tablnam, ncode))
    print('DATA SUCCESFULLY DELETED')
    y.execute("COMMIT")


# PROJECT FRONT PAGE

def firstpage():
    project = "GROSS GLOBAL INDEX"
    space = ' '

    print("\n" * 4)
    print(space * 20 + '*' * 38)
    space = ' '
    print(space * 20 + '*' + space * 9 + project + space * 9 + '*')
    print(space * 20 + '*' * 38)

    print("\n" * 4)
    print(space * 40 + "Prepared by :")
    print('\n' * 2)
    print(space * 50 + "AVANI SHARMA             \n")
    print(space * 50 + "ADM NO.=23JE0185     \n")

    print("Press any key to continue".center(125))
    ch = input()


# MAIN PROGRAM

firstpage()

print("#" * 100)
print("\n")

while (1):
    print('THIS IS THE MAIN MENU')
    print("\n")
    print("@" * 148)
    print(
        "@                                                                                                                                        @")
    print()
    print(
        "@   1. ADD A YEAR BASED NATION'S DATA                                                                                                    @")
    print('~' * 148)
    print(
        "@   2. DISPLAY GROSS GLOBAL INDEX FOR THE GIVEN YEAR                                                                                     @")
    print('~' * 148)
    print(
        "@   3. UPDATE A NATION'S DATA FOR THE GIVEN YEAR                                                                                         @")
    print('~' * 148)
    print(
        "@   4. DISPLAYING A PARTICULAR NATION'S DATA OVER ALL THE YEARS FOR COMPARITIVE ANALYSIS OF THE STATE OF IMPROVISATION                   @")
    print('~' * 148)
    print(
        "@   5.RANKLIST OF NATION'S ANNUAL PERFORMANCE GLOBALLY                                                                                   @")
    print('~' * 148)
    print(
        "@   6. DELETING A PARTICULAR NATION'S DATA FOR THE GIVEN YEAR                                                                            @")
    print('~' * 148)
    print(
        "@   7. EXIT                                                                                                                              @")
    print('~' * 148)
    print("@" * 148)
    print("\n")

    choice = int(input("Enter your Choice :  "))
    print()
    if choice == 1:
        adding()
        ch = input('PRESS ENTER TO PROCEED')
    elif choice == 2:
        dispGGI()
        ch = input('PRESS ENTER TO PROCEED')
    elif choice == 3:
        updateyear()
        ch = input('PRESS ENTER TO PROCEED')
    elif choice == 4:
        onenation()
        ch = input('PRESS ENTER TO PROCEED')
    elif choice == 5:
        ranklist()
        ch = input('PRESS ENTER TO PROCEED')
    elif choice == 6:
        delete()
        ch = input('PRESS ENTER TO PROCEED')

    elif choice == 7:

        print("you are out of project")
        break
    else:
        print("Sorry ,wrong choice.Press any key to exit")
        ch = input()
        break
y.close()



