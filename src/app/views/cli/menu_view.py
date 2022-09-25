from dataclasses import dataclass, field

from app.models.view_models.menu import Menu
from app.models.view_models.menu_entry import MenuEntry
from app.views.cli.view import View
from app.views.cli.interactive import Interactive 

@dataclass
class MenuView(View, Interactive):
    menu: Menu = field(default_factory=lambda: Menu())
    
    def print(self) -> None:
        print("Select Operation: ")
        for index, menu_entry in enumerate(self.menu):
            print(f"{index}.\t{menu_entry}")
    
    def prompt(self) -> None:
        option = int(input("Select Option: "))
        self.menu[option].execute()
            