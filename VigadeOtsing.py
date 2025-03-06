print("*** Numbri mang ***")
print()

while True:
    try:
        a = abs(int(input("Kirjuta taisarv => ")))
        break
    except ValueError:
        print("Viga, se ei ole tais arv")

if a == 0:
    print("Nulliga pole mõtet midagi ette võtta.")
else:
    try:
        print("Teeme kindlaks, kui palju paaris ja mitu paaritu numbrit on arvus")
        print()
        c = b = a
        paaris = 0
        paaritu = 0
        while b > 0:
            digit = b % 10
            if digit % 2 == 0:
                paaris += 1
            else:
                paaritu += 1
            b = b // 10

        print(f"Paarisarvud: {paaris}")
        print(f"Paaritud numbrid: {paaritu}")
        print()

        print("Pöörame sisestatud numbri ümber", c)
        print()
        b = 0
        while a > 0:
            number = a % 10
            a = a // 10
            b = b * 10
            b += number
        print("Pööratud number", b)
        print()

        print("Syracuse hüpoteesi testimine")
        print()
        c = b
        while c != 1:
            if c % 2 == 0:
                print(f"{c} - paarisarv. jagame 2-ga.")
                c = c // 2
            else:
                print(f"{c} - paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2-ga")
                c = (3 * c + 1) // 2
            print(f"Praegune väärtus: {c}")
        print("Hüpotees on õige: oleme jõudnud 1-ni")
    except Exception as e:
        print(f"Ilmnes viga: {e}")
