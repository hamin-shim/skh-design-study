# SK hynix 설계 직무 면접 핵심 총정리 v1

작성일: 2026-10-09
근거 자료: `하이닉스_CMOS설계_대화요약.md`, `sk-hynix-interview-context.md`, `CMOS 설계 면접 총정리.html`(15장 덱), `A!SK_설계_전공문항은행.md`(Q1~Q47), `2026-10-04_Half-Day_준비로드맵.md`, codex-skh `설계_JD_상세해설_및_준비범위.md`
용도: A!SK 전공 문항, AI 문제해결 PT, 심층 인터뷰 전공 꼬리질문에 공통으로 쓰는 **한 장짜리 지도 + 영역별 필수 항목**. 상세 답변은 문항은행 Q번호를 따라간다.

---

## 0. 이 자료 읽는 법

| 표시 | 뜻 |
|---|---|
| ★★★ | 거의 확실히 나오거나, 다른 질문의 기반이 되는 항목 |
| ★★ | 나올 가능성이 높고 메모리 설계와 직접 연결 |
| ★ | 꼬리질문·차별화용 |
| ✓학습 | 이전 대화에서 이미 공부한 내용 (복습만) |
| ○미학습 | 아직 다루지 않은 내용 (다음 공부 대상) |
| → Qn | 문항은행 해당 번호에 3분 답변 있음 |

각 항목은 **꼭 알아야 할 것 → 나올 질문 → 면접 한 문장 → 함정** 순서다.
기출은 개인 후기 기반이라 단정할 수 없다. 후기에서 반복된 주제: CMOS 인버터, 전파 지연, 노이즈 마진, 조합 vs 순차, FF vs 래치, setup/hold, STA, clock skew, jitter, blocking vs non-blocking, SRAM vs DRAM, DRAM 동작, HBM, NAND 셀, 상황형(회로 오류 원인 분석 순서, 타이밍 오류, 신호 무결성). 수준은 **수식 유도보다 개념·원인·영향·해결책**.

---

## 1. 전체 지도: 모든 질문은 R · C · V로 돌아온다

```
소자            게이트             지연·타이밍          전력               메모리·시스템
I_ON, V_TH  →  인버터,NAND,NOR  →  t_p=0.69RC,STA  →  αCV²f + 누설  →  디코더·WL·SA·셀·I/O·HBM
"전류를 얼마나"  "R과 C를 어떻게"   "얼마나 빨리"      "그 대가"          "어디에 쓰이나"
```

**핵심 두 식 (외울 것은 이것뿐)**
- 속도 ∝ I / (C · V)
- 전력 ∝ α · C · V² · f + 누설(∝ 10^(−V_TH/S))

**모든 trade-off의 출발 고리**
VDD↓ → 동적 전력 제곱 감소 → 속도↓ → V_TH↓로 보상 → 누설 지수 증가 → S ≥ 60 mV/dec 한계 때문에 끝없이 못 내린다.

**산포의 출발점**: σV_TH ∝ 1/√(W·L) (Pelgrom) → 지연·누설·센스앰프 offset·SRAM 안정성이 흔들린다. 메모리는 평균이 아니라 **분포의 tail**이 스펙을 정한다.

**면접 유형별로 쓰는 법**
| 유형 | 요구 | 답 틀 |
|---|---|---|
| A!SK 전공 (1분 준비, ~2분 답) | 정확한 개념 + 왜 | 정의 → 원리(왜) → 한계·trade-off → 설계자 대응 → 연결 |
| AI 문제해결 PT | 정답 없는 trade-off, 원인 분석 | 대상 확정 → 물리·회로식 연결 → 크기 비교(지수 vs 선형) → 제약(worst case) → 결정과 보완 → 리스크·검증 |
| 심층 인터뷰 꼬리질문 | 내 경험의 깊이 | 경험 → 그때 쓴 원리 → 숫자와 기준 → 한계와 다시 한다면 |

---

## 2. 소자: MOSFET 기본 (✓학습)

### 2.1 동작 영역과 핵심 효과 ★★★ → Q11, Q31
| 항목 | 꼭 알 것 |
|---|---|
| 동작 영역 | OFF/subthreshold: V_GS<V_TH (전류 0 아님) / Triode: V_DS<V_GS−V_TH / Saturation: V_DS≥V_GS−V_TH. V_GS로 ON 여부, V_DS로 영역 구분 |
| V_TH vs V_T | V_TH=문턱전압, V_T=kT/q≈25.9 mV. 교재마다 표기가 다르니 식마다 확인 |
| Body effect | V_SB↑ → V_TH↑. 원인은 직렬 연결이 아니라 source–body 전압차. NAND 직렬 스택 위쪽 NMOS, DRAM pass TR의 '1' 전달 손실과 연결 |
| Subthreshold swing | S = n(kT/q)ln10, 이상 한계 ≈60 mV/dec(300K). I_OFF를 10배 줄이려면 V_TH를 S만큼 올려야 함 |
| CLM | I_D≈I_Dsat(1+λV_DS), λ∝1/L. 문제의 본질은 전류 증가가 아니라 **이상 전류원 특성이 깨지는 것**(r_o 감소 → 이득 g_m·r_o 감소). 대응: cascode, 긴 L |
| Velocity saturation | 고전계에서 v→v_sat. I_Dsat이 overdrive에 2차→1차. CLM과 다른 현상 |
| Short channel effect | V_TH roll-off, DIBL(V_TH,eff=V_TH0−ηV_DD), punch-through, HCI. 결과적으로 I_OFF 증가·산포 증가 |
| 온도 | T↑ → S↑, V_TH↓ → I_OFF 지수 증가. I_ON은 V_TH↓(증가)와 이동도↓(감소)가 경쟁하므로 단정 금지 (일반적인 고전압에서는 이동도 효과로 느려짐, 저전압에서는 역전 가능: temperature inversion) |

**나올 질문**: "Short channel effect를 설명하세요", "온도가 오르면 트랜지스터는?", "MOSFET 동작 영역별 용도는?"(Triode=스위치·저항, Saturation=증폭·전류원, Subthreshold=초저전력·누설)

### 2.2 I_ON/I_OFF 산포와 V_DD 예산 ★★★
- **같은 ΔV_TH가 I_OFF에는 지수, I_ON에는 1~2차.** I_OFF 산포(decade) ≈ ΔV_TH/S. 예: ΔV_TH=200 mV, S=100 mV/dec → 100배. I_ON은 수십 %~2배.
- 물리적 이유: ON은 채널 전하에 선형인 drift 전류, OFF는 장벽을 열적으로 넘는 diffusion 전류(Boltzmann 지수).
- 흔들리는 변수는 L, W, t_ox, 도핑(RDF), μ인데, **지수로 증폭되는 통로가 V_TH 하나**라 I_OFF는 V_TH만 봐도 거의 설명된다. S는 원인이 아니라 환산 계수.
- V_DD = gate swing 전체 예산, V_TH = OFF 억제용과 ON 구동용의 경계. I_ON/I_OFF ∝ (V_DD−V_TH)^α × 10^(V_TH/S).
- DRAM 연결: V_PP 부스트와 negative WL로 WL swing을 V_DD에서 분리 → 셀은 V_TH를 높게 두고도 I_ON 확보.

> **한 문장**: "I_OFF는 V_TH에 지수적으로, I_ON은 overdrive의 1~2제곱에 비례하기 때문에 같은 V_TH 산포라도 I_OFF는 100배 이상 퍼지고, 그래서 누설은 worst-case tail 기준으로 설계합니다."

