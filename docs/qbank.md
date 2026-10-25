# A!SK 설계 직무 전공 문항은행

작성일: 2026-10-07 (10장 추가: 2026-10-18)
용도: Half-Day 중 A!SK(비대면 영상 인터뷰) 전공 문항 대비 + 심층 인터뷰 전공 질문 공용

---

## 0. 형식과 전략

### 알려진 형식 (2026 상반기 후기 기준, 하반기 변경 가능)

| 구분 | 문항 | 준비 | 답변 |
|---|---|---|---|
| 공통 | 3개 (1분 자기소개, 갈등 경험 ×2) | 1분 (스킵 가능) | 30초 ~ 1분 |
| 전공 | 4개 | 1분 | 30초 ~ 3분 |

- **A!SK는 자소서 기반이 아니다.** 같은 날 같은 직군 응시자 전원에게 **동일한 공통 문항**이 나온다. 따라서 A!SK 대비의 중심은 개인 경험이 아니라 **직군 공통 전공지식의 깊이**다. 각 문항의 "연결 문장"은 차별화용 선택 요소이고, 개인 경험 질문(Q30 등)은 **심층 인터뷰(대면) 대비**로 분류한다.
- 기출 검색 시 A!SK 문항과 대면 면접 질문을 섞지 않는다. 취업 커뮤니티 "가이드"의 예시 문항은 실제 A!SK 기출인지 불분명한 경우가 많다.
- 설계 직무 A!SK 전공 문항 원문은 거의 공개되지 않았다. 후기상 단서: "PE보다 어려웠다", "디지털/RTL만 준비했는데 아날로그가 나왔다", "DRAM·NAND에서 아날로그·디지털 회로가 쓰이는 부분" 유형.
- **2026 회로설계 A!SK 실제 응시 후기(10/18 추가)**: 어려운 문항 "NAND에서 ○○ 에러가 날 수 있다, 어떻게 검증하겠나", 쉬운 문항 "timing report·slack, 논리가 어떻게 합성됐나" → **10장(Q48~Q61)을 최우선**으로 본다.
- PE 직군에서 DRAM 정의·물리 특성·NAND 차이·HBM 구조가 나왔다면, 설계에서도 **메모리 제품 기본 + 회로/디지털 기본 + 내 경험 연결**이 같은 깊이로 나온다고 가정한다.
- 답변시간 최대 3분 → **1분 30초 ~ 2분**을 목표로 한다. 30초 이내로 끝내면 깊이가 부족해 보이고, 3분을 꽉 채우면 구조가 흐려진다.

### 출제 범위 판단 (2026-10 기준)

- **나올 범위**: SK하이닉스 제품군이 중심이다 — DRAM(DDR5, LPDDR, GDDR, HBM), NAND(4D NAND, SSD, UFS), AI 메모리(HBM, PIM/AiM, CXL). 그리고 이 제품을 만드는 데 필요한 **범용 회로 기초**(MOSFET, CMOS, 아날로그 기본 회로, Timing, 저전력)도 범위다.
- **사실상 제외할 범위**: CIS(이미지센서)는 2025년 3월 사업 철수 후 인력을 AI 메모리로 전환했다. 디스플레이, RF, 독립 주제로서의 DSP, 전력 IC 제품 자체는 하이닉스 제품군이 아니다.
- **단, 원리는 겹친다**: DSP·신호처리 개념(필터, 주파수 응답, 샘플링)은 I/O Equalization(CTLE = 고역 강조 필터, DFE = 피드백 필터)과 PLL/DLL Loop 해석에 그대로 쓰인다. 전원 회로 개념은 메모리 내부 전압 생성으로 나온다. 즉 "카메라센서"는 안 나와도 **"고속 I/O의 신호 왜곡을 필터로 보상하는 원리"는 나올 수 있다.**

### 3분 답변 공통 골격 (정의 → 원리 → 한계 → 설계자 관점 → 연결)

1. **정의 한 문장** (10초): "DRAM은 트랜지스터 1개와 커패시터 1개에 전하로 데이터를 저장하는 휘발성 메모리입니다."
2. **원리·왜** (40초): 동작이 왜 그렇게 되는지 물리적 이유
3. **한계·Trade-off** (30초): 그 구조 때문에 생기는 문제
4. **설계자 관점 대응** (30초): 회로·설계로 그 문제를 어떻게 다루는가
5. **연결 한 문장** (10초, 선택): 내 경험 또는 SK하이닉스 제품과 연결

### 1분 준비시간 사용법

- 종이에 **키워드 5개만** 위 골격 순서대로 적는다. 문장을 쓰지 않는다.
- 모르는 부분이 있으면 "확실히 아는 범위 → 추정 → 확인 방법" 순서로 말할 문장을 정한다.
- 답변 첫 문장은 반드시 **결론 또는 정의**로 시작한다.

### 모르는 질문 대응 문장

> "정확한 수치는 확실하지 않지만, 원리상 ○○ 때문에 ○○ 방향으로 영향이 있을 것으로 이해하고 있습니다. 실제 설계에서는 ○○ Simulation이나 데이터로 확인하겠습니다."

---

## 1. 메모리 제품 기본 (최우선 — PE 기출과 같은 축)

### Q1. DRAM이란 무엇이고, 셀은 어떻게 동작하나요?

**핵심 답변**
- DRAM은 **1T1C 셀**, 즉 Access Transistor 1개와 Storage Capacitor 1개로 1bit를 저장하는 휘발성 메모리다. 커패시터에 전하가 있으면 1, 없으면 0이다.
- **Read 동작**
  1. Bit Line을 VDD/2로 Precharge·Equalize한다.
  2. Word Line을 켜면 셀 커패시터와 Bit Line 사이에 **Charge Sharing**이 일어난다. Bit Line 전압이 VDD/2에서 아주 조금(수십~백수십 mV) 오르거나 내려간다.
  3. **Sense Amplifier**가 Bit Line과 기준 Bit Line(BLB)의 미세한 차이를 Full Swing(VDD/0)으로 증폭한다.
  4. 증폭된 값이 다시 셀에 써진다(**Restore**). Read가 파괴적(Destructive)이기 때문이다.
- 커패시터 전하는 누설전류로 빠지므로 주기적으로 **Refresh**해야 한다. 그래서 "Dynamic"이다.

**심화 (3분 확장용)**
- ΔV ≈ (VDD/2) × Cs / (Cs + Cbl). Bit Line 커패시턴스가 셀보다 수 배 크므로 신호가 작다. 따라서 **셀 커패시턴스 확보**와 **Sense Amp의 Offset**이 DRAM 설계의 핵심 제약이다.
- Word Line은 VDD보다 높은 **VPP**로 구동한다. NMOS Access Tr은 Vth만큼 전압이 떨어지므로, 셀에 VDD를 온전히 쓰려면 Gate에 VDD+Vth 이상이 필요하다. VPP는 칩 내부 **Charge Pump**로 만든다.
- 누설 경로: Junction Leakage, GIDL, Subthreshold Leakage. 꺼진 Word Line에 음전압(Negative WL)을 거는 이유가 Subthreshold Leakage를 줄이기 위해서다.


---

### Q2. DRAM은 왜 Refresh가 필요하고, Refresh는 어떤 비용을 만드나요?

- 셀 커패시터 전하가 누설전류로 빠져 일정 시간이 지나면 Sense Amp가 판별할 수 없게 된다. 이 시간을 **Retention Time**이라 한다.
- 규격상 모든 Row를 DDR4는 64ms, DDR5는 32ms 안에 한 번씩 Refresh한다. 고온(85°C 이상)에서는 누설이 커져 주기를 절반으로 줄인다.
- **비용**
  1. Refresh 중에는 해당 Bank에 접근할 수 없어 **성능 손실**이 생긴다.
  2. 셀을 반복해서 Read·Restore하므로 **대기 전력**이 커진다. 용량이 커질수록 Refresh할 Row가 늘어 부담이 더 커진다.
- **설계 대응**: Same-bank Refresh(DDR5), Self Refresh·온도 보상 Refresh(TCSR), Retention이 약한 셀을 Redundancy로 대체하기, Leakage를 줄이는 Negative WL 등

---

### Q3. DRAM, SRAM, NAND의 차이를 설명하세요.

| 항목 | SRAM | DRAM | NAND Flash |
|---|---|---|---|
| 셀 | 6T (Cross-coupled Inverter) | 1T1C | Floating Gate / Charge Trap Tr |
| 저장 방식 | Latch 상태 | 커패시터 전하 | 게이트 절연막 내 전하 → Vth 변화 |
| 휘발성 | 휘발 | 휘발 (Refresh 필요) | 비휘발 |
| 속도 | 가장 빠름 (ns 이하~수 ns) | 수십 ns | Read 수십 µs, Program 수백 µs, Erase ms |
| 집적도 | 낮음 | 중간 | 가장 높음 (MLC/TLC/QLC + 3D 적층) |
| 접근 단위 | Word | Row(Page) Open 후 Column | Read/Program은 Page, Erase는 Block |
| 내구성 | 무제한 | 무제한 | P/E Cycle 제한 |
| 용도 | CPU Cache | Main Memory, HBM | SSD, Storage |

**핵심 문장**: "세 메모리는 **속도·집적도·비휘발성**의 Trade-off에서 서로 다른 지점을 선택한 것이고, 그래서 컴퓨터는 Cache–Main Memory–Storage의 **메모리 계층 구조**로 이를 조합해 씁니다."

**DRAM vs NAND 물리적 차이를 더 물으면**
- DRAM은 전하를 **커패시터**에 담아 Bit Line으로 직접 꺼내 읽는다(전하량 판별).
- NAND는 전하를 **트랜지스터 게이트 절연막 안**에 가둬 **Vth를 바꾸고**, 특정 Read 전압에서 셀이 켜지는지(전류가 흐르는지)로 읽는다. 전하가 터널 산화막에 둘러싸여 있어 전원이 꺼져도 유지된다.

---

### Q4. NAND Flash의 Program/Erase/Read 동작을 설명하세요.

