import csv
from functions import t12 , get_key_press
notes = []

def add_note():
    t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    notes.append({"title": title, "content": content})
    t12("Note added successfully!")

def view_notes():
    t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
    if not notes:
        t12("No notes to display.")
        return
    t12("Displaying all notes:")
    for i, note in enumerate(notes):
        a2 = (f"{i+1}. {note['title']}")
        t12(a2)

def select_note():
    view_notes()
    t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
    selected_index = int(input("Enter the number of the note you want to view: ")) - 1
    if selected_index >= len(notes) or selected_index < 0:
        t12("Invalid selection.")
        return
    selected_note = notes[selected_index]
    a = (f"Title: {selected_note['title']}")
    a1 = (f"Content: {selected_note['content']}")
    t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
    t12(a)
    t12(a1)

def export_to_csv(notes):
    t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
    # Open a file for writing
    with open('notes.csv', 'a', newline='') as csvfile:
        # Create a writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Title', 'Content'])

        # Write the notes data
        for note in notes:
            writer.writerow([note['title'], note['content']])

    print('Notes exported to notes.csv')
    
def main_menu():
    while True:
        t12("\033[32m========================================================================================================================================================== \033[0m", 0.01)
        t12("Welcome to the Note Taking and Sharing Program")
        t12("1. Add a note")
        t12("2. View all notes")
        t12("3. View a specific note")
        t12("4. Export notes to csv")
        t12("5. Quit")
        t12("Enter your choice: ")
        user_choice = get_key_press(["1", "2", "3", "4", "5"])
        if user_choice == "1":
            add_note()
        elif user_choice == "2":
            view_notes()
        elif user_choice == "3":
            select_note()
        elif user_choice == "4":
            export_to_csv(notes)
        elif user_choice == "5":
            t12("Would you like to export your notes before you quit [y/n]?")
            check = get_key_press(["y", "n"])
            if check == 'y':
                export_to_csv(notes)
            else:
                pass
            break
        else:
            t12("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
    