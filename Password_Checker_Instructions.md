PROJECT 1: PASSWORD SECURITY CHECKER

Level: Beginner
Language: Python
Difficulty: Easy
Estimated time: 2–4 hours

PROJECT DESCRIPTION
Create a Python program that analyzes a password entered by a user and determines its strength based on predefined security criteria.

FUNCTIONAL REQUIREMENTS
1. Ask the user to enter a password.
2. Verify that the password contains at least 8 characters.
3. Verify that it contains at least one uppercase letter.
4. Verify that it contains at least one lowercase letter.
5. Verify that it contains at least one digit.
6. Verify that it contains at least one special character.
7. Calculate a score out of 5 based on the number of conditions satisfied.
8. Classify the password:
   - Weak: 0–2 points
   - Medium: 3–4 points
   - Strong: 5 points
9. Display the password's strength and score.
10. Allow the user to test another password or exit the program.

EXPECTED OUTPUT

   PASSWORD CHECKER

Enter your password: Hello123!

Password strength: STRONG
Security score: 5/5

Would you like to try again? (yes/no): yes

Enter your password: hello

Password strength: WEAK
Security score: 1/5

Would you like to try again? (yes/no): no

Program terminated.

TECHNICAL CONSTRAINTS
- Use at least 3 functions.
- Use conditional statements (if, elif, else).
- Use at least one loop (for or while).
- Use strings and string operations.
- Avoid external Python libraries.
- Organize the program into reusable functions.

DELIVERABLE
A working Python file named password_checker.py that meets all the requirements.

NOTE
The scoring system is simplified for educational purposes and does not constitute a real-world password security assessment.
