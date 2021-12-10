from __future__ import annotations
from event import Event
from typing import List, Dict, Optional, Callable


class Element:
    tagName: str
    innerText: str
    attributes: dict

    parent: Optional[Element]
    children: List[Element]
    # 설명 : 복합체 패턴. 트리 구조의 DOM element 를 구성합니다.

    event_listeners: Dict[str, List[function]]

    # 설명 : 감시자 패턴을 통해 들어오는 이벤트를 전달하려 합니다.

    def __init__(self, tagName: str):
        self.tagName = tagName
        self.innerText = ""
        self.attributes = {}
        self.parent = None
        self.children = []
        self.event_listeners = {}
        # 설명 : 제가 무근본 개발자라 여기서 삽질을 좀 했습니다 ㅋㅋ 클래스 필드에 바로 리스트나 딕셔너리 할당해놓으면, 모든 인스턴스가 그 값을 공유하더라고요

    def __str__(self):
        # 설명 : 렌더링
        attributes = ' '.join([f'{k}="{v}"' for k, v in self.attributes.items()])
        rendered_children = '\n'.join([str(c) for c in self.children]) if len(self.children) > 0 else ''
        return f"""<{self.tagName} {attributes}>{self.innerText}{rendered_children}</{self.tagName}>"""

    def __setattr__(self, attr, val):
        super().__setattr__(attr, val)

    @property
    def childElementCount(self):
        return len(self.children)

    @property
    def isLeaf(self):
        # 설명 : 복합체 패턴의 Leaf 임을 체크
        return len(self.children) == 0

    def getAttribute(self, attr_name: str):
        self.attributes.get(attr_name)

    def setAttribute(self, attr_name: str, value: str):
        self.attributes[attr_name] = value

    def append(self, *el: Element):
        # 설명 : 복합체 패턴의 자식 노드를 추가
        for ch in el:
            ch.parent = self
        self.children += el

    def removeChild(self):
        # 설명 : 복합체 패턴의 자식 노드를 제거
        _temp = self.children
        for ch in self.children:
            ch.parent = None
        self.children = []
        return _temp

    def addEventListener(self, event_type: str, listener: Callable):
        # 설명 : 감시자 패턴을 사용하기 위해 Callable 한 감시자(옵저버)를 추가하는 메서드
        if self.event_listeners.get(event_type) is not None:
            self.event_listeners.get(event_type).append(listener)
        else:
            self.event_listeners[event_type] = [listener, ]

    def event(self, event: Event):
        # 설명 : 감시자에게 이벤트를 뿌려주는 메서드
        event.path.append(self)

        event_listeners = self.event_listeners.get(event.type)
        if event_listeners is None:
            pass
        else:
            # 설명 : 감시하고 있던 옵저버들을 호출
            for event_listener in event_listeners:
                event_listener.__call__(event)

        if event.bubbles and self.parent is not None:
            # 설명 : 이벤트 버블링이 가능한 이벤트일 경우 버블링
            self.parent.event(event=event)

    def click(self):
        event = Event(type="click", target=self, bubbles=True)
        self.event(event=event)

    def mouseover(self):
        event = Event(type="mouseover", target=self, bubbles=True)
        self.event(event=event)

    def focus(self):
        event = Event(type="focus", target=self, bubbles=True)
        self.event(event=event)

    def querySelector(self, selector: str):
        pass
