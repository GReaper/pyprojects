import sys
from notebook import Notebook

class Menu:
    '''display a menu and respond to choices when run.'''
    def __init__(self):
        self._notebook = Notebook()
        self._choices = {"1" : self._show_notes, 
                            "2": self._search_notes, 
                            "3":  self._add_note, 
                            "4": self._modify_note, 
                            "5": self._quit}
        
    def run(self):
        '''Display the menu and respond to choices'''
        while True:
            self._display_menu()
            choice = input("Enter an option: ")
            action = self._choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def _display_menu(self):
        print("""Notebook Menu
        
        1. Show all notes
        2. Search notes
        3. Add note
        4. Modify note
        5. Quit
        """)
        
    def _show_notes(self,  notes=None):
        if not notes:
            notes = self._notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id,  note.tags,  note.memo))
            
            
    def _search_notes(self):
        filter = input("Search for: ")
        notes = self._notebook.search(filter)
        self._show_notes(notes)
        
    def _add_note(self):
        memo = input("Enter a memo: ")
        self._notebook.new_note(memo)
        print("Your note has been added.")
        
    def _modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = ("Enter tags: ")
        if memo:
            self._notebook.modify_memo(id,  memo)
        if tags:
            self._notebook.modify_tags(id,  tags)
            
    def _quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
