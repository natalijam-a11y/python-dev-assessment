This repository contains my onboarding assessment tasks. I've covered the entire flow—starting from Git basics and PEP 8 formatting, moving through data structures and Object-Oriented Programming (OOP), and finishing with robust error handling and fetching real-time data from an external REST API.

I developed each task on its own dedicated branch and successfully merged everything into the `main` branch upon completion.

---

## Project Structure (Tasks Completed)

* `hello.py` – My very first script and initial setup with Git.
* `bad_style.py` – Code refactoring and formatting to strictly comply with PEP 8 standards.
* `dsa_challenges.py` – Data structures practice (working with lists and dictionaries) and logic problem-solving.
* `book_store.py` – OOP practice. Created a `Book` class that dynamically calculates a book's age and generates a clean summary.
* `debug_errors.py` – Error handling and debugging. Resolved logical bugs (like division by zero) using `try-except` blocks and verified the flow using the VS Code debugger.
* `api_client.py` – API integration. Used the `requests` library to fetch live data from the JSONPlaceholder API, implementing thorough network exception handling and safe nested data parsing.

What I found most challenging: In the API task, the trickiest part was safely extracting the city from the user data. Since the address is a nested dictionary (a dict inside a dict), I had to make sure the code wouldn't crash if a specific key was missing. I resolved this by utilizing chained .get() methods.

What I found most interesting: Definitely working with the VS Code Debugger! It felt awesome to set a breakpoint, freeze the program mid-execution, and literally watch the line skip a potential crash and jump straight into my except recovery block. It felt like having time-control over my code.

One thing I learned/improved upon: I really leveled up my understanding of how Python evaluates data types under the hood. For instance, it was an eye-opener when I passed a string instead of a list into my function, and Python threw an IndexError instead of a TypeError. I learned that Python treats strings similarly to lists of characters!
