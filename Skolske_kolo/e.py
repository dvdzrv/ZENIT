vstup = 12
možnosti = [5,7,13]


def solve(vstup, možnosti):
    delitel = možnosti[0]
    kvocient = vstup // delitel
    modulus = vstup % delitel

    if modulus == 0:
        print(f"{kvocient} X {delitel}")
        return True

    if kvocient == 0 or len(možnosti) == 1:
        return False

    while not solve(vstup - delitel * kvocient, možnosti[1:]):
        if kvocient - 1 != 0:
            kvocient -= 1
            continue
        return solve(vstup, možnosti[1:])

    print(f"{kvocient} X {delitel}")
    return True


solve(vstup, možnosti)