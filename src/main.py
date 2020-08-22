from selenium import webdriver as web
import random as r
alphabetupper = ['A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z']
alphabetlower = ['a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z']
ran1alphalow = r.choice(alphabetlower)
ran1alphaup = r.choice(alphabetupper)
ran1int = r.randint(0, 9)
ran2alphalow = r.choice(alphabetlower)
ran2alphaup = r.choice(alphabetupper)
ran2int = r.randint(0, 9)
ran3alphaup = r.choice(alphabetupper)
ran3alphalow = r.choice(alphabetlower)
ran3int = r.randint(0, 9)
ran4alphaup = r.choice(alphabetupper)
ran4alphalow = r.choice(alphabetlower)
ran4int = r.randint(0, 9)
ran5alphaup = r.choice(alphabetupper)
ran5alphalow = r.choice(alphabetlower)
ran5int = r.randint(0, 9)
ran6alphaup = r.choice(alphabetupper)
ran6alphalow = r.choice(alphabetlower)
ran6int = r.randint(0, 9)
ran7alphaup = r.choice(alphabetupper)
ran7alphalow = r.choice(alphabetlower)
ran7int = r.randint(0, 9)
ran8alphaup = r.choice(alphabetupper)
ran8alphalow = r.choice(alphabetlower)
ran8int = r.randint(0, 9)
ran9alphaup = r.choice(alphabetupper)
ran9alphalow = r.choice(alphabetlower)
ran9int = r.randint(0, 9)
ran10alphaup = r.choice(alphabetupper)
ran10alphalow = r.choice(alphabetlower)
ran10int = r.randint(0, 9)


class bruteForceMainLogic:
    @staticmethod
    def password(passwguess):
        global password
        password = None  # todo Learn Selenium
        if passwguess == password:
            pass  # todo Write method
    digits = input("Digit Amount:")
    global passwguess
    while True:
        if digits == 1:
            global passwguess1
            print('1 Digit is too small.')
            if r.randint(1, 3) == 1:
                passwguess1 == str(ran1int)
            elif r.randint(1, 3) == 2:
                passwguess1 == str(ran1alphaup)
            elif r.randint(1, 3) == 3:
                passwguess1 == str(ran1alphalow)
            else:
                pass
        elif digits == 2:
            global passwguess2
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess2 = str(ran2int)
            elif r.ranint(1, 3) == 2:
                passwguess2 = str(ran2alphaup)
            elif r.ranint(1, 3) == 3:
                passwguess2 = str(ran2alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2)
        elif digits == 3:
            global passwguess3
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess3 = str(ran3int)
            elif r.randint(1, 3) == 2:
                passwguess3 = str(ran3alphaup)
            elif r.randint(1, 3) == 3:
                passwguess3 = str(ran3alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3)
        elif digits == 4:
            global passwguess4
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess4 = str(ran4int)
            elif r.randint(1, 3) == 2:
                passwguess4 = str(ran4alphaup)
            elif r.randint(1, 3) == 3:
                passwguess4 = str(ran4alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4)
        elif digits == 5:
            global passwguess5
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess5 = str(ran5int)
            elif r.randint(1, 3) == 2:
                passwguess5 = str(ran5alphaup)
            elif r.randint(1, 3) == 3:
                passwguess5 = str(ran5alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(passwguess5)
        elif digits == 6:
            global passwguess6
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess6 = str(ran6int)
            elif r.randint(1, 3) == 2:
                passwguess6 = str(ran6alphaup)
            elif r.randint(1, 3) == 3:
                passwguess6 = str(ran6alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(
                passwguess5) + str(passwguess6)
        elif digits == 7:
            global passwguess7
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess7 = str(ran7int)
            elif r.randint(1, 3) == 2:
                passwguess7 = str(ran7alphaup)
            elif r.randint(1, 3) == 3:
                passwguess7 = str(ran7alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(
                passwguess5) + str(passwguess6) + str(passwguess7)
        elif digits == 8:
            global passwguess8
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess8 = str(ran8int)
            elif r.randint(1, 3) == 2:
                passwguess8 = str(ran8alphaup)
            elif r.randint(1, 3) == 3:
                passwguess8 = str(ran8alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(
                passwguess5) + str(passwguess6) + str(passwguess7) + str(passwguess8)
        elif digits == 9:
            global passwguess9
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess9 = str(ran9int)
            elif r.randint(1, 3) == 2:
                passwguess9 = str(ran9alphaup)
            elif r.randint(1, 3) == 3:
                passwguess9 = str(ran9alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(
                passwguess5) + str(passwguess6) + str(passwguess7) + str(passwguess8) + str(passwguess9)
        elif digits == 10:
            global passwguess10
            print('Attempting...')
            if r.randint(1, 3) == 1:
                passwguess10 = str(ran10int)
            elif r.randint(1, 3) == 2:
                passwguess10 = str(ran10alphaup)
            elif r.randint(1, 3) == 3:
                passwguess10 = str(ran10alphalow)
            else:
                pass
            passwguess = str(passwguess1) + str(passwguess2) + str(passwguess3) + str(passwguess4) + str(
                passwguess5) + str(passwguess6) + str(passwguess7) + str(passwguess8) + str(passwguess9) + str(
                passwguess10)
