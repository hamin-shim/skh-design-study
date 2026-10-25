# NAND Flash 회로설계자 관점 정리

목적: SK하이닉스 Product Engineering 직무 면접에서 NAND 제품군을 DRAM과 비교하고, 회로설계자 관점으로 설명하기 위한 노트

---

## 1. NAND와 DRAM의 핵심 차이

NAND는 DRAM과 메모리 철학이 다르다.

> DRAM은 capacitor에 전하를 저장하고 자주 refresh해서 빠르게 읽고 쓰는 volatile memory이고, NAND는 floating gate 또는 charge trap에 전하를 가둬서 전원이 꺼져도 유지되는 non-volatile storage다.

| 구분 | DRAM | NAND Flash |
|---|---|---|
| 저장 방식 | capacitor 전하 | floating gate 또는 charge trap의 전하 |
| 휘발성 | 전원 꺼지면 데이터 사라짐 | 전원 꺼져도 데이터 유지 |
| 기본 cell | 1T1C | 1 transistor 계열 flash cell |
| 동작 단위 | byte/word 단위 접근 가능 | page 단위 read/program, block 단위 erase |
| 속도 | 빠름 | DRAM보다 느림 |
| 용도 | main memory, HBM, LPDDR | SSD, UFS, eMMC, storage |
| 핵심 이슈 | refresh, retention, sense margin, leakage | Vth distribution, retention, endurance, read disturb |
| 회로 관점 | 작은 전압 차이를 빠르게 sense | threshold voltage 상태를 정밀하게 판별 |

---

## 2. DRAM 구조 복습

DRAM cell은 보통 `1T1C` 구조다.

```text
Word Line
   |
Access Transistor
   |
Storage Capacitor
   |
Ground / plate
```

데이터는 capacitor에 전하가 있느냐 없느냐로 저장된다.

```text
전하 많음 -> 1
전하 적음 -> 0
```

하지만 capacitor 전하는 시간이 지나면 새기 때문에 refresh가 필요하다.

읽을 때는 bitline에 아주 작은 전압 변화가 생기고, sense amplifier가 이 차이를 증폭해서 0/1을 판단한다.

DRAM 회로설계 핵심:

- capacitor 용량 확보
- leakage 감소
- access transistor 특성
- bitline capacitance
- sense amplifier offset/noise
- timing margin
- refresh 정책

---

## 3. NAND Flash 구조

NAND는 capacitor가 아니라 transistor의 threshold voltage, 즉 `Vth`를 이용해 데이터를 저장한다.

과거에는 `floating gate`, 요즘 3D NAND에서는 주로 `charge trap` 구조를 많이 쓴다고 이해하면 된다.

개념 구조:

```text
Control Gate / Word Line
------------------------
Insulator
Floating Gate or Charge Trap
Insulator
Channel
```

전자를 가둬두면 transistor의 `Vth`가 변한다.

```text
전하 적음 -> Vth 낮음
전하 많음 -> Vth 높음
```

읽을 때는 특정 read voltage를 걸어보고 cell이 켜지는지 안 켜지는지로 상태를 판단한다.

---

## 4. NAND는 왜 NAND인가

NAND cell들은 여러 개가 직렬로 연결된다. 이 구조를 `NAND string`이라고 한다.

단순화하면:

```text
Bit Line
  |
Select Transistor
  |
Cell 0
  |
Cell 1
  |
Cell 2
  |
...
  |
Cell n
  |
Select Transistor
  |
Source Line
```

여러 memory cell transistor가 직렬로 연결되어 있어서 NAND 구조라고 부른다.

DRAM은 각 cell을 비교적 직접 접근하는 느낌이 강하지만, NAND는 string 안의 여러 cell이 연결되어 있기 때문에 read/program/erase가 더 복잡하다.

---

## 5. NAND의 동작 단위

NAND에서 중요한 단위:

```text
Cell < Page < Block < Plane < Die < Package
```

- `Cell`: 실제 bit를 저장하는 최소 단위
- `Page`: read/program 기본 단위
- `Block`: erase 기본 단위
- `Plane`: 병렬 동작을 위한 내부 영역
- `Die`: 하나의 NAND chip
- `Package`: 여러 die를 쌓아 만든 제품

중요한 점:

```text
Read: page 단위
Program: page 단위
Erase: block 단위
```

NAND는 DRAM처럼 아무 byte나 바로 덮어쓰기 어렵다. 새 데이터를 쓰기 전에 erase가 필요하고, erase는 block 단위로 수행된다.

그래서 SSD controller가 필요하다. Controller는 wear leveling, bad block management, ECC, garbage collection 등을 관리한다.

---

## 6. Read, Program, Erase

### Read

Read는 cell의 `Vth`가 기준 전압보다 높은지 낮은지 판단하는 과정이다.

```text
Read voltage 인가
-> cell이 켜지는가?
-> bitline 전류가 흐르는가?
-> sense amp가 판단
```

### Program

Program은 cell에 전자를 주입해서 `Vth`를 높이는 과정이다.

주로 tunneling 현상을 이용해 charge trap 또는 floating gate에 전자를 넣는다.

