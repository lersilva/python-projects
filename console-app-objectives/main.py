def main():
    objectives = []
    print("Please enter your objectives for the new year of 2024. Enter 'done' when finished.")

    while True:
        objective = input("Enter an objective: ")
        if objective.lower() == 'done' and len(objectives) >= 3:
            break
        elif objective.lower() == 'done':
            print("You need to enter at least 3 objectives before finishing.")
        else:
            objectives.append(objective)

    print("\nYour objectives for 2024 are:")
    for i, objective in enumerate(objectives, 1):
        print(f"{i}. {objective}")

    print("\nPress any key to exit.")
    input()

if __name__ == "__main__":
    main()