# 구현 세부사항 및 알고리즘 설명 (Implementation Details)

## 개요

이 문서는 **Reverse Overflow 기반 Multiple Stack 자료구조**의 내부 구현 및 알고리즘 로직을 설명합니다.  
해당 구조는 하나의 고정 크기 배열에서 여러 개의 스택이 공간을 **동적으로 공유**하며 동작합니다.  
각 스택은 자신의 기본 영역을 우선 사용하되, **공간 부족 시 인접 스택의 미사용 공간을 역방향으로 침범**하여 사용하는 구조입니다.  
또한, **pop 연산 시 침범한 공간을 회수**하는 로직을 포함하고 있습니다.

---

## 데이터 구조

### 1. 기본 배열 및 스택 상태 구조

- **arr (배열)**  
  전체 스택들이 공유하는 고정 크기의 1차원 배열입니다.  
  모든 push/pop 연산은 이 배열을 통해 이루어집니다.

- **starts[], ends[] (스택의 시작 및 종료 지점)**  
  각 스택의 기본 영역의 시작 인덱스와 종료 인덱스를 저장하는 배열입니다.  
  예: `starts[i] = 0`, `ends[i] = 99` 형태로 스택의 구간을 정의합니다.

- **tops[] (현재 top 위치)**  
  각 스택의 현재 top 인덱스를 나타내는 배열입니다.  
  스택 연산 시 이 값을 기준으로 push/pop이 진행됩니다.

- **owner[] (Reverse Overflow 전용)**  
  `arr[i]`에 저장된 데이터가 어느 스택에 속하는지를 나타내는 배열입니다.  
  값이 `-1`이면 비어있음을 의미하고, `0`, `1`, ..., `n-1`은 해당 인덱스의 소유 스택을 의미합니다.

- **free_indices (선택적)**  
  빠른 빈 공간 탐색을 위한 힙 또는 큐 형태의 자료구조입니다.  
  공간 확보가 필요한 경우, 이 구조를 통해 빠르게 빈 인덱스를 탐색할 수 있습니다.

---

## 알고리즘 동작 흐름

### 1. Push 연산

1. **기본 영역 내 Push**  
   - `tops[i] + 1 <= ends[i]` 이고, 해당 위치가 비어 있다면 정상적으로 push 수행  
   - `arr[tops[i] + 1] = value`, `tops[i]++`, `owner[tops[i]] = i`로 갱신

2. **Reverse Overflow 발생 시**  
   - 기본 영역이 모두 찼을 경우, 인접 스택의 영역을 **역방향(끝 → 시작)** 으로 탐색  
   - 가장 가까운 비어있는 인덱스를 찾고, 해당 위치에 값을 저장  
   - `owner[]` 업데이트, `tops[]` 갱신

3. **오버플로우 처리**  
   - 모든 인접 스택에서도 공간을 찾지 못하면 push 실패  
   - `FAILURE` 또는 예외 처리

---

### 2. Pop 연산

1. **기본 영역 또는 침범 영역에서 Pop**  
   - `tops[i] >= starts[i]` 조건을 만족하면 pop 가능  
   - `value = arr[tops[i]]`, `arr[tops[i]] = null`, `owner[tops[i]] = -1`, `tops[i]--`

2. **회수 (Reclaim) 로직**  
   - 해당 위치가 **자신의 기본 영역이 아닌 경우 (침범했던 위치)**,  
     `owner[]` 정보를 통해 **원래 스택의 소유 공간**으로 복구  
   - 복구된 인덱스는 다시 인접 스택의 사용 가능 영역으로 처리됨

---

## 구현 예시 (의사코드)

```plaintext
function push(stack, value):
    next_pos = tops[stack] + 1
    if next_pos <= ends[stack] and arr[next_pos] is empty:
        arr[next_pos] = value
        owner[next_pos] = stack
        tops[stack] = next_pos
        return SUCCESS
    else:
        // Reverse Overflow 탐색
        for i from array.length - 1 to 0:
            if arr[i] is empty:
                arr[i] = value
                owner[i] = stack
                tops[stack] = i
                return SUCCESS
        return FAILURE

function pop(stack):
    if tops[stack] < starts[stack]:
        return UNDERFLOW
    value = arr[tops[stack]]
    arr[tops[stack]] = null
    owner[tops[stack]] = -1
    // 회수 로직: 침범 영역 복원
    if tops[stack] not in base area of stack:
        // 복원 처리 (optional)
    tops[stack] = tops[stack] - 1
    return value
