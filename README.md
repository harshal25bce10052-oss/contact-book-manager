# Python Contact Book Manager 

### Hello! 
This is a super simple **Contact Book** program made in Python. It lets you save your friends’ names, phone numbers, and emails on your computer using a file called `contacts.json`. No database, no internet – just pure Python!

### What can it do?
1.  Add a new contact  
2.  View all contacts  
3.  Search contacts (by name, phone, or email)  
4.  Delete a contact  
5.  Exit the program  

Everything you add gets saved automatically so it’s still there when you open the program again!

### Files in this project
- `main.py` → the only file you need to run  
- `contacts.json` → created automatically when you add your first contact (don’t delete it if you want to keep your data!)

### How to run it (super easy)
1. Make sure you have **Python 3** installed  
2. Download or copy the `main.py` file  
3. Open terminal/command prompt in that folder  
4. Type this and press Enter:  
   ```bash
   python main.py
   ```
   (or `python3 main.py` on Mac/Linux)

That’s it! The menu will appear and you can start adding contacts.

### Example of how it looks
```
==================================
  PYTHON CONTACT BOOK MANAGER (v1)
==================================
1. Add New Contact
2. View All Contacts
3. Search Contacts
4. Delete Contact
5. Exit
----------------------------------
Enter your choice (1-5): 
```

### Things I learned while making this 
- How to read/write JSON files  
- Working with lists and dictionaries  
- Using `try-except` for errors  
- Making functions clean and reusable  
- Basic menu-based programs  

### Future ideas (maybe in v2)
- Edit/update a contact  
- Better looking table with `tabulate`  
- Add birthday field  
- Export to CSV  
