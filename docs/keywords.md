# A!SK 설계 예상 문항·필수 키워드·3분 답변 구조 v1

작성·확인일: 2026-10-05

## 1. 준비 기준과 근거 수준

- **사용자 전달 응시 가이드:** 설계 관련 기초 직무 문제에 전공 지식·공부한 내용을 기반으로 구체적으로 답변한다는 안내. 가이드 원문 파일을 별도로 검증한 것은 아닙니다.
- **사용자 설명:** 직무 지식 문항은 통상 3분 답변. 아래는 이를 기준으로 한 연습 자료이며 이번 개인 안내의 시간을 별도로 확정하지 않습니다.
- **사용자 회상 실제 문항:** 과거 PE A!SK에서 DRAM 구조를 물성·1T1C 등과 연결해 자세히 설명하는 질문, HBM을 자세히 설명하는 질문이 나왔음. 정확한 녹취 문항은 아니며 설계 전형의 동일 출제를 보장하지 않습니다.
- **사용자 전달 유튜버 의견:** 정의·원리·사례·trade-off·최신 동향의 5단계. 공식 평가표·배점으로 확인하지 않았으며 답변을 구체화하는 훈련 틀로 사용합니다.
- **아래 24개:** 설계 JD와 공개 기술 자료에서 만든 예상 질문. 실제 기출·출제 빈도·채용 인원 예측과 구분합니다. 개인 자소서·경험은 답변에 넣지 않습니다.

기초 설명은 [A!SK 설계 기초지식](AISK_설계_기초지식_v1.md), 업무 범위는 [설계 JD 해설](JD/설계_JD_상세해설_및_준비범위.md)을 함께 봅니다. 이 파일은 개념을 알고 난 뒤 3분 답변으로 조립하는 자료입니다.

## 2. 3분 답변을 조립하는 방법

| 연습 시간 | 역할 | 실제 넣을 내용 |
|---|---|---|
| 0:00~0:20 | 정의·답변 범위 | 무엇인지 한두 문장, 질문의 비교 대상 |
| 0:20~1:30 | 원리 | 구조 → 입력/동작 → 물리·전기적 변화 → 결과 |
| 1:30~1:55 | 사례 | 그 원리 때문에 어떤 제품·회로·상황에 쓰이는가 |
| 1:55~2:40 | Trade-off | 무엇을 개선하면 무엇이 불리해지는가, 왜 그런가 |
| 2:40~3:00 | 동향·정리 | 확인된 동향 하나와 해당 원리의 연결 |

시간 배분은 연습 제안이며 평가 비율이 아닙니다. 각 문항의 5단계는 **말을 확장할 골격**입니다. 그대로 읽으면 모두 3분이 되는 완성 원고는 아닙니다. 원리에 동작 순서·단순식·비교 사례를 더해 녹화하며 길이를 조정합니다. 핵심이 충분하면 군더더기로 시간을 채우지 않습니다.

최신 동향은 원리 설명 뒤의 짧은 연결입니다. 독립적인 최신 뉴스가 없는 기초 문항에는 '현재 제품에서 중요해지는 설계 조건'을 설명하고, 이를 새로운 기술 발표로 포장하지 않습니다. 질문이 동향을 요구하지 않으면 원리와 trade-off에 시간을 더 쓸 수 있습니다.

**필수 키워드의 의미:** 해당 문항에서 개념을 빠뜨리지 않도록 보는 목록입니다. 단어를 모두 외쳐야 한다는 뜻은 아닙니다. 변형 질문의 범위에 맞춰 원리 2~3개를 중심으로 인과관계를 설명합니다.

## 3. 학습 우선순위와 질문 지도

학습 순서는 **memory 제품·동작 → 소자·회로 → 아날로그·주파수 → digital/timing → 물리 구현·검증**입니다. DRAM·NAND·HBM부터 준비하는 이유는 사용자 회상과 회사 제품에 직접 연결되기 때문이며 출제 확률을 수치화한 것은 아닙니다. 아날로그와 digital을 제외하는 근거로 사용하지 않습니다.

| 문항 | 주제 | 먼저 잡을 인과관계 |
|---|---|---|
| Q01 | DRAM의 1T1C 구조와 읽기·쓰기·refresh를 물리적 원리와 연결해 설명해 주세요. | access transistor, storage capacitor, WL/BL, Q=CV, charge sharing, sense amplifier, restore, leakage/refresh |
| Q02 | NAND 플래시의 동작 원리와 DRAM의 차이를 설명해 주세요. | charge storage layer, Vth, tunneling, read/program/erase, NAND string, page/block, nonvolatile, endurance |
| Q03 | HBM의 구조와 고대역폭을 얻는 원리, 설계상의 trade-off를 설명해 주세요. | stacked DRAM, TSV, wide I/O, core/base die, interposer/package, bandwidth, heat, yield/power |
| Q04 | SRAM·DRAM·NAND를 cell 구조와 용도 관점에서 비교해 주세요. | 6T, cross-coupled inverter, 1T1C, Vth storage, volatile, density, latency, cost/bit |
| Q05 | DRAM sense amplifier와 precharge의 역할을 설명해 주세요. | BL/BLB, VDD/2, charge sharing, positive feedback, restore, offset/noise, timing |
| Q06 | SLC·MLC·TLC·QLC와 3D NAND의 차이를 설명해 주세요. | bits/cell, 2^b states, Vth distribution, read margin, program-verify, ECC, vertical stacking |
| Q07 | DRAM row·column·bank와 timing 사양이 필요한 이유를 설명해 주세요. | ACT, row buffer, READ/WRITE, PRE, bank, tRCD, tRAS, tRP |
| Q08 | MBIST·BISR·ECC는 무엇이며 어떻게 다른가요? | built-in test, March, fault model, redundancy/repair, syndrome, correction limit |
| Q09 | DDR·LPDDR·GDDR·HBM은 어떻게 다르고 설계 목표는 무엇인가요? | DRAM family, bandwidth, energy/bit, pin rate/width, capacity, package, workload |
| Q10 | MOSFET의 동작영역과 analog/digital에서 사용하는 방식을 설명해 주세요. | VGS/VDS/Vth, cutoff/triode/saturation, channel, bias, gm, leakage |
| Q11 | Short-channel effect와 미세화의 trade-off를 설명해 주세요. | gate control, Vth roll-off, DIBL, subthreshold leakage, velocity saturation, reliability, FinFET/GAA |
| Q12 | CMOS inverter의 동작과 sizing·delay·power 관계를 설명해 주세요. | pull-up/down, PMOS/NMOS, CL, tPLH/tPHL, noise margin, αCV²f, leakage |
| Q13 | PVT corner와 mismatch가 회로에 미치는 영향을 설명해 주세요. | process/voltage/temperature, global/local variation, corner, Monte Carlo, delay/leakage/offset |
| Q14 | Small-signal model은 무엇이며 왜 bias가 필요한가요? | DC operating point, linearization, gm, ro/gmb, dependent source, Cgs/Cgd, validity |
| Q15 | Common-source·source follower와 current mirror의 역할을 설명해 주세요. | inverting gain, gm·Rout, input/output resistance, buffer, reference current, compliance/headroom |
| Q16 | Differential amplifier의 원리와 common-mode rejection을 설명해 주세요. | vd=v1−v2, vcm=(v1+v2)/2, differential pair, tail current, Ad/Ac, CMRR, offset/mismatch |
| Q17 | OP Amp의 동작과 negative feedback·virtual short를 설명해 주세요. | AOL, differential input, negative feedback, ACL, virtual short, input/output range, saturation |
| Q18 | 증폭기의 주파수 응답·GBW·slew rate·안정성을 설명해 주세요. | H(jω), pole/zero, Bode, −3dB, Miller, noise gain, slew rate, loop gain/phase margin |
| Q19 | Setup·hold·slack·critical path와 timing 위반 대응을 설명해 주세요. | launch/capture, setup/hold, arrival/required, slack, skew, constraint, max/min path |
| Q20 | Pipeline과 저전력 기법을 PPA trade-off로 설명해 주세요. | throughput/latency, stage/register, αCV²f, leakage, clock/power gating, retention/isolation, DVFS |
| Q21 | Metastability와 CDC의 원리·대응을 설명해 주세요. | asynchronous input, setup/hold, resolution time, MTBF, synchronizer, pulse/bus, handshake/FIFO |
| Q22 | 회로/RTL에서 layout까지 흐름과 DRC·LVS·기생 추출을 설명해 주세요. | schematic/RTL, synthesis/netlist, floorplan/placement/CTS/routing, DRC, LVS, PEX, sign-off |
| Q23 | SI·PI·IR drop·crosstalk가 회로 동작에 미치는 영향을 설명해 주세요. | signal/power integrity, resistance/RLC, static/dynamic droop, coupling, reflection, timing/noise margin |
| Q24 | 설계 검증과 CAE의 역할, coverage·모델·AI 사용의 한계를 설명해 주세요. | spec/DUT, reference/checker, assertion, code/functional coverage, regression, PDK/library/constraint, reproducibility |

