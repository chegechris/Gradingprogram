def get_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 87 <= marks < 90:
        return 'A-'
    elif 84 <= marks < 87:
        return 'B+'
    elif 80 <= marks < 84:
        return 'B'
    elif 77 <= marks < 80:
        return 'B-'
    elif 74 <= marks < 77:
        return 'C+'
    elif 70 <= marks < 74:
        return 'C'
    elif 67 <= marks < 70:
        return 'C-'
    elif 64 <= marks < 67:
        return 'D+'
    elif 62 <= marks < 64:
        return 'D'
    elif 60 <= marks < 62:
        return 'D-'
    elif 0 <= marks < 60:
        return 'F'
    else:
        return 'Invalid marks'

def main():
    while True:
        try:
            marks = float(input("Enter the marks: "))
            grade = get_grade(marks)
            if grade == 'Invalid marks':
                print("Marks should be between 0 and 100.Check again")
            else:
                print(f"The grade for {marks} is: {grade}")

        except ValueError:
            print("Invalid input. Please enter a numeric value for the marks.")

        # Ask the user if they want to continue
        user_response = input("Continue? (yes/no): ").strip().lower()
        if user_response != 'yes':
            print("Terminating the program.")
            break

if __name__ == "__main__":
    main()
