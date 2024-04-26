
names = input("Enter student names (separated by commas): ").split(",")

for student in names:
    student = student.strip()
    print(f"Entering feedback for {student}")

    understanding_level = input("Understanding level score (1 - basic, 2 - good, 3 - excellent): ")
    contribution_level = input("Contribution level score (1 - basic, 2 - good, 3 - excellent): ")
    completion_level = input("Completion level score (1 - basic, 2 - good, 3 - excellent): ")

    punctuality_level = input("Punctuality level score (1 - basic, 2 - good, 3 - excellent): ")
    engagement_level = input("Engagement level score (1 - basic, 2 - good, 3 - excellent): ")
    further_learning_level = input("Further learning level score (1 - basic, 2 - good, 3 - excellent): ")

    understanding_descriptions = {"1": "basic understanding", "2": "good understanding", "3": "excellent understanding"}
    contribution_descriptions = {"1": "", "2": "", "3": ""}
    completion_descriptions = {"1": "", "2": "", "3": ""}

    feedback = f"General comments\n{student} did well with functions and loops. Contributed well to class discussions.\n"
    feedback += f"{student} demonstrated {understanding_descriptions.get(understanding_level)} with Python and general programming principles.\n"
    feedback += f"Learner punctuality and engagement\n{student} engaged well throughout the module with camera on most of the time.\n"
    feedback += "Recommendations on further learning\nHave a look at advanced concepts such as recursiveness."

    filename = f"{student}_feedback.txt"
    with open(filename, "w") as file:
        file.write(feedback)
