from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from element import Element


class Event:
    # 설명 : 이벤트에서는 이벤트 버블링, event.path, event.target 을 구현하려고 하였습니다.

    type: str
    target: Element
    bubbles: bool
    path: List[Element]
    # 설명 : 버블링 여부와, path 를 저장하는 필드를 선언해줍니다.

    def __init__(self, type: str, target: Element, bubbles: bool):
        self.type = type
        self.target = target
        self.bubbles = bubbles
        self.path = []