- **Program**: Control Gate에 높은 전압(~20V)을 걸어 채널의 전자를 **F-N Tunneling**으로 Charge Trap(또는 Floating Gate)에 주입한다 → Vth 상승
- **ISPP (Incremental Step Pulse Programming)**: Program 펄스를 조금씩 올리고 매번 Verify해서, 목표 Vth에 도달한 셀은 Inhibit한다. 셀마다 다른 Program 속도를 보정해 **Vth 분포를 좁게** 만든다. MLC/TLC처럼 레벨이 많을수록 필수다.
- **Erase**: 기판(Well)에 고전압을 걸어 전자를 빼낸다. **Block 단위**로만 가능하다.
- **Read**: 선택 Word Line에 판별 전압(Vread_ref), 비선택 Word Line에는 무조건 켜지는 Vpass를 걸고 String 전류 유무로 판단한다.
- **3D NAND**: 평면 미세화 한계(셀 간 간섭, 전자 수 감소)를 **수직 적층**으로 넘었고, 대부분 Charge Trap(SiN) 방식이다. SK하이닉스는 Peri 회로를 셀 아래에 두는 **4D NAND(PUC)** 로 면적을 줄였다.
- **설계 관점**: 고전압 생성(Charge Pump), Page Buffer, ISPP 알고리즘 제어, Read Disturb·Program Disturb 관리, ECC(LDPC)와의 협업

---

### Q5. HBM의 구조와 원리, 왜 AI에서 중요한지 설명하세요. ★

**핵심 답변**
- HBM은 여러 DRAM Core Die를 **TSV(Through Silicon Via)** 로 수직 적층하고, 맨 아래 **Base(Logic) Die**를 통해 GPU와 연결하는 고대역폭 메모리다.
- GPU 옆 **Silicon Interposer** 위에 함께 실장하는 **2.5D 패키지**라서, 보드 배선보다 훨씬 짧고 촘촘한 배선을 쓸 수 있다.
- **핵심 원리 = 넓은 버스**: 일반 DRAM은 핀 수가 적어 핀당 속도를 높여야 한다. HBM은 **I/O 1024개(HBM4는 2048개)** 를 쓴다. 핀당 속도는 상대적으로 낮아도 **전체 Bandwidth가 크고, bit당 전송 에너지가 낮다**.
- **AI에서 중요한 이유**: LLM 추론은 연산보다 **Weight를 메모리에서 읽어오는 속도**에 막히는 경우가 많다(Memory Wall). 그래서 Bandwidth와 용량이 곧 성능이 된다.

**심화**
- **Base Die**: PHY, TSV 인터페이스, 테스트·Repair 로직이 들어간다. HBM4부터는 Base Die를 Logic 공정으로 만들어 고객 맞춤 기능(Custom HBM)을 넣는 방향이다.
- **설계·패키지 난제**
  1. **발열**: 적층할수록 열이 갇힌다 → Refresh 증가·Retention 악화로 이어진다.
  2. **TSV 수율**: 하나만 불량이어도 스택 전체가 불량이다 → Redundancy TSV와 Repair가 필요하다.
  3. **PI/SI**: 수천 개 I/O가 동시에 스위칭 → 전원 노이즈(SSN)
  4. **높이 제한 안에서 적층 수 증가**: Die를 얇게 하고 Warpage를 제어해야 한다.
- SK하이닉스는 적층 Die 사이를 액체 Underfill로 한 번에 채우는 **MR-MUF**로 열 방출과 생산성을 확보했다. 16단 이상에서는 Hybrid Bonding이 검토된다.


---

### Q6. Sense Amplifier의 구조와 동작을 설명하세요.

- DRAM Bit Line Sense Amp는 **Cross-coupled Inverter Latch** 구조로, BL과 BLB의 미세 전압차를 양의 피드백으로 VDD/0까지 증폭한다.
- 동작 순서: Precharge(BL=BLB=VDD/2) → WL On(Charge Sharing) → SA Enable(NMOS 쪽 SAN을 GND로, PMOS 쪽 SAP를 VDD로) → 증폭 → Column Select로 데이터 출력 → Restore → WL Off → Precharge
- **설계 이슈**
  - **Offset**: 좌우 트랜지스터의 Vth Mismatch가 신호보다 크면 오판한다 → 트랜지스터 크기·Layout 대칭성, Offset Cancellation 기법
  - **면적**: Bit Line마다 들어가므로 셀 피치에 맞춰 작아야 한다 → 크기와 Offset 사이의 Trade-off
  - **Enable 타이밍**: 너무 빠르면 신호가 덜 생긴 상태로 오판하고, 너무 늦으면 tRCD가 늘어난다.

---

### Q7. DRAM 미세화가 어려운 이유는 무엇인가요?

1. **커패시턴스 확보**: 셀 면적이 줄어도 Sense Margin을 위해 일정 수준의 Cs가 필요하다 → 커패시터 종횡비 증가(공정 한계), High-k 유전막
2. **누설 증가**: 채널이 짧아지면 Subthreshold Leakage와 GIDL이 늘어 Retention이 나빠진다 → Buried Channel Array Tr(BCAT) 같은 3D 구조
3. **셀 간 간섭**: Row Hammer — 특정 Row를 반복 활성화하면 인접 Row 셀의 전하가 빠진다.
4. **Bit Line 커패시턴스·저항 증가**: 신호가 작아지고 지연이 증가한다.
- **설계 대응**: Sense Amp 개선, On-die ECC, Row Hammer 방어(TRR, RFM, PRAC), Redundancy Repair
- 장기적으로는 **3D DRAM**, **4F² 셀(VCT)** 이 거론된다.

---

### Q8. DDR / LPDDR / GDDR / HBM의 차이는?

- **DDR**: 서버·PC Main Memory. 용량과 범용성을 중시하고 DIMM 형태로 쓴다.
- **LPDDR**: 모바일용으로 저전력을 최우선한다. 낮은 I/O 전압, Deep Sleep, DVFS 등을 쓰고 SoC 근처에 실장한다.
- **GDDR**: 그래픽용으로 핀당 속도를 극대화한다. GDDR7은 **PAM3** 신호를 쓴다.
- **HBM**: 넓은 버스 + 적층으로 Bandwidth와 전력 효율을 최대화한다. 대신 비용이 높고 패키징이 복잡하다.
- **핵심 문장**: "같은 DRAM 셀이라도 **인터페이스와 패키지를 어디에 최적화하느냐**에 따라 제품이 갈립니다. 설계 차별화는 Core보다 Peri·I/O 회로에서 크게 납니다."

### Q9. DDR5에서 DDR4 대비 바뀐 점은?

- 모듈당 **독립 Sub-channel 2개**(32bit ×2)로 효율 향상, Burst Length 16
- **On-die ECC**: 칩 내부에서 단일 비트 오류를 정정해 미세화로 인한 셀 불량을 흡수한다.
- **PMIC on DIMM**: 전원 관리를 보드에서 모듈로 옮겨 전압 안정성을 높였다. ← **내 Power 경험과 직접 연결되는 포인트**
- 수신단 **DFE(Decision Feedback Equalizer)**: 고속에서 ISI를 보상한다.
- Same-bank Refresh, 낮아진 VDD(1.1V)

---

## 2. 회로 설계 기본 (CMOS·아날로그 Peri)

### Q10. CMOS Inverter의 동작과 소비전력 성분을 설명하세요.

- 입력이 Low면 PMOS가 켜져 출력이 High, 입력이 High면 NMOS가 켜져 출력이 Low다. 정상 상태에서는 VDD–GND 직접 경로가 없어 정적 전력이 거의 없다.
- **소비전력**
  1. **Dynamic**: P = α·C·V²·f. 부하 커패시터를 충·방전하는 전력으로, 전압의 제곱에 비례해 **전압을 낮추는 것이 가장 효과적**이다.
  2. **Short-circuit**: 입력 천이 중 PMOS와 NMOS가 동시에 켜지는 순간 흐르는 전류다. 입력 Slew가 느릴수록 커진다.
  3. **Leakage**: Subthreshold, Gate, Junction Leakage. 미세 공정일수록 비중이 크고 온도에 민감하다.
- **VTC의 Switching Threshold**는 PMOS/NMOS 크기비로 조정한다. 이동도 차이 때문에 보통 PMOS를 2~3배 크게 쓴다.

### Q11. MOSFET의 Short Channel Effect를 설명하세요.

- 채널이 짧아지면 Drain 전계가 Source 쪽 장벽까지 영향을 준다.
- **DIBL**: Drain 전압이 높을수록 Vth가 낮아진다. **Vth Roll-off**: 채널이 짧을수록 Vth가 낮아진다.
- 결과: Leakage 증가, 속도 포화(Velocity Saturation), Hot Carrier로 인한 신뢰성 저하
- **대응**: Gate의 채널 장악력을 높이는 구조(FinFET, GAA), High-k Metal Gate, Halo Implant
- **DRAM 관점**: Peri Tr은 속도, Cell Tr은 누설이 우선이다. 그래서 Cell Tr은 채널을 길게 만드는 Recess·Buried 구조를 쓴다.

### Q12. PVT Corner는 무엇이며 왜 중요한가요?

- **P**rocess(FF/TT/SS/FS/SF), **V**oltage(±5~10%), **T**emperature(-40~125°C)에 따라 트랜지스터 속도와 누설이 달라진다.
- **Setup·속도 검증**은 SS·저전압·고온(최근 공정은 Temperature Inversion으로 저온이 최악일 수 있음), **Hold·누설·전력 검증**은 FF·고전압 쪽에서 본다.
- 메모리는 수십억 셀 중 **최악의 셀**도 동작해야 하므로, Corner에 더해 **Monte Carlo(Mismatch)** 와 3~6σ 수준의 분포를 본다.

### Q13. DRAM에서 PLL과 DLL의 차이와 용도는?

