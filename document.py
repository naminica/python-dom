from element import Element


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # 설명 : 메타 클래스을 통해 싱글톤 패턴 구현. 단일 인스턴스만 생성 될 수 있도록 __call__ 메서드 수정
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DocumentElement(Element, metaclass=SingletonMeta):

    def __init__(self):
        super().__init__(tagName="DOM")

    @staticmethod
    def createElement(tagName: str):
        return Element(tagName=tagName)

    def getElementById(self, id: str):
        pass


document = DocumentElement()
