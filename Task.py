import os

os.makedirs("Feedback", exist_ok=True)

def map_score_to_description(score, descriptions):
    return descriptions.get(score, "Invalid score entered. Please ensure scores are 1, 2, or 3.")

names = input("RyanK, Ryan, Sandy, Mohammad, Ashley, LukeG): ").split(",")

for student in names:
    student = student.strip()
    print(f"Entering feedback for {student}")

    understanding_score = input("Understanding level score (1 - basic, 2 - good, 3 - excellent): ")
    contribution_score = input("Contribution level score (1 - basic, 2 - good, 3 - excellent): ")
    completion_score = input("Completion level score (1 - basic, 2 - good, 3 - excellent): ")
    punctuality_score = input("Punctuality level score (1 - basic, 2 - good, 3 - excellent): ")
    engagement_score = input("Engagement level score (1 - basic, 2 - good, 3 - excellent): ")
    further_learning_score = input("Further learning level score (1 - basic, 2 - good, 3 - excellent): ")

    descriptions = {
        "1": "basic",
        "2": "good",
        "3": "excellent"
    }
    
    feedback = (
        f"General comments\n{student.title()} demonstrated {map_score_to_description(understanding_score, descriptions)} understanding of Python and general programming principles, "
        f"and contributed {map_score_to_description(contribution_score, descriptions)} to class discussions. They completed tasks with a {map_score_to_description(completion_score, descriptions)} level of thoroughness.\n\n"
        f"Learner punctuality and engagement\n{student.title()} was {map_score_to_description(punctuality_score, descriptions)} punctual and engaged {map_score_to_description(engagement_score, descriptions)} throughout the module.\n\n"
        f"Recommendations on further learning\n{student.title()} should look at advanced concepts such as recursion to further enhance their understanding, as they have shown a {map_score_to_description(further_learning_score, descriptions)} aptitude for further learning."
    )

    filename = os.path.join("Feedback", f"{student.title()}_feedback.txt")
    with open(filename, 'w') as file:
        file.write(feedback)
    print(f"Feedback for {student.title()} written to {filename}")

print("Feedback complete")