```text
전자 주입 -> Vth 증가
```

### Erase

Erase는 저장된 전자를 빼서 `Vth`를 낮추는 과정이다.

```text
전자 제거 -> Vth 감소
```

Program/erase는 높은 전압을 쓰고 cell oxide에 스트레스를 준다. 그래서 반복하면 cell이 열화되고 endurance 문제가 생긴다.

---

## 7. SLC, MLC, TLC, QLC

DRAM은 보통 cell 하나에 1bit를 저장한다고 보면 되지만, NAND는 cell 하나에 여러 bit를 저장할 수 있다.

| 종류 | cell당 bit | 상태 수 |
|---|---:|---:|
| SLC | 1bit | 2개 |
| MLC | 2bit | 4개 |
| TLC | 3bit | 8개 |
| QLC | 4bit | 16개 |

핵심은 상태 수가 늘어날수록 `Vth distribution`을 더 촘촘하게 나눠야 한다는 것이다.

SLC는 단순하다.

```text
Erase state       Program state
낮은 Vth          높은 Vth
```

QLC는 16개 상태를 구분해야 한다.

```text
S0 S1 S2 S3 S4 ... S15
```

상태 간 margin이 좁아지기 때문에 read error, retention, noise, cell-to-cell interference에 더 민감해진다.

면접 문장:

> QLC는 같은 면적에 더 많은 데이터를 저장할 수 있지만, Vth window가 좁아져 신뢰성 관리와 read reference voltage 최적화가 더 중요해집니다.

---

## 8. Vth Distribution

NAND의 핵심은 `Vth distribution`이다.

각 cell은 정확히 하나의 Vth를 갖는 것이 아니라 공정 편차, program variation, noise 때문에 분포를 이룬다.

```text
상태 A 분포      상태 B 분포
   /\              /\
  /  \            /  \
 /    \          /    \
```

상태 간 거리가 충분하면 read가 쉽다.

하지만 시간이 지나거나 cell이 열화되면 분포가 이동하거나 넓어진다.

```text
상태 A 분포  상태 B 분포
    /\       /\
   /  \     /  \
  /    \___/    \
       겹침 발생
```

분포가 겹치면 read voltage로 구분하기 어려워지고 bit error가 증가한다.

---

## 9. NAND 주요 불량과 신뢰성 이슈

### Retention

저장된 전하가 시간이 지나며 빠져나가 Vth가 변하는 현상.

```text
시간 경과 -> charge loss -> Vth shift -> read error
```

### Endurance

Program/erase를 반복하면서 oxide가 손상되고 cell 특성이 열화되는 문제.

```text
P/E cycle 증가 -> oxide stress 증가 -> Vth distribution 악화
```

### Read disturb

읽기 동작을 반복할 때 선택되지 않은 주변 cell에도 pass voltage가 걸리면서 Vth가 변하는 현상.

### Program disturb

어떤 cell을 program할 때 근처 cell 상태가 의도치 않게 영향을 받는 현상.

### Cell-to-cell interference

인접 cell의 전하 상태 변화가 coupling을 통해 내 cell의 Vth에 영향을 주는 현상.

### Bad block

공정상 또는 사용 중 결함으로 정상 동작하지 않는 block. NAND에서는 bad block이 어느 정도 존재하는 것이 자연스럽고, controller가 관리한다.

---

## 10. 2D NAND와 3D NAND

옛날 NAND는 평면으로 cell을 작게 만드는 방향이었다.

```text
2D NAND: 옆으로 줄이기
```

하지만 너무 작아지면 간섭, leakage, 신뢰성 문제가 커진다. 그래서 요즘은 위로 쌓는다.

```text
3D NAND: 수직으로 쌓기
```

3D NAND는 cell을 수직 방향으로 여러 층 쌓아서 용량을 늘린다.

그래서 NAND는 요즘 `몇 nm`보다 `몇 layer`가 중요하다.

예:

```text
176-layer NAND
238-layer NAND
321-layer NAND
```

SK hynix의 `321-layer QLC NAND`는 수직으로 321층을 쌓고, cell 하나에 4bit를 저장하는 방식이라고 보면 된다.

---

## 11. 회로설계자 입장에서 보는 NAND

NAND는 단순히 memory cell만 보는 것이 아니라 peripheral circuit이 매우 중요하다.

주요 회로 블록:

- row decoder
- column decoder
- page buffer
- sense amplifier
- charge pump
- high voltage switch
- voltage generator
- state machine/control logic
- ECC 관련 interface
- bad block management interface

특히 NAND는 program/erase에 높은 전압이 필요해서 `charge pump`와 high-voltage 회로가 중요하다.

DRAM 회로가 빠른 sensing과 refresh/timing이 중요하다면, NAND 회로는 다음이 중요하다.

- 여러 Vth state를 정확히 읽는 sensing
- read reference voltage 생성
- program verify
- high voltage generation
- disturb 억제
- endurance/retention 보정
- ECC와 controller 협업

---

## 12. ISPP: Incremental Step Pulse Programming

NAND program은 한 번 전압을 걸고 끝나는 것이 아니라, `ISPP` 방식으로 점진적으로 program한다.

