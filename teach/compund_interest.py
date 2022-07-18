def compound_interest(principal, rate, time):
    digits = 1 + rate / 100
    ci = principal * (pow(digits, time))
    return ci

def main():
    ci = compound_interest(2000, 0.02, 20)
    print(ci)

if __name__ == '__main__':
    main()