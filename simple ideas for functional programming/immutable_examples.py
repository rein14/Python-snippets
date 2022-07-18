import random

def main():
    
    test_list = [20, 60, -20, 0, 5, 67, 14 ,99]
    sorted_list = sorted(test_list)
    print(f"original list: {test_list}")
    print(f"sorted list: {sorted_list}")

    test_list.sort()
    print(f"original list: {test_list}")

    cards =['2', '3', '4', '5', '6', '7', '8', '9', "Q", "K"]

    shuffled_cards = random.sample(cards, k=len(cards))

    print(f"Shuffled cards: {shuffled_cards}")
    print(f"original cards: {cards}")
if __name__ == "__main__":
    main()