- **PLL**: VCO로 **새 주파수를 합성**하고 위상을 맞춘다. 지터가 누적될 수 있고 Loop가 2차 이상이라 안정도 설계가 필요하다.
- **DLL**: 입력 클럭을 **가변 지연선으로 지연**시켜 위상만 맞춘다. 주파수 생성이 없어 지터 누적이 적고 안정적이다.
- DRAM은 외부 클럭을 받아 쓰므로 주로 **DLL**을 쓴다. 칩 내부 클럭 트리 지연을 보상해 **출력 데이터(DQ/DQS)를 외부 CK에 정렬**하는 것이 목적이다.
- 저전력 모드에서는 DLL을 끄거나 업데이트를 줄여 전력을 아낀다. 대신 재진입할 때 Lock 시간이 걸린다.

### Q14. 고속 I/O에서 Signal Integrity 문제와 대응은?

- **ISI**: 채널의 대역 제한으로 이전 비트가 다음 비트에 영향을 준다 → Equalization(송신 FFE, 수신 CTLE·DFE)
- **반사**: 임피던스 불연속 → **ODT(On-Die Termination)**, 출력 드라이버 임피던스 Calibration(ZQ Calibration)
- **Crosstalk**: 인접 신호 간 커플링 → 배선 간격, 차폐
- **SSN/Ground Bounce**: 다수 출력이 동시에 스위칭 → Decap, Data Bus Inversion(DBI)
- **판단 지표**: Eye Diagram의 Eye Height·Width, BER

### Q15. Power Integrity, IR Drop과 대응 방법은? (내 경험 최대 활용 문항)

- **IR Drop**: 전원망 저항으로 인한 **정적 전압 강하**
- **L·di/dt Noise**: 부하가 급변할 때 생기는 **동적 강하**
- 칩 내부 전압이 떨어지면 게이트 지연이 늘어 **Timing Fail**로 이어진다. 메모리는 Sense Margin 감소로도 나타난다.
- **대응**: 전원 Mesh 강화(폭·Via 수), On-chip Decap, 전원 Pad·Bump 배치, 스위칭 분산(Clock Skew 활용, 동작 순서 분산), 내부 Regulator
- **연결 문장**: "보드 레벨에서 CPU·GPU 근처에 Bypass Capacitor를 계층적으로 배치하는 이유를 공부했는데, 칩 내부 PDN도 Package–Bump–On-chip Decap으로 이어지는 같은 계층 구조라는 점에서 제 경험이 칩 설계의 PI 이해로 확장될 수 있다고 생각합니다."

### Q16. Charge Pump와 Level Shifter는 왜 메모리에 필요한가요?

- 메모리는 외부 전원 하나(또는 소수)를 받아 **내부에서 여러 전압을 만든다**.
  - DRAM: VPP(WL 승압), VBB·VNWL(음전압), VBLP(VDD/2 Precharge), VCP(Cell Plate)
  - NAND: Program·Erase용 20V 내외 고전압
- **Charge Pump**: 커패시터와 스위치로 전압을 단계적으로 끌어올린다. 효율, 리플, 부하 전류에 따른 출력 유지가 설계 포인트다.
- **Level Shifter**: 서로 다른 전압 도메인 간 신호를 변환한다. 변환하지 않으면 PMOS가 완전히 꺼지지 않아 누설이 생기고 오동작한다.
- **연결 문장**: "PMIC와 DC-DC 컨버터를 검토한 경험이 있어, 칩 내부 전압 생성 회로의 효율·리플·부하 응답 Trade-off를 같은 언어로 이해할 수 있습니다."

---

## 3. 디지털 설계·검증 (내 A급 경험과 직결)

### Q17. Setup / Hold Time과 Violation 해결 방법은? ★

- **Setup**: 클럭 엣지 **전에** 데이터가 안정돼야 하는 시간. 조건: Tclk ≥ Tclk-q + Tlogic + Tsetup − Skew
- **Hold**: 클럭 엣지 **후에** 데이터가 유지돼야 하는 시간. 조건: Tclk-q + Tlogic_min ≥ Thold + Skew
- **Setup Violation 해결**: 로직 단수 축소·재구성, Pipeline 삽입, 셀 Upsizing, LVT 셀로 교체, Useful Skew. 최후 수단은 주파수를 낮추는 것이다.
- **Hold Violation 해결**: 경로에 Buffer·Delay 셀 삽입. **클럭 주파수와 무관**하므로 칩이 나온 뒤 클럭을 낮춰도 고칠 수 없다. 그래서 더 치명적이다.
- **Slack** = Required Time − Arrival Time. 음수면 Violation이다.
- **연결**: "VLSI 프로젝트에서 Matrix Multiplier의 Critical Path와 Slack을 확인하고 ○○로 개선했습니다." ← **실제 수치를 복원해서 채울 것**

### Q18. Metastability와 CDC(Clock Domain Crossing) 처리 방법은?

- 비동기 신호가 Setup/Hold 창 안에서 바뀌면 Flip-flop 출력이 0도 1도 아닌 상태에 오래 머문다(Metastability).
- **대응**
  - 1bit 제어 신호: **2-FF Synchronizer**로 안정화 시간을 확보한다. MTBF는 대기 시간에 지수적으로 증가한다.
  - 멀티비트 데이터: **비동기 FIFO** + Gray Code 포인터(한 번에 1bit만 바뀜), 또는 Handshake
  - 펄스: Pulse Synchronizer(Toggle 방식)
- 검증: CDC 전용 정적 검사 툴로 Synchronizer 누락을 찾는다.

### Q19. Blocking vs Non-blocking Assignment의 차이는?

- Blocking(`=`)은 순서대로 즉시 대입해 조합 논리 표현에 쓴다.
- Non-blocking(`<=`)은 우변을 모두 계산한 뒤 블록 끝에서 동시에 대입해 Flip-flop의 동시 갱신을 표현한다.
- 순차 논리에 Blocking을 쓰면 Simulation과 합성 결과가 달라질 수 있다(Race). Shift Register 예시로 설명하면 좋다.
- 조합 always 블록에서 모든 경우에 대입하지 않으면 **의도치 않은 Latch**가 생긴다.

### Q20. RTL에서 GDSII까지의 설계 Flow를 설명하세요. ★

1. **Spec·Architecture** → 2. **RTL 코딩**(Verilog) → 3. **기능 검증**(Simulation, Coverage) → 4. **Logic Synthesis**(Constraint: Clock·I/O Delay → Gate Netlist) → 5. **DFT 삽입**(Scan, MBIST) → 6. **Floorplan·Placement·CTS·Routing** → 7. **Sign-off**: STA(Parasitic 반영), DRC, LVS, IR Drop/EM, Gate-level Simulation → 8. **GDSII Tape-out**
- **각 단계의 목적을 한 마디씩** 말할 수 있어야 한다. "합성은 기능을 공정 라이브러리 셀로 바꾸며 PPA 목표를 맞추는 단계"처럼.
- **메모리 회사 특화 포인트**: DRAM Core·Peri는 **Full-custom**(회로도 → Transistor-level Simulation → 수작업 Layout → LVS/DRC → Post-layout Simulation) 비중이 크고, Controller·Base Die·테스트 로직은 위 Digital Flow를 탄다.
- **연결**: "저는 두 Flow를 모두 경험했습니다. VLSI 수업에서는 RTL→Gate-level→PPA를, 경진대회에서는 회로도→Layout→LVS를 직접 수행했습니다."

### Q21. Pre-layout과 Post-layout Simulation의 차이는?

- Pre는 트랜지스터·이상적 배선 기준이고, Post는 Layout에서 추출한 **기생 R·C(PEX)** 를 반영한다.
- 배선 RC 때문에 지연이 증가하고 Slew가 나빠진다. 인접 배선 커플링으로 Crosstalk 지연이 생기기도 한다.
- 차이가 크면 배선 폭·길이, 드라이버 크기, 배치를 수정한다.
- **연결**: 디지털집적회로 과목에서 직접 비교한 경험이 있다. **어느 경로에서 몇 % 차이가 났는지 복원할 것**

### Q22. DRC와 LVS의 차이는?

- **DRC**: Layout이 공정 규칙(최소 폭·간격·Enclosure 등)을 지키는지 검사한다 → **제조 가능성**
- **LVS**: Layout에서 추출한 회로가 회로도와 같은 연결·소자인지 비교한다 → **설계 의도 일치**
- 추가 검사: ERC, Antenna, Latch-up, EM
- **연결**: 경진대회에서 Inhibition 회로를 추가한 뒤 LVS로 검증했다. **실제로 어떤 Mismatch가 나왔고 어떻게 고쳤는지** 하나는 말할 수 있어야 한다.

### Q23. 저전력 설계 기법을 설명하세요.

- **Dynamic 전력 감소**: Clock Gating(가장 효과적, 클럭 트리가 전체 전력의 큰 부분), Operand Isolation, DVFS(전압↓ → 제곱 효과)
- **Leakage 감소**: Power Gating(Header/Footer Switch + Retention FF + Isolation Cell), Multi-Vt(Critical Path만 LVT), Body Bias
- **Trade-off**: Power Gating은 Wake-up 지연과 Rush Current, 면적 증가를 만든다. Clock Gating은 Glitch를 막기 위해 ICG 셀(Latch 기반)을 써야 한다.
- **메모리 관점**: Self Refresh, Deep Power Down, I/O 전압 낮추기(LPDDR), Data Bus Inversion
- **연결**: 저전력 2D DCT 프로젝트에서 어떤 기법을 써서 얼마를 줄였는지 → **복원 필요**

### Q24. MBIST란 무엇이고, March Test는 어떤 Fault를 검출하나요? ★

- **MBIST**: 칩 내부에 메모리 테스트 패턴 생성기·비교기를 내장해 외부 장비 없이 고속으로 메모리를 테스트하는 DFT 기법이다.
- **March C-**: {⇕(w0); ⇑(r0,w1); ⇑(r1,w0); ⇓(r0,w1); ⇓(r1,w0); ⇕(r0)}, 복잡도 10N
- **검출 Fault**: Stuck-at Fault, Transition Fault, Address Decoder Fault, 일부 Coupling Fault(인접 셀 간섭)
- 올라가는 방향과 내려가는 방향을 모두 쓰는 이유: 셀 간 Coupling을 양방향으로 자극하기 위해서다.
- **BISR·Redundancy**: 불량 Row/Column을 여분 Row/Column으로 대체한다(Fuse로 주소 재매핑). **DRAM 수율의 핵심 기술**이다.
- **ECC와의 차이**: MBIST·Repair는 **제조 시점의 하드 불량**, ECC는 **사용 중 발생하는 오류**(소프트 에러, Retention 약화)를 다룬다.

