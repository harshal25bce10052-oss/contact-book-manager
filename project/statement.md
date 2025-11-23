# Project Statement – Python Contact Book Manager 

## Problem Statement  
In today's world, almost everyone has many contacts (friends, family, classmates, teachers, etc.), and remembering all phone numbers and emails is very hard without any tool. Mobile phones have built-in contact apps, but sometimes we want something very simple that runs on a computer, doesn't need internet, and we can understand or modify the code ourselves.  
Many beginners also want a practical project to practice file handling, JSON, loops, functions, and basic user input in Python. This project solves both needs: a real-world useful mini application + a great learning exercise.

## Scope of the Project  
This is a console-based (terminal) Contact Book application written in pure Python with no external dependencies except the standard library.  
It can:
- Add new contacts  
- View all saved contacts  
- Search contacts by name, phone, or email  
- Delete existing contacts  
- Automatically save everything to a `contacts.json` file so data remains even after closing the program  

The project is intentionally kept simple and focused on core Python concepts so that first-year students can read, understand, and extend it easily.

## Target Users  
1. First-year college students learning Python who need a complete, working project for practice or assignment  
2. Anyone who wants a lightweight, offline contact manager that runs on any computer with Python installed  
3. Teachers/tutors looking for a clean example to teach file I/O, JSON, functions, and menu-driven programs  

## High-level Features  
- **Persistent Storage** – All contacts are saved in a human-readable `contacts.json` file  
- **Add Contact** – Requires only a name; phone and email are optional  
- **View All Contacts** – Clean numbered list with clear formatting  
- **Search Functionality** – Case-insensitive search across name, phone, and email  
- **Delete Contact** – Select by number after viewing the list, with confirmation feel  
- **Simple Menu Interface** – Easy-to-use numbered menu (1–5)  
- **Basic Error Handling** – Handles empty file, corrupted JSON, invalid inputs, file permission issues, etc.  
- **100% Beginner-Friendly Code** – Well-commented, meaningful variable names, small functions  