## 4. 문항별 필수 키워드와 답변 골격

### 메모리 제품·동작

#### Q01. DRAM의 1T1C 구조와 읽기·쓰기·refresh를 물리적 원리와 연결해 설명해 주세요.

**필수 키워드:** access transistor, storage capacitor, WL/BL, Q=CV, charge sharing, sense amplifier, restore, leakage/refresh

1. **정의:** DRAM은 capacitor의 전하로 bit를 저장하는 휘발성 메모리이며 대표 cell은 1T1C입니다.
2. **원리:** WL이 access transistor를 제어하고 BL을 통해 충·방전합니다. Read에서는 precharge된 BL과 cell이 전하를 공유해 작은 전압 차이를 만들고 SA가 판별·복원합니다. 누설 때문에 접근하지 않은 cell도 refresh해야 합니다.
3. **사례·용도:** 주기억장치와 HBM core die에 사용합니다. 물성 질문이면 C≈εA/d, 유전체·면적·두께와 전하 보존을 연결합니다. 실제 capacitor는 입체 구조라 평판식은 직관용 근사입니다.
4. **Trade-off:** 작은 cell의 집적도 이점 ↔ 충분한 C·retention·sensing margin 확보. C를 키우면 신호 여유가 좋아질 수 있지만 면적·구조·공정 비용이 생깁니다. Refresh는 보존을 얻는 대신 시간·전력을 사용합니다.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] 1c LPDDR6 개발은 미세화와 고속·저전력을 함께 추구하는 사례입니다. 1c는 세대 명칭이며 cell capacitor 개수나 실제 1nm를 뜻하지 않습니다. [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/)

**변형 질문:** Refresh를 없애면? / 온도가 오르면? / C가 줄어들면 BL 신호는? / SA 없이 읽을 수 있나?

**오답 방지:** Read 후 restore와 주기적 refresh를 동일 동작으로만 설명하지 않기. DRAM의 누설을 한 경로·한 물성으로 단정하지 않기.

