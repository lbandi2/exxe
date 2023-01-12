from parcel.tracking import Tracking
from parcel.info import Info


class Parcel:
    def __init__(self, info: Info, tracking: Tracking) -> None:
        self.info = info
        self.tracking = tracking

# Parcel(Info([]), Tracking([]))