### Q25. Pipeline의 장단점은?

- 장점: Critical Path가 쪼개져 **동작 주파수와 Throughput**이 늘어난다.
- 단점: **Latency 증가**, Register 추가로 면적·전력 증가, Hazard 처리 필요, 클럭 부하 증가
- 판단 기준: 목표 Throughput과 허용 Latency, 전력 예산
- **연결**: Matrix Multiplier에서 PPA를 비교한 내용으로 답하기

### Q26. 검증 Coverage의 종류와, Coverage 100%가 버그 없음을 의미하는가?

- Code Coverage(Line, Branch, Toggle, FSM), Functional Coverage(스펙상 시나리오), Assertion
- **100%여도 버그가 없다는 뜻은 아니다**: Code Coverage는 "실행됐는가"만 보고 "결과가 맞는가"는 보지 않는다. 또한 스펙에서 누락된 시나리오는 Coverage 항목 자체가 없다.

---

## 4. 산업·사고형 질문 (A!SK에서 깊게 나올 수 있는 유형)

### Q27. AI 시대 메모리 병목(Memory Wall)과 메모리 회사의 대응은?

- 연산 성능 증가 속도를 메모리 Bandwidth가 따라가지 못한다. LLM은 파라미터가 크고 재사용이 적어 **Bandwidth Bound**이다.
- **대응 방향**
  1. **HBM**: 대역폭 확대
  2. **PIM**(Processing-in-Memory): 데이터 이동 없이 메모리 안에서 연산한다. SK하이닉스 GDDR6-AiM이 예시다.
  3. **CXL**: 메모리 용량 확장과 Pooling
  4. **고용량 eSSD**: 추론 데이터 저장

### Q28. DRAM 설계에서 가장 중요한 기술은 무엇이라고 생각하나요? (공개 예시 문항)

- 정답이 없는 질문이다. **관점 하나를 고르고 근거를 대는 구조**로 답한다.
- 추천 답변 축: **"작은 신호를 신뢰성 있게 읽고, 적은 전력으로 빠르게 내보내는 기술"**
  1. Core: 셀 신호가 작아지는 미세화 속에서 **Sense Margin 확보**(Sense Amp, Redundancy, ECC)
  2. Peri/I/O: 속도와 전력 효율(DLL, Equalization, 저전압 I/O)
  3. 전원: 수많은 내부 전압을 안정적으로 생성·분배(Charge Pump, PDN)
- 마무리: "저는 그중 전원과 검증 관점에서 기여하고 싶습니다."

### Q29. 회로 설계 시 고려해야 할 주요 요소는? (공개 예시 문항)

- **PPA**(성능·전력·면적) + **신뢰성**(PVT, Aging, EM, Latch-up) + **검증 가능성·테스트 용이성**(DFT) + **일정**
- 하나를 올리면 다른 것이 떨어지므로 **제품 Spec이 정한 우선순위**로 판단한다. 모바일은 전력, 서버는 신뢰성, HBM은 대역폭과 발열이 우선이다.
- **연결**: 경진대회에서 기능 구현 후 면적 546.12㎛², 전력 304.92㎼를 함께 확인한 경험

### Q30. Timing Violation을 해결한 경험이 있나요? (가이드 예시 문항 — A!SK보다는 심층 인터뷰 대비용)

- 반드시 **실제 경험**으로 답한다. VLSI 프로젝트 기록을 복원해 아래 구조로 미리 작성한다.
  1. 어떤 블록, 목표 주파수 ○○MHz
  2. 합성 결과 Slack ○○ns, Critical Path는 ○○ → ○○
  3. 원인 판단(예: 곱셈기 + 누산 경로가 한 사이클에 몰림)
  4. 조치(Pipeline 삽입, 로직 재구성 등)와 결과 Slack
  5. 대가: 면적·Latency가 ○○ 증가
- 기록을 복원할 수 없다면 "수업 프로젝트 수준에서 ○○를 경험했고, 실제 설계라면 ○○ 순서로 접근하겠다"로 범위를 정직하게 긋는다.

---

## 5. 아날로그·Mixed-signal 기본 (디지털만 준비한 지원자가 놀란 영역)

> 공통 원칙: 아날로그 문항은 **"그 회로가 메모리 어디에 쓰이는가"** 를 마지막에 붙이면 설계 직군 답변이 된다.

### Q31. MOSFET의 동작 영역과 각 영역의 용도를 설명하세요.

- **Cutoff** (VGS < Vth): 꺼짐. 실제로는 Subthreshold Leakage가 흐른다 → DRAM Retention의 적
- **Triode/Linear** (VDS < VGS − Vth): ID ≈ μCox(W/L)[(VGS−Vth)VDS − VDS²/2]. VDS가 작으면 **저항처럼** 동작한다 → 스위치, 전원 Switch, Pass Gate
- **Saturation** (VDS ≥ VGS − Vth): ID ≈ ½μCox(W/L)(VGS−Vth)²(1+λVDS). VDS와 거의 무관하게 **전류원처럼** 동작한다 → 증폭기, 전류원
- **소신호 파라미터**
  - gm = ∂ID/∂VGS = 2ID/Vov: 입력 전압 변화를 전류 변화로 바꾸는 능력
  - ro = 1/(λID): 출력저항. Channel Length Modulation 때문에 유한하다
  - **Intrinsic Gain = gm·ro**: 트랜지스터 하나로 얻을 수 있는 최대 이득. 미세 공정일수록 작아진다
- **디지털 vs 아날로그 관점**: 디지털은 Cutoff↔Triode를 오가는 스위치로 쓰고, 아날로그는 Saturation에 Bias를 걸어 증폭기로 쓴다.

### Q32. Common Source 증폭기와 Source Follower를 설명하세요.

- **Common Source**: 입력 Gate, 출력 Drain. 이득 Av = −gm(RD ∥ ro). 반전 증폭으로 **전압 이득**이 목적이다.
- **Source Follower**: 출력 Source. 이득 ≈ 1(Body Effect로 약간 작음). 출력저항이 1/gm으로 낮아 **버퍼·레벨 시프트**에 쓴다.
- **Cascode**: CS 위에 Common Gate를 쌓아 출력저항을 약 gm·ro² 수준으로 키운다 → 이득 증가. 대가는 **Headroom 감소**(트랜지스터가 쌓이는 만큼 필요한 전압이 늘어남). 저전압 메모리에서 Cascode를 마음껏 못 쓰는 이유다.

### Q33. Current Mirror의 원리와 오차 요인은?

- 기준 트랜지스터를 Diode 연결해 기준 전류에 맞는 VGS를 만들고, 같은 VGS를 다른 트랜지스터에 걸어 **W/L 비율만큼 전류를 복사**한다.
- **오차 요인**
  1. Channel Length Modulation: 두 트랜지스터의 VDS가 다르면 전류가 달라진다 → Cascode Mirror
  2. Vth·β Mismatch: 공정 산포 → 큰 면적, Layout 매칭
- **메모리 용도**: Bias 전류 공급, Sense Amp·Receiver의 전류원, Reference 전류 분배

### Q34. 차동 증폭기를 쓰는 이유와 CMRR은?

- 두 입력의 **차이만 증폭**하고, 공통으로 들어온 노이즈(전원 노이즈, 커플링)는 제거한다.
- **CMRR** = 차동 이득 / 공통모드 이득. Tail 전류원의 출력저항이 클수록, 좌우 대칭이 좋을수록 커진다.
- **메모리 용도**
  - Bit Line Sense Amp(BL vs BLB)
  - **DQ 입력 Receiver**: DDR 데이터 입력은 VREF와 비교하는 의사차동(Pseudo-differential) 구조이고, CK와 DQS는 완전 차동 신호다
- **핵심 문장**: "메모리는 작은 신호를 노이즈가 많은 환경에서 읽어야 하기 때문에 차동 구조를 기본으로 씁니다."

### Q35. OP Amp의 안정도(Phase Margin)와 보상 방법은? ★ (Power 경험 연결 최적)

- 피드백 회로는 Loop Gain이 1(0dB)이 되는 주파수에서 위상이 −180°에 가까우면 **양의 피드백이 되어 발진**한다.
- **Phase Margin** = 180° + (Unity Gain 주파수에서의 위상). 보통 **60° 이상**을 목표로 한다. 작으면 Step 응답에 Ringing과 Overshoot가 생긴다.
- **2단 OP Amp + Miller 보상**: 두 단 사이에 Cc를 걸면 1단 Pole은 저주파로, 2단 Pole은 고주파로 벌어진다(**Pole Splitting**). Unity Gain 주파수 ≈ gm1/Cc. Cc가 만드는 RHP Zero는 직렬 저항(Nulling Resistor)으로 처리한다.
- **Trade-off**: 안정도를 위해 Cc를 키우면 대역폭과 Slew Rate가 떨어진다.
- **연결 문장**: "보드 VRM에서도 출력 커패시터와 보상 회로로 Loop의 Phase Margin을 확보하고, 부하 Step 응답으로 검증합니다. 칩 내부 Regulator도 같은 원리라고 이해하고 있습니다."

### Q36. Bandgap Reference의 원리는?

- 온도·전원에 무관한 기준 전압(~1.2V)을 만드는 회로다.
- **원리**: BJT의 VBE는 온도가 오르면 약 −2mV/°C로 **감소**한다(CTAT). 서로 다른 전류 밀도로 동작하는 두 BJT의 차이 ΔVBE = VT·ln(n)은 온도에 **비례**해 증가한다(PTAT). 둘을 적절한 비율로 더하면 온도 계수가 상쇄된다.
- **메모리 용도**: 모든 내부 전압(VPP, VCORE 등) Regulator의 기준이다. PTAT 성분은 **온도 센서**로도 쓰여 Refresh 주기 조절에 활용된다.
- **이슈**: 저전압에서 1.2V를 만들기 어렵다(→ 전류 모드 Bandgap), Offset이 출력 오차로 직결된다, Start-up 회로가 필요하다.

