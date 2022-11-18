num = int(input('Enter a number!:'))

va = 'va'

Yekan = ['', 'yek', 'do', 'seh', 'chahar',
         'pang', 'shesh', 'haft', 'hasht', 'noh']
dahtabist = ['', 'yazdah', 'davazdah', 'sizdah', 'chahardah',
             'panzdah', 'shanzdah', 'hevdah', 'hejdah', 'nozdah']
Dahgan = ['', 'dah', 'bist', 'si', 'chehel',
          'pangah', 'shast', 'haftad', 'hashtad', 'navad']
sadgan = ['', 'sad', 'devist', 'sisad', 'chaharsad',
          'pansad', 'sheshsad', 'haftsad', 'hashtsad', 'nohsad']
hezar = 'hezar'

if 0 < num < 10:
    print(Yekan[num])

elif 10 < num < 20:
    print(dahtabist[(num - 10)])

elif 0 < num < 100 and num % 10 == 0:
    print(Dahgan[(num // 10)])

elif 20 < num < 100 and num % 10 != 0:
    print(Dahgan[(num // 10)], va, Yekan[num % 10])


#########  sadgan  #########

elif 99 < num < 1000 and num % 100 == 0:
    print(sadgan[(num // 100)])

elif 99 < num < 1000 and num % 100 != 0:
    if (num % 100) // 10 == 0:
        print(sadgan[(num // 100)], Dahgan[(num %
              100) // 10], va, Yekan[num % 10])

    elif (num % 100) // 10 != 0 and 10 < (num % 100) < 20:
        print(sadgan[(num // 100)], va, dahtabist[(num % 100)-10])

    elif (num % 100) // 10 != 0 and (num % 10) == 0:
        print(sadgan[(num // 100)], va,
              Dahgan[(num % 100) // 10], Yekan[num % 10])
    else:
        print(sadgan[(num // 100)], va,
              Dahgan[(num % 100) // 10], va, Yekan[num % 10])


########  hezar  #########

elif 999 < num < 10000 and (num % 1000) // 100 == 0 and (num % 100) // 10 == 0 and (num % 10) == 0:
    print(Yekan[(num // 1000)], hezar)

elif 1000 < num < 10000:
    if (num % 1000) // 100 == 0 and ((num % 1000) % 100) // 10 != 0 and ((num % 1000) % 100) > 20 and (num % 10) != 0:
        print(Yekan[(num//1000)], hezar, va, sadgan[(num % 1000) //
              100], Dahgan[(num % 100) // 10], va, Yekan[num % 10])
    elif (num % 1000) // 100 == 0 and ((num % 1000) % 100) // 10 == 0:
        print(Yekan[(num//1000)], hezar, sadgan[(num % 1000) // 100],
              va, Dahgan[(num % 100) // 10], Yekan[num % 10])
    elif (num % 1000) // 100 != 0 and ((num % 1000) % 100) // 10 == 0:
        print(Yekan[(num//1000)], hezar, va, sadgan[(num % 1000) //
              100], Dahgan[(num % 100) // 10], va, Yekan[num % 10])

    elif (num % 1000) // 100 == 0 and ((num % 1000) % 100) // 10 != 0 and 10 < ((num % 1000) % 100) < 20:
        print(Yekan[(num//1000)], hezar, va,
              dahtabist[(num // 10) - ((num // 10) - (num % 10))])

    elif (num % 1000) // 100 == 0 and ((num % 1000) % 100) // 10 != 0 and ((num % 1000) % 100) < 10:
        print(Yekan[(num//1000)], hezar, sadgan[(num % 1000) // 100],
              va, Dahgan[(num % 100) // 10], Yekan[num % 10])
    elif (num % 1000) // 100 == 0 and ((num % 1000) % 100) // 10 != 0 and (num % 10) == 0:
        print(Yekan[(num//1000)], hezar, sadgan[(num % 1000) // 100],
              va, Dahgan[(num % 100) // 10], Yekan[num % 10])
    elif (num % 1000) // 100 != 0 and (num % 100) == 0 and (num % 10) == 0:
        print(Yekan[(num//1000)], hezar, va, sadgan[(num % 1000) //
              100], Dahgan[(num % 100) // 10], Yekan[num % 10])
    else:
        print(Yekan[(num//1000)], hezar, va, sadgan[(num % 1000) //
              100], va, Dahgan[(num % 100) // 10], va, Yekan[num % 10])
elif num == 10000:
    print('dah hezar')
else:
    print('your number is incorrect!!')















    # MATIN ARJOMANDMANESH #
