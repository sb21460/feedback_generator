import os

os.makedirs("Feedback", exist_ok=True)

def map_score_to_description(score, descriptions):
    return descriptions.get(score, "Invalid score; please ensure scores are 1, 2, or 3.")

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
  
    feedback = (
        f"General comments\n{student} demonstrated {map_score_to_description(understanding_score, descriptions)} understanding of Python and general programming principles, "
        f"and contributed {map_score_to_description(contribution_score, descriptions)} to class discussions. They completed tasks with a {map_score_to_description(completion_score, descriptions)} level of thoroughness.\n\n"
        f"Learner punctuality and engagement\n{student} was {map_score_to_description(punctuality_score, descriptions)} punctual and engaged {map_score_to_description(engagement_score, descriptions)} throughout the module.\n\n"
        f"Recommendations on further learning\n{student} should look at advanced concepts such as recursion to further enhance their understanding, as they have shown a {map_score_to_description(further_learning_score, descriptions)} aptitude for further learning."
    )

    filename = os.path.join("Feedback", f"{student}_feedback.txt")
    with open(filename, 'w') as file:
        file.write(feedback)
    print(f"Feedback for {student} written to {filename}")

print("Feedback complete")