### Q37. LDO Regulator의 구조와 설계 이슈는?

- **구조**: Error Amp + Pass Transistor(주로 PMOS) + 피드백 분압기. 출력을 분압해 Reference와 비교하고 Pass Tr의 Gate를 조절한다.
- **주요 지표**: Dropout 전압(입출력 최소 차이), PSRR(입력 전원 노이즈 차단), Load Transient(부하 급변 시 출렁임), 정지 전류, 효율 ≈ Vout/Vin
- **안정도**: 출력 Pole이 부하 전류에 따라 이동해 보상이 까다롭다.
- **DC-DC와 비교**: LDO는 노이즈가 작고 빠르며 작지만 효율이 낮다. DC-DC(Switching)는 효율이 높지만 리플과 인덕터가 필요하다. 칩 내부에는 인덕터를 넣기 어려워 **LDO·Charge Pump 위주**다.
- **메모리 용도**: 외부 VDD에서 Core·Peri용 내부 전압 생성
- **연결**: 보드 레벨에서 PMIC와 DC-DC를 검토한 경험 → 효율·리플·과도응답을 같은 기준으로 비교 가능

### Q38. Comparator/Latch의 구조와 이슈는? (Sense Amp와 연결)

- **구조**: Preamp(작은 신호 증폭, Offset 감소) + **Regenerative Latch**(양의 피드백으로 빠르게 Full Swing)
- **이슈**
  - **Offset**: Mismatch가 판별 오류로 직결된다
  - **Kickback Noise**: Latch 동작이 입력으로 되돌아가 신호를 흔든다
  - **Metastability**: 입력차가 너무 작으면 결정이 늦어진다
- **메모리 용도**: Bit Line Sense Amp, DQ Receiver의 샘플러, NAND Page Buffer의 판별, 내부 전압 검출기

### Q39. 소자 Mismatch와 아날로그 Layout 기법은?

- 같은 크기로 그린 트랜지스터도 공정 산포로 Vth와 β가 다르다.
- **Pelgrom 법칙**: σ(ΔVth) = A_Vt / √(W·L). **면적을 4배 키우면 Mismatch는 절반**이다 → 정확도와 면적의 Trade-off
- **Layout 기법**: Common Centroid, Interdigitation(공정 기울기 상쇄), Dummy 소자(가장자리 효과 제거), 같은 방향 배치, 대칭 배선
- **메모리 관점**: Sense Amp는 수십억 개라 **6σ 이상**에서도 동작해야 하는데, 셀 피치 때문에 크게 만들 수 없다. 그래서 Offset 보상 회로나 Bit Line 구조로 극복한다.

### Q40. RC 지연과 Word Line·Bit Line 설계의 관계는?

- 긴 배선은 분포 RC로 동작하고, 지연은 대략 **길이의 제곱에 비례**한다(R과 C가 모두 길이에 비례).
- **DRAM 적용**: Word Line을 길게 하면 끝단 셀이 늦게 열리고, Bit Line을 길게 하면 Cbl이 커져 신호가 작아진다.
- **대응**: 계층형 구조 — Main WL + **Sub Word Line Driver**로 쪼개기, Bit Line 길이를 줄이고 Sense Amp 수를 늘리기(면적 증가)
- **Trade-off 문장**: "Array를 잘게 나눌수록 속도와 Sense Margin은 좋아지지만 Driver와 Sense Amp가 늘어 면적 효율(Cell Efficiency)이 떨어집니다. 이 균형이 DRAM Architecture의 핵심입니다."

---

## 6. 통합 문항 (후기에 언급된 유형 — 최우선)

### Q41. DRAM과 NAND에서 아날로그 회로와 디지털 회로가 쓰이는 부분을 설명하세요. ★★

**답변 골격**: "메모리는 셀에서 나온 작은 아날로그 신호를 디지털 데이터로 바꾸고, 그 데이터를 다시 고속 아날로그 신호로 칩 밖에 내보내는 제품입니다. 그래서 신호 경로의 양 끝과 전원은 아날로그, 그 사이의 제어는 디지털이 담당합니다."

| 구분 | DRAM | NAND |
|---|---|---|
| **아날로그** | Bit Line Sense Amp, 내부 전압 생성(VPP·VBB·VBLP, Bandgap, Regulator, Charge Pump), I/O Driver·Receiver·ODT·ZQ Calibration, DLL, 온도 센서 | Page Buffer의 Sensing, **고전압 생성**(Program·Erase ~20V Charge Pump), Read·Verify 전압 생성기, I/O, 온도 센서 |
| **디지털** | Command·Address Decoder, Bank Control·Timing 제어, Refresh 제어, On-die ECC, Mode Register, MBIST·Test Logic, Repair(Fuse) 제어 | **ISPP·Program/Erase 알고리즘 상태기계**, Command 처리, Column 제어, Test Logic. 칩 밖 **SSD Controller**(FTL, LDPC ECC, Wear Leveling)는 대규모 디지털 SoC |
| **HBM 추가** | Base Die의 PHY(Mixed-signal), TSV 인터페이스, Test·Repair Logic(디지털) | — |

**심화 포인트**
- **DRAM은 속도가 핵심**이라 아날로그 비중이 Sense Amp·I/O·Clock에 집중된다.
- **NAND는 고전압과 정밀한 Vth 제어가 핵심**이라 고전압 회로와 Program 알고리즘(디지털)의 협업이 중요하다. 다치 저장(TLC/QLC)일수록 Read 전압 정밀도(아날로그)와 ECC(디지털) 부담이 함께 커진다.
- **경계가 흐려지는 추세**: Equalization(DFE)처럼 아날로그 신호를 디지털 피드백으로 보상하는 Mixed-signal 회로, Calibration을 디지털로 자동화하는 기법이 늘고 있다.

---

## 7. 시나리오형 문항 ("~하면 어떻게 되고, 어떻게 대응하나")

> 답변 골격: **현상 → 물리적 원인 → 회로·제품 영향 → 설계 대응 → Trade-off**

### Q42. 온도가 올라가면 DRAM에 어떤 일이 생기고, 설계는 어떻게 대응하나요? ★

- **현상·원인**: Leakage(Junction, Subthreshold)가 지수적으로 증가 → Retention Time 감소. 트랜지스터는 이동도가 떨어져 일반적으로 느려지고, Vth도 낮아져 Leakage가 더 늘어난다.
- **영향**: Refresh 주기 단축(85°C 이상에서 2배) → 성능과 전력 손실. Peri Timing 마진 감소
- **대응**: 온도 센서 기반 Refresh 주기 조절, Negative WL로 Leakage 억제, PVT를 반영한 Timing 설계, HBM은 Thermal Via·Dummy Bump와 MR-MUF 같은 패키지 방열
- **Trade-off**: Refresh를 늘리면 신뢰성은 오르지만 성능과 전력이 떨어진다.

### Q43. 저전력을 위해 공급 전압을 낮추면 어떤 문제가 생기나요?

- Dynamic 전력은 V²에 비례해 크게 줄어든다.
- **문제**
  1. 구동 전류가 줄어 **속도가 떨어진다** (Vov 감소)
  2. **Vth는 함께 낮추기 어렵다** — 낮추면 Leakage가 폭증한다 → Headroom 부족
  3. 아날로그 회로의 신호 여유 감소: Cascode 사용 곤란, Sense Margin 감소
  4. 노이즈 대비 신호 비율 악화
- **대응**: 다중 전압 도메인(Core는 낮게, 필요한 곳만 높게), 승압 회로, Multi-Vt, Offset 보상, LPDDR처럼 I/O 전압만 따로 낮추기

### Q44. I/O 속도를 2배로 높이려면 어떤 문제가 생기고 어떻게 해결하나요?

- **문제**: 채널 손실로 인한 ISI 증가, 비트 시간이 줄어 Jitter·Skew 마진 부족, 반사·Crosstalk 민감도 증가, I/O 전력 증가
- **대응**: Equalization(FFE·CTLE·DFE), Training(Read/Write Leveling으로 타이밍 정렬), Duty Cycle 보정, 신호 방식 변경(GDDR7 PAM3: 같은 주파수에 더 많은 bit), 또는 **핀 수를 늘리는 방향**(HBM의 넓은 버스)
- **핵심 문장**: "속도를 올리는 방법은 핀당 속도를 높이는 것과 핀 수를 늘리는 것 두 가지이고, GDDR과 HBM이 각각 그 대표입니다."

### Q45. Sense Margin이 부족하다는 결과가 나왔습니다. 어떻게 접근하겠습니까?

- **신호 측면**: ΔV = (VDD/2)·Cs/(Cs+Cbl) → Cbl 줄이기(Bit Line 분할, 면적 증가), Cs 늘리기(공정 협업)
- **판별 측면**: Sense Amp Offset 줄이기(크기, Layout 대칭, Offset Cancellation), Enable 타이밍 최적화(신호가 충분히 생긴 뒤 증폭)
- **전원·노이즈 측면**: VBLP 정확도, 증폭 순간의 전원 노이즈, 인접 Bit Line 커플링
- **검증**: 어떤 PVT Corner와 위치(Array 끝단?)에서 부족한지 먼저 분리한다 → Monte Carlo로 분포를 확인한다
- **연결**: "문제를 신호, 판별, 노이즈로 나눠 범위를 좁히는 접근은 하네스 불량을 공통 전원과 개별 신호로 나눠 찾았던 방식과 같습니다."

### Q46. HBM 적층을 12단에서 16단으로 늘리면 어떤 설계 문제가 생기나요?

