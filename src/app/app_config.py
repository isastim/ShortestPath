from argparse import ArgumentParser, Namespace
from dataclasses import dataclass, field

from app.controller.board_controller import BoardController
from app.controller.path_agent import PathAgent
from app.models.board import Board
from app.models.list_board_adapter import ListBoardAdapter
from app.models.postition import Position
from app.utils.json_parser import JSONParser

@dataclass
class AppConfig:
    argument_parser: ArgumentParser = field(init=False, default_factory=ArgumentParser)
    args: Namespace = field(init=False)
    json_parser: JSONParser = field(init=False)
    board_controller: BoardController = field(init=False)
    path_agent: PathAgent = field(init=False)
    
    def __post_init__(self) -> None:
        self.__parse_args()
        self.__init_controller()
        
    def __parse_args(self) -> None:
        self.argument_parser.add_argument("--config-file", help="Config file to set parameters of the app", required=True)
        self.args: Namespace = self.argument_parser.parse_args()
        self.json_parser = JSONParser(self.args.config_file)
        
    def __init_controller(self) -> None:
        board: Board = ListBoardAdapter(self.json_parser.board)
        self.board_controller = BoardController(board)
        self.path_agent = PathAgent(board)
        
    
    def run_app(self) -> None:
        self.board_controller.print()
        self.path_agent.find_shortest_path(Position(*self.json_parser.start), Position(*self.json_parser.destination))
        self.path_agent.print()
        
    