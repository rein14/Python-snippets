def simple_interest(princinpal, rate, time):
    simple = princinpal * rate * time
    return simple

def main():
    simple = simple_interest(2000, 0.02, 20) 
    print(f'simple interest is: {simple}')

if __name__ == '__main__':
    main()