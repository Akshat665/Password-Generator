1. The program starts by asking the user to enter the desired password length.

2. It then asks the user to choose the type of password:
   - (a) Alphanumeric (letters + numbers)
   - (n) Numeric only
   - (l) Alphabetic only

3. Based on the user's choice, the program selects the appropriate character set:
   - string.ascii_letters → for alphabets
   - string.digits → for numbers
   - combination of both → for alphanumeric passwords

4. The program uses the random module to randomly pick characters from the selected set.

5. A loop (or generator expression) runs for the given length and builds the password.

6. Finally, the generated password is displayed to the user.