`ISPP = Incremental Step Pulse Programming`

개념:

```text
조금 program
-> verify
-> 부족하면 더 program
-> verify
-> 목표 Vth에 들어오면 stop
```

QLC처럼 상태가 많을수록 Vth를 정확히 원하는 범위에 넣어야 하므로, 쓰기 동작 자체가 analog tuning에 가깝다.

---

## 13. DRAM Sense Amp vs NAND Sense Amp

둘 다 sense amplifier가 있지만 성격이 다르다.

### DRAM sense amp

- bitline의 아주 작은 전압 차이를 빠르게 증폭
- destructive read 이후 restore 필요
- speed와 offset이 중요

### NAND sensing

- selected cell/string에 전류가 흐르는지 판단
- 기준 read voltage와 비교
- 여러 Vth level을 구분해야 함
- read retry, reference voltage 조정 가능

즉 DRAM은 빠른 binary sensing에 가깝고, NAND는 여러 threshold 상태를 안정적으로 판별하는 쪽에 가깝다.

---

## 14. NAND가 DRAM보다 느린 이유

NAND는 구조적으로 DRAM보다 느리다.

이유:

- string 구조라 접근이 복잡함
- page 단위 read/program
- block 단위 erase
- program/erase에 높은 전압과 긴 시간이 필요
- verify 과정 필요
- ECC 처리 필요
- controller의 address translation 필요

그래서 NAND는 CPU가 직접 main memory처럼 쓰기 어렵고, SSD/UFS/eMMC 같은 storage로 쓰인다.

---

## 15. PE 직무와 연결

PE 관점에서 NAND를 보면 이런 질문으로 바뀐다.

- 특정 block에서 error가 많이 나는가?
- P/E cycle이 증가할수록 fail이 증가하는가?
- retention time에 따라 Vth distribution이 이동하는가?
- 고온 보관 후 read error가 증가하는가?
- read disturb 조건에서 특정 wordline이 취약한가?
- die/plane/block/page 위치별 fail pattern이 있는가?
- ECC로 복구 가능한 수준인가?
- read reference voltage 조정으로 개선되는가?

즉 NAND PE는 단순히 "불량입니다"가 아니라, `Vth distribution`, `P/E cycle`, `retention age`, `temperature`, `block 위치`, `read count`를 나누어 봐야 한다.

---

## 16. 면접 답변용 정리

### 질문: NAND와 DRAM의 차이를 설명해주세요.

> DRAM은 capacitor에 전하를 저장하는 volatile memory이고, refresh가 필요하지만 빠른 random access가 가능해 main memory로 쓰입니다. 반면 NAND Flash는 floating gate나 charge trap에 전하를 저장해 threshold voltage를 변화시키는 non-volatile memory입니다. 전원이 꺼져도 데이터가 유지되지만, page 단위 program/read와 block 단위 erase 구조라 DRAM보다 느리고 controller 관리가 중요합니다. PE 관점에서는 DRAM은 retention, refresh, leakage, sense margin이 중요하고, NAND는 Vth distribution, retention, endurance, read disturb, P/E cycle에 따른 신뢰성 분석이 중요하다고 생각합니다.

### 질문: NAND에서 Vth distribution이 왜 중요한가요?

> NAND는 cell의 threshold voltage 상태를 구분해 데이터를 저장합니다. SLC는 2개 상태만 구분하면 되지만, QLC는 16개 상태를 구분해야 해서 상태 간 margin이 좁습니다. 시간이 지나거나 P/E cycle이 증가하면 Vth distribution이 이동하거나 넓어져 read error가 증가할 수 있습니다. 따라서 PE 관점에서는 retention time, 온도, P/E cycle, read count, block 위치별로 error pattern과 Vth shift를 분석해야 합니다.

### 질문: 3D NAND는 왜 필요한가요?

> 2D NAND는 cell을 평면 방향으로 계속 줄이다 보니 간섭, leakage, 신뢰성 문제가 커졌습니다. 3D NAND는 cell을 수직으로 적층해 용량을 늘리는 방식입니다. 그래서 최신 NAND는 몇 nm보다 몇 layer인지가 중요하고, 적층 수가 늘어날수록 공정 균일도, channel 특성, layer별 편차, 수율 관리가 중요해진다고 이해하고 있습니다.

---

## 17. 복습 질문

1. NAND와 DRAM은 데이터를 각각 어디에 저장하는가?
2. NAND에서 Vth가 데이터 저장과 어떤 관계가 있는가?
3. NAND string 구조는 왜 read/program/erase를 복잡하게 만드는가?
4. Page와 block은 각각 어떤 동작의 기본 단위인가?
5. QLC가 SLC보다 신뢰성 관리가 어려운 이유는 무엇인가?
6. Retention, endurance, read disturb는 각각 무엇인가?
7. 2D NAND에서 3D NAND로 넘어간 이유는 무엇인가?
8. NAND에서 charge pump가 중요한 이유는 무엇인가?
9. ISPP는 왜 필요한가?
10. NAND PE에서 Vth distribution을 어떤 조건별로 분석해야 하는가?
