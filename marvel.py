
characters = [
    [1, "thor", "odinson", "asgard", 1500, "strongest avenger"],
    [2, "clint", "barton", "earth", 35, "hawkeye"],
    [3, "tony", "stark", "earth", 52, "iron man"],
    [4, "peter", "parker", "earth", 17, "spiderman"],
    [5, "groot", "groot", "planet", 18, "tree"]
]

def main():
    print("MARVEL CHARACTER DATABASE")
    print("-" * 75)

    for character in characters:
        print(" | ".join(str(value) for value in character))

if __name__ == "__main__":
    main()