### 2.3 Scaling 로드맵 ★★
| 세대 | 기술 | 해결 | 건드리는 항 |
|---|---|---|---|
| 90/65nm | Strained Si | V_TH를 못 낮추는 상황에서 I_ON | μ |
| 45/32nm | HKMG | 얇은 SiO₂ 게이트 터널링, poly depletion | C_ox(물리 두께와 분리) |
| 22nm | FinFET | DIBL·S 악화 | electrostatics |
| 3nm↓ | GAA(nanosheet) | fin 한계 | 4면 gate |

- 방향은 일관되게 "gate가 채널을 더 많이 감싼다".
- 설계 영향: FinFET은 W가 fin 개수로 양자화 → SRAM cell ratio·아날로그 미세 조정 제약. GAA는 sheet 폭으로 일부 회복. 기생 R/C·self-heating 증가 → **DTCO**.
- DRAM 셀 TR도 gate가 채널을 감싸는 방향은 같다(saddle-fin, 차세대 4F² 수직 채널). 다른 것은 **목표**: 로직은 I_ON·속도, DRAM 셀은 I_OFF·retention. 그래서 게이트를 실리콘 안에 묻어(**BCAT, recess channel**) 좁은 면적에서도 채널을 U자로 길게 확보한다. 주변회로에는 HKMG 도입(SK hynix 뉴스룸 "HKMG" 검색).
  - 읽을거리(한국어): [서울경제 D램 특집 2편, Planar→RCAT→BCAT→VCAT (2022-01)](https://sedaily.com/NewsView/260ZLT02IO), [디지털데일리 3D 메모리 로드맵, 8F²→6F²→4F²→3D (2024-11)](https://m.ddaily.co.kr/page/view/2024112516263197873)

---

## 3. CMOS 게이트·지연·전력 (✓학습)

### 3.1 CMOS 인버터 ★★★ → Q10
- VTC: 전이 구간 이득이 클수록 노이즈 마진(NM_H=V_OH−V_IH, NM_L=V_IL−V_OL)이 넓다.
- V_M ≈ VDD/2로 맞추려면 μn≈2~3μp라서 PMOS 폭을 2~3배. **진짜 이유는 상승 R과 하강 R을 맞추는 것**이고, 이후 모든 사이징의 기준 R이 된다.
- 정적 전력≈0 (한쪽이 항상 꺼짐), 남는 것은 누설.

### 3.2 전파 지연 손잡이 ★★★
t_p = 0.69 · R_eq · C_L, R_eq ∝ VDD / (W·(VDD−V_TH)^α)

| 손잡이 | 효과 | 대가 |
|---|---|---|
| W↑ | R↓ | 입력 C↑로 앞단 느려짐, 면적. **self-loading으로 0.69·R·C_int 근처에서 포화** |
| VDD↑ | 전류↑ | 전력 V², 신뢰성(TDDB·HCI·BTI·EM 가속) |
| V_TH↓ | 전류↑ | 누설 지수 증가 |
| C_L↓ | 직접 감소 | 마음대로 못 줄임: C_L = 다음 단 입력 C(fan-out) + 배선 C → fan-out 제한, 가까운 배치, 버퍼로 분할 |

### 3.3 입력 패턴·사이징·큰 fan-in ★★
- **같은 전환인데 지연이 다른 이유 두 가지**: ① 몇 개의 TR이 전류를 주나 ② 내부 노드 C_int까지 충·방전하나. NAND2 하강 69/62/50 ps, 상승 35/76/57 ps (최악은 PMOS 1개 + C_int까지 충전). → 늦게 오는 신호를 출력 쪽 TR에, STA는 최악 케이스로.
- **사이징 규칙**: 최악 경로 ΣR = 기준 인버터(N1, P2)의 R. NAND2=N2/P2, NOR2=N1/P4. 공유 TR이 있으면 경로별 저항 예산을 나눈다(×개수 아님).
- **NAND 선호 이유**: NOR은 느린 PMOS를 직렬로 쌓아 크기와 입력 용량이 커진다.
- **큰 fan-in**: Elmore τ = R₁C₁ + (R₁+R₂)C₂ + … → 지연 ∝ N². 대책: progressive sizing(접지 쪽 크게), transistor ordering(늦은 신호를 출력 쪽), 게이트 쪼개기(NAND/NOR 트리, **디코더 predecode가 이 구조**).

### 3.4 Logical effort ★ (공식 유도는 후순위, 직관만)
- d = g·h + p. g = 같은 전류를 낼 때 입력 용량이 인버터의 몇 배인가 = 로직 기능의 비용. NAND2 4/3, NOR2 5/3, n입력 NAND (n+2)/3, NOR (2n+1)/3.
- 최적은 단마다 g·h가 같아지는 지점. 단당 effort ≈ 4(FO4), 단수 N ≈ log₄F. 2단 버퍼 u=√x.
- 진짜 이해: 단이 적으면 한 단이 너무 무겁고, 많으면 p가 쌓인다. → **WL 드라이버·클럭 버퍼 체인 설계 원리**.

### 3.5 전력 ★★★ → Q10, Q23, Q43
| 성분 | 식/원인 | 특징 |
|---|---|---|
| 동적 | α·C·V²·f | 대부분. VDD 제곱 |
| 단락 | 입력 slope 동안 N·P 동시 ON | 입력이 느릴수록 증가 |
| 누설 | subthreshold ∝ e^(−V_TH/nV_T), GIDL, gate 누설, junction | 대기 상태에서 지배적 |

**저전력 기법**: clock gating(α↓, **래치 기반 ICG로 glitch 방지**), power gating(누설↓, retention FF·isolation cell·wake-up rush current), multi-V_TH(critical path만 LVT), multi-VDD(level shifter 필요), DVFS. 메모리에서는 self-refresh, deep power-down, LPDDR의 낮은 I/O 전압.

#### 저전력 기법 상세
**① Clock gating: α를 어떻게 낮추나**
- α(activity factor) = 한 사이클에 노드가 0→1로 충전될 확률. 클럭은 매 사이클 토글하므로 α = 1이고, 클럭 트리와 FF 클럭 핀의 C가 커서 동적 전력의 큰 몫을 차지한다.
- 레지스터 값이 바뀌지 않는 사이클(EN = 0)에는 그 레지스터 묶음의 클럭을 아예 멈춘다 → 게이트 뒤쪽 클럭망과 FF 내부 노드가 토글하지 않으니 α = 0.
- RTL `if (en) q <= d;`는 원래 MUX로 이전 값을 다시 넣으며 클럭은 매번 토글한다. 합성 툴이 이 MUX를 ICG 셀로 바꾸면 클럭 자체가 멈춘다.
- **AND만 쓰면 glitch가 나는 이유**: EN은 클럭 상승 엣지에서 출발한 로직을 거쳐 늦게 바뀐다. 즉 CLK = 1인 구간 중간에 바뀔 수 있다. 이때 GCLK = CLK·EN은 엉뚱한 시점에 시작하는 펄스나 짧게 잘린 펄스가 되고, FF가 잘못된 엣지를 잡거나 최소 펄스 폭을 어긴다.
- **ICG(Integrated Clock Gating) 셀**: CLK = 0일 때만 투명한 래치로 EN을 잡은 뒤 AND한다. CLK = 1 동안에는 래치가 값을 고정하므로 AND 입력이 클럭 high 구간에 절대 바뀌지 않아 온전한 펄스만 나온다. STA는 EN이 클럭 상승 전에 도착하는지(clock gating setup) 검사한다.
- 대가: ICG 면적, 클럭 경로 지연으로 skew 관리, EN 타이밍 마진.

**② Power gating: 무엇을 하나**
- Clock gating은 동적 전력만 줄인다. 클럭이 멈춰도 VDD가 연결돼 있으면 누설은 계속 흐른다.
- 오래 쉬는 블록은 상시 VDD와 블록 사이에 스위치 트랜지스터(header PMOS 또는 footer NMOS, 누설 작은 HVT)를 두고 꺼서 전원 자체를 끊는다 → 누설 ≈ 0.
- 함께 필요한 것: **retention FF**(상시 전원의 작은 래치에 상태 저장 후 복구), **isolation cell**(꺼진 블록의 떠 있는 출력을 0/1로 고정해 켜진 블록의 X 전파·단락 전류 방지), **rush current 관리**(켤 때 블록 C를 한꺼번에 충전해 이웃 IR drop → 스위치를 단계적으로 켬).
- 순서: 끌 때 격리 → 저장 → 차단, 켤 때 전원 → 복구 → 격리 해제. 깨어나는 데 시간이 걸려 짧게 쉬면 clock gating, 오래 쉬면 power gating.

**③ Multi-V_TH**
- 같은 기능의 셀을 V_TH만 다르게 준비(LVT·SVT·HVT). 누설은 V_TH에 지수라 LVT는 빠르지만 누설이 크다.
- 대부분 경로는 timing 여유가 있으므로 기본은 HVT·SVT, slack이 음수인 critical path만 LVT로 교체(또는 LVT로 시작해 여유 있는 경로를 HVT로). 대가: 공정 마스크 추가.

**④ Multi-VDD와 DVFS**
- Multi-VDD: 블록마다 고정된 다른 전압(voltage island). 경계에 level shifter 필요(낮은 쪽 '1'이 높은 쪽 PMOS를 완전히 끄지 못해 정적 전류·오동작).
- DVFS: 부하가 적을 때 f를 낮추고, 낮은 f에서는 timing 여유가 생기므로 V도 낮춘다. P ∝ V²f라 거의 세제곱으로 감소. 올릴 때는 V 먼저(낮은 V에서 f만 올리면 setup 위반), 내릴 때는 f 먼저. PMIC·VRM과 PLL 재설정이 필요하고 전환 시간이 든다.

**더 보기**: [한국어 · 저전력 IC 설계 기법 기고(elec4, 2021)](https://www.elec4.co.kr/article/articleView.asp?idx=28521) · [영어 · 기법별 정리와 면접 Q&A](https://ecrionix.org/low-power/) · [Power gating 위키](https://en.wikipedia.org/wiki/Power_gating) · [Multi-threshold CMOS 위키](https://en.wikipedia.org/wiki/Multi-threshold_CMOS)

### 3.6 로직 스타일과 메모리 ★★ (덱 11장)
| 스타일 | 장점 | 대가 | 메모리 속 위치 |
|---|---|---|---|
| Complementary | 정적 전력≈0, 마진 큼 | 2N개 | 디코더, 주변 로직 |
| Ratioed | N+1개, 면적 작음 | DC 전류, V_OL≠0 | **SRAM 읽기·쓰기 "싸움"(cell ratio, pull-up ratio)** |
| Pass transistor | 소자 적음, MUX | V_TH 손실, 구동력 없음 | **DRAM access TR → WL을 VPP로 부스트** |
| Dynamic | 빠름, PUN 불필요 | 누설·글리치·charge sharing 취약 | **비트라인 precharge** |

> 메모리 셀과 주변회로는 대부분 complementary가 아닌 쪽이라, 면접에서는 "메모리 질문 속에 숨어서" 나온다.

### 3.7 Glitch ★★
- 원인: 지연이 다른 경로가 한 게이트에서 만나 출력이 잠깐 튐.
- 영향: 전력(α↑, 깊은 로직일수록 누적), 기능(dynamic 노드·클럭·리셋·WL에서 오동작).
- **메모리 연결**: 주소 전환 중 디코더 glitch → 엉뚱한 WL이 순간 열림 → 셀 데이터 교란 → 그래서 **주소가 안정된 뒤 enable로 WL을 띄운다.**
- 대책: 경로 균형, 래치로 끊기, 래치 기반 clock gating, enable 타이밍 정렬.

---

## 4. 디지털 설계·타이밍 (○미학습, 후기 빈출 → 다음 공부 1순위)

### 4.1 조합 vs 순차, 래치 vs FF ★★★
- 조합: 출력이 현재 입력만의 함수. 순차: 상태(이전 값)를 저장.
- **래치 = level-sensitive**(enable 동안 투명), **FF = edge-triggered**(master-slave 래치 2개). 래치는 작고 time borrowing이 가능하지만 타이밍 분석이 어렵고, 의도치 않은 래치는 버그.
- RTL 함정: 조합 always 블록에서 if/case의 모든 경우를 할당하지 않으면 **래치가 추론**된다 (default 할당, else 처리).

### 4.2 Setup / Hold ★★★ → Q17
- Setup: 클럭 엣지 **전**에 데이터가 안정돼야 하는 시간. Hold: 엣지 **후**에 유지돼야 하는 시간.
- **Setup 조건**: T_clk ≥ t_cq + t_logic,max + t_setup − t_skew (+ jitter 여유)
- **Hold 조건**: t_cq + t_logic,min ≥ t_hold + t_skew
  (t_skew = capture 클럭이 launch보다 늦게 도착하는 양. 양의 skew는 setup에 유리, hold에 불리)
- **Hold 위반은 주파수를 낮춰도 안 고쳐진다** → 식에 T_clk가 없다. 같은 엣지에서 launch와 capture가 경쟁하는 문제. 대책: 짧은 경로에 buffer/delay 삽입, skew 조정.
- Setup 위반 대책: 로직 단수 줄이기, pipeline, 리타이밍, 사이징·LVT 셀, 배치 개선, 주파수 낮추기(마지막 수단).
- Jitter: 클럭 엣지의 시간 흔들림. cycle-to-cycle jitter는 setup 여유를 깎는다. hold는 같은 엣지 기준이라 영향이 작다.
- Skew 원인: 클럭 배선 길이·부하 차이, 버퍼 PVT 차이. CTS로 균형, useful skew로 일부러 활용하기도 한다.

> **한 문장**: "Setup은 가장 느린 경로가 다음 엣지 전에 도착하는지, hold는 가장 빠른 경로가 같은 엣지에서 이전 값을 덮어쓰지 않는지의 문제라서, setup은 주파수로 완화되지만 hold는 주파수와 무관해 지연을 넣어 고쳐야 합니다."

### 4.3 STA ★★
- 모든 경로를 입력 벡터 없이 정적으로 계산해 setup/hold 만족 여부를 확인. 빠르고 전수 검사지만 **기능의 정답은 검증하지 않는다** → 시뮬레이션과 서로 대체 불가.
- 제약(SDC): 클럭 정의, input/output delay, false path, multicycle path. 잘못된 제약이면 STA 통과도 의미 없음.
- PVT 코너(SS/FF, 고온/저온, 저전압/고전압)별로 확인. 셋업은 느린 코너, 홀드는 빠른 코너가 보통 최악. OCV로 칩 내 편차 반영.
- "RTL sim은 통과, 합성 후 setup slack 음수" 대응 순서: 제약이 맞는가 → 어느 경로인가(로직 단수? 배선? fan-out?) → 구조(pipeline) vs 구현(사이징·배치) 중 어디서 풀지.

### 4.4 Metastability와 CDC ★★ → Q18
- 비동기 신호가 setup/hold를 어기면 FF 출력이 중간값에 머물다 임의로 결정 → 오동작 전파.
- MTBF ∝ e^(t_r/τ) / (T₀·f_clk·f_data): 결정 시간 t_r을 늘릴수록 지수적으로 개선.
- 대책: **1비트는 2-FF synchronizer**, 멀티비트는 Gray code(한 번에 1비트만 변화), **async FIFO**, handshake. 멀티비트를 FF 2단으로 각각 동기화하면 비트마다 다른 사이클에 넘어가 틀린 값이 된다.

### 4.5 Verilog 기본 ★★ → Q19
- 순차 always(@posedge clk): **non-blocking(<=)**, 조합 always(@*): **blocking(=)**. 섞으면 시뮬레이션 race, 합성 결과와 불일치.
- FSM: Moore(상태만으로 출력) vs Mealy(상태+입력, 빠르지만 glitch 가능). 상태 인코딩 binary/one-hot.
- reset: 동기(타이밍 분석 쉬움) vs 비동기(클럭 없이 리셋, 해제 시 동기화 필요: async assert, sync deassert).

### 4.6 Pipeline ★★ → Q25
- 장점: 임계 경로를 나눠 f_max·throughput↑. 단점: latency(사이클 수)↑, 레지스터 면적·클럭 전력↑, hazard·제어 복잡. 레지스터 overhead(t_cq+t_setup)가 단마다 붙어 무한히 나눌 수 없다.

### 4.7 설계 Flow와 물리 검증 ★★ → Q20~Q22
- 사양 → RTL → 기능 시뮬레이션 → 합성(SDC) → DFT 삽입 → floorplan·전원 계획 → placement → CTS → routing → 기생 추출 → STA·IR/EM·DRC/LVS signoff → GDSII.
- Pre-layout은 배선 기생이 추정치, post-layout은 추출한 R·C 반영 → 지연·전력이 달라진다.
- **DRC = 제조 규칙 만족, LVS = 레이아웃 연결이 회로도와 일치.** 둘 다 통과해도 성능·타이밍·IR drop은 보장 안 됨.
- 메모리 설계는 셀 어레이·SA·WL 드라이버 같은 **full-custom**과 제어 로직의 **디지털 구현**이 섞여 있다.

### 4.8 검증 ★ → Q24, Q26
- MBIST: 칩 내부에서 메모리를 자동 테스트. **March C−** {⇕(w0); ⇑(r0,w1); ⇑(r1,w0); ⇓(r0,w1); ⇓(r1,w0); ⇕(r0)}, 10N → stuck-at, transition, address decoder, 일부 coupling fault 검출. 결과로 redundancy repair(fuse).
- Coverage: code(line·branch·toggle) / functional / assertion. **100%여도 버그 없음이 아니다** (검증 계획에 없는 시나리오, 잘못된 reference model).

---

## 5. SRAM (○미학습, 다음 공부 A) ★★

- 6T: cross-coupled 인버터 2개 + access TR 2개. 빠르고 refresh 불필요, 면적·누설이 큼 → cache, 로직 칩 내장 메모리.
- **Hold**: WL=0, 래치가 값 유지. 지표 hold SNM.
- **Read**: BL/BLB를 VDD로 precharge → WL on → '0' 저장 노드 쪽 BL이 방전. 이때 '0' 노드가 access TR 때문에 살짝 올라감 → 반대 인버터 V_M을 넘으면 뒤집힘(**read disturb**). 그래서 **pull-down이 access를 이겨야**: cell ratio(PD/access) 크게.
- **Write**: BL을 강제로 0 → **access가 pull-up을 이겨야** 뒤집힘: pull-up ratio(PU/access) 작게.
- 상충: read 안정성(access 약하게) vs write 능력(access 강하게) → ratioed 설계의 전형. 보조: read/write assist(WL underdrive, negative BL), 8T(읽기 포트 분리).
- SNM: 버터플라이 곡선 안의 최대 정사각형. V_TH mismatch(Pelgrom)와 VDD↓에 취약 → **V_min**을 결정.
- FinFET: 비율을 fin 개수로만 조정(1:1:1, 1:2:1 등) → 미세 조정 불가.

> **한 문장**: "6T SRAM은 ratioed 구조라서 읽기는 pull-down이 access를 이기도록 cell ratio를, 쓰기는 access가 pull-up을 이기도록 pull-up ratio를 정하는데, 둘이 상충해 V_TH 산포가 큰 저전압에서 V_min을 결정합니다."

---

## 6. DRAM (○미학습, 하이닉스 주력 → 최우선) ★★★

### 6.1 셀과 읽기 동작 → Q1, Q6
- **1T1C**: access NMOS(pass TR) + 커패시터. 전하 유무로 데이터 저장, 누설로 전하가 빠지므로 refresh 필요.
- **읽기 순서**
  1. Precharge: BL/BLB를 VBL = VDD/2로 equalize
  2. ACT: WL을 **VPP**로 올림 → 셀과 BL이 **charge sharing**
     **ΔV = (VDD/2) · C_S / (C_S + C_BL)** — C_BL이 C_S보다 훨씬 커서 ΔV는 수십~100 mV 수준으로 작다
  3. Sense amp(cross-coupled 래치) enable → BL을 VDD/0으로 증폭
  4. **Restore**: 증폭된 값이 열린 WL을 통해 셀에 다시 쓰인다 (읽기는 파괴적)
  5. Column select로 데이터를 local/global IO로 → I/O
  6. PRE: WL off, BL 다시 equalize
- 타이밍 파라미터: tRCD(ACT→RD), CL(RD→데이터), tRAS(ACT→PRE 최소, restore 완료), tRP(PRE→다음 ACT).
- **왜 VPP?** NMOS pass TR은 '1'을 VDD−V_TH(+body effect)까지만 전달 → WL을 VDD+V_TH 이상으로 부스트해야 '1'을 온전히 쓴다. VPP는 charge pump로 만든다.
- **Negative WL / VBB**: 꺼진 셀의 subthreshold 누설을 줄여 retention↑.

### 6.2 Sense amp ★★★ → Q6, Q45
- 구조: cross-coupled 인버터 래치 + equalize/precharge TR + enable(SAN/SAP). 작은 ΔV를 양귀환으로 풀스윙.
- **Offset**: 래치 TR의 V_TH mismatch → ΔV가 offset보다 작으면 오판정. 소자를 키우면 σ∝1/√(WL)로 줄지만 면적·BL 피치·속도 손실. 대책: offset cancellation, 레이아웃 대칭, enable 타이밍(신호가 충분히 생긴 뒤 증폭).
- **Sense margin 부족 접근**: 신호(C_BL↓: BL 분할, C_S↑) / 판별(offset↓, 타이밍) / 노이즈(VBLP 정확도, 인접 BL coupling, 증폭 순간 전원 노이즈) → 어떤 corner·위치에서 부족한지 먼저 분리 → Monte Carlo.
- Bitline 구조: folded(8F², 노이즈 상쇄 유리) vs open(6F², 고집적, 노이즈 취약). 현재 DRAM은 6F² open이 주류, 차세대로 4F²(수직 채널) 연구.

### 6.3 Refresh·Retention·Row hammer ★★★ → Q2, Q42
- 표준: 일정 시간(일반 온도 64 ms) 안에 모든 row를 refresh. 고온(85°C 초과)에서는 누설 증가로 주기를 2배 빠르게.
- **가장 새는 tail 셀이 retention과 refresh 주기를 정한다.** 비용: refresh 동안 bank 사용 불가(성능), refresh 전력(특히 대기 전력·모바일).
- 대응: 온도 센서 기반 refresh 주기 조절(TCSR), self-refresh, 부분 refresh, ECC·repair로 약한 셀 처리.
- **Row hammer**: 한 row를 반복 활성화하면 인접 row 셀 전하가 교란. 셀 간격이 좁아질수록 심해짐. 대책: TRR, RFM, PRAC(DDR5 표준 확장) 등 인접 row 추가 refresh.

### 6.4 셀 TR vs 주변회로 TR ★★
| | 셀 TR | 주변회로(peri) TR |
|---|---|---|
| 목표 | I_OFF 최소화(retention) | 속도(I_ON) |
| V_TH | 높게 | 낮게, multi-V_TH |
| 구조 | 매립형 WL(BCAT)로 유효 L↑ | HKMG 도입 |
| 보완 | VPP, negative WL | — |
- **PT 예제: 셀 V_TH를 올리면?** 이득: I_OFF 지수↓ → retention↑ → refresh 전력↓. 손실: I_ON↓로 write 시간↑, '1' 쓰기에 더 높은 VPP 필요 → 산화막 신뢰성·pump 전력. 숨은 변수: 도핑으로만 올리면 junction leakage·GIDL↑ → **최적점 존재**. 제품별: 모바일은 retention, 서버/HBM은 고온 retention 안에서 속도.

### 6.5 DRAM 미세화가 어려운 이유 ★★ → Q7
- C_S 유지(종횡비 큰 커패시터, high-k) / 셀 TR 누설(짧아진 L) / C_BL 대비 신호 감소 → sense margin / 셀 간 간섭(row hammer) / 산포 증가 → tail 셀 증가.
- 설계 대응: BL 분할, SA offset 보상, on-die ECC, repair, refresh 관리. 공정·구조 대응: 4F², 3D DRAM 연구, EUV.

### 6.6 제품군 ★★ → Q8, Q9
| 제품 | 방향 | 핵심 |
|---|---|---|
| DDR5 | 서버·PC | 1.1V, 채널을 32bit 서브채널 2개로 분할, BL16, **on-die ECC**, DIMM 위 PMIC, 수신단 DFE |
| LPDDR | 모바일 | 저전력: 낮은 I/O 전압, 대기 전력 관리, 패키지 실장 |
| GDDR | 그래픽 | **핀당 속도** 극대화 (GDDR7은 PAM3) |
| HBM | AI 가속기 | **핀 수**(넓은 버스) 극대화, TSV 적층 |

> "속도를 올리는 방법은 핀당 속도를 높이는 것과 핀 수를 늘리는 것 두 가지이고, GDDR과 HBM이 각각 그 대표입니다."

---

## 7. HBM과 AI 메모리 ★★★ → Q5, Q27, Q46

- **정의**: DRAM die를 TSV로 수직 적층하고 base(logic) die 위에 올려, interposer로 GPU/가속기 바로 옆에 붙인 고대역폭 DRAM.
- **정정해 둔 개념**: HBM은 CPU의 cache와 DRAM 사이 계층이 아니라 **가속기 쪽의 메인 메모리**다. 서버 DRAM과 위아래가 아니라 나란한 관계. SRAM의 대체재가 아님.
- **왜 넓은 버스인가**: 대역폭 = 핀 수 × 핀당 속도. 핀당 속도를 올리면 I/O 전력·SI 부담이 급증하므로, 짧은 배선으로 핀을 매우 많이(스택당 1024개, HBM4는 2048개) 두고 핀당 속도는 상대적으로 낮춘다 → **bit당 에너지(pJ/bit)가 낮다.** C·V²·f에서 C(짧은 배선)와 f를 낮추고 폭으로 벌충하는 설계.
- **설계 이슈**
  - 열: 적층 중간·상단 die 방열 경로가 길다 → refresh 증가, 타이밍 마진 감소. SK hynix는 **MR-MUF**(적층 후 액상 몰드 충전)로 방열·생산성 확보.
  - 전원: 위층까지 TSV로 전원 공급 → IR drop, 전원 TSV·decap.
  - 신호: TSV 부하, die 간 타이밍 정렬.
  - 높이: 규격 높이 안에 더 많은 단 → die 박막화, warpage, 차세대 hybrid bonding.
  - 수율: die 수만큼 수율이 곱해짐 → 적층 전 **KGD** 테스트, TSV redundancy·repair.
  - base die: 테스트·repair·PHY 로직을 담는다. HBM4부터 base die에 로직 공정 적용 추세(뉴스룸으로 최신 확인).
- **Memory wall**: 연산 성능 증가 속도를 메모리 대역폭이 못 따라감. 특히 LLM 추론은 가중치를 매번 읽어 메모리 대역폭에 묶인다. 대응: HBM, **PIM**(SK hynix GDDR6-AiM: 메모리 안에서 곱셈·누산), **CXL**(메모리 확장·풀링, CMM-DDR5).

> **한 문장**: "HBM은 핀당 속도 대신 핀 수를 늘려 대역폭을 얻는 TSV 적층 DRAM이라 bit당 I/O 에너지가 낮고, 대신 적층으로 열·전원·수율 문제가 생겨 설계와 패키지가 함께 풀어야 합니다."

---

## 8. NAND Flash (○미학습) ★★ → Q3, Q4

- **셀**: 게이트 아래 전하 저장층(floating gate 또는 **CTF**)에 전자를 가두어 V_TH를 바꾼다. SK hynix **4D NAND = CTF(3D 적층) + PUC**(주변회로를 셀 어레이 아래에 배치해 면적 절감).
- **String**: 셀 여러 개를 직렬 연결 → 고집적, 랜덤 접근 느림.
- **Program**: 선택 WL에 고전압(~20V), 채널은 0V → **FN 터널링**으로 전자 주입. **ISPP**: 전압을 단계적으로 올리며 verify 반복 → V_TH 분포를 좁게. 프로그램하지 않을 string은 채널을 self-boosting으로 띄워 inhibit.
- **Erase**: 블록 단위, 기판(well)에 고전압 → 전자 방출.
- **Read**: 선택 WL에 판별 전압(분포 사이), **비선택 WL에는 Vpass**로 무조건 켜기 → string 도통 여부를 page buffer가 sensing.
- **다치**: TLC 8개, QLC 16개 V_TH 상태 → 분포 간격이 좁아져 read 전압 정밀도(아날로그)와 ECC(LDPC, 디지털) 부담 증가, 프로그램 시간 증가.
- **신뢰성**: program/read/pass disturb, retention(전하 손실), P/E 사이클에 따른 산화막 열화 → wear leveling, read retry, ECC.
- **주변회로**: page buffer(sensing + 데이터 래치), **charge pump**(고전압), 고전압 스위치·level shifter, ISPP 상태기계, 칩 밖 SSD 컨트롤러(FTL·ECC).

---

## 9. 아날로그·Mixed-signal (○미학습, "디지털만 준비했다가 당황" 후기 영역) ★★ → Q31~Q40

| 회로 | 꼭 알 것 | 메모리 속 위치 |
|---|---|---|
| CS 증폭기 | A_v ≈ −g_m·(r_o ∥ R_D). 이득 vs 대역폭 vs headroom | 기본 블록 |
| Source follower | 이득≈1, 낮은 출력 임피던스 → 버퍼 | 레벨 이동, 버퍼 |
| Current mirror | 같은 V_GS로 전류 복사. 오차: CLM(V_DS 차이), V_TH mismatch → cascode, 큰 L | 바이어스 |
| 차동쌍 | 공통 노이즈 제거, CMRR. 전원 노이즈에 강함 | SA, 수신기 |
| OP amp 안정도 | 피드백 루프의 위상 여유 ≥ 45~60°. Miller 보상(pole splitting): 안정도 vs 대역폭 | regulator, 기준 전압 |
| Bandgap | V_BE(CTAT) + ΔV_BE = V_T·ln n(PTAT) → 온도 무관 ≈1.2V | 모든 내부 전압의 기준 |
| LDO | 오차 증폭기 + PMOS pass. dropout, PSRR, load transient, 출력 커패시터와 안정도 | 내부 전원(VCORE 등) |
| Comparator/래치 | offset(mismatch), kickback, metastability | BL SA, 수신기 |
| Charge pump | 커패시터 펌핑으로 VDD보다 높거나 음의 전압 생성. 효율·리플·면적 trade-off | **DRAM VPP·VBB, NAND 프로그램 고전압** |
| Level shifter | cross-coupled PMOS로 전압 도메인 변환 | WL 드라이버, 도메인 경계 |
| PLL vs DLL | **PLL**: VCO로 주파수 생성·체배, jitter 누적, 2차 이상 루프 안정도 / **DLL**: 지연선으로 위상만 정렬, jitter 누적 없음, 1차라 안정, 체배 불가 | **DRAM은 DLL로 외부 CK와 출력 DQ 위상 정렬** |

**I/O: Signal Integrity** ★★ → Q14, Q44
- 문제: 채널 손실로 ISI, 임피던스 불연속으로 반사, 인접 선 crosstalk, jitter → eye가 닫힌다.
- 대응: ODT(종단 정합), **ZQ calibration**(출력 임피던스를 외부 저항 기준으로 보정), equalization(FFE·CTLE·DFE), training(read/write leveling), duty cycle 보정.

- IR drop(정적, 배선 저항) + L·di/dt(동적, 부하 급변) → 전원이 출렁이면 지연·노이즈 마진·SA 판정이 흔들린다.
- 대응: 전원 mesh 강화, on-chip decap, 부하 동작 시점 분산, regulator 루프 보상. 원인 분리는 load step 시뮬레이션의 undershoot 크기·회복 시간·ringing으로.

---

## 10. 메모리 블록 ↔ 개념 연결표 (덱 13장 확장) ★★★

| 회로 블록 | 앞에서 배운 개념 | 면접에서 묻는 trade-off |
|---|---|---|
| Row/Col 디코더 | fan-in, NAND 트리, predecode, glitch | access time 최악 경로, 주소 안정 후 enable |
| WL 드라이버 | 버퍼 체인(logical effort), 큰 RC 부하, level shifter | 단수·사이징, VPP 부스트 |
| BL·Sense amp | charge sharing, 래치 이득, V_TH mismatch | offset vs 면적·속도, BL 길이 vs 밀도 |
| 6T SRAM | ratioed 사이징 | 읽기 안정성 vs 쓰기 능력, V_min |
| DRAM 셀 | pass TR, 누설, V_TH 산포 tail | VPP·NWL, refresh vs 속도·전력 |
| 내부 전원 | BGR, LDO, charge pump, PI | 효율 vs 면적 vs 노이즈 |
| 클럭 | DLL/PLL, skew, jitter | 정렬 정확도 vs 전력·lock 시간 |
| I/O | C·V²·f, SI, ODT, EQ | 핀당 속도 vs 핀 수, 대역폭당 전력 |
| 테스트 | MBIST, redundancy, fuse, ECC | 테스트 시간·면적 vs 수율 |

> 같은 R·C·V 언어를 블록마다 다시 쓰는 것뿐이다.

---

## 11. 상황형·Trade-off 질문 (PT와 심층 공용)

### 11.1 답 틀
- **상황형(원인 분석)**: 현상 정의 → 범위 좁히기(언제·어디서·어떤 corner) → 가설 → 필요한 데이터·측정 → 검증 → 대책과 부작용
- **Trade-off형 6단계**: 대상 확정 → 물리·회로식 연결 → **크기 비교(지수 vs 선형)** → 제약(worst case, tail, 고온) → **결정과 보완책** → 리스크·검증
- "장단점이 있다"에서 끝내지 않는다. 핵심은 3번(크기 비교)과 5번(결정).
- 발표 팁: 가정을 먼저 말해 범위를 정한다 / 제3의 변수를 하나 넣어 "실제로는 최적점이 있다"를 보인다 / 반박 질문은 이미 인지한 리스크로 받는다.
- AI 문제해결 PT: AI 답을 그대로 쓰지 말고 **틀린 전제나 빠진 조건을 하나 이상 찾아 말한다**(예: hold 위반을 주파수로 고치자는 제안, HBM을 cache 계층으로 설명하는 오류).

### 11.2 연습 주제 (문항은행·로드맵·대화에서 모음)
| 주제 | 키 trade-off | 참조 |
|---|---|---|
| 온도 상승 시 DRAM | 누설 지수↑ → refresh↑ vs 성능·전력 | Q42 |
| VDD 낮추기 | 전력 V² vs 속도·sensing margin·누설 | Q43 |
| I/O 속도 2배 | 핀당 속도(EQ·전력) vs 핀 수(면적·패키지) | Q44 |
| Sense margin 부족 | 신호 / 판별 / 노이즈 분리 | Q45 |
| HBM 12→16단 | 열·전원·높이·수율 | Q46 |
| 내부 전압 출렁임 | 루프 대역폭·위상 여유·decap·IR | Q47 |
| 셀 V_TH 높이기 | retention vs write 속도·VPP 신뢰성 | 6.4 |
| SA 소자 크게 | offset vs 면적·BL 피치·속도 | 6.2 |
| BL 길이 늘리기 | 밀도 vs ΔV 감소 | 6.1 |
| Refresh 주기 늘리기 | 전력 vs tail 셀 fail (ECC·repair·온도별) | 6.3 |
| 합성 후 setup violation | 제약 확인 → 경로 → 구조 vs 구현 | 4.3, 로드맵 PT #1 |
| MBIST 특정 주소 fail | 셀 vs 디코더 vs 타이밍 분리, 패턴·온도 의존성 | 4.8, PT #2 |
| Pipeline 후 전력·면적 증가 | throughput vs latency·레지스터 | 4.6, PT #3 |
| Clock gating glitch | AND 게이트 gating vs 래치 기반 ICG | 3.5, PT #7 |

---

## 12. 빠른 문답 40 (한 문장으로 답하기 연습)

| # | 질문 | 한 문장 답 |
|---|---|---|
| 1 | PMOS를 왜 크게? | 정공 이동도가 낮아 같은 전류를 내려면 폭을 키워 상승·하강을 맞춘다 |
| 2 | NAND가 NOR보다 선호? | NOR은 느린 PMOS를 직렬로 쌓아 크기와 입력 용량이 커진다 |
| 3 | 같은 전환, 다른 지연? | 켜진 트랜지스터 수와 내부 노드 충·방전 여부가 다르다 |
| 4 | 큰 부하는 어떻게 구동? | 단당 effort ≈ 4인 버퍼 체인으로 단수를 정한다 |
| 5 | W를 계속 키우면? | 자기 확산 용량도 커져 지연이 포화되고 앞단이 느려진다 |
| 6 | VDD를 낮추면? | 전력은 제곱으로 줄지만 느려지고, V_TH로 보상하면 누설이 는다 |
| 7 | 왜 V_TH를 마음대로 못 낮추나? | S가 60 mV/dec 아래로 못 가 누설이 지수로 증가한다 |
| 8 | V_TH 산포의 영향? | 지연·누설·SA offset이 흔들려 마진과 사이징이 필요하다 |
| 9 | I_OFF 산포가 I_ON보다 큰 이유? | I_OFF는 V_TH에 지수, I_ON은 1~2차로 반응한다 |
| 10 | 온도↑ 누설은? | V_TH↓와 S↑로 지수적으로 증가한다 |
| 11 | CLM의 문제? | 전류원 출력 저항이 낮아져 증폭기 이득이 줄어든다 |
| 12 | 동적 전력 식? | α·C·V²·f, 줄이려면 α(clock gating)와 V가 가장 효과적이다 |
| 13 | 누설 줄이는 회로 기법? | power gating, multi-V_TH, body bias, 메모리는 negative WL |
| 14 | 래치 vs FF? | 래치는 레벨, FF는 엣지에 반응하고 FF는 래치 두 개로 만든다 |
| 15 | Setup/hold 정의? | 엣지 전후로 데이터가 안정돼야 하는 최소 시간이다 |
| 16 | Hold 위반을 주파수로 못 고치는 이유? | hold 조건식에 클럭 주기가 없기 때문이다 |
| 17 | Clock skew가 setup에? | capture가 늦으면 setup엔 유리, hold엔 불리하다 |
| 18 | STA vs 시뮬레이션? | STA는 타이밍 전수 검사, 시뮬레이션은 기능 검증이라 서로 대체 못 한다 |
| 19 | Metastability 대책? | 1비트는 2-FF 동기화, 멀티비트는 Gray code·async FIFO |
| 20 | Blocking vs non-blocking? | 조합은 =, 순차는 <=, 섞으면 race와 합성 불일치 |
| 21 | 의도치 않은 래치? | 조합 블록에서 모든 경우를 할당하지 않으면 생긴다 |
| 22 | Pipeline의 대가? | latency·레지스터·클럭 전력이 늘고 hazard 제어가 필요하다 |
| 23 | DRC vs LVS? | DRC는 제조 규칙, LVS는 회로도와의 연결 일치를 본다 |
| 24 | Pre vs post-layout 차이? | 추출한 배선 R·C가 반영돼 지연·전력이 달라진다 |
| 25 | SRAM vs DRAM? | SRAM은 6T 래치로 빠르고 refresh가 없지만 크고, DRAM은 1T1C로 작지만 refresh가 필요하다 |
| 26 | SRAM 사이징 원칙? | 읽기는 cell ratio, 쓰기는 pull-up ratio로 승부를 정한다 |
| 27 | DRAM 읽기가 파괴적인 이유? | charge sharing으로 셀 전하가 BL에 나눠지므로 SA가 다시 써야 한다 |
| 28 | Charge sharing 식? | ΔV = (VDD/2)·C_S/(C_S+C_BL) |
| 29 | DRAM WL을 왜 VPP로? | NMOS pass TR은 VDD−V_TH만 전달해 '1'을 온전히 쓰지 못한다 |
| 30 | BL을 왜 VDD/2로 precharge? | '1'과 '0' 모두 같은 크기 신호를 만들고 전력·속도에 유리하다 |
| 31 | Refresh 주기를 정하는 것? | 평균이 아니라 가장 새는 tail 셀의 retention이다 |
| 32 | Row hammer? | 반복 활성화가 인접 row 전하를 교란해, 인접 row를 추가 refresh한다 |
| 33 | 셀 TR과 peri TR 목표 차이? | 셀은 누설 최소, peri는 속도 최대라 V_TH와 구조가 다르다 |
| 34 | HBM이 대역폭이 높은 이유? | TSV로 적층해 핀 수를 1024개 이상으로 넓혔다 |
| 35 | HBM은 메모리 계층 어디? | cache 아래가 아니라 가속기 옆의 메인 메모리다 |
| 36 | NAND Program 원리? | 고전압 FN 터널링으로 전하를 넣고 ISPP로 V_TH 분포를 좁힌다 |
| 37 | NAND Read에서 Vpass? | 비선택 셀을 무조건 켜서 선택 셀만 판정하게 한다 |
| 38 | PLL vs DLL? | PLL은 주파수를 만들고, DLL은 위상만 맞추며 DRAM 출력 정렬에 쓴다 |
| 39 | 메모리에 charge pump가 필요한 이유? | VPP·음전압·NAND 고전압처럼 VDD 밖의 전압이 필요하다 |
| 40 | 글리치와 메모리? | 디코더 글리치가 엉뚱한 WL을 열 수 있어 주소 안정 후 enable로 띄운다 |

---

## 13. 조심할 개념 (자주 틀리는 것)

1. V_T(thermal)와 V_TH(threshold) 혼동. 교재마다 표기가 다르다.
2. V_GS < V_TH여도 전류는 0이 아니다.
3. Body effect 원인은 V_SB다.
4. CLM의 문제는 V_DS 의존성이고, velocity saturation과 다른 현상이다.
5. 온도와 I_ON은 두 효과가 경쟁하므로 단정하지 않는다.
6. Process variation은 V_TH만 변하는 게 아니다. 지수 통로가 V_TH일 뿐이다. S는 원인이 아니라 환산 계수.
7. Scaling은 trade-off다.
8. Hold 위반은 주파수를 낮춰도 안 고쳐진다.
9. STA 통과는 기능 정답을 뜻하지 않는다. Coverage 100%도 버그 없음이 아니다.
10. HBM은 DRAM 기반, 가속기 쪽 메모리다. cache 계층이 아니다.
11. DRAM 읽기는 파괴적이고 restore가 동작의 일부다.
12. NOR이 느린 건 직렬 PMOS 때문이다(로직 기능 탓 아님).

---

## 14. 학습 상태와 다음 순서

| 영역 | 상태 | 비고 |
|---|---|---|
| MOSFET·산포·scaling (2장) | ✓학습 | 복습: 한 문장 답만 말해보기 |
| CMOS 게이트·지연·전력·로직 스타일·glitch (3장) | ✓학습 | 덱 15장 그대로 |
| 디지털 타이밍·RTL·flow (4장) | ○ | **후기 빈출인데 비어 있음 → 1순위** |
| SRAM (5장) | ○ | 다음 공부 A |
| DRAM (6장) | ○ | 다음 공부 B, 하이닉스 주력 |
| HBM·AI 메모리 (7장) | △ | 개념 정정만 함 → 다음 공부 C |
| NAND (8장) | ○ | D |
| 아날로그·I/O·PI (9장) | ○ | 학습계획 v1 3주차 |

권장 순서는 기존 `Half-Day_학습계획_v1.md`의 주차 배치를 따른다. 이 자료는 그 계획의 **각 주차에서 무엇을 말할 수 있어야 하는지 확인하는 체크리스트**로 쓴다.

---

## 15. 확인이 필요한 것

- Half-Day AI 문제해결 PT의 실제 형식(시간, AI 도구, 과제 유형)은 공식 확인 정보가 없다. 공지·후기가 나오면 11장 연습 방식을 조정한다.
- 기출 주제(0장)는 코멘토·잡플래닛 등 개인 후기 기반이다. 리포트샵 자료는 접근이 막혀 확인하지 못했다.
- HBM4, 4D NAND 단수 같은 최신 제품 수치는 SK hynix 뉴스룸에서 면접 직전에 다시 확인한다.
- 지원 세부 분야(analog/core vs digital)는 아직 정하지 않았다. 둘 다 준비하는 것이 기본값이다.

---

## 16. 주제별 학습 자료 링크 (슬라이드 하단 "더 보기"와 같음)

(한) 한국어, (영) 영어. 뉴스룸 링크는 기존 `참고자료_링크모음.md`와 codex-skh 읽을거리 목록에서 가져왔다.

| 주제 | 자료 |
|---|---|
| DRAM 셀 TR 구조 (BCAT, 4F²) | [서울경제 D램 특집 2편(한)](https://sedaily.com/NewsView/260ZLT02IO) · [디지털데일리 3D 메모리 로드맵(한)](https://m.ddaily.co.kr/page/view/2024112516263197873) |
| 면접 형식·직무 | [Half-Day 공식 소개(한)](https://talent.skhynix.com/hub/ko/company/story/217) · [2026 하반기 공고·JD(한)](https://www.skcareers.com/Recruit/Detail/R261762) · [JOB로그 설계 편(한)](https://news.skhynix.co.kr/ambassador-job-log-ep3/) · [DRAM 설계의 모든 것(한)](https://www.skcareersjournal.com/1161) |
| 기본 강의 | [MIT 6.374 디지털 IC 강의노트(영)](https://ocw.mit.edu/courses/6-374-analysis-and-design-of-digital-integrated-circuits-fall-2003/pages/lecture-notes) · [Berkeley EE141 강의영상(영)](https://www.janrabaey.com/digital-ic) |
| MOSFET 기본·산포 | [문턱전압 용어 상식(한)](https://news.skhynix.co.kr/threshold-voltage/) · [전자·정공·채널(한)](https://news.skhynix.co.kr/electron-hole-channel/) · [CLM(영)](https://en.wikipedia.org/wiki/Channel_length_modulation) · [Subthreshold 누설(영)](https://en.wikipedia.org/wiki/Subthreshold_conduction) · [공정 산포(영)](https://en.wikipedia.org/wiki/Process_variation_(semiconductor)) · [FinFET·GAA(영)](https://en.wikipedia.org/wiki/Multigate_device) |
| 지연·사이징·신뢰성 | [Elmore delay(영)](https://en.wikipedia.org/wiki/Elmore_delay) · [Logical effort(영)](https://en.wikipedia.org/wiki/Logical_effort) · [EM(영)](https://en.wikipedia.org/wiki/Electromigration) · [BTI(영)](https://en.wikipedia.org/wiki/Negative-bias_temperature_instability) · [Clock gating(영)](https://en.wikipedia.org/wiki/Clock_gating) · [DVFS(영)](https://en.wikipedia.org/wiki/Dynamic_voltage_scaling) |
| 저전력 기법 | [elec4 저전력 IC 설계 기고(한)](https://www.elec4.co.kr/article/articleView.asp?idx=28521) · [기법별 정리와 면접 Q&A(영)](https://ecrionix.org/low-power/) · [Power gating(영)](https://en.wikipedia.org/wiki/Power_gating) · [Multi-threshold CMOS(영)](https://en.wikipedia.org/wiki/Multi-threshold_CMOS) |
| Glitch | [Hazard (logic)(영)](https://en.wikipedia.org/wiki/Hazard_(logic)) |
| Setup/hold, skew | [셋업·홀드 용어해설(한)](http://www.ktword.co.kr/test/view/view.php?m_temp1=5542&id=1349) · [클럭 스큐(한)](https://www.jaenung.net/tree/47853) · [Setup time(영)](https://vlsiweb.com/setup-time/) |
| STA, CDC, Verilog | [STA 기초(영)](https://chipverify.com/rtl-synthesis/static-timing-analysis-fundamentals) · [Metastability(영)](https://en.wikipedia.org/wiki/Metastability_(electronics)) · [Async FIFO(영)](https://vlsiweb.com/asynchronous-fifos/) · [Cummings, Nonblocking Assignments 논문(영)](https://rfsoc.mit.edu/6S965/_static/F24/lectures/CummingsSNUG2000SJ_NBA.pdf) |
| Flow, DRC/LVS, MBIST | [Synopsys STA 용어(영)](https://www.synopsys.com/glossary/what-is-static-timing-analysis.html) · [Synopsys LVS 용어(영)](https://www.synopsys.com/glossary/what-is-layout-versus-schematic-checking.html) · [MBIST·March 알고리즘(영)](https://www.design-reuse.com/articles/45915/memory-testing-self-repair-mechanism.html) |
| SRAM | [6T SRAM 강의 PDF, read/write 조건·SNM(영)](https://www.eng.biu.ac.il/temanad/files/2017/02/06-SRAM-2016.pdf) · [SRAM(영)](https://en.wikipedia.org/wiki/Static_random-access_memory) |
| DRAM 동작·SA | [메모리 반도체 구조 알아보기(한)](https://news.skhynix.co.kr/understanding-dram-structure/) · [Onur Mutlu 강의 채널(영)](https://www.youtube.com/onurmutlulectures) · [DRAM Circuit Design 교재(영)](https://www.wiley-vch.de/en/areas-interest/engineering/dram-circuit-design-978-0-470-18475-2) · [Sense amplifier(영)](https://en.wikipedia.org/wiki/Sense_amplifier) |
| Refresh, Row hammer | [Row hammer(영)](https://en.wikipedia.org/wiki/Row_hammer) · Mutlu 채널의 RowHammer 강의(영) |
| DDR5·LPDDR | [Kingston DDR5 개요(영)](https://www.kingston.com/kr/blog/pc-performance/ddr5-overview) · [LPDDR5X 개발 인터뷰(한)](https://news.skhynix.co.kr/lpddr5x-developer-interview/) |
| HBM·PIM | [HBM3E 12단 MR-MUF(한)](https://news.skhynix.co.kr/hbm3e-12hi-one-team-mr-muf/) · [iHBM 발열 대응(한)](https://news.skhynix.co.kr/ihbm-solution/) · [HBM 패키지 인터뷰(영)](https://news.skhynix.com/hbm-package-technology-interview-1/) · [PIM의 모든 것(영)](https://news.skhynix.com/all-about-pim-for-next-generation-ai-computing/) |
| NAND | [낸드플래시 원리와 구조(한)](https://news.skhynix.co.kr/principle-of-nand-flash-memory/) · [Pathfinder 4D 낸드·PUC(한)](https://news.skhynix.co.kr/pathfinder-3-4d-nand) |
| 아날로그, DLL | [Razavi 아날로그 CMOS 강의(영)](https://www.youtube.com/playlist?list=PLxWY2Q1tvbBua1l-fk2n9YSzZJNbUJfet) · [DRAM 인터페이스용 DLL 서베이 논문(영)](https://pure.korea.ac.kr/en/publications/survey-and-analysis-of-delay-locked-loops-used-in-dram-interfaces/) · [Delay-locked loop(영)](https://en.wikipedia.org/wiki/Delay-locked_loop) |
| SI·PI | [Signal integrity 기초(영)](https://www.protoexpress.com/blog/how-to-solve-signal-integrity-problems-the-basics/) · DRAM Circuit Design 교재의 I/O·전원 장 |

디지털 타이밍과 아날로그는 한국어로 잘 정리된 공개 자료가 적어 영어 자료 비중이 높다.
