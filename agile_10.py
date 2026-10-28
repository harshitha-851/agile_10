class StudentCalculator:
    def __init__(self):
        self.marks = []

    def get_inputs(self):
        print("Student Grade Calculator")
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects <= 0:
                print("Number of subjects must be greater than zero.")
                return False
            
            self.marks = []
            for i in range(1, num_subjects + 1):
                while True:
                    try:
                        mark = float(input(f"Enter marks for subject {i} (0-100): "))
                        if 0 <= mark <= 100:
                            self.marks.append(mark)
                            break
                        print("Invalid input. Marks must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a valid numerical value.")
            return True
        except ValueError:
            print("Invalid input. Number of subjects must be an integer.")
            return False

    def calculate_results(self):
        if not self.marks:
            return 0, 0
        total = sum(self.marks)
        average = total / len(self.marks)
        return total, average

    def display_results(self):
        if not self.marks:
            return
        total, average = self.calculate_results()
        print("\n--- Performance Summary ---")
        print(f"Total Marks:   {total:.2f}")
        print(f"Average Marks: {average:.2f}%")
if __name__ == "__main__":
    calc = StudentCalculator()
    if calc.get_inputs():
        calc.display_results()
