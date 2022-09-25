from dataclasses import dataclass, field
import json
from typing import Any, Dict, List


@dataclass
class JSONParser:
    json_file: str
    json: Dict = field(init=False)
    board: List = field(init=False)
    start: List = field(init=False)
    destination: List = field(init=False)
    
    def __post_init__(self) -> None:
        with open(self.json_file, "r") as file:
            self.json = json.loads(file.read())
        self.board = self.json["board"]
        self.start = self.json["start"]
        self.destination = self.json["destination"]