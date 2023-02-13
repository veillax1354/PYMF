
notes = []

def add_note():
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    notes.append({"title": title, "content": content})
    print("Note added successfully!")

def view_notes():
    if not notes:
        print("No notes to display.")
        return
    print("Displaying all notes:")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note['title']}")

def select_note():
    view_notes()
    selected_index = int(input("Enter the number of the note you want to view: ")) - 1
    if selected_index >= len(notes) or selected_index < 0:
        print("Invalid selection.")
        return
    selected_note = notes[selected_index]
    print(f"Title: {selected_note['title']}")
    print(f"Content: {selected_note['content']}")

def main_menu():
    while True:
        print("Welcome to the Note Taking and Sharing Program")
        print("1. Add a note")
        print("2. View all notes")
        print("3. View a specific note")
        print("4. Quit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            add_note()
        elif user_choice == "2":
            view_notes()
        elif user_choice == "3":
            select_note()
        elif user_choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
