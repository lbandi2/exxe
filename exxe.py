from html_parser import Parser
from webpage_bp.job import ChromeH

TRACK_ID = "806214832"


class Exxe:
    URL = "https://solex.blulogistics.net/SolexRC/g?Numero="
    
    def __init__(self, track_id) -> None:
        self.track_id = track_id
        self.parser = Parser(ChromeH(url=self.URL + self.track_id))
        self.info = self.parser.info
        self.tracking = self.parser.tracking






if __name__ == '__main__':
    track = Exxe(TRACK_ID)
    # print(track.track_id)