**원리 복습:** [B1: MIT DRAM 동작 강의](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/f342551f652653e3ee0d0c56a926efeb_9eWKuWyXYKY.pdf) [B2: Micron DRAM cell·미세화 설명](https://www.micron.com/about/blog/memory/dram/inside-1a-the-worlds-most-advanced-dram-process-technology) [B27: MIT capacitor·유전체 기본식](https://web.mit.edu/viz/EM/visualizations/notes/modules/capacitors.pdf)

#### Q02. NAND 플래시의 동작 원리와 DRAM의 차이를 설명해 주세요.

**필수 키워드:** charge storage layer, Vth, tunneling, read/program/erase, NAND string, page/block, nonvolatile, endurance

1. **정의:** NAND는 절연된 저장층의 전하가 바꾸는 Vth 상태로 데이터를 저장하는 비휘발성 메모리입니다.
2. **원리:** 대표적인 n-channel 설명에서 program으로 전자를 저장하면 Vth가 올라갑니다. Read는 기준 gate 전압에서 전류가 흐르는지를 판별하고 erase로 저장 상태를 초기화합니다. Floating gate와 charge trap 구현을 구분합니다.
3. **사례·용도:** SSD·UFS에 적용합니다. DRAM은 capacitor 전하를 읽고 복원·refresh하고, NAND는 저장층의 Vth 상태를 읽는다는 차이에서 출발합니다.
4. **Trade-off:** 직렬 string으로 접점 등을 공유해 집적도에 유리하지만 접근·동작 제약이 있습니다. 일반적으로 page read/program, block erase이며 DRAM식 작은 단위의 빠른 덮어쓰기에 불리합니다. Program/erase에는 내구성 비용도 있습니다.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] 3D는 이미 정착한 구조입니다. 2026년의 연결은 고적층·QLC와 성능·신뢰성의 균형이며, 321-layer QLC cSSD 공급 사례를 쓸 수 있습니다. [T2: SK하이닉스 321-layer QLC cSSD 공급 (2026-04-08)](https://news.skhynix.com/en/begin-supply-321-layer-qlc-nand-cssd-2/)

**변형 질문:** 왜 erase 후 program하나? / 선택하지 않은 string cell은 어떻게 지나가나? / TLC에서 0/1 판별은 어떻게 확장되나?

**오답 방지:** 직렬이라 셀 선택이 불가능하다고 말하지 않기. 선택 WL과 나머지 WL의 pass bias를 구분. Block erase를 직렬 구조 하나만으로 설명하지 않기.

**원리 복습:** [B3: KIOXIA NAND 저장·동작 원리](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html) [B4: KIOXIA page/block 동작과 latency](https://www.kioxia.com/en-jp/rd/technology/topics/topics-51.html)

#### Q03. HBM의 구조와 고대역폭을 얻는 원리, 설계상의 trade-off를 설명해 주세요.

**필수 키워드:** stacked DRAM, TSV, wide I/O, core/base die, interposer/package, bandwidth, heat, yield/power

1. **정의:** HBM은 DRAM die를 적층하고 넓은 I/O 경로를 사용하는 고대역폭 메모리입니다.
2. **원리:** TSV가 die 간 수직 연결을 제공하고, package의 연결을 통해 processor와 통신합니다. 적층은 용량과 통합에, 넓은 I/O와 data rate는 대역폭에 연결됩니다. Core die와 base die의 역할을 구분합니다.
3. **사례·용도:** AI accelerator가 많은 데이터를 이동할 때 사용합니다. Bandwidth=(총 data width×pin당 data rate)/8로 단위를 맞추며 실제 효율·access pattern을 따로 봅니다.
4. **Trade-off:** 폭·적층으로 bandwidth·capacity를 얻는 대신 package 복잡도·비용·적층 수율·전원/열 관리 부담이 생깁니다. HBM도 DRAM이라 refresh가 필요하며 high bandwidth와 low latency는 같은 말이 아닙니다.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] HBM4에서는 interface 확대와 함께 advanced-logic base die 및 memory·logic·package의 통합 최적화가 중요해집니다. [T1: SK하이닉스 HBM4 개발·양산 준비 발표 (2025-09-12)](https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

**변형 질문:** 적층만 늘리면 bandwidth도 늘까? / TSV는 데이터를 저장하나? / HBM과 3D NAND는 어떤 점이 다른가?

**오답 방지:** HBM을 SRAM 또는 3D NAND로 설명하지 않기. Core cell 자체가 모두 logic FinFET/GAA라고 일반화하지 않기.

**원리 복습:** [T1: SK하이닉스 HBM4 개발·양산 준비 발표 (2025-09-12)](https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

#### Q04. SRAM·DRAM·NAND를 cell 구조와 용도 관점에서 비교해 주세요.

**필수 키워드:** 6T, cross-coupled inverter, 1T1C, Vth storage, volatile, density, latency, cost/bit

1. **정의:** 세 메모리는 저장 상태를 유지하는 물리적 방법이 다릅니다.
2. **원리:** SRAM은 대표적으로 두 cross-coupled inverter의 상태를 6T cell로 유지하고, DRAM은 capacitor 전하, NAND는 절연 저장층의 전하에 따른 Vth 상태를 이용합니다.
3. **사례·용도:** SRAM은 cache·buffer, DRAM은 working memory, NAND는 persistent storage에 적용합니다.
4. **Trade-off:** SRAM의 빠른 접근 ↔ 큰 cell 면적. DRAM의 집적도 ↔ refresh. NAND의 비휘발성·용량 ↔ program/erase latency·endurance·접근 단위. 정확한 가격·성능 비교는 구현·조건에 따라 달라집니다.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] AI memory hierarchy에서 서로 대체하기보다 HBM·DRAM·SSD의 역할을 함께 최적화하는 방향으로 연결합니다. [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

**변형 질문:** 전원을 끄면 각각 왜 상태를 잃거나 유지하나? / SRAM은 왜 refresh가 필요 없나?

**오답 방지:** SRAM은 무조건 저전력이라고 단정하지 않기. 전체 chip 전력과 bit당 저장 구조를 구분.

**원리 복습:** [B1: MIT DRAM 동작 강의](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/f342551f652653e3ee0d0c56a926efeb_9eWKuWyXYKY.pdf) [B3: KIOXIA NAND 저장·동작 원리](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

#### Q05. DRAM sense amplifier와 precharge의 역할을 설명해 주세요.

**필수 키워드:** BL/BLB, VDD/2, charge sharing, positive feedback, restore, offset/noise, timing

1. **정의:** SA는 cell에서 생긴 작은 BL 전압 차이를 판별해 논리 수준으로 키우는 주변회로입니다.
2. **원리:** 대표 구조에서 BL을 중간 전압으로 precharge/equalize하고 WL을 켜면 전하 공유가 생깁니다. Cross-coupled 구조의 재생 작용이 차이를 증폭하며 cell을 복원합니다.
3. **사례·용도:** DRAM read·refresh에서 사용됩니다. ΔVBL은 Ccell/(Ccell+CBL)과 초기 전압 차이에 연결해 직관적으로 설명합니다.
4. **Trade-off:** 작은 Ccell·큰 CBL은 신호 여유를 줄일 수 있습니다. 빠른 sensing ↔ offset·noise·전력·면적의 조건을 확인하고 활성 타이밍을 설계해야 합니다.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 미세화·고속 제품에서도 작은 신호를 안정적으로 읽는 것이 설계 과제라는 해석을 덧붙입니다. 특정 최신 SA 구조를 확인 없이 이름 붙이지 않습니다.

**변형 질문:** Precharge 없이 바로 읽으면? / mismatch가 크면? / CBL이 커지면?

**오답 방지:** 재생형 SA를 선형 OP Amp와 동일하게 설명하지 않기.

**원리 복습:** [B1: MIT DRAM 동작 강의](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/f342551f652653e3ee0d0c56a926efeb_9eWKuWyXYKY.pdf) [B2: Micron DRAM cell·미세화 설명](https://www.micron.com/about/blog/memory/dram/inside-1a-the-worlds-most-advanced-dram-process-technology)

#### Q06. SLC·MLC·TLC·QLC와 3D NAND의 차이를 설명해 주세요.

**필수 키워드:** bits/cell, 2^b states, Vth distribution, read margin, program-verify, ECC, vertical stacking

1. **정의:** TLC/QLC는 cell당 bit 수, 3D NAND는 cell 배치 구조를 나타내는 별개 축입니다.
2. **원리:** b bit는 2^b개 상태가 필요해 TLC 8개·QLC 16개 Vth 상태를 구분합니다. Program-verify로 목표 범위에 맞추고 read reference로 판별합니다.
3. **사례·용도:** 고용량 SSD에 사용하며 layer 증가와 bit/cell 증가는 서로 다른 방식으로 용량을 확대합니다.
4. **Trade-off:** 같은 cell에서 더 많은 bit ↔ 좁은 판별 여유·정교한 program·ECC·endurance 관리. 적층 확대 ↔ 제조 난도·전기적 특성·수율 관리.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] SK하이닉스의 321-layer QLC cSSD는 두 축을 결합한 사례입니다. 층수·bit 수만으로 SSD 성능을 결론 내리지 않습니다. [T2: SK하이닉스 321-layer QLC cSSD 공급 (2026-04-08)](https://news.skhynix.com/en/begin-supply-321-layer-qlc-nand-cssd-2/)

**변형 질문:** QLC는 왜 TLC보다 상태 판별이 어렵나? / 층수가 두 배면 속도도 두 배인가?

**오답 방지:** QLC의 16상태를 16bit/cell로 혼동하지 않기.

**원리 복습:** [B5: KIOXIA 다중 상태 저장·program-verify](https://www.kioxia.com/en-jp/rd/technology/multi-level-cell.html) [T2: SK하이닉스 321-layer QLC cSSD 공급 (2026-04-08)](https://news.skhynix.com/en/begin-supply-321-layer-qlc-nand-cssd-2/)

#### Q07. DRAM row·column·bank와 timing 사양이 필요한 이유를 설명해 주세요.

**필수 키워드:** ACT, row buffer, READ/WRITE, PRE, bank, tRCD, tRAS, tRP

1. **정의:** 메모리 array는 row·column으로 주소를 조직화하고 bank 단위로 동작을 관리합니다.
2. **원리:** ACT로 row를 열어 sensing/restore하고 column 명령으로 데이터를 선택하며 PRE로 다음 row 접근을 준비합니다. 각 내부 동작 시간이 명령 간 제약으로 나타납니다.
3. **사례·용도:** Row-hit·row-conflict 접근 사례로 같은 외부 clock에서도 latency가 달라질 수 있음을 설명합니다.
4. **Trade-off:** Bank 병렬성은 처리량에 유리하지만 주변회로·전력·명령 제약이 늘고 모든 bank 동작을 무제약으로 겹칠 수는 없습니다.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 고대역폭 제품도 timing 제약·access pattern·controller scheduling을 함께 봐야 한다는 제품 성능 관점으로 연결합니다.

**변형 질문:** tRCD/tRP를 무리하게 줄이면? / 주파수를 올리면 모든 latency가 줄어드나?

**오답 방지:** tRCD는 ACT→READ/WRITE, tRP는 PRE→다음 ACT, tRAS는 최소 active 기간으로 구분.

**원리 복습:** [B6: Microchip DDR timing 설명](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html)

#### Q08. MBIST·BISR·ECC는 무엇이며 어떻게 다른가요?

**필수 키워드:** built-in test, March, fault model, redundancy/repair, syndrome, correction limit

1. **정의:** MBIST는 test, BISR는 repair, ECC는 데이터 오류 검출·정정입니다.
2. **원리:** Test pattern과 기대값을 비교해 fault를 찾고 redundancy로 불량 자원을 대체할 수 있습니다. ECC는 정보에 check bit를 더해 code의 능력 범위에서 오류를 처리합니다.
3. **사례·용도:** 내장 memory의 test/repair와 메모리·storage 데이터 보호에 적용합니다.
4. **Trade-off:** 검출·복구 능력을 얻는 대신 test 시간·spare 면적·check bit·decoder latency가 생깁니다. ECC가 모든 고장을 고치거나 원인을 없애지는 못합니다.
5. **최신 동향·현재 제품과의 연결:** [제품 연결] 고용량·복잡한 memory 제품의 품질은 circuit뿐 아니라 test·repair·data protection과 연결된다는 관점으로 마무리합니다.

**변형 질문:** ECC만 있으면 MBIST가 필요 없나? / March는 모든 fault를 찾나?

**오답 방지:** 알고리즘별 fault coverage와 code별 정정 능력을 구분.

**원리 복습:** [B7: Synopsys embedded memory test·repair](https://www.synopsys.com/implementation-and-signoff/test-automation/synopsys-ip-sms.html)

#### Q09. DDR·LPDDR·GDDR·HBM은 어떻게 다르고 설계 목표는 무엇인가요?

**필수 키워드:** DRAM family, bandwidth, energy/bit, pin rate/width, capacity, package, workload

1. **정의:** 모두 DRAM 기반 제품군이지만 interface·package·목표 workload가 다릅니다.
2. **원리:** Bandwidth를 폭과 전송률로 나누어 설명하고, LPDDR는 저전력 동작·전원 관리, HBM은 넓은 연결과 적층이라는 구현 차이를 짚습니다.
3. **사례·용도:** DDR는 시스템 주메모리, LPDDR는 모바일 등 전력 제약 환경, GDDR는 graphics, HBM은 AI/HPC의 대역폭 요구에 연결합니다.
4. **Trade-off:** Bandwidth·capacity·energy/bit·비용·package 조건을 함께 비교해야 하며 한 제품이 모든 환경에 최적은 아닙니다.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] 1c LPDDR6의 고속·저전력 개발과 HBM4의 memory/logic 통합을 서로 다른 목표의 사례로 제시합니다. [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

**변형 질문:** HBM이 빠른데 왜 모든 시스템에 쓰지 않나? / 저전력과 낮은 총전력은 같은 뜻인가?

**오답 방지:** 표준 속도·배점·시장 수치를 기억만으로 말하지 않기.

**원리 복습:** [T1: SK하이닉스 HBM4 개발·양산 준비 발표 (2025-09-12)](https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/) [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

### 소자·회로 기초

#### Q10. MOSFET의 동작영역과 analog/digital에서 사용하는 방식을 설명해 주세요.

**필수 키워드:** VGS/VDS/Vth, cutoff/triode/saturation, channel, bias, gm, leakage

1. **정의:** Gate가 채널의 전도 상태를 조절하는 소자입니다.
2. **원리:** 긴 채널 NMOS 모델에서 VGS와 VDS를 Vth·overdrive와 비교해 영역을 구분하고, saturation에서도 전류가 흐름을 설명합니다.
3. **사례·용도:** Digital switching과 analog bias/증폭에 쓰입니다. MOS saturation과 amplifier 출력 포화는 다른 용어입니다.
4. **Trade-off:** 구동을 높이는 전압·sizing 선택 ↔ capacitance·전력·headroom·누설 비용을 봅니다.
5. **최신 동향·현재 제품과의 연결:** [기술 방향] 미세 소자에서는 긴 채널 모델만으로 성능을 설명하기 어려워 SCE와 공정 모델이 필요하다는 방향으로 연결합니다.

**변형 질문:** Saturation이면 전류가 멈추나? / PMOS의 부호는 어떻게 해석하나?

**오답 방지:** Cutoff 전류가 정확히 0이라고 말하지 않기.

**원리 복습:** [B8: MIT MOSFET I–V](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/908ce7edc329bf6d8a628d8a2b1cb3c9_MIT6_012S09_rec09.pdf)

#### Q11. Short-channel effect와 미세화의 trade-off를 설명해 주세요.

**필수 키워드:** gate control, Vth roll-off, DIBL, subthreshold leakage, velocity saturation, reliability, FinFET/GAA

1. **정의:** 채널이 짧아지면서 source/drain 전기장이 gate의 제어에 더 큰 영향을 주는 현상입니다.
2. **원리:** DIBL은 높은 drain 전압이 source 쪽 장벽을 낮추는 효과입니다. 고전계의 velocity saturation도 함께 구분해 긴 채널 전류식의 한계를 설명합니다.
3. **사례·용도:** 소자의 누설·구동·timing·analog gain·장기 신뢰성 판단에 쓰는 기초입니다.
4. **Trade-off:** 작은 소자의 집적 이점 ↔ 누설·특성 변화·설계 여유 관리. 낮은 Vth는 구동에 유리할 수 있지만 standby leakage 비용이 있습니다.
5. **최신 동향·현재 제품과의 연결:** [기술 방향] FinFET·GAA의 여러 면 gate 제어를 완화 방향으로 이해합니다. SK하이닉스의 모든 memory cell이 그 구조라고 일반화하지 않습니다.

**변형 질문:** DIBL과 CLM은 같은가? / L을 줄이면 전류가 무조건 1/L로 증가하나?

**오답 방지:** Body effect·CLM·gate tunneling을 전부 SCE 하나로 뭉뚱그리지 않기.

**원리 복습:** [B9: 대학 short-channel MOSFET 강의](https://www.eecis.udel.edu/~vsaxena/courses/ece515/f18/Lecture%20Notes/MOSFET_SCE.pdf) [B10: TU Delft MOS 소자 모델](https://analog-electronics.tudelft.nl/webbook/SED/_build/html/ModelingActiveDevices/ActiveDevices_MOS_transistors.html)

#### Q12. CMOS inverter의 동작과 sizing·delay·power 관계를 설명해 주세요.

**필수 키워드:** pull-up/down, PMOS/NMOS, CL, tPLH/tPHL, noise margin, αCV²f, leakage

1. **정의:** 상보 PMOS/NMOS로 입력 논리를 반전하는 기본 회로입니다.
2. **원리:** 입력이 낮으면 pull-up, 높으면 pull-down하며 출력 C의 충·방전으로 delay가 생깁니다. 전환 중 두 소자가 함께 도통할 수도 있습니다.
3. **사례·용도:** Logic gate·buffer chain의 출발점이며 큰 부하를 구동할 때 sizing·단계화를 검토합니다.
4. **Trade-off:** Width 증가의 drive 이점 ↔ 입력·기생 C·면적·전력 증가. 낮은 VDD의 switching power 이점 ↔ timing·noise 조건.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 고속·저전력 memory 요구를 drive·load·전압 trade-off로 연결하고 새로운 inverter 기술을 임의로 최신이라 말하지 않습니다.

**변형 질문:** PMOS는 왜 더 크게 잡는 경우가 있나? / 부하를 두 배로 하면? / rise time과 propagation delay는?

**오답 방지:** 전체 경로는 앞단의 부하까지 보며 한 gate만 커지면 항상 빨라진다고 말하지 않기.

**원리 복습:** [B11: MIT CMOS delay](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/de333d22ec4230412f4e7bdd4da3d6ce_MIT6_012S09_lec13.pdf)

#### Q13. PVT corner와 mismatch가 회로에 미치는 영향을 설명해 주세요.

**필수 키워드:** process/voltage/temperature, global/local variation, corner, Monte Carlo, delay/leakage/offset

1. **정의:** PVT는 동작·공정 조건의 변화, mismatch는 소자 간 국부 차이입니다.
2. **원리:** 모델·전압·온도 변화로 전류·Vth·delay가 변하고, mismatch로 대칭 회로의 offset 등이 생깁니다. Corner와 통계적 분석의 역할을 구분합니다.
3. **사례·용도:** Timing closure와 sensing·차동회로의 margin/yield 검토에 사용합니다.
4. **Trade-off:** 넓은 조건에서 안정 동작 ↔ sizing·전력·margin·검증 비용. 과도한 worst-case 설계도 비용이 있습니다.
5. **최신 동향·현재 제품과의 연결:** [설계 방향] 제품 고속화·저전력화의 효익을 검증할 때 nominal 수치보다 조건 전체의 동작 여유를 봐야 한다는 해석을 제시합니다.

**변형 질문:** Typical만 통과하면 충분한가? / 온도가 높으면 언제나 느린가?

**오답 방지:** Corner 통과와 모든 mismatch/yield 보장을 동일시하지 않기.

**원리 복습:** [B10: TU Delft MOS 소자 모델](https://analog-electronics.tudelft.nl/webbook/SED/_build/html/ModelingActiveDevices/ActiveDevices_MOS_transistors.html) [B16: TI OP Amp 강의](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html)

### 아날로그·주파수

#### Q14. Small-signal model은 무엇이며 왜 bias가 필요한가요?

**필수 키워드:** DC operating point, linearization, gm, ro/gmb, dependent source, Cgs/Cgd, validity

1. **정의:** 비선형 소자를 DC 동작점 주변에서 선형 근사해 변화량을 해석하는 모델입니다.
2. **원리:** 먼저 bias를 구하고 미분으로 gm·go를 정의해 전류원·저항으로 바꿉니다. 고주파에서는 capacitance를 포함하며 종속원을 제거하지 않습니다.
3. **사례·용도:** 증폭기의 gain·입출력 저항·주파수 응답 해석에 사용합니다.
4. **Trade-off:** 간단한 선형 분석 ↔ 큰 입력의 clipping·slewing 등에는 근사가 깨질 수 있습니다. Small-signal은 low-frequency와 같은 뜻이 아닙니다.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 실제 설계는 공정 모델의 AC·transient 결과와 해석을 대조합니다. 별도 최신기술 주장 대신 고속 회로에서 기생성분을 포함해야 함을 연결합니다.

**변형 질문:** Q점이 바뀌면 gm은? / DC 전압원과 전류원은 소신호에서 어떻게 처리하나?

**오답 방지:** MOSFET 그 자체를 완전한 선형 소자라고 설명하지 않기.

**원리 복습:** [B12: MIT small-signal 모델](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/ce96d1ec5951846e0d1240383b10d8af_lec11.pdf)

#### Q15. Common-source·source follower와 current mirror의 역할을 설명해 주세요.

**필수 키워드:** inverting gain, gm·Rout, input/output resistance, buffer, reference current, compliance/headroom

1. **정의:** CS는 전압 증폭, follower는 buffer, mirror는 bias 전류 복제에 쓰는 기본 구조입니다.
2. **원리:** CS의 gm 전류 변화가 출력 저항에서 전압으로 바뀌고, follower는 source가 gate 변화를 따라갑니다. Mirror는 기준 가지의 VGS와 비율을 활용합니다.
3. **사례·용도:** Gain stage·출력 buffer·증폭기 bias에 적용합니다. 하나만 묻는 질문이면 해당 구조를 중심으로 나머지는 비교에만 씁니다.
4. **Trade-off:** 큰 gain ↔ bandwidth/headroom, 낮은 출력 저항 ↔ bias 전류, 정확한 mirror ↔ 면적·전압 여유·mismatch 관리.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 속도·전력·동작 범위를 함께 최적화하는 기본 block이라는 설명으로 마무리합니다.

**변형 질문:** CS의 RD를 크게 하면 항상 좋은가? / Mirror는 모든 출력 전압에서 동작하나?

**오답 방지:** 근사식을 쓸 때 ro·부하·동작영역을 명시.

**원리 복습:** [B13: MIT common-source 증폭기](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/7a51249eb734152c5ce95df393cf4f1f_lec19.pdf)

#### Q16. Differential amplifier의 원리와 common-mode rejection을 설명해 주세요.

**필수 키워드:** vd=v1−v2, vcm=(v1+v2)/2, differential pair, tail current, Ad/Ac, CMRR, offset/mismatch

1. **정의:** 두 입력의 차이를 증폭하고 공통 성분의 영향을 줄이는 회로입니다.
2. **원리:** Tail current를 공유하는 pair에서 입력 차이가 전류 분배를 바꿉니다. 두 입력을 동시에 올리는 common-mode 변화와 차동 변화는 다르며 입력 범위도 확인합니다.
3. **사례·용도:** OP Amp 입력단·차동 수신·작은 전압 차이 검출에 활용합니다. DRAM sensing과는 차이 검출이라는 목적을 연결하되 선형 회로와 재생형 SA를 구분합니다.
4. **Trade-off:** 공통 noise 억제 ↔ 두 경로·bias·headroom·matching 부담. 유한 tail resistance·mismatch는 common-mode 영향·offset을 만듭니다.
5. **최신 동향·현재 제품과의 연결:** [제품 적용] 작은 신호·고속 interface를 안정적으로 다루는 제품 요구에 연결합니다. Differential이라는 이유만으로 모든 noise가 제거되지는 않습니다.

**변형 질문:** 두 입력을 같이 올리면 출력은? / CMRR은 무엇의 비인가? / 공통 noise는 왜 항상 없어지지 않나?

**오답 방지:** CMRR=|Ad/Ac|, dB는 20log10. Differential input과 differential output 구분.

**원리 복습:** [B14: MIT differential amplifier](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/9932f87a7b5ec3d088d0e0836a05c622_MIT6_012F09_lec19.pdf)

#### Q17. OP Amp의 동작과 negative feedback·virtual short를 설명해 주세요.

**필수 키워드:** AOL, differential input, negative feedback, ACL, virtual short, input/output range, saturation

1. **정의:** 입력 전압 차이를 큰 open-loop gain으로 증폭하는 회로입니다.
2. **원리:** Vout=AOL(v+−v−)에서 negative feedback이 오차를 줄입니다. 충분한 gain과 선형 동작 조건에서 v+≈v−로 근사하며 실제 short는 아닙니다.
3. **사례·용도:** 반전·비반전 증폭·buffer·active filter에 쓰며 간단한 gain 식 하나를 조건과 함께 제시합니다.
4. **Trade-off:** Feedback의 gain 정확도·선형성 이점 ↔ 유한 bandwidth·stability·출력/입력 범위. 실제 offset·noise·bias current도 오차가 됩니다.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 회로 속도·정확도·저전력 요구에 맞춰 finite gain·부하·전압 여유를 함께 봅니다. 최신 OP Amp 구조를 확인 없이 붙이지 않습니다.

**변형 질문:** Open-loop에서 virtual short를 써도 되나? / 출력 rail에 붙으면? / Comparator와 차이는?

**오답 방지:** Negative feedback이면 언제나 선형·안정하다고 말하지 않기.

**원리 복습:** [B15: MIT OP Amp 구성·제약](https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/resources/lecture_12/) [B16: TI OP Amp 강의](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html)

#### Q18. 증폭기의 주파수 응답·GBW·slew rate·안정성을 설명해 주세요.

**필수 키워드:** H(jω), pole/zero, Bode, −3dB, Miller, noise gain, slew rate, loop gain/phase margin

1. **정의:** 주파수 응답은 주파수별 gain·phase이고, slew rate는 큰 신호의 출력 변화율 한계입니다.
2. **원리:** RC·기생 C가 pole을 만들며 Miller effect가 입력 부하에 영향을 줍니다. 단일 dominant-pole voltage-feedback OP Amp의 BW≈GBW/noise gain 근사는 조건부입니다.
3. **사례·용도:** 부하 C 증가나 큰 진폭 사인파에서 응답이 달라지는 예를 사용합니다.
4. **Trade-off:** 높은 gain·낮은 전력 ↔ bandwidth·settling·drive/stability 조건. 보상은 안정성을 얻는 대신 속도 등에 비용이 있습니다.
5. **최신 동향·현재 제품과의 연결:** [기초의 제품 적용] 고속 interface·bias 회로의 속도와 안정성 조건으로 연결합니다. 독립적인 최신 뉴스가 없는 기본 원리에는 동향을 억지로 만들지 않습니다.

**변형 질문:** 작은 신호는 되는데 큰 신호만 왜곡되면? / Feedback인데 왜 발진하나? / Phase margin은 어느 plot에서?

**오답 방지:** 1개 질문이 GBW라면 GBW와 SR 비교를 주력으로, 안정성 질문이면 loop gain을 주력으로. 모든 키워드를 3분에 나열하지 않기.

**원리 복습:** [B17: MIT 주파수 응답·Miller effect](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/44ed13d9b5e46dd459d9bca431fc547a_lec23.pdf) [B18: TI feedback 안정성](https://www.ti.com/document-viewer/lit/html/SSZT093/GUID-E77AE2AF-5CB9-404C-92A2-222AA9AF2FE8)

### 디지털·timing

#### Q19. Setup·hold·slack·critical path와 timing 위반 대응을 설명해 주세요.

**필수 키워드:** launch/capture, setup/hold, arrival/required, slack, skew, constraint, max/min path

1. **정의:** Clock edge 주변에 data가 안정되어야 하는 조건이며 slack은 그 조건의 여유입니다.
2. **원리:** Setup은 늦은 도착, hold는 너무 이른 변화와 연결합니다. Setup slack=required−arrival, hold slack=arrival−required로 부호 방향을 구분합니다.
3. **사례·용도:** Register→logic→register 경로에서 clock·data delay를 나누어 보며 합성·배치 후 STA에 사용합니다.
4. **Trade-off:** Pipeline·sizing·buffer·배선 수정은 timing을 개선하지만 면적·전력·latency 또는 다른 경로에 비용을 줄 수 있습니다.
5. **최신 동향·현재 제품과의 연결:** [제품 적용] 고속 메모리 logic/base die에서도 단순 주파수 목표뿐 아니라 PVT·배선·clock 조건에서 timing closure가 필요하다는 해석으로 연결합니다.

**변형 질문:** Clock을 느리게 하면 hold도 해결되나? / 가장 gate가 많은 경로가 critical path인가?

**오답 방지:** Hold를 period 증가만으로 해결하지 않기. 잘못된 constraint를 회로 실패와 혼동하지 않기.

**원리 복습:** [B19: Synopsys STA](https://www.synopsys.com/glossary/what-is-static-timing-analysis.html)

#### Q20. Pipeline과 저전력 기법을 PPA trade-off로 설명해 주세요.

**필수 키워드:** throughput/latency, stage/register, αCV²f, leakage, clock/power gating, retention/isolation, DVFS

1. **정의:** Pipeline은 경로를 단계로 나누며 저전력 기법은 불필요한 switching·leakage 또는 전압/주파수를 줄입니다.
2. **원리:** Pipeline은 단계 조합 지연을 줄이지만 register·clock 부하를 더합니다. Clock gating은 clock switching, power gating은 공급 차단, DVFS는 동작점 변경입니다.
3. **사례·용도:** 처리량 목표가 있는 datapath와 idle mode가 많은 블록을 예로 듭니다.
4. **Trade-off:** 높은 throughput ↔ latency·area·clock power, power-off ↔ state 보존·wake-up·isolation 비용. 낮은 VDD ↔ timing 여유 감소.
5. **최신 동향·현재 제품과의 연결:** [제품 동향] LPDDR6 발표의 DVFS·저전력 목표를 실제 적용 사례로 연결할 수 있습니다. 모든 IC가 동일한 방식으로 동작한다고 확대하지 않습니다. [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/)

**변형 질문:** Pipeline이면 모든 작업이 빨라지나? / Clock gating이 leakage도 끊나?

**오답 방지:** Performance가 주파수·throughput·latency 중 무엇인지 먼저 정하기.

**원리 복습:** [B20: Cadence low-power 기법](https://resources.system-analysis.cadence.com/power-integrity/msa2021-low-power-design-techniques-for-power-integrity-in-vlsi) [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/)

#### Q21. Metastability와 CDC의 원리·대응을 설명해 주세요.

**필수 키워드:** asynchronous input, setup/hold, resolution time, MTBF, synchronizer, pulse/bus, handshake/FIFO

1. **정의:** Clock과 맞지 않는 신호를 받을 때 저장 소자가 즉시 안정 논리값을 결정하지 못할 수 있습니다.
2. **원리:** Synchronizer는 충분한 해결 시간을 주어 다음 단계 실패 확률을 낮춥니다. 제거를 보장하지는 않습니다.
3. **사례·용도:** 서로 다른 clock domain이나 외부 입력에서 단일 level·pulse·multi-bit transfer를 구분합니다.
4. **Trade-off:** 동기화 신뢰성 ↔ latency·회로 비용. 2FF는 단일 level의 대표 방식이며 짧은 pulse·bus에는 별도 전달 protocol이 필요합니다.
5. **최신 동향·현재 제품과의 연결:** [설계 적용] 여러 clock/mode가 있는 제품에서 전달 사양과 검증을 함께 설계하는 관점으로 연결합니다.

**변형 질문:** 각 bus bit에 2FF를 달면 충분한가? / 주파수를 올리면 확률은 어떻게 달라질까?

**오답 방지:** MTBF 개선과 실패 가능성 0을 동일시하지 않기.

**원리 복습:** [B21: Intel metastability·CDC](https://cdrdv2-public.intel.com/650346/wp-01082-quartus-ii-metastability.pdf)

### 물리 구현·검증·환경

#### Q22. 회로/RTL에서 layout까지 흐름과 DRC·LVS·기생 추출을 설명해 주세요.

**필수 키워드:** schematic/RTL, synthesis/netlist, floorplan/placement/CTS/routing, DRC, LVS, PEX, sign-off

1. **정의:** 기능·회로 정의를 실제 소자 위치·배선으로 구현하고 여러 조건을 검증하는 과정입니다.
2. **원리:** Digital 구현과 custom schematic→layout의 차이를 짚고, DRC는 공정 규칙, LVS는 연결·소자 일치, PEX는 기생성분 추출임을 설명합니다.
3. **사례·용도:** Pre/post-layout 비교에서 배선 RC로 delay·waveform·coupling이 달라지는 사례를 듭니다.
4. **Trade-off:** 배치·배선 최적화로 PPA를 얻지만 혼잡·기생·검증·제조 규칙 제약이 있습니다.
5. **최신 동향·현재 제품과의 연결:** [제품 적용] HBM의 memory/logic/package 통합 요구는 블록 내부뿐 아니라 연결과 조건까지 검증할 필요를 보여주는 사례입니다. [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

**변형 질문:** LVS 통과면 기능도 맞나? / MOS 소자 배치와 standard-cell P&R은 무엇이 다른가?

**오답 방지:** DRC/LVS를 functional simulation 또는 timing sign-off로 설명하지 않기.

**원리 복습:** [B22: Synopsys DRC](https://www.synopsys.com/glossary/what-is-design-rule-checking.html) [B23: Synopsys LVS](https://www.synopsys.com/glossary/what-is-layout-versus-schematic-checking.html) [B24: Synopsys parasitic extraction](https://www.synopsys.com/glossary/what-is-parasitic-extraction.html)

#### Q23. SI·PI·IR drop·crosstalk가 회로 동작에 미치는 영향을 설명해 주세요.

**필수 키워드:** signal/power integrity, resistance/RLC, static/dynamic droop, coupling, reflection, timing/noise margin

1. **정의:** SI는 신호가 요구 파형·timing으로 도착하는지, PI는 필요한 공급 전압이 유지되는지의 문제입니다.
2. **원리:** 전원 저항의 I·R 전압강하와 transient의 RLC 동작, 신호 간 coupling·impedance 불연속을 구분합니다.
3. **사례·용도:** 동시 switching·큰 부하 변화에서 전원/신호가 흔들려 delay·판별 margin이 줄어드는 사례를 듭니다.
4. **Trade-off:** 더 강한 전원망·decap·spacing으로 여유를 얻는 대신 면적·routing·비용 등 제약이 생깁니다.
5. **최신 동향·현재 제품과의 연결:** [제품 적용] 넓고 빠른 I/O와 적층 package에서는 die·package·board의 전원/신호 조건을 함께 보는 중요성을 HBM 구조와 연결합니다. [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

**변형 질문:** Nominal VDD는 맞는데 왜 fail하나? / IR drop과 모든 transient droop는 같은가?

**오답 방지:** SI는 signal/noise, PI는 전원으로 시작하되 서로 timing에 영향을 주는 연결을 설명.

**원리 복습:** [B25: Cadence PI 분석](https://www.cadence.com/en_US/home/resources/white-papers/how-to-achieve-10x-faster-power-integrity-analysis-and-signoff-wp.html)

#### Q24. 설계 검증과 CAE의 역할, coverage·모델·AI 사용의 한계를 설명해 주세요.

**필수 키워드:** spec/DUT, reference/checker, assertion, code/functional coverage, regression, PDK/library/constraint, reproducibility

1. **정의:** Verification은 설계가 사양을 만족하는지 확인하고 CAE는 도구·모델·환경·방법론을 구축합니다.
2. **원리:** Reference로 기대값을 정하고 scenario·assertion·coverage로 확인 범위를 관리합니다. Model·constraint 자체의 오류도 검토해야 합니다.
3. **사례·용도:** C/System model과 RTL 검증, 설계 환경 버전 관리·자동 regression의 사례를 듭니다.
4. **Trade-off:** 더 넓은 검증·정확도 ↔ runtime·구축 비용. 높은 code coverage도 functional correctness를 보장하지 않습니다.
5. **최신 동향·현재 제품과의 연결:** [확인된 방향] 회사는 설계 자동화·data/AI 최적화를 공개해 왔습니다. 아래 회사 자료는 2022년 설명이며 최신 조직 운영을 확정하는 근거가 아닙니다. AI 결과도 사양·검증 근거로 확인한다는 준비 관점으로 연결합니다. [T5: SK하이닉스 설계 자동화·data/AI 설명 (2022-10-06)](https://news.skhynix.com/en/quality-design-new-deal/)

**변형 질문:** AI RTL이 simulation을 통과하면 충분한가? / PDK·library·constraint 차이는?

**오답 방지:** UVM은 언어 자체가 아닌 검증 방법론. AI의 자동 생성과 sign-off 책임을 혼동하지 않기.

**원리 복습:** [B26: Accellera UVM](https://www.accellera.org/community/uvm) [T5: SK하이닉스 설계 자동화·data/AI 설명 (2022-10-06)](https://news.skhynix.com/en/quality-design-new-deal/)

## 5. 먼저 녹화할 메모리 답변 예시 3개

아래 문단은 5단계가 어떻게 연결되는지 보여주는 초안입니다. 말속도와 설명 깊이에 따라 시간이 달라집니다. 실제 3분은 직접 녹화해 확인합니다. 문장을 통째로 외우기보다 동작 순서와 인과관계를 기억합니다.

### 예시 A. DRAM — 구조·물성에서 refresh까지

DRAM은 capacitor에 저장된 전하로 데이터를 표현하는 휘발성 메모리입니다. 대표 cell은 하나의 access transistor와 하나의 capacitor로 이루어진 1T1C 구조이며, transistor는 접근을 제어하고 capacitor가 상태를 저장합니다.

Write에서는 word line으로 transistor를 켜고 bit line을 통해 capacitor를 충전하거나 방전합니다. Read에서는 미리 준비한 bit line과 cell이 연결돼 전하를 공유합니다. Bit line에도 capacitance가 있으므로 cell의 값이 큰 전압으로 바로 전달되는 것이 아니라 작은 전압 차이로 나타나고, sense amplifier가 이를 판별해 증폭합니다. 읽는 과정이 저장 상태를 교란하기 때문에 값을 복원해야 합니다. 또 접근하지 않은 cell도 누설로 전하가 줄어들기 때문에 주기적인 refresh가 필요합니다. 이것이 읽은 뒤 restore와 refresh를 구분해야 하는 이유입니다.

물성 측면에서는 Q=CV이므로 저장 capacitance와 전압이 전하량에 연결됩니다. Capacitance는 유전율·유효 면적·유전체 두께에 영향을 받습니다. 면적이 줄어도 충분한 C를 유지하기 위해 입체 구조와 재료를 고려할 수 있지만, 얇은 막을 무조건 쓰면 누설·신뢰성 제약도 함께 봐야 합니다. Access transistor 역시 켜졌을 때의 구동과 꺼졌을 때의 누설이 모두 중요합니다.

이 구조는 작은 cell로 대용량 working memory를 구현하는 데 유리해 주메모리와 HBM에 사용됩니다. 대신 refresh에 시간·전력을 사용하고 sensing margin도 확보해야 합니다. 따라서 집적도만 높이는 것이 아니라 capacitor·누설·주변회로·timing을 함께 설계해야 합니다. 최근 1c LPDDR6 개발처럼 제품 방향도 미세화와 고속·저전력을 함께 추구합니다. 즉 DRAM의 핵심은 작은 전하를 빠르고 안정적으로 보존하고 판별하는 것입니다.

근거·확장: [B1: MIT DRAM 동작 강의](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/f342551f652653e3ee0d0c56a926efeb_9eWKuWyXYKY.pdf) [B2: Micron DRAM cell·미세화 설명](https://www.micron.com/about/blog/memory/dram/inside-1a-the-worlds-most-advanced-dram-process-technology) [B27: MIT capacitor·유전체 기본식](https://web.mit.edu/viz/EM/visualizations/notes/modules/capacitors.pdf) [T3: SK하이닉스 1c LPDDR6 개발 (2026-03-10)](https://news.skhynix.com/en/1c-lpddr6-development-2026/)

### 예시 B. NAND와 DRAM — 저장 원리에서 용도까지

NAND는 절연된 전하 저장층의 상태가 바꾸는 문턱전압으로 데이터를 보존하는 비휘발성 메모리입니다. DRAM이 capacitor 전하를 저장하는 것과 달리, NAND는 저장 전하가 transistor의 켜지는 조건을 바꾼다는 점이 핵심입니다.

대표적인 n-channel 설명에서는 program 시 높은 전계로 전자를 저장층에 넣어 문턱전압을 높이고, erase는 저장 상태를 초기화합니다. Read는 정해진 gate 전압에서 전류가 흐르는지를 sensing해 상태를 구분합니다. 실제 저장층은 floating gate 또는 charge trap 등으로 구현되므로 모든 NAND를 같은 단면으로 설명하지는 않겠습니다. TLC·QLC는 문턱전압을 여러 범위로 나눠 한 cell에 여러 bit를 저장합니다.

여러 cell을 직렬 string으로 연결하면 접점과 배선을 공유해 집적도에 유리합니다. Read에서는 선택 cell을 판별하면서 나머지 cell에 pass bias를 주어 전류 경로를 만듭니다. 그러므로 cell을 전혀 선택할 수 없는 것이 아니라, array 구조와 주변회로·bias 조건에 맞춘 접근이 필요합니다. 일반적인 동작 단위는 page read/program과 block erase이며, block erase를 직렬 연결 하나만의 결과로 단정하지는 않겠습니다.

Trade-off는 비휘발성과 높은 저장 밀도를 얻는 대신 program/erase 시간·접근 단위·반복 동작의 내구성을 관리해야 한다는 것입니다. 이 때문에 NAND는 SSD·UFS 같은 저장장치에 적합하고, DRAM은 refresh가 필요해도 잦은 빠른 read/write가 필요한 주메모리에 적합합니다. 용도가 다르다는 결론은 저장 원리와 동작 제약에서 나옵니다.

현재 3D NAND는 이미 정착한 구조이며 고적층·QLC를 통해 용량을 높이면서 판별 여유·성능·신뢰성을 확보하는 것이 중요합니다. SK하이닉스의 321-layer QLC cSSD 공급은 그 방향을 보여주는 사례입니다. 집적도 숫자뿐 아니라 실제 제품의 접근 성능과 데이터 신뢰성까지 연결해 이해해야 합니다.

근거·확장: [B3: KIOXIA NAND 저장·동작 원리](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html) [B4: KIOXIA page/block 동작과 latency](https://www.kioxia.com/en-jp/rd/technology/topics/topics-51.html) [B5: KIOXIA 다중 상태 저장·program-verify](https://www.kioxia.com/en-jp/rd/technology/multi-level-cell.html) [T2: SK하이닉스 321-layer QLC cSSD 공급 (2026-04-08)](https://news.skhynix.com/en/begin-supply-321-layer-qlc-nand-cssd-2/)

### 예시 C. HBM — bandwidth를 구조로 설명하기

HBM은 여러 DRAM die를 적층하고 넓은 데이터 경로를 사용하는 고대역폭 메모리입니다. 데이터 저장은 DRAM 원리에 기반하므로 cell의 전하 보존·refresh가 필요하다는 점은 일반 DRAM과 같습니다.

구조적으로 저장을 담당하는 core die와 interface·logic 역할을 담당하는 base die를 구분하며, die 간 수직 연결에 TSV를 사용합니다. 외부 processor와의 연결에는 package의 배선 구조도 중요합니다. 적층은 작은 설치 면적에 capacity를 확보하는 데 연결되고, bandwidth는 넓은 data I/O와 pin당 data rate가 함께 결정합니다. 따라서 die를 더 쌓는 것과 I/O 폭을 늘리는 것은 같은 의미가 아닙니다.

원리를 숫자로 보면 이론 bandwidth는 총 유효 data width와 data rate를 곱한 뒤 byte 단위로 바꾸면 됩니다. 많은 병렬 경로로 데이터를 옮기므로 한 pin의 속도만 높이는 것과 다른 방식으로 대역폭을 확보합니다. 그러나 실제 성능은 명령·refresh·access pattern·controller 효율에 영향을 받으므로 이론값과 항상 같지는 않습니다.

AI accelerator에서는 많은 데이터를 계산기에 공급해야 하므로 이 구조가 memory bandwidth 병목을 줄이는 데 도움이 됩니다. 대신 적층 die의 열을 빼내고, 많은 연결에 전원을 안정적으로 공급하며, die와 package 수율을 확보해야 합니다. 높은 bandwidth·capacity를 얻는 대신 열·SI/PI·test·package 비용과 난도가 높아지는 것입니다. 높은 bandwidth가 곧 모든 접근의 낮은 latency를 뜻하지도 않습니다.

최근 HBM4에서는 넓은 interface뿐 아니라 advanced logic process를 적용한 base die와 memory·logic·package·고객 시스템의 통합 최적화가 중요해지고 있습니다. 설계 관점에서는 cell·주변회로만 따로 보는 것이 아니라 interface timing과 power·thermal 조건까지 함께 이해해야 합니다.

근거·확장: [T1: SK하이닉스 HBM4 개발·양산 준비 발표 (2025-09-12)](https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/) [T4: SK하이닉스 memory·logic·package 통합 방향 (2026-07-08)](https://news.skhynix.com/en/hbm-to-essd/)

## 6. 전달된 NAND 예시에서 보완한 부분

'구조 → trade-off → 용도'로 설명하는 방향은 그대로 사용합니다. 다음은 과도한 단순화를 피하기 위한 보완입니다.

- **셀 선택:** 직렬 string에서도 선택 WL과 나머지 WL의 pass bias로 선택 cell을 읽습니다. '특정 cell을 아예 선택할 수 없다'와 '제품의 접근 단위가 page다'를 구분합니다.
- **Read/program/erase 단위:** page read/program과 block erase를 구분합니다. Block erase는 array의 공유 구조·erase bias 조건과 연결되며 직렬이라는 사실 하나만으로 전부 설명하지 않습니다. Host에 보이는 byte/LBA 접근과 내부 array 동작 단위도 다릅니다.
- **상태와 bit:** SLC의 단순 높은/낮은 Vth 설명을 TLC·QLC에서는 여러 Vth 분포의 판별로 확장합니다. 특정 상태의 bit mapping을 보편적인 하나의 규칙으로 외우지 않습니다.
- **최신 동향:** 3D 전환이라는 설명은 배경이고, 2026년에 붙일 구체 사례는 고적층·QLC 제품과 성능·신뢰성입니다.
- **채용 인원:** 전달 자료의 '6월 설계를 가장 많이 채용'은 별도 확인하지 않았으며 문항 우선순위나 채용 규모 사실로 채택하지 않았습니다.

## 7. 첫 연습 순서와 자가 점검

1. Q01 DRAM → Q02 NAND 비교 → Q03 HBM을 녹화합니다. 먼저 60초로 원리만 설명하고, 3분으로 사례·trade-off·동향을 더합니다.
2. Q04~09로 제품 동작·sensing·상태 수·timing·보호 기법을 연결합니다.
3. Q10~13으로 소자·회로의 비이상 특성을 복습합니다.
4. Q14~18로 small-signal·차동·OP Amp·주파수 응답을 준비합니다.
5. Q19~24로 timing·저전력·CDC·layout·SI/PI·검증을 연결합니다.
6. 첫 회독 뒤에는 질문을 섞고 변형 질문 하나에 30~60초로 추가 답합니다.

연습용 점검 항목이며 공식 채점표가 아닙니다.

- [ ] 정의가 맞고 질문에 직접 답했는가?
- [ ] 원리가 구조·전압·전류·전하·timing 등의 인과관계로 설명됐는가?
- [ ] 용도가 그 원리에서 자연스럽게 이어졌는가?
- [ ] 얻는 것과 비용을 이유까지 설명했는가?
- [ ] 동향은 확인된 사례이거나 제품 적용이라는 해석으로 명확히 구분했는가?
- [ ] 수식의 조건·단위와 단순 모델의 한계를 밝혔는가?
- [ ] 변형 질문에도 같은 원리로 답할 수 있는가?
- [ ] 키워드 나열·개인 경험·지원동기로 시간을 채우지 않았는가?

## 8. 출처 사용 범위

회사 JD와 공개 제품 자료로 업무·제품을 연결하고, 대학·EDA 업체·memory 업체·표준 단체의 자료로 원리를 확인했습니다. 참고 링크를 제공한 기초 항목은 출제 예측 근거가 아닌 복습 자료입니다. 일부 문서 페이지는 열기 제한이 있어 검색 가능한 공개 요약을 참고했습니다. 회사 내부 문제·실제 채점표는 확보하지 않았습니다.

제품 동향의 확인 시점은 2026-10-05입니다. 회사 발표의 개발·공급·계획을 구분했고, 발표 이후의 상태를 추정으로 덧붙이지 않았습니다. T1은 2025년 HBM4 발표, T4는 2026년 제품 방향 자료입니다. T5는 2022년 공개 설명으로, 최신 운영 상태의 근거로 사용하지 않습니다.