- **열**: 중간·상단 Die의 방열 경로가 길어져 온도 상승 → Refresh 증가, Timing 마진 감소
- **전원 공급**: 위층까지 TSV로 전원을 올려야 해서 IR Drop 증가 → 전원 TSV 수 증가, Die별 Decap
- **신호**: TSV 부하 증가, Die 간 타이밍 정렬
- **물리적 제약**: 패키지 높이 규격 안에 넣으려면 Die를 더 얇게 해야 한다 → Warpage. 접합 방식 변화(Hybrid Bonding) 검토
- **수율·테스트**: Die 수가 늘수록 스택 수율이 곱으로 떨어진다 → 적층 전 KGD(Known Good Die) 테스트, TSV Redundancy·Repair 강화

### Q47. 내부 전압이 부하 급변 시 크게 출렁입니다. 원인과 대응은?

- **원인 분리**: Regulator Loop 대역폭이 부족해 응답이 느리다 / Phase Margin이 부족해 Ringing이 생긴다 / Decap이 부족하다 / 전원 배선 저항이 크다(IR Drop)
- **확인**: Load Step Simulation으로 Undershoot 크기와 회복 시간, Ringing 여부를 보고 원인을 구분한다
- **대응**: On-chip Decap 추가(면적 증가), Loop 보상 재조정, 전원 Mesh 강화, 부하 동작 시점 분산

---


## 9. 학습 순서 (면접까지 약 4~6주 가정)

| 주차 | 범위 | 완료 기준 |
|---|---|---|
| **0순위** | **10장 Q48~Q61 (STA·합성·NAND 에러·검증·DFT)** | 실제 후기 반영. Q48·Q52·Q54·Q55를 2분 답변으로 녹음 |
| 1주 | Q1~Q9 (메모리 제품) + **Q41** | 각 문항 2분 답변을 녹음하고, 정의 문장을 막힘없이 말하기 |
| 2주 | **Q31~Q40 (아날로그)** + Q10~Q16 (회로·Peri·PI) | 수식 없이 원리로 설명하고, 각 회로가 메모리 어디에 쓰이는지 말하기 |
| 3주 | Q17~Q26 (디지털·검증) + Q42~Q47 (시나리오) | 시나리오 문항을 "현상 → 원인 → 영향 → 대응 → Trade-off"로 답하기 |
| 4주~ | Q27~Q29 + 무작위 모의 | 1분 준비 + 2분 답변을 4문항 연속으로 진행 |

※ 경험 수치 복원(Q30, 경험 연결 지도)은 **심층 인터뷰 대비**로 별도 진행한다.

**자가 채점 기준 (문항당 5점)**
1. 첫 문장이 정의·결론인가
2. "왜"(물리적·회로적 이유)를 말했는가
3. 한계나 Trade-off를 말했는가
4. 설계자가 할 수 있는 대응을 말했는가
5. 틀린 내용 없이 1분 30초 ~ 2분 안에 끝냈는가

---

## 10. 회로설계자 실무 문항 (2026-10-18 실제 응시 후기 반영 — 최우선) ★★★

