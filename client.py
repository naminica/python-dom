from __future__ import annotations
from document import document, DocumentElement
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from event import Event


def decorator(func):
    def decorated():
        print(f"<<< {func.__name__.upper()} 실행 >>>")
        func()
        print()
        print()

    return decorated


@decorator
def case1():
    a = document.createElement("a")

    a.setAttribute("href", "https://www.lawandgood.com")
    a.innerText = "로앤굿 바로가기"
    document.append(a)
    sp1 = document.createElement("span")
    sp2 = document.createElement("span")
    sp1.innerText = "첫 자식"
    sp2.innerText = "두 번째 자식"
    a.append(sp1, sp2)

    print(document)


@decorator
def case2():
    print(id(document))
    print(id(DocumentElement()))


@decorator
def case3():
    document.removeChild()
    a = document.createElement("a")
    sp = document.createElement("span")
    a.innerText = "부모"
    sp.innerText = "자식"

    a.append(sp)
    document.append(a)

    def clickEventHandler(event: Event):
        print(f"클릭되었습니다. - {event.target} AND {event.path}")

    sp.addEventListener('click', clickEventHandler)
    a.addEventListener('click', clickEventHandler)

    print("CLICK 시작!")
    sp.click()


@decorator
def case4():
    print('재미로 querySelector 도 구현해보려 했으나 시간 관계 상 포기')


if __name__ == "__main__":
    # CLIENT

    case1()
    case2()
    case3()
    case4()
