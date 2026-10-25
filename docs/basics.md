# A!SK 설계 직군 기초지식 v1

작성·확인일: 2026-10-05

보완: MOSFET 비이상 특성·short-channel effect를 Q01 보충 A~C에, 아날로그 증폭·주파수 응답을 A01~A08에 추가. 기존 37항목은 출제 범위 전체를 뜻하지 않습니다.

## 자료의 범위

SK하이닉스 설계 JD와 공개 직무 소개에서 필요한 개념을 골라 순서대로 학습하는 자료입니다. 사용자의 요청에 따라 자소서·개인 경험 기반 예상 질문은 넣지 않았습니다. 아래 질문은 실제 기출 목록이나 회사가 공개한 출제 범위가 아니라 **직무에서 도출한 학습·구두 설명용 질문**입니다.

설명회 현장 정리는 A!SK를 직무 기초 지식·인성 질문에 응답하는 전형으로 소개합니다. 이 문서는 그중 기술 기초만 다룹니다. 정확한 문항 수·시간·선택 방식은 확정하지 않습니다. [설명회 현장 정리](https://www.letuin.com/event/viewRn?no=403)

## 3분 답변 연습 자료

사용자 설명에 따른 통상 3분 직무 답변은 [예상 문항·키워드·3분 답변 구조](AISK_설계_예상문항_키워드_3분답변_v1.md)에서 연습합니다. 본 문서의 30~60초는 개념 확인을 위한 짧은 연습이며 실제 문항 제한 시간을 뜻하지 않습니다. 새 자료는 정의 → 원리 → 사례 → trade-off → 동향의 틀을 사용하되 공식 채점표로 단정하지 않습니다.

## 1. 설계 업무를 먼저 이해하기

설계는 메모리 제품의 요구를 회로·논리로 구현하고, 실제 칩에 배치하며, 요구 조건에서 동작하는지 검증하는 업무입니다. 시스템·아키텍처부터 디지털/아날로그 회로, layout, verification까지 포함됩니다. [회사 직무 소개](https://talent.skhynix.com/hub/ko/job/introduce)

| JD 업무 | 하는 일 | 공부할 개념 |
|---|---|---|
| 회로설계 | 요구 기능·전기적 성능을 회로로 구현 | MOSFET·CMOS, 메모리 주변회로, RTL, timing/PPA |
| 배치설계 | 회로를 소자 위치와 배선으로 구현 | layer, custom/자동 layout, DRC/LVS, 기생 RC |
| 회로검증 | 사양대로 동작하는 조건과 실패 조건 확인 | 모델·testbench, scenario, coverage, corner, regression |
| CAE | 설계·검증의 환경과 방법론 구축 | PDK·모델·constraint, 자동화, 정확도·재현성 |

기술 공부의 순서는 **소자 → 논리 → 메모리 → 설계 구현 → 성능·전력 → 검증·제품 안정성**입니다. 설계 직군이므로 공정 종류의 암기보다 '이 소자·회로가 왜 그렇게 동작하고 어떤 조건에서 실패하는가'를 먼저 설명합니다.

## 2. 학습 순서와 완료 기준

| 순서 | 단원 | 먼저 설명할 질문 | 완료 기준 |
|---|---|---|---|
| 1 | MOSFET·CMOS와 회로 기초 | Q01~Q06 + Q01 보충 A~C + A01~A08 | 비이상 소자 특성과 인버터·파형·부하 설명 |
| 2 | 디지털 논리·RTL | Q07~Q10 | 상태·clock·assignment를 구분 |
| 3 | 메모리 제품과 동작 | Q11~Q17 | SRAM/DRAM/NAND와 HBM 구조·역할 구분 |
| 4 | 설계·배치 흐름 | Q18~Q21 | 설계 결과물이 다음 단계로 넘어가는 이유 설명 |
| 5 | Timing·PPA·저전력 | Q22~Q28 | 원인·영향·개선의 trade-off 설명 |
| 6 | 검증·test·repair | Q29~Q33 | 무엇을 확인하는 검증인지 구분 |
| 7 | PVT·SI/PI·환경 | Q34~Q37 | 실제 제품 환경의 위험과 확인 방법 설명 |

모든 항목을 처음부터 완벽하게 외우지 않습니다. 먼저 각 질문에 30~60초로 답하고, 틀린 원리와 설명하지 못하는 연결을 복습합니다. 시간은 연습용 기준입니다.

## 3. MOSFET·CMOS와 회로 기초

### Q01. MOSFET은 어떻게 전류를 제어하나요?

게이트 전압이 채널 형성·전도 상태를 조절해 source와 drain 사이 전류를 제어합니다. NMOS와 PMOS는 캐리어와 켜지는 전압 방향이 다릅니다. gate 전압은 source 기준으로 보며, body 조건도 특성에 영향을 줍니다.

기초 모델의 NMOS에서 cutoff는 VGS < Vth, triode는 VGS > Vth이고 VDS < VGS−Vth, saturation은 VDS ≥ VGS−Vth인 조건으로 구분합니다. 실제 cutoff에도 누설이 있고, 이 단순 모델을 미세 소자의 정확한 식으로 그대로 사용하지 않습니다.

**확인 질문:** NMOS의 Vth가 높아지면 같은 전압에서 구동과 누설에 어떤 trade-off가 생길까?

근거·복습: [MIT MOSFET 특성](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/908ce7edc329bf6d8a628d8a2b1cb3c9_MIT6_012S09_rec09.pdf)

#### Q01 보충 A. Short-channel effect는 무엇이고 설계에 왜 중요한가요?

채널이 짧아지면서 source/drain의 전기장이 채널에 미치는 영향이 커지고, gate가 전류를 제어하는 능력이 약해지는 현상입니다. 미세화와 함께 나타나는 고전계 효과도 함께 공부합니다. '작게 만들면 무조건 빠르고 전력도 줄어든다'는 가정이 왜 성립하지 않는지 설명하는 기초입니다.

| 개념 | 원인·의미 | 설계에서 볼 영향 |
|---|---|---|
| Vth roll-off | 일반적으로 채널 길이 감소에 따라 문턱전압이 낮아지는 경향 | off-state leakage와 동작 여유 변화. 공정·구조에 따른 예외도 있음 |
| DIBL | drain 전압이 source 쪽 전위 장벽을 낮춤 | VDS 증가에 따른 유효 Vth 감소·누설 증가 |
| Velocity saturation | 큰 채널 방향 전기장에서 캐리어 속도 증가가 제한 | 긴 채널의 square-law 전류식·단순 1/L 개선을 그대로 적용할 수 없음 |
| Punch-through | source/drain 공핍영역의 영향이 겹쳐 gate 제어가 약화 | 원치 않는 전류 경로. DIBL과 같은 현상으로 외우지 않음 |
| Hot-carrier degradation | 높은 전기장으로 에너지를 얻은 캐리어가 계면·절연막에 손상을 유발 | 장기 Vth·구동 성능 변화와 신뢰성 |

학습 질문: 'L을 줄였는데 누설이 늘어나는 이유는?', 'DIBL과 Vth roll-off는 어떻게 다른가?', '미세 소자에서 긴 채널 전류식이 어긋나는 이유는?'

먼저 원인 → 소자 특성 변화 → 회로 영향까지 설명하고, 세부 모델식·공정별 수치는 이후 공부합니다. 실제 출제 여부는 확인되지 않았으며, 이 항목은 소자 기초 학습 범위에 포함합니다.

복습: [대학 short-channel MOSFET 강의](https://www.eecis.udel.edu/~vsaxena/courses/ece515/f18/Lecture%20Notes/MOSFET_SCE.pdf), [TU Delft MOS 모델·비이상 특성](https://analog-electronics.tudelft.nl/webbook/SED/_build/html/ModelingActiveDevices/ActiveDevices_MOS_transistors.html)

#### Q01 보충 B. Subthreshold·body effect·channel-length modulation은 무엇인가요?

- **Subthreshold conduction / swing:** VGS < Vth에서도 전류는 0이 아닙니다. SS는 subthreshold 영역에서 전류가 10배 변하는 데 필요한 gate 전압 변화량이며, 작을수록 급하게 전환됩니다. 이상적 일반 MOSFET의 상온 약 60 mV/dec 한계는 조건을 붙여 설명합니다. 낮은 Vth의 구동 이점과 standby leakage의 비용을 연결합니다.
- **Body effect:** source와 body 사이 전압이 달라지면 Vth가 달라집니다. 보통 bulk NMOS에서 source-body 역바이어스 증가 시 Vth가 높아집니다. 모든 소자 구조에서 동일하게 적용한다고 말하지 않습니다.
- **Channel-length modulation:** saturation에서도 VDS 증가로 유효 채널이 짧아지며 ID가 증가할 수 있습니다. 유한한 output resistance와 analog gain에 연결됩니다. 이것을 DIBL과 동일하게 설명하거나 짧은 채널에서만 존재한다고 말하지 않습니다.
- **gm·ro:** gm은 동작점에서 gate 전압 변화에 대한 drain 전류의 민감도, ro는 drain 전압 변화에 대한 전류 변화의 역수입니다. 소자의 구동·증폭 특성을 이해하는 지표입니다.

복습: [TU Delft MOS 소자 모델](https://analog-electronics.tudelft.nl/webbook/SED/_build/html/ModelingActiveDevices/ActiveDevices_MOS_transistors.html)

#### Q01 보충 C. 완화 방법은 어느 수준까지 알아야 하나요?

FinFET·GAA는 gate의 채널 제어를 강화하는 구조로 이해합니다. High-k는 같은 전기적 gate 제어를 위한 절연막의 물리 두께를 확보해 gate tunneling을 줄이는 관점과 연결합니다. 이를 모든 누설·SCE를 없애는 방법이라고 말하지 않습니다. Channel 길이·전압·Vth 선택은 속도·누설·면적·신뢰성 사이의 판단입니다.

[Synopsys FinFET의 gate 제어·누설 설명](https://www.synopsys.com/articles/finfet-design.html)

SK하이닉스 연결: DRAM의 저장 전하·retention, 주변회로의 sensing·timing, logic/controller의 standby power와 reliability를 이해할 때 소자의 누설·구동 특성이 기반이 됩니다. 실제 DRAM cell transistor·주변회로·logic die의 구조는 다를 수 있으므로 '메모리 소자는 모두 FinFET/GAA'라고 일반화하지 않습니다.

**첫 회독 순서:** MOSFET 동작영역(Q01) → subthreshold·body effect·CLM(보충 B) → SCE·DIBL·고전계 효과(보충 A) → 완화의 방향(보충 C) → CMOS inverter(Q02).

### Q02. CMOS inverter는 어떻게 0과 1을 반전하나요?

PMOS는 출력과 VDD를, NMOS는 출력과 GND를 연결합니다. 입력이 낮으면 PMOS가 켜져 출력을 높이고, 입력이 높으면 NMOS가 켜져 출력을 낮춥니다. 출력 부하 capacitance의 충전·방전 때문에 전환에 시간이 걸립니다.

**확인 질문:** 출력 H→L은 주로 어느 소자의 구동에, L→H는 어느 소자의 구동에 연결되는가?

### Q03. PMOS/NMOS width를 늘리면 항상 빨라지나요?

같은 조건에서 width가 커지면 구동 능력은 커질 수 있지만 소자 capacitance·면적도 늘어납니다. 특정 부하의 충·방전은 빨라질 수 있어도 앞단이 구동할 입력 부하와 전체 경로 전력·지연까지 고려해야 합니다. PMOS/NMOS의 상대 크기는 상승·하강 특성과 switching point에도 영향을 줍니다.

**확인 질문:** 출력 부하가 큰 gate만 키울지, 앞단도 함께 바꿀지 어떤 데이터로 판단할까?

Q02~03 복습: [MIT CMOS 지연 강의](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/de333d22ec4230412f4e7bdd4da3d6ce_MIT6_012S09_lec13.pdf)

#### Q03 보충. Gate–body와 junction capacitance — 2026-10-09

Bulk MOSFET의 기본 모델을 기준으로 구분합니다. Gate–body Cgb는 MOS 구조의 capacitance, source/drain–body Csb/Cdb는 PN 접합의 capacitance입니다. Body가 source에 연결되어도 물리적인 capacitance가 없어지는 것은 아닙니다.

**Gate 계열:** 단위 면적당 Cox = εox/tox [F/m²], 소자 gate oxide의 총 capacitance Cox,total = Cox·WL [F]. CMOS inverter의 입력 크기 추정은 Cin ≈ Cox(WnLn+WpLp)이며 실제 동작영역·overlap/fringing을 함께 봅니다.

**Gate–body Cgb:** Gate 전압이 변할 때 body 쪽 전하가 얼마나 반응하는가와 관련됩니다. Inversion channel이 없는 depletion 상태에서는 oxide와 semiconductor depletion capacitance의 직렬 조합으로 생각합니다.

\[
C_{gb,\mathrm{intrinsic}}\approx\frac{C_{ox,\mathrm{total}}C_{dep}}{C_{ox,\mathrm{total}}+C_{dep}},\qquad C_{dep}\approx\frac{\varepsilon_{Si}WL}{x_{dep}}
\]

위 식은 depletion 상태의 기본 근사이며 cutoff 전체에 동일한 숫자를 적용하는 식이 아닙니다. Accumulation에서는 이상적인 Cgb가 Cox,total에 가까워질 수 있습니다. Strong inversion의 통상적인 quasi-static transistor 모델에서는 channel이 gate와 body 사이를 차폐해 intrinsic Cgb를 작게 봅니다. Frequency·bias·기생성분에 따라 실제 값은 달라집니다.

| 상태 | Intrinsic Cgs | Intrinsic Cgd | Intrinsic Cgb |
|---|---|---|---|
| Cutoff, depletion | 작음 | 작음 | oxide/depletion 직렬 조합, bias 의존 |
| Triode, 작은 VDS·strong inversion | 약 Cox·WL/2 | 약 Cox·WL/2 | 약 0 |
| Saturation·strong inversion | 약 2Cox·WL/3 | 약 0 | 약 0 |

긴 채널 기본 근사입니다. 표의 0은 intrinsic 성분이며 overlap/fringing을 포함한 전체 capacitance가 0이라는 뜻이 아닙니다.

복습: [Montana MOS capacitance 강의](https://www.montana.edu/aolson/eele414/lecture_notes/eele414_module_02_MOSFETs.pdf), [MIT high-frequency MOS 모델](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/ce96d1ec5951846e0d1240383b10d8af_lec11.pdf)

**Junction capacitance Csb/Cdb:** NMOS의 n+ source/drain과 p-body가 PN 접합을 만듭니다. 역바이어스에서 공핍층이 capacitor의 간격처럼 작용해 Cj ≈ εSi·Aj/xdep로 이해합니다. 역바이어스가 커지면 공핍층이 넓어져 capacitance가 줄어듭니다. 역바이어스에서도 capacitance는 존재하며 PN 접합의 순방향 diffusion capacitance와는 구분합니다.

\[
C_j(V_R)=\frac{C_{j0}}{(1+V_R/\Phi_0)^m}
\]

VR은 양수로 정의한 역바이어스 크기, Cj0는 해당 접합의 zero-bias capacitance, Φ0는 junction potential, m은 grading coefficient입니다. Abrupt junction의 대표 m은 1/2입니다.

Layout의 면적·옆면을 나누는 모델에서는

\[
C_{db}\approx\frac{A_D C_{J0}}{(1+V_R/\Phi_0)^m}+\frac{P_D C_{JSW0}}{(1+V_R/\Phi_{sw})^{m_{sw}}}
\]

AD는 drain diffusion 면적, PD는 모델에 반영하는 옆면 둘레입니다. 이 식의 CJ0는 단위 면적당 [F/m²], CJSW0는 단위 길이당 [F/m] 계수로, 앞 식의 접합 전체 Cj0 [F]와 구분합니다. Csb도 source geometry·bias로 같은 방식으로 봅니다. 세부 gate-edge 분리는 PDK 모델을 따릅니다.

복습: [UMBC MOS equations·junction 모델](https://eclipse.umbc.edu/robucci/cmpe447/attachments/AIC_02_-_MOSFET_EQUATIONS.pdf)

**CMOS inverter 연결:** Gate 계열은 앞단의 입력 부하, 출력에 연결된 NMOS·PMOS drain junction은 출력 부하에 기여합니다. Body가 각각 AC 기준 전압에 고정된 단순 모델에서 CL ≈ Cdb,n+Cdb,p+Cwire+Cin,next+기타 출력 기생성분으로 봅니다. Gate–drain coupling의 효과는 단순 고정 C 합산으로 전부 표현하지 못합니다. Width를 늘리면 drive뿐 아니라 gate 부하·diffusion geometry에 따른 junction 부하도 달라지므로 전체 경로를 확인합니다.

확인 질문: 역바이어스가 커지면 Cj는? / Body와 source가 같은 node라도 Cdb는? / Strong inversion에서 intrinsic Cgb가 작아지는 이유는? / 큰 diffusion 면적·둘레가 출력 delay에 미치는 영향은?

### Q04. Propagation delay와 rise/fall time은 어떻게 다른가요?

Propagation delay는 입력 변화가 출력으로 전달되는 시간이며, 보통 정의된 입력·출력 기준 전압의 교차 시점 차이로 측정합니다. Rise/fall time은 출력 자체가 정해진 낮은/높은 전압 구간을 이동하는 시간입니다. 예를 들어 delay의 50% 기준과 전이 시간의 10~90% 기준을 섞어 말하지 않습니다. 실제 측정 기준은 사양을 확인합니다.

### Q05. Noise margin은 무엇인가요?

유효한 0·1의 출력 수준과 다음 회로가 0·1로 인식할 입력 경계 사이의 허용 여유입니다. 단순히 출력 전압이 높은 것만으로 판단하지 않고 전달 특성과 입력 기준을 봅니다. NML = VIL−VOL, NMH = VOH−VIH로 표현합니다.

Q04~05 복습: [MIT CMOS inverter·noise margin·delay 자료](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/resources/lec14/)

### Q06. RC와 피드백은 회로에서 왜 중요한가요?

RC는 회로가 변화를 따라가는 시간에 영향을 줍니다. 단순 1차 RC의 시간상수는 τ = RC이고, 저역통과 회로의 차단주파수는 fc = 1/(2πRC)입니다. 실제 회로는 여러 pole·기생성분을 포함할 수 있습니다.

Negative feedback은 출력 일부를 입력에 되돌려 차이를 줄이는 동작입니다. 회로 특성을 안정적으로 정할 수 있지만 주파수에 따른 위상 변화 때문에 안정성 확인이 필요합니다. 'negative feedback이면 항상 안정하다'고 말하지 않습니다.

**추가 학습:** 이득·대역폭·phase margin의 의미. 복잡한 OP Amp 내부 설계는 첫 회독 이후. [TI 피드백 안정성 설명](https://www.ti.com/document-viewer/lit/html/SSZT093)

## 3-1. 아날로그 증폭·주파수 응답 — A01~A08

2026-10-05 보완. 설계 JD의 아날로그 회로를 준비하려면 MOSFET·인버터·RC 이후 아래 기초도 연결해야 합니다. 출제 여부·빈도를 확인한 목록은 아니며, 개인 경험과 무관한 공통 학습 항목입니다.

학습 순서: bias → small-signal → 기본 증폭기 → current mirror·차동쌍 → OP Amp → 주파수 응답 → 피드백 안정성 → noise·offset.

### A01. Bias와 small-signal은 무엇인가요?

DC bias로 동작점 Q를 정하고, 그 주변의 작은 변화를 선형화해 해석합니다. 'small'은 절대 전압만이 아니라 비선형 특성을 선형 근사해도 되는 범위입니다. 소신호라고 무조건 저주파인 것은 아닙니다.

MOSFET의 저주파 모델은 gm·vgs 전류원과 ro 등을 이용하며 필요하면 body effect도 반영합니다. 고주파에서는 Cgs·Cgd 등 capacitance를 포함합니다. 이상적인 독립 DC 전압원은 소신호에서 단락, 독립 DC 전류원은 개방하지만 종속원은 유지합니다.

**질문:** 왜 bias가 바뀌면 gain이 달라질까? 소신호 모델로 큰 입력의 clipping까지 예측할 수 있을까?

복습: [MIT MOSFET 저주파·고주파 소신호 모델](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/ce96d1ec5951846e0d1240383b10d8af_lec11.pdf)

### A02. Common-source·source follower·common-gate는 어떻게 다른가요?

| 회로 | 먼저 이해할 특성 |
|---|---|
| Common-source | 반전 전압 증폭. 단순 저주파 조건에서 Av ≈ −gm·(RD∥ro∥RL) |
| Source follower / common-drain | 보통 1보다 작은 비반전 gain, 높은 입력·낮은 출력 저항을 이용한 buffer |
| Common-gate | 낮은 입력 저항, 비반전 특성. 입력 위치가 source인 구조 |

Gain만 비교하지 않고 입력·출력 저항, bias·headroom·부하 조건을 봅니다. Common-source의 drain 저항을 키우면 gain 이점과 출력 swing·대역폭의 제약이 함께 생길 수 있습니다. 기본 근사식은 회로·주파수 조건에 맞춰 사용합니다.

복습: [MIT common-source 증폭기](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/7a51249eb734152c5ce95df393cf4f1f_lec19.pdf), [기타 MOS 증폭단](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/pages/lecture-notes/)

### A03. Current mirror와 differential pair는 무엇인가요?

Current mirror는 기준 전류를 다른 가지에 복제·비례시키는 bias 구조입니다. 소자 비율뿐 아니라 saturation 유지에 필요한 전압, 유한 ro, mismatch를 봅니다. 어떤 출력 전압에서도 정확히 같은 전류가 흐르는 이상적인 구조는 아닙니다.

Differential pair는 두 입력의 차이에 따라 tail current가 양쪽 가지로 나뉘는 구조입니다. 차동 입력 vd = v1−v2, 공통모드 입력 vcm = (v1+v2)/2를 구분합니다. 공통모드 입력도 소자의 동작영역과 허용 입력 범위에 영향을 줍니다.

**질문:** 두 입력을 똑같이 높이는 것과 한 입력만 높이는 것은 어떻게 다른가? Tail current source가 이상적이지 않으면 무엇이 달라질까?

복습: [MIT differential amplifier](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/9932f87a7b5ec3d088d0e0836a05c622_MIT6_012F09_lec19.pdf), [current source 강의 L22](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/pages/lecture-notes/)

### A04. OP Amp와 virtual short는 어떻게 이해하나요?

OP Amp는 입력 전압 차이를 큰 open-loop gain으로 증폭합니다. Negative feedback으로 선형 동작하고 gain이 충분할 때 두 입력 전압을 거의 같다고 근사하는 것이 virtual short입니다. 실제 단락은 아니며, open-loop·포화 상태에서 적용하지 않습니다.

이상적 inverting gain은 −Rf/Rin, non-inverting gain은 1+Rf/Rg입니다. 실제로는 유한 gain·입출력 범위·부하·주파수의 제약을 확인합니다. Comparator는 입력 차이를 판정하는 용도로 구분합니다.

**질문:** 회로에 feedback이 있어도 출력이 rail에 붙으면 v+≈v−를 적용해도 될까?

복습: [MIT OP Amp 구성과 실제 제약](https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/resources/lecture_12/)

### A05. 주파수 응답·pole·zero·Bode plot은 무엇인가요?

전달함수 H(jω)의 크기와 위상을 주파수에 따라 보는 것입니다. dB 전압비는 20log10|Av|이며, 단순 1차 저역통과의 −3dB 주파수는 fc = 1/(2πRC)입니다. 단위 Hz와 rad/s를 구분합니다.

실수 1차 pole은 높은 주파수에서 약 −20dB/dec의 기울기를 더하고, zero는 +20dB/dec를 더합니다. 위상은 pole/zero의 위치와 종류에 따라 달라집니다. Inverting 증폭기의 Cgd에는 Miller effect가 나타나 입력에서 본 유효 capacitance와 bandwidth에 영향을 줄 수 있습니다.

**질문:** 출력 부하 C가 커지면 pole과 응답 속도는 어떻게 달라질까? 높은 gain과 넓은 bandwidth를 동시에 얻기 어려운 이유는?

복습: [MIT 증폭기 주파수 응답·Miller effect](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/44ed13d9b5e46dd459d9bca431fc547a_lec23.pdf)

### A06. GBW·slew rate·settling time은 어떻게 다른가요?

GBW는 주로 소신호의 gain과 bandwidth를 연결하고, slew rate는 출력 변화율의 큰 신호 한계입니다. 단일 dominant-pole voltage-feedback OP Amp에서 closed-loop bandwidth ≈ GBW/noise gain으로 근사합니다. Inverting 회로의 noise gain은 signal gain의 절댓값과 다릅니다.

Settling time은 출력이 지정 오차 범위에 들어가 유지되는 시간입니다. Slewing과 작은 신호 settling·ringing 모두에 영향을 받을 수 있습니다. 사인 출력의 최대 기울기는 2πf·Vpeak이므로 slew rate 제약은 출력 진폭에도 의존합니다.

**질문:** 작은 사인파는 정상인데 진폭을 키우면 왜 왜곡될까?

복습: [TI bandwidth·slew rate·settling 강의](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html)

### A07. Negative feedback인데 왜 발진할 수 있나요?

주파수가 올라가며 위상 지연이 누적되면 feedback의 작용이 달라집니다. 안정성은 loop gain Aβ의 크기·위상으로 판단합니다. Phase margin은 loop gain이 0dB가 되는 주파수에서 −180°까지의 위상 여유입니다. 여러 crossing·복잡한 loop에서는 숫자 하나만으로 판정하지 않습니다.

추가 pole·capacitive load는 안정성에 영향을 줄 수 있습니다. Compensation은 안정성·대역폭·응답 속도의 trade-off를 수반합니다. Closed-loop signal gain의 Bode plot과 loop gain plot을 구분합니다.

복습: [TI 피드백·capacitive load 안정성](https://www.ti.com/document-viewer/lit/html/SSZT093/GUID-E77AE2AF-5CB9-404C-92A2-222AA9AF2FE8)

### A08. Offset·noise·CMRR·PSRR은 무엇인가요?

Offset은 입력 차이가 없을 때도 오차가 생기는 비이상 특성이고, noise는 시간에 따라 변하는 불확실한 성분입니다. Input-referred 값은 출력 오차·noise를 입력으로 환산한 값입니다. Noise density와 bandwidth에 적분한 RMS noise를 구분합니다.

CMRR은 common-mode 입력 영향의 억제, PSRR은 공급 전압 변화 영향의 억제와 연결됩니다. Mismatch는 차동회로의 offset·대칭성에도 영향을 줍니다.

복습: [TI offset·noise·CMRR·PSRR 강의](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html)

### SK하이닉스 설계와 연결하는 방법

메모리 cell의 작은 신호를 판별하는 sensing, 기준 전압·bias, 전원 제어, I/O·clock 회로를 이해할 때 위 개념이 필요합니다. 다만 DRAM의 재생형 sense amplifier를 일반적인 선형 OP Amp와 동일한 회로라고 설명하지 않습니다. 동작 목적·feedback·시간에 따른 동작이 다릅니다.

첫 회독 완료 기준: 간단한 CS 회로와 차동 입력을 설명하고, OP Amp의 feedback 조건을 구분하며, 1차 Bode plot을 읽고 gain·bandwidth·slew rate·stability를 혼동하지 않는 수준입니다. 상세 transistor sizing·다단 보상 설계·복잡한 전달함수 유도는 다음 단계로 둡니다. 이 구분은 학습 순서이며 출제 제외 판정이 아닙니다.

## 4. 디지털 논리·RTL

### Q07. 조합회로와 순차회로는 어떻게 다른가요?

조합회로 출력은 현재 입력으로 결정되고, 순차회로는 저장된 상태에도 의존합니다. AND·mux·가산기는 조합회로 예시이고 register·counter·FSM은 상태를 이용합니다. 순차회로라고 모든 회로가 반드시 edge-triggered인 것은 아닙니다.

### Q08. Latch와 flip-flop, reset은 무엇인가요?

Latch는 활성 level 동안 입력을 따라가고, flip-flop은 지정 clock edge에서 값을 저장합니다. 동기 reset은 clock 동작에 맞춰 반영되고 비동기 reset은 clock과 무관하게 반영됩니다. 비동기 reset 해제에도 timing·동기화 문제가 생길 수 있습니다.

Q07~08 복습: [MIT 순차논리 강의](https://fpga.mit.edu/6205/_static/F22/lectures/L03.pdf)

### Q09. RTL·gate-level·합성은 어떻게 연결되나요?

RTL은 register 사이의 데이터 이동과 연산을 기술하는 수준이고, gate-level은 논리 gate·cell과 연결로 표현합니다. 합성은 합성 가능한 기술과 제약·library를 바탕으로 논리 구현을 만듭니다. 같은 Verilog 언어라도 기술 수준이 다르며 모든 simulation 문법이 hardware로 합성되는 것은 아닙니다.

### Q10. Blocking과 non-blocking assignment는 왜 구분하나요?

Blocking(=)은 해당 procedural block의 실행 순서에서 바로 값이 반영되고, non-blocking(<=)은 우변 평가와 업데이트를 분리해 예약된 시점에 값을 반영합니다. 보통 조합 블록은 blocking, clocked 순차 블록은 non-blocking으로 기술해 의도와 simulation 의미를 맞춥니다. 문법만으로 조합/순차 hardware가 자동 결정되는 것은 아닙니다.

**확인 질문:** clocked block에서 a<=b; b<=a;를 하면 이전 값을 교환하는 이유는?

복습: [AMD Verilog assignment 설명](https://docs.amd.com/r/2024.2-English/ug901-vivado-synthesis/Blocking-and-Non-Blocking-Assignments)

## 5. 메모리 제품과 동작

### Q11. SRAM·DRAM·NAND는 어떻게 다른가요?

| 구분 | 저장 원리의 대표 예 | 전원 끄면 | 주 용도 |
|---|---|---|---|
| SRAM | feedback으로 상태 유지, 대표적으로 6T cell | 소실 | cache·내부 buffer |
| DRAM | capacitor에 저장한 전하, 대표적으로 1T1C | 소실 | main memory·HBM |
| NAND | 저장 전하에 따른 threshold 상태 | 유지 | SSD·UFS 등의 저장 |

SRAM은 전원 공급 중 DRAM과 같은 주기적 refresh가 필요하지 않습니다. NAND는 비휘발성이지만 retention·endurance가 무한하지 않습니다. 속도·면적·용량·전력은 사용 조건과 구현까지 함께 비교합니다.

### Q12. DRAM의 read와 refresh는 왜 필요한가요?

Word line을 활성화하면 저장 capacitor와 bit line 사이 charge sharing으로 작은 전압 변화가 생깁니다. Sense amplifier가 차이를 증폭하며 cell 값을 복원합니다. 읽기가 저장 전하를 교란하므로 restore가 필요하고, 읽지 않은 cell도 leakage로 정보가 약해져 주기적 refresh가 필요합니다.

### Q13. Sense amplifier와 precharge는 무엇인가요?

Sense amplifier는 cell에서 온 작은 신호 차이를 판별·증폭합니다. Precharge는 다음 접근을 위해 bit line을 기준 상태로 준비하는 단계입니다. 작동 순서·offset·noise·타이밍 여유가 읽기 신뢰성과 연결됩니다.

Q11~13의 SRAM/DRAM 기초: [MIT memory 강의](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/)

### Q14. NAND의 read·program·erase와 TLC/QLC는 무엇인가요?

Program/erase는 저장 전하와 threshold 상태를 바꾸고, read는 정해진 기준 조건에서 상태를 구분합니다. 일반적으로 page 단위로 읽고 program하며 block 단위로 erase합니다. TLC는 cell당 3bit, QLC는 4bit를 저장하므로 더 많은 상태를 구분해야 합니다. 용량 이점과 함께 판별 여유·속도·신뢰성의 trade-off가 생깁니다.

Floating gate와 charge trap 구조를 구분하고 모든 NAND가 floating gate라고 말하지 않습니다. [Micron NAND 기술·제품 안내](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand), [3D charge-trap NAND 기술](https://www.micron.com/products/storage/nand-flash/176-layer-nand)

### Q15. 메모리의 row·column·bank와 timing 사양은 무엇인가요?

Row를 활성화해 내부에 읽어낸 데이터에서 column을 선택합니다. Bank는 명령·동작을 조직화하는 단위로, 여러 bank를 활용하면 병렬성을 얻을 수 있지만 모든 명령이 무제약으로 동시에 수행되는 것은 아닙니다.

DRAM에서 tRCD는 activation 이후 read/write까지의 제약, tRP는 precharge 이후 다음 activation까지의 제약, tRAS는 row가 활성 상태로 유지되어야 하는 최소 시간과 관련됩니다. 값 암기보다 필요한 동작이 완료되기 전에 다음 명령을 보내면 무엇이 잘못되는지 이해합니다. [Microchip DDR timing 설명](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html)

### Q16. HBM은 무엇이고 왜 bandwidth가 큰가요?

HBM은 여러 DRAM die를 적층하고 많은 I/O를 이용하는 고대역폭 메모리입니다. 전송률 하나만 높이는 대신 넓은 데이터 경로를 활용합니다. 이론 bandwidth는 총 유효 data width와 pin당 data rate로 계산하며, 실제 성능에는 access pattern·효율·시스템 조건이 반영됩니다.

Core die의 저장 기능과 base/logic die의 인터페이스·logic 역할을 구분합니다. HBM은 DRAM 기반이라 refresh·retention 개념이 사라지지 않습니다. [회사 HBM·logic 기술 방향](https://news.skhynix.co.kr/tsmc-technology-symposium-2026/)

### Q17. NAND die·controller·SSD는 무엇이 다른가요?

NAND die는 데이터를 실제로 저장하는 칩, controller는 host 요청과 NAND 동작을 관리하는 칩, SSD는 controller·NAND·firmware·전원 등의 통합 제품입니다. NAND 내부 회로설계와 controller RTL 설계, board HW 설계를 구분합니다. 제품 구조 설명은 [제품군별 설계 지도](JD/회로설계_Digital설계_차이와_제품군.md) 참고.

## 6. 설계·배치 흐름

### Q18. 디지털 설계는 RTL에서 실제 칩까지 어떻게 진행되나요?

대표 흐름은 spec/architecture → RTL·검증 → synthesis → floorplan·전원 계획 → placement → clock tree → routing → 기생 추출·sign-off입니다. 실제로는 검증과 분석을 반복하며 이전 단계로 돌아갑니다. Gate netlist와 layout DB가 무엇인지 구분합니다.

Custom 회로는 schematic·소자 sizing·simulation → layout → 추출 후 특성 확인으로 이해합니다. 두 흐름 모두 연결·성능·공정 제약을 검증합니다. [Synopsys 물리 설계 흐름](https://www.synopsys.com/content/dam/synopsys/services/datasheets/physical-design-assistance-ds.pdf)

### Q19. Custom layout·자동 배치·배선, contact·via는 무엇인가요?

Custom layout은 소자와 배선을 직접 설계하고, 자동 배치·배선은 library cell·macro를 제약에 맞춰 놓고 연결하는 방식입니다. Contact는 보통 소자 영역과 배선층, via는 배선층 사이의 연결에 쓰이며 구체 명칭은 PDK에 따라 확인합니다. Active·gate·well·metal의 역할을 구분합니다.

### Q20. DRC와 LVS가 통과하면 설계가 완성된 건가요?

DRC는 layout이 공정의 폭·간격 등 제조 규칙을 만족하는지 봅니다. LVS는 layout에서 추출한 소자·연결이 schematic/netlist와 일치하는지 봅니다. 둘이 통과해도 기능·timing·power·noise 등의 사양을 추가 확인해야 합니다.

복습: [DRC](https://www.synopsys.com/glossary/what-is-design-rule-checking.html), [LVS](https://www.synopsys.com/glossary/what-is-layout-versus-schematic-checking.html)

### Q21. Pre/post-layout 결과가 왜 달라지나요?

배선과 소자 배치에는 의도하지 않은 저항·capacitance 등이 생깁니다. 추출한 기생성분을 반영하면 신호 지연·파형·coupling·전력 등 결과가 달라질 수 있습니다. Post 결과가 항상 단순히 나빠진다고만 말하지 않고 무엇이 달라졌는지 분석합니다.

복습: [기생성분 추출](https://www.synopsys.com/glossary/what-is-parasitic-extraction.html)

## 7. Timing·PPA·저전력

### Q22. Setup과 hold는 무엇인가요?

Setup은 capture clock edge 이전, hold는 그 이후에 데이터가 안정되어야 하는 시간입니다. Setup은 주로 데이터가 늦게 도착하는 문제, hold는 너무 일찍 변하는 문제와 연결됩니다. Hold 위반은 clock period를 늘리는 것만으로 보통 해결되지 않습니다.

### Q23. Critical path와 slack은 무엇인가요?

Timing 목표를 가장 제한하는 경로가 critical path입니다. Setup slack은 required time−arrival time, hold slack은 arrival time−required time으로 생각하면 여유의 방향을 구분할 수 있습니다. 음수 slack은 해당 분석 조건의 timing 위반을 뜻합니다. 단순히 gate 수가 가장 많은 경로라고 단정하지 않습니다.

### Q24. STA와 functional simulation은 어떻게 다른가요?

Functional simulation은 주어진 입력에서 논리 동작이 기대와 맞는지 확인합니다. STA는 모델·constraint로 timing 경로를 분석합니다. STA 통과는 기능의 정확성을 보장하지 않고, simulation 통과는 모든 경로의 timing 만족을 보장하지 않습니다.

Q22~24 복습: [Synopsys STA](https://www.synopsys.com/glossary/what-is-static-timing-analysis.html)

### Q25. Pipeline과 PPA는 어떤 관계인가요?

Pipeline은 연산을 register로 나누어 단계 사이의 조합 경로를 줄입니다. Throughput·clock 목표에 도움이 될 수 있지만 latency·register·clock 부하·제어 비용이 달라집니다. PPA는 power·performance·area이며, performance도 최대 주파수인지 처리량인지 지연인지 먼저 정의해야 합니다.

**확인 질문:** 주파수가 올라가도 최종 처리 속도가 좋아지지 않는 경우는?

### Q26. CMOS의 dynamic power와 leakage power는 무엇인가요?

Switching power의 대표 근사는 P ≈ α·C·V²·f이며 activity·capacitance·전압·주파수에 연결됩니다. 실제 dynamic power에는 전환 중 short-circuit 등의 기여도 있습니다. Leakage는 전환하지 않을 때도 흐르는 누설과 연결되며 V·Ileak로 생각합니다.

전압을 낮추면 switching power가 줄지만 timing과 noise margin도 확인해야 합니다. 전력을 한 식만으로 정확하게 산출했다고 말하지 않습니다. [Cadence 저전력 기법](https://resources.system-analysis.cadence.com/power-integrity/msa2021-low-power-design-techniques-for-power-integrity-in-vlsi)

### Q27. Clock gating과 power gating은 무엇이 다른가요?

Clock gating은 필요 없는 clock 전환을 멈춰 switching을 줄이는 방식이고, power gating은 공급 경로를 차단해 주로 leakage를 줄이는 방식입니다. Power gating은 상태 보존·isolation·wake-up 순서를 고려해야 합니다. Clock gating에서도 glitch 없는 제어와 test 접근을 확인합니다.

복습: [Cadence clock gating](https://community.cadence.com/cadence_blogs_8/b/di/posts/understanding-clock-gating-report-and-cells), [low-power 검증 자료](https://www.cadence.com/content/dam/cadence-www/global/en_US/documents/tools/system-design-verification/low-power-wp.pdf)

### Q28. Metastability와 CDC는 어떻게 대응하나요?

비동기 입력이나 다른 clock domain의 신호가 setup/hold를 만족하지 못하면 저장 소자가 일정 시간 안정된 논리값을 확정하지 못할 수 있습니다. Synchronizer는 이를 다음 회로가 받아 실패할 확률을 줄입니다. 없애는 보장이라고 말하지 않습니다.

단일 level 신호에 쓰는 2-flop 방식이 multi-bit bus·짧은 pulse 전달까지 자동 보장하지는 않습니다. 조건에 따라 handshake·async FIFO 등을 검토합니다. [Intel metastability 안내](https://www.intel.com/content/www/us/en/docs/programmable/683068/18-1/metastability-analysis.html), [CDC·synchronizer white paper](https://cdrdv2-public.intel.com/650346/wp-01082-quartus-ii-metastability.pdf)

## 8. 검증·test·repair

### Q29. 회로검증에서 testbench·reference model은 무엇인가요?

Testbench는 DUT에 조건과 입력을 주고 결과를 확인하는 환경입니다. Reference model은 기대 결과의 기준이며 checker/scoreboard가 실제 결과와 비교할 수 있습니다. Assertion은 지켜야 할 관계를 검사합니다. 모델의 가정도 틀릴 수 있으므로 독립적인 기준·작은 예제로 확인합니다.

### Q30. Coverage와 regression은 무엇인가요?

Code coverage는 코드 구조가 실행된 범위, functional coverage는 사양상의 상황을 검증한 범위입니다. 높은 code coverage만으로 기능 검증 완료를 선언하지 않습니다. Regression은 변경 후 기존 test를 반복해 재발과 부작용을 확인하는 것입니다. UVM은 이러한 검증 환경을 구조화·재사용하는 표준 방법론이며 언어 자체가 아닙니다.

Q29~30 복습: [Accellera UVM](https://www.accellera.org/community/uvm), [UVM 사용자 가이드](https://www.accellera.org/images/downloads/standards/uvm/uvm_users_guide_1.2.pdf)

### Q31. MBIST와 March test는 무엇인가요?

MBIST는 내장 회로가 memory에 주소·데이터·read/write 동작을 주고 기대값과 비교하는 구조입니다. March test는 주소를 정해진 방향으로 순회하며 read/write를 수행하는 알고리즘 계열입니다. 특정 알고리즘·조건에 따라 stuck-at·transition·coupling 등 검출 범위가 달라지므로 모든 fault 검출을 보장하지 않습니다.

### Q32. MBIST·BISR·ECC는 어떻게 다른가요?

MBIST는 test, BISR는 분석된 불량에 대해 여분 자원 등을 이용한 repair, ECC는 데이터의 오류를 검출·정정하는 code입니다. ECC의 검출·정정 한계는 code에 따라 다릅니다. Fault의 원인을 없애는 것과 잘못된 데이터를 정정하는 것은 구분합니다.

Q31~32 참고: [Synopsys embedded memory test·repair](https://www.synopsys.com/implementation-and-signoff/test-automation/synopsys-ip-sms.html)

### Q33. DFT와 design verification, 양산 test는 무엇이 다른가요?

Design verification은 설계가 사양대로 동작하는지 확인하고, DFT는 실제 제작된 chip을 test하기 쉽게 scan·BIST 등 구조를 설계에 넣는 것입니다. 양산 test는 제조된 chip의 특성·결함을 측정해 판정합니다. Simulation·MBIST·tester 각각이 확인하는 범위를 구분합니다.

## 9. 실제 동작 조건·SI/PI·설계 환경

### Q34. PVT corner와 mismatch는 무엇인가요?

PVT는 process·voltage·temperature 조건입니다. Corner는 정의한 조건 조합에서 성능·동작을 확인하는 관점이고, mismatch는 소자 간의 국부적인 차이입니다. 전압·온도·공정 변화가 delay·leakage·sensing 등에 영향을 줍니다. 온도가 오르면 모든 회로가 무조건 느려진다고 단정하지 않습니다.

### Q35. SI와 PI, IR drop은 무엇인가요?

SI는 신호가 수신단에서 값과 timing 기준을 만족하는지, PI는 필요한 전압이 위치와 시간에 맞게 공급되는지의 문제입니다. IR drop은 전원 경로 저항에 전류가 흘러 생기는 전압 감소입니다. 공급 전압 감소가 delay·noise margin에 영향을 줄 수 있어 회로 기능과 연결됩니다.

정적 IR drop과 순간 부하·전원망 RLC에 따른 동적 전압 변화를 구분합니다. Crosstalk는 인접 신호 coupling, reflection은 impedance 불연속과 연결됩니다. [Cadence PI 분석](https://www.cadence.com/en_US/home/resources/white-papers/how-to-achieve-10x-faster-power-integrity-analysis-and-signoff-wp.html)

### Q36. PDK·library·constraint와 CAE는 무엇인가요?

PDK는 공정에 맞는 모델·규칙 등의 설계 환경, library는 구현·분석에 쓰는 cell 등의 기능·timing·power 정보, constraint는 clock·입출력·동작 조건 등의 요구입니다. 서로 목적이 다릅니다. CAE는 이 환경·도구·방법론을 구축하고 자동화·정확도·생산성을 개선하는 역할로 이해합니다. [회사 CAE 직무 설명](https://news.skhynix.co.kr/the-work-of-avengers-class-activity-and-innovation/)

### Q37. 특정 조건에서만 회로가 실패하면 어떤 순서로 보나요?

먼저 기대 사양과 실패 조건·재현성을 확인합니다. 다음으로 모델·입력·constraint 오류와 실제 기능/timing/power 문제를 구분하고, 조건을 하나씩 바꾸어 가설을 나눕니다. 개선 후에는 원래 문제뿐 아니라 다른 corner·mode·기능에 부작용이 없는지 확인합니다.

학습용 상황: 저전압에서만 fail, post-layout에서만 fail, low-power mode 복귀 후 fail. 실제 기출이 아니라 여러 기초 개념을 연결하는 연습입니다.

## 10. 처음에는 뒤로 둘 범위

첫 회독은 위 개념의 원리·역할·trade-off를 설명하는 데 집중합니다. 다음은 기본기가 정리된 뒤 확장합니다.

- 고급 PLL·ADC·SerDes 내부 설계, 상세 analog loop 보상.
- UVM 전체 환경 구현, formal property의 심화 증명.
- Full-chip sign-off tool의 세부 명령·파일 형식.
- 최신 제품의 수치 전부, 모든 공정 recipe·장비 구조.
- 특정 내부 조직의 채용 인원이나 배치 확률 추정.

이는 출제되지 않는다는 뜻이 아니라 학습 순서를 정한 것입니다. 설계 JD의 넓은 범위를 먼저 연결한 다음 세부화합니다.

## 11. A!SK 구두 연습 방법

개념 질문은 **정의 한 문장 → 동작 원리 → 설계에서 중요한 이유 → 한계나 trade-off** 순서로 답합니다. 억지로 개인 경험을 붙이지 않습니다.

예: 'Clock gating은 사용하지 않는 블록의 clock 전환을 멈추는 기법입니다. Clock은 데이터가 바뀌지 않아도 반복적으로 전환하므로 gating으로 불필요한 switching power를 줄일 수 있습니다. 다만 glitch가 없도록 제어해야 하고, power gating처럼 공급을 끊는 방식은 아니어서 leakage를 같은 방식으로 줄이지는 못합니다.'

각 항목 체크: [ ] 정의를 말함 / [ ] 원리를 설명함 / [ ] 혼동하기 쉬운 개념과 구분 / [ ] 조건 변경의 영향 설명.

### 첫 회독 7회 순서

1. Q01~06 + Q01 보충 A~C: 소자·비이상 특성·SCE·CMOS. 이어 A01~A08의 증폭·주파수 기초를 학습하며, 필요하면 이 회차를 나눕니다.
2. Q07~10: 논리·RTL.
3. Q11~17: memory 구조·동작·제품.
4. Q18~21: 설계와 물리 구현.
5. Q22~28: timing·PPA·저전력·CDC.
6. Q29~33: verification·test·repair.
7. Q34~37 + 랜덤 5문항: 조건·SI/PI·환경, 전체 연결.

한 회차에 이해가 막히면 그 회차를 반복합니다. 첫 회독 이후 질문을 순서 없이 섞어 연습합니다.

## 12. 자료 선택과 한계

직무 범위는 첨부 JD와 회사 공개 소개를 기준으로, 기술 개념은 대학 강의·EDA 업체·메모리 업체·표준 단체의 1차 자료로 확인했습니다. 일부 제품 뉴스룸 페이지는 직접 열기가 제한되어 공개 검색 내용 범위에서 참고했습니다. 회사별 최신 제품 스펙·공정 모델의 정확한 수치에는 본 문서의 기초 근사식을 적용하지 않습니다.

[설계 JD 상세 해설](JD/설계_JD_상세해설_및_준비범위.md)과 [제품군 지도](JD/회로설계_Digital설계_차이와_제품군.md)는 직무의 전체 맥락을 확인할 때 사용합니다. A!SK의 공식 출제 예측 자료로 표기하지 않습니다.
