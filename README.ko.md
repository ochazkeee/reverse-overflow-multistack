# Reverse Overflow 기반 Multiple Stack 구조

## 개요  
이 프로젝트는 여러 개의 스택(Multiple Stacks)을 하나의 배열에서 공간을 공유하며 효율적으로 구현한 자료구조입니다.  
특히 스택이 자신의 영역을 초과할 경우, 인접한 스택의 남은 공간을 역방향으로 침범하여 사용하는 **Reverse Overflow** 전략을 채택했습니다.

기존의 균등 분할 방식보다 공간 활용률이 우수하며, 동적 리사이즈 없이도 다양한 시나리오에 유연하게 대응할 수 있습니다.

## 특징

- Reverse Overflow 알고리즘  
  하나의 배열을 여러 개의 스택이 공유하고, 각 스택은 자신이 성장하는 방향으로 확장되며, 공간 부족 시 다른 스택의 남은 공간을 역방향으로 침범하여 사용합니다.

- 동적 메모리 할당 없음  
  고정된 배열 내에서 공간을 최대한 활용하여 메모리 효율을 높입니다.

- 회수 로직 포함  
  pop 시, 사용하던 공간을 회수하고 조정하여 다음 push 시 활용 가능하도록 합니다.

- 성능 비교 자료 포함
  기존의 균등 분할 방식, Knuth의 linked stack 등과의 공간 및 시간 효율 비교 결과는 docs/comparison.md에 정리되어 있습니다.

## 디렉토리 구조

```
reverse-overflow-multistack/
├── README.md                  # Main project introduction (English)
├── README.ko.md               # Korean summary version
├── LICENSE
├── docs/
│   ├── en/
│   │   ├── structure.md       # Core concepts and algorithm design
│   │   ├── comparison.md      # Performance evaluation and comparison
│   │   ├── implementation.md  # Code-level implementation notes
│   │   └── faq.md             # Frequently asked questions
│   └── ko/
│       ├── structure.ko.md
│       ├── comparison.ko.md
│       ├── implementation.ko.md
│       └── faq.ko.md
├── src/                       # C source code
│   ├── main.c
│   ├── multiple_stack.c
│   └── multiple_stack.h
├── benchmarks/                # Python scripts for performance testing
│   ├── implementations.py
│   ├── test.py
│   └── images/                # Experimental result visualizations
│       ├── experiment_0.png
│       ├── experiment_1.png
│       ├── experiment_2.png
│       ├── experiment_3.png
│       └── experiment_4.png
└── CMakeLists.txt             # CMake build configuration
```



## 문서 안내

- `docs/structure.md` - 구조 및 알고리즘 핵심 개념
- `docs/comparison.md` - 기존 방식과의 비교, 장단점 분석
- `docs/implementation.md` - 구현 세부사항 및 주요 로직 설명
- `docs/faq.md` - 자주 묻는 질문 정리

## 빌드 방법

```bash
mkdir build
cd build
cmake ..
make
./reverse_stack_demo
```

---

## 참고 및 참여 안내

이 프로젝트는 아직 완성되지 않은 상태이며, 이론적 아이디어와 개인적인 구현 실험을 바탕으로 개발 중입니다.  
Reverse Overflow 방식은 공간 효율성을 높이기 위한 한 가지 전략으로 제안된 것으로,  
추후 구현의 안정성과 성능 측면에서 개선이 이루어질 수 있습니다.

본 자료는 MIT 라이선스 하에 공개되어 있으며, 자유롭게 사용 및 수정하실 수 있습니다.  
다만 아이디어나 구현 방식에 대해 의견이 있으신 경우,  
[이슈를 남기거나](https://github.com/ochazkeee/reverse-overflow-multistack/issues) 직접 기여해주시면 감사하겠습니다.

이 구조나 아이디어에 대한 비판, 토론, 제안 모두 환영합니다.  
아직 부족한 부분이 많지만, 학습과 실험의 과정으로서 공개하는 만큼 너그러운 시선으로 봐주시면 감사하겠습니다.
