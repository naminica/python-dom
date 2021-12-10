# python DOM
굉장히 간소화되고 추상화된 "javascript DOM 을 python 으로 구현해보는 프로젝트"

* 주의 : 디자인 패턴 세션 용도로 제작된 프로젝트로, 퀄리티가 조악합니다.

## 주요 패턴
- DOM 의 트리 구조를 복합체 패턴으로 구현
- DOM 의 이벤트, 핸들러 구조를 감시자 패턴으로 구현
- Document 는 싱글톤 패턴으로 구현


### 복합체 패턴
![](https://t1.daumcdn.net/cfile/tistory/9959CC495C8910EB0F)
- Component 인터페이스 -> Leaf 와 Composite 를 같은 타입으로 취급하기 위한 인터페이스
- Leaf, 트리 구조에서 자식 노드가 없는 가장 밑단
- Composite, 자식으로 여러개의 Component 를 가질 수 있다.

DOM 에서는 Leaf 와 Composite 를 별도 클래스로 구분해서 사용하지는 않기에, 하나의 Element 클래스로 구현 


### 감시자 패턴
![](https://scvgoe.github.io/img/observer.gif)  
- Subject 가 등록된 Observer 들에게 Notify 하는 패턴  

객체지향과 디자인 패턴을 생각하면 Observer 를 클래스로 구현하는 것이 맞겠으나, 최대한 javascriptfull 한 코드를 만들어보려고 전달되는 Observer 는 그냥 함수로 결정  


### 싱글톤 패턴
![](https://gmlwjd9405.github.io/images/design-pattern-singleton/singleton-example.png)
- 벙글톤 패턴

패턴 두 개만 넣으려니 심심하기도 하고, document 객체가 2개일 수는 없으니까 싱글톤으로 document 구현


## REF
https://spiralmoon.tistory.com/entry/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-%EB%B3%B5%ED%95%A9%EC%B2%B4-%ED%8C%A8%ED%84%B4-Composite-pattern
https://scvgoe.github.io/2018-12-24-GoF%EC%9D%98-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-(Summary)-9.-%EA%B0%90%EC%8B%9C%EC%9E%90(Observer)/
https://gmlwjd9405.github.io/2018/07/06/singleton-pattern.html