def simple_interest(principal, rate, time):
    simple = principal * rate * time
    return simple

def main():
    simple = simple_interest( rate, principal, time) 
    print(f'simple interest is: {simple}')

if __name__ == '__main__':
    main()

principal = input('Enter principal: ')
rate = input('Enter rate: ')
time = input('Enter time: ')