> **근거**: 2026년 회로설계 A!SK 실제 응시자(지인) 후기. 어려웠던 문항은 "NAND에서 ○○ 에러가 날 수 있다. 어떻게 검증하겠나", 쉬웠던 문항은 "회로설계자가 알아야 할 것: timing report, setup/hold margin을 부르는 개념(→ **Slack**으로 추정, 지인 확인 필요), 논리 구조가 어떻게 합성되었는지".
> **의미**: 소자 물성보다 **설계 실무(합성·STA·검증)** 와 **메모리 신뢰성(에러 → 검증)** 비중이 크다. 쉬운 문항은 반드시 맞히고, 어려운 문항에서 "에러 메커니즘 → 검증 계획" 틀로 변별력을 만든다.
> 슬라이드 요약: [회로설계 A!SK 출제 카테고리 맵](https://claude.ai/artifact/VXRcZdKZRGpTKUziM2HUKW)

### 검증형 문항 답변 골격 (Q54~Q61 공통)

**① 가설**(어떤 바이어스·조건이 어떤 셀에 스트레스를 주나) → **② 시뮬레이션**(바이어스 회로를 PVT corner로) → **③ 재현**(가속 스트레스 패턴) → **④ 측정**(Vth 분포, fail bit 수 = RBER) → **⑤ 판정·대응**(ECC 정정 한계 대비 마진 → 수정 → 재검증)

---

### 10-A. STA·타이밍 리포트

### Q48. Slack이 무엇이고, Timing Report는 어떻게 읽나요? ★★

- **정의**: Slack = Required Time − Arrival Time (setup 기준). 데이터가 "도착해야 하는 시각"과 "실제 도착한 시각"의 차이로, **양수면 마진(MET), 음수면 위반(VIOLATED)** 이다.
  - Setup: Required = 클럭 주기 + 캡처 클럭 지연 − t_setup − uncertainty
  - Hold: Slack = Arrival − Required, Required = 캡처 클럭 지연 + t_hold + uncertainty
- **리포트 읽는 순서**
  1. **Startpoint / Endpoint**: 어느 FF에서 어느 FF로 가는 경로인가 (어느 클럭 도메인인가)
  2. **Path Type**: max = setup 검사, min = hold 검사
  3. **Data arrival time**: 런치 클럭 지연 + CK→Q + 조합 셀·배선 지연의 누적. **어느 셀이 지연을 많이 먹는지** 본다
  4. **Data required time**: 캡처 클럭 엣지 + 클럭 지연 − uncertainty − setup
  5. **Slack**: 음수면 위반
- **요약 지표**: WNS(Worst Negative Slack, 가장 나쁜 경로), TNS(Total Negative Slack, 음수 slack 합 → 위반이 얼마나 넓게 퍼졌나)
- **면접 한 문장**: "Slack은 타이밍 여유를 숫자로 나타낸 값입니다. 리포트에서 경로의 시작과 끝, 누적 지연에서 큰 셀을 찾고, setup이면 로직 깊이를, hold면 데이터 경로 지연을 손봅니다."
- **연결**: VLSI Matrix Multiplier의 Critical Path·Slack 확인 경험 (수치 복원 필요)

### Q49. 합성 후 WNS가 −0.3ns로 나왔습니다. 어떻게 해결하겠습니까? (Timing Closure 시나리오)

- **먼저 분리**: 위반 경로가 몇 개인가(TNS) / 한 경로 문제인가, 넓게 퍼졌나 / 제약(SDC)이 맞나 — 실제로는 타이밍이 필요 없는 경로(**false path**)나 여러 사이클이 허용되는 경로(**multicycle path**)를 잘못 걸어 생긴 가짜 위반인지 먼저 확인한다.
- **진짜 위반이면 (setup)**: 로직 재구성·단수 축소 → Pipeline 삽입(latency 증가 trade-off) → 셀 upsizing·LVT 교체(면적·누설 증가) → Retiming → Useful skew → 최후에 주파수 하향
- **Hold 위반이면**: 데이터 경로에 delay 버퍼 삽입. 주파수와 무관해 실리콘 이후엔 못 고치므로 반드시 사인오프 전에 잡는다.
- **배치 후 단계**: 배선 지연이 커진 경우 배치 조정, 버퍼링, ECO(Engineering Change Order)로 국소 수정
- **Trade-off 문장**: "타이밍을 맞추는 수단은 대부분 면적·전력·latency를 대가로 하므로, 위반 크기와 경로 수를 보고 가장 싼 수단부터 씁니다."

### Q50. STA와 동적 시뮬레이션은 어떻게 다르고, 왜 둘 다 필요한가요?

- **STA**: 입력 패턴 없이 **모든 경로**의 지연을 계산해 setup/hold를 검사한다. 빠르고 빠짐이 없지만 **기능**은 보지 않는다.
- **동적 시뮬레이션**: 입력 벡터를 넣어 **기능**을 확인한다. 넣은 패턴만 확인하므로 타이밍 전수 검증엔 부적합하다.
- **Corner·OCV**: STA는 PVT corner(SS/FF, 저전압·고온 등)마다 돌린다. 같은 칩 안 위치별 편차는 OCV(On-Chip Variation) 마진으로 반영한다. 일반적으로 setup은 느린 corner, hold는 빠른 corner가 최악이다.
- **면접 한 문장**: "기능은 시뮬레이션이, 타이밍은 STA가 책임지는 분업 구조입니다."

---

### 10-B. 합성·RTL 해석

### Q51. RTL은 어떻게 게이트 회로로 합성되나요? ★★

- **입력**: RTL(Verilog) + 표준셀 라이브러리(.lib: 셀별 지연·면적·전력) + 제약(SDC: 클럭 주기, 입출력 지연, false/multicycle path)
- **단계**
  1. **Translation**: RTL을 기술 독립적인 일반 논리(generic boolean, FF)로 변환
  2. **Logic optimization**: 불필요한 논리 제거, 공유, 재구성
  3. **Technology mapping**: 라이브러리의 실제 셀(NAND2, DFF, MUX 등)로 매핑하면서 **SDC 타이밍을 만족하는 셀 크기·구조 선택**
- **출력**: 게이트 넷리스트 + 리포트(timing, area, power, check_design 경고)
- **핵심**: 합성은 "코드 번역"이 아니라 **제약을 만족시키는 최적화**다. 같은 RTL도 클럭 목표가 빡빡하면 큰 셀·병렬 구조로, 느슨하면 작은 셀로 합성된다.

### Q52. 다음 RTL 구문은 어떤 하드웨어로 합성되나요? ★★

| RTL 구문 | 합성 결과 | 주의점 |
|---|---|---|
| `always @(posedge clk)` + `<=` | D Flip-flop | 리셋 방식(동기/비동기)에 따라 셀이 다름 |
| 조합 `always @(*)`에서 else·default 누락 | **의도치 않은 Latch** | 값을 유지해야 하므로 latch 생성 → 타이밍 분석 어려움, glitch |
| `case`, `? :` | MUX | `case`는 병렬 MUX, 중첩 `if-else`는 **우선순위 MUX 체인**(지연 김) |
| `+`, `*` | 가산기·곱셈기 | 큰 면적·긴 지연 → critical path 후보 |
| `for` 루프 | **하드웨어 복제** | 반복 실행이 아님. 루프 수만큼 회로가 생김 |
| `=`/`<=` 혼용 | 시뮬과 합성 결과 불일치 | 순차엔 `<=`, 조합엔 `=` |
| `initial`, `#delay` | 합성 안 됨 | 시뮬레이션 전용 |

- **면접 한 문장**: "RTL은 동작을 기술하는 게 아니라 하드웨어 구조를 기술하는 것이므로, 코드를 쓸 때 어떤 셀이 생길지 머릿속에 그리면서 써야 합니다."

### Q53. 합성 결과가 의도대로인지 어떻게 확인하나요? 합성 후 시뮬레이션이 RTL과 다르면?

- **확인 수단**
  1. **리포트**: check_design 경고(latch 추론, 미연결 포트, multiple driver), 면적·셀 수가 예상과 맞는지
  2. **LEC**(Logic Equivalence Check): RTL과 넷리스트가 수학적으로 같은 논리인지 형식 검증
  3. **STA**: 타이밍 만족 여부
  4. **GLS**(Gate-Level Simulation): SDF 지연을 넣어 리셋·초기화·X 전파 확인
- **RTL ≠ 합성 후 결과 원인**: sensitivity list 누락, blocking/non-blocking 혼용(race), 초기값(`initial`)에 의존, X 처리 차이, 합성 툴의 최적화로 제거된 로직

---

### 10-C. NAND 에러·신뢰성과 검증 (실제 "어려웠던 문항" 유형)

### Q54. NAND Flash에서 생길 수 있는 에러 유형을 설명하세요. ★★★

| 에러 | 언제·왜 | Vth 변화 | 대응 |
|---|---|---|---|
| **Program disturb** | 같은 WL의 비선택(inhibit) 셀 게이트에도 Vpgm이 걸림. 채널 부스팅이 부족하면 원치 않는 주입 | 상승 | Self-boosting, inhibit 조건 최적화 |
| **Pass disturb** | 프로그램 중 선택 string의 비선택 WL에 Vpass 반복 | 상승(소거 셀) | Vpass 최적화, 프로그램 순서 |
| **Read disturb** | 같은 블록 비선택 WL에 Vread(높은 통과 전압) 반복 인가 → 약한 터널링 | 상승(소거 셀) | Read count 관리, read reclaim(블록 이동) |
| **Retention** | 시간·고온에서 저장 전하 누설·de-trap | 하강 | Read retry, refresh, ECC |
| **Endurance** | P/E 반복으로 터널 산화막 열화, trap 생성 | 분포 넓어짐 | Wear leveling, bad block 관리 |
| **셀 간 간섭** | 인접 셀 프로그램 시 capacitive coupling (3D CTF는 측면 전하 이동도) | 이동 | 프로그램 순서, ISPP 세분화 |

- **왜 점점 어려워지나**: SLC → MLC → TLC → QLC로 갈수록 한 셀에 Vth 상태가 2 → 16개로 늘어 **상태 사이 간격이 좁아진다**. 같은 Vth shift도 에러가 된다.
- **최종 방어선**: ECC(BCH → LDPC). 모든 대응의 목적은 **fail bit 수를 ECC 정정 능력 안에 두는 것**이다.
- **면접 첫 문장**: "NAND 에러는 크게 동작 중 스트레스로 Vth가 올라가는 disturb류, 시간이 지나 전하가 빠지는 retention, 반복 사용으로 산화막이 열화되는 endurance로 나눌 수 있습니다."

### Q55. Read disturb가 생길 수 있습니다. 어떻게 검증하겠습니까? ★★★

- **① 가설**: Read 시 선택 WL 외 같은 블록의 모든 WL에 Vread가 걸린다. 반복되면 소거 상태(낮은 Vth) 셀에 약한 FN 터널링이 일어나 Vth가 올라간다.
- **② 시뮬레이션(회로 설계자 몫)**: Vread를 만드는 charge pump·regulator와 WL driver의 출력이 PVT corner에서 목표보다 높게 튀지 않는지, WL 위치(near/far)별 전압 차이
- **③ 재현**: 한 블록의 한 WL만 수만~수십만 회 반복 read (예시 수치, 실제 기준은 제품 스펙). 상온·고온 모두, P/E cycling을 거친 열화 블록도 함께
- **④ 측정**: Read 기준 전압을 조금씩 sweep해 **Vth 분포**를 그리고, read 횟수에 따라 소거 상태 분포의 윗꼬리가 다음 상태 경계로 얼마나 다가오는지, fail bit 수(RBER) 추이
- **⑤ 판정·대응**: ECC 정정 한계에 도달하는 read 횟수를 구하고, 그보다 여유 있게 **read reclaim 기준**을 정한다. 마진이 부족하면 Vread 낮추기(대신 비선택 셀 통과 저항 증가 → 센싱 마진 감소 trade-off) 검토 → 재검증
- **설계자 관점 한 줄**: "Vth 분포를 칩 밖에서 볼 수 있게 하는 **테스트 모드**(read 전압 조정 기능) 자체도 설계에서 만들어야 하는 기능입니다."

### Q56. Retention 에러는 어떻게 검증하나요? (10년 보증을 어떻게 확인하나)

- **문제**: 실제 10년을 기다릴 수 없다 → **고온 가속 시험(bake)**
- **원리**: 전하 누설은 온도에 지수적으로 빨라진다(Arrhenius). 고온에서 짧게 구운 시간을 활성화 에너지 가정으로 실온 기간에 환산한다. (JEDEC SSD 시험 규격에서 흔히 Ea ≈ 1.1 eV 가정)
- **절차**: 프로그램 → (P/E cycling으로 수명 말기 상태 재현) → 고온 bake → 시간별 Vth 분포 하강과 fail bit 측정
- **판정·대응**: ECC 한계 대비 마진. 부족하면 read retry 테이블(기준 전압을 낮춰 다시 읽기), 주기적 refresh, 프로그램 목표 Vth 상향(대신 disturb·endurance 악화 trade-off)
- **포인트**: 수명 초기 셀보다 **P/E를 많이 겪은 셀이 retention이 훨씬 나쁘다** → 반드시 열화 후 retention을 본다.

### Q57. Program disturb는 왜 생기고, 회로적으로 어떻게 막나요?

- **원인**: NAND는 WL 단위로 프로그램한다. 같은 WL에서 프로그램하지 않을 셀(inhibit)도 게이트에 높은 Vpgm을 받는다.
- **Self-boosting**: inhibit string의 BL에 Vcc를 걸고 SSL을 끄면 채널이 floating 된다. WL에 Vpass·Vpgm이 오를 때 커패시턴스 결합으로 **채널 전압이 같이 올라가** 게이트-채널 전압차가 줄어 주입이 억제된다.
- **Trade-off**: Vpass를 높이면 부스팅은 잘 되지만 비선택 WL 셀의 **pass disturb**가 커진다 → Vpass 최적점이 존재
- **검증**: 체커보드·특정 패턴으로 프로그램한 뒤 inhibit 셀의 Vth 분포 상승 측정, 부스팅 누설이 큰 고온 조건 포함

### Q58. NAND에서 ECC, Read Retry, ISPP는 각각 어떤 역할인가요?

- **ISPP**(Incremental Step Pulse Program): 프로그램 펄스를 조금씩 올리며 매번 verify read로 목표 Vth 도달을 확인한다. **스텝이 작을수록 분포는 좁지만 프로그램이 느리다.** 설계 자체에 "프로그램-검증" 루프가 들어 있는 구조.
- **Read retry**: 분포가 이동했을 때 read 기준 전압을 바꿔 다시 읽는다.
- **ECC**: 남은 fail bit를 정정. BCH(hard decision)에서 LDPC로 이동. LDPC는 기준 전압을 여러 번 바꿔 읽은 결과(soft information)로 정정 능력이 더 크다(대신 읽기 지연 증가).
- **면접 한 문장**: "ISPP는 쓸 때 분포를 좁히고, read retry는 읽을 때 이동을 따라가며, ECC는 남은 에러를 고치는 3단 방어입니다."

### Q59. DRAM에서는 어떤 에러가 생기고, 어떻게 검증하나요?

| 에러 | 원인 | 검증 | 대응 |
|---|---|---|---|
| **Retention fail** | 셀 커패시터 누설(접합·subthreshold·GIDL), 고온에서 악화 | Refresh 주기를 늘리며 고온에서 fail 셀 수 측정 | Refresh, 온도 기반 refresh, Negative WL |
| **VRT** | 일부 셀의 retention이 시간에 따라 무작위로 바뀜 | 같은 시험을 여러 번 반복해 변동 셀 포착 | 마진 있는 refresh 주기, ECC |
| **Row hammer** | 한 row를 반복 activate → 인접 row 셀 전하 누설 가속 | 공격 패턴(single/double-sided)으로 activate 반복 후 인접 row bit flip 측정 | TRR, DDR5 RFM, 추가 refresh |
| **소프트 에러** | 알파 입자·중성자에 의한 전하 교란 | 방사선 가속 시험 | ECC (DDR5 On-die ECC) |

- **연결**: Q2(Refresh), Q42(온도) 답과 이어서 말한다.

---

### 10-D. 검증 방법론·DFT

### Q60. 설계 단계별로 무엇을 어떻게 검증하나요? "시뮬레이션은 통과했는데 칩이 안 된다"면? ★★

| 단계 | 검증 | 확인하는 것 |
|---|---|---|
| RTL | 시뮬레이션(testbench, assertion, coverage) | 기능 |
| 합성 후 | LEC, STA | 논리 동등성, 타이밍 |
| 넷리스트 | GLS + SDF | 리셋·X 전파, 실제 지연 반영 동작 |
| 레이아웃 후 | DRC, LVS, RC 추출 후 STA·post-sim | 규칙, 회로 일치, 기생 반영 |
| 아날로그 | Corner, Monte Carlo | 공정 산포 마진 |
| 실리콘 | 테스트(ATE), MBIST, 특성 측정 | 실제 불량·마진 |

- **"시뮬 통과·칩 실패" 좁히는 순서**: ① 타이밍(corner·OCV 누락, hold) ② 모델 차이(post-layout RC, IR drop) ③ 테스트 조건(전압·온도·패턴) ④ 공정 산포·결함 ⑤ 검증 커버리지 구멍(시뮬하지 않은 시나리오)
- **연결**: LIF 뉴런 대회 Layout/LVS, Pre/Post 지연 차이

### Q61. Scan Chain과 ATPG, Stuck-at Fault를 설명하세요.

- **Scan chain**: 테스트 모드에서 칩 안의 FF들을 시프트 레지스터처럼 연결해, 외부에서 **내부 상태를 직접 넣고(제어) 꺼내 볼 수 있게(관측)** 만든다. 순차 회로 테스트를 조합 회로 테스트로 바꾼다.
- **ATPG**: Fault 모델을 기준으로 테스트 패턴을 자동 생성한다.
  - **Stuck-at fault**: 노드가 0 또는 1에 고정
  - **Transition fault**: 0→1/1→0 전이가 늦음(지연 불량, at-speed 테스트로 검출)
- **비용**: Scan MUX로 면적·타이밍 약간 증가, 테스트 시간
- **메모리는 별도**: 메모리 어레이는 scan 대신 **MBIST**(Q24)로 테스트하고 Redundancy로 Repair한다.
- **면접 한 문장**: "DFT는 만든 칩을 테스트할 수 있게 설계 단계에서 관측·제어 경로를 미리 심어두는 것이고, 메모리 회사에선 테스트와 Repair가 곧 수율입니다."

---

## 11. DRAM 불량 기초 문항 (2026-10-25 추가 — 쉬운 문항 대비) ★★

> 출처: "메모리 하루 정복 ① DRAM" 덱(https://claude.ai/artifact/6AWV744xABPdsMszA2VhrT) 불량 Q&A + 꼬리질문 Q-A~C.
> 공통 원칙: **조건 하나만 바꿔서 사라지는지 본다.** 온도 민감 → 누설 · 전압 민감 → margin · 타이밍 민감 → 구동력 · 패턴 민감 → 커플링 · ACT 횟수 민감 → row hammer. Q59(DRAM 에러 표)와 함께 본다.

### 11-A. 먼저 알아둘 용어

- **ACT(Activate)**: "이 행을 열어라" 명령. WL을 VPP로 올려 그 행 셀 전부를 SA로 읽어 들인다. 읽기·쓰기 전에 항상 ACT, 끝나면 PRE로 닫는다.
- **T(전달비) = Cs/(Cs+C_BL)**: 셀 전압 차이 중 BL까지 전달되는 비율. 전하 보존 Cs·V_cell + C_BL·VDD/2 = (Cs+C_BL)·V_f 에서 ΔV = T·(V_cell − VDD/2).
- **유효 신호** = ΔV − (누설로 잃은 몫 + 커플링 노이즈). 이것이 SA offset보다 커야 맞게 읽힌다. 남는 여유가 sense margin.
- **SA는 시간으로 켠다**: 전압 문턱이 아니라 설계자가 정한 지연 뒤 SAE 신호(PVT를 따라가는 replica 지연).

### Q62. Retention fail이란 무엇이고 어떻게 확인하나요?

- 셀이 refresh 주기만큼 데이터를 못 버티는 불량. 누설(접합, GIDL, 서브문턱, 유전막)로 전하가 빠져 '1'이 '0'으로 읽힌다.
- 확인: 데이터를 쓰고 refresh를 멈춘 채 대기 시간을 늘려 가며 읽어 **몇 ms에서 처음 실패하는지**로 retention 시간을 잰다. 고온에서 하면 꼬리 셀이 잘 드러난다.

### Q63. 고온에서만 불량이 납니다. 무엇을 의심하나요?

- 누설이 온도에 지수적으로 늘므로 retention 불량이 1순위 → refresh 주기를 줄였을 때 사라지면 retention 확정.
- 그대로면 고온에서 TR이 느려져 생기는 **타이밍 불량**(tRCD·tWR 부족) → 타이밍을 늘려 재확인.

### Q64. 저전압에서만 불량이 납니다. 원인 후보는?

- ΔV가 VDD에 비례해 줄어 **sense margin 부족**이 1순위. 그 밖에 VPP가 덜 올라 '1'을 다 못 채우는 쓰기 불량, TR이 느려진 타이밍 불량.
- 전압 고정 + 타이밍만 늘려 보면 타이밍 문제인지 margin 문제인지 갈린다.

### Q65. 체커보드 패턴에서만 틀리고 전부 0/1일 땐 괜찮습니다. 왜?

- 이웃 BL끼리 반대 방향으로 증폭될 때 서로를 끌어당기는 **BL 간 커플링 노이즈**. 같은 값이면 함께 움직여 상쇄된다.
- 대책: BL 차폐, BL twist, 레이아웃 간격, SA 타이밍 조정.

### Q66. 쓰고 바로 읽으면 틀리는데, 시간을 두고 쓰면 괜찮습니다.

- 셀 C를 끝까지 채우는 시간(**tWR**) 부족 = 쓰기 불량. access TR I_ON 부족, 셀 콘택 저항 증가가 후보.
- tWR을 줄여 가며 실패 경계를 찾는다. 대책: VPP 상향, 쓰기 드라이버 강화, 공정 측 콘택 저항 개선.

### Q67. 불량 지도에서 한 행 전체, 또는 한 열 전체가 죽어 있습니다.

- 셀이 아니라 **공유 회로** 문제. 한 행 전체 → WL open/short, WL 드라이버, 행 디코더. 한 열 전체 → BL, 그 BL의 SA, column select.
- 대책: 예비 행·열로 통째로 치환(repair). **불량 모양(점·선·면)이 원인 회로를 가리킨다.**

### Q68. 불량 셀이 있는 칩을 어떻게 정상으로 출하하나요?

- 어레이에 **예비 행·열(redundancy)**을 미리 넣고, 테스트에서 찾은 불량 주소를 fuse에 기록 → 그 주소 접근 시 디코더가 예비로 돌린다.
- 출하 후 불량은 PPR로 행 치환, 남는 단일 비트는 on-die ECC가 정정.

### Q69. Hard error와 soft error는 어떻게 다른가요?

- Hard: 결함·약한 셀 때문에 **같은 조건에서 반복 재현** → 테스트로 찾아 repair.
- Soft: 알파 입자·중성자가 전하를 순간적으로 바꾸는 **무작위 일회성** → 다시 쓰면 정상, 테스트로 못 막으니 ECC로 대응.

### Q70. March test는 무엇이고 무엇을 잡나요?

- 주소를 오름·내림차순으로 훑으며 각 셀에 "읽고-쓰고"를 정해진 순서로 반복하는 알고리즘(예: March C−).
- stuck-at, coupling fault(다른 셀을 쓸 때 같이 바뀜), 주소 디코더 불량을 잡는다. 칩 안에 넣어 자동으로 돌리면 MBIST(Q24).

### Q71. 원인 모를 DRAM 불량을 받았습니다. 어떤 순서로 분석하나요? ★★

1. 불량 모양 확인: 점(셀), 선(행·열), 면(블록)
2. 재현 패턴 확정
3. 조건을 하나씩 바꿈: 온도(누설), 전압(margin), 타이밍(구동력), 데이터 패턴(커플링), ACT 횟수(hammer)
4. 셀 / SA / 주변회로 / 공정 중 어디인지 귀속
5. 대책 선택: repair, 설계 수정, 테스트 추가, ECC
- **이 순서는 NAND 에러 문항(Q54~Q58)에도 그대로 쓴다.**

### Q72. 같은 셀에서 BL 길이를 2배로 늘리면 ΔV, tRCD, 면적은? (꼬리질문 Q-A)

- C_BL ≈ 2배(접합·배선 C 모두 길이 비례) → T: 1/6 → 1/11, ΔV ≈ 83 → 45 mV (Cs 10 fF, C_BL 50 fF 예시).
- 속도: 분포 RC라 먼 쪽 셀 지연 ∝ 길이², SA 시상수 C_BL/gm 2배 → tRCD·tRP↑.
- 면적: SA 줄 절반 → 면적·비트당 원가↓.
- 결론: 밀도 ↔ sense margin·속도, margin↓은 retention↓ → refresh↑로 번진다.

### Q73. 칩 온도가 95 °C로 오르면 refresh 주기는? 왜? (꼬리질문 Q-B)

- 85 °C 초과 → 64 ms에서 32 ms로(2배 자주).
- 이유: 접합 누설(열적 생성)이 대략 10 °C마다 2배 가까이, access TR은 V_TH↓·서브문턱 기울기 완만 → 꺼진 상태 누설↑ → 꼬리 셀 retention↓.
- 대가: refresh 전력, refresh 중 bank 사용 불가(대역폭). 온도 센서 기반 조절(TCSR). 서버·HBM에서 특히 중요.

### Q74. 특정 행 옆에서만 bit flip이 난다는 불량 보고. 원인을 어떻게 좁히고 회로로 어떻게 막나요? (꼬리질문 Q-C) ★★

- **Row hammer**: 공격 행을 64 ms 안에 ACT·PRE로 수만 번 반복 → WL 흔들림의 커플링 + 전자 주입으로 이웃(피해) 행 셀이 refresh 전에 뒤집힘. 미세화로 WL 간격↓·셀 전하↓ → 악화.
- 좁히기: ACT 횟수↑에 불량↑ → hammer / 행을 열어 둔 시간에 비례 → row press / refresh 주기 절반에 사라짐 → 전하 손실 확증 / ACT 무관하게 항상 실패 → WL short 등 공정 결함 → repair. 데이터 패턴(공격·피해 반대 값)·온도도 sweep.
- 회로 대책: 행별 ACT 카운트 → 임계치 넘으면 이웃 행 추가 refresh (TRR, RFM, DDR5 PRAC), 잔여 단일 비트는 on-die ECC.
- **면접 한 문장**: "결론부터 단정하지 않고 ACT 횟수·열린 시간·refresh 주기를 하나씩 바꿔 hammer인지 결함인지 가른 뒤, 횟수 기반 추가 refresh와 ECC로 막겠습니다."
