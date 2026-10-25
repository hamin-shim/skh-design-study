# A!SK·설계 직무 참고자료 모음

작성일: 2026-10-07
연결 문서: `A!SK_설계_전공문항은행.md` (각 자료 옆 Q번호 = 관련 문항)

> 사용 원칙: 뉴스룸은 **"하이닉스가 자기 기술을 어떤 언어로 설명하는가"** 를 익히는 용도다. 원리 깊이는 교재·강의로 채운다. 하루 공부 = 원리 공부 1개념 + 뉴스룸 기사 1편.

---

## 1. SK하이닉스 뉴스룸 — 최우선

### 1-1. 설계 직무 이해 (먼저 읽기, 각 10분)

| 자료 | 볼 포인트 |
|---|---|
| [앰버서더 JOB로그 3편 — 반도체의 두뇌를 구현한다, '설계'](https://news.skhynix.co.kr/ambassador-job-log-ep3/) (2025.07) | DRAM 설계팀·NAND 설계팀 TL 인터뷰. 회로설계 → 배치설계 → 검증 흐름, 디지털(IP) 설계 구분 |
| [SK하이닉스 DRAM 설계의 모든 것](https://www.skcareersjournal.com/1161) (SK Careers Journal, 2018) | 회로설계를 "외부 전원을 받아 내부 전압을 만드는 **아날로그 회로 설계**"로 설명 → 아날로그 출제의 근거 |
| [반도체 회로 설계는 나의 운명 — DRAM 지한규 책임](https://news.skhynix.co.kr/semiconductor-circuit-design-is-my-destiny/) | DDR4 개선·DDR5 설계 실무 |
| [반도체 직무탐구 인터뷰 시리즈](https://news.skhynix.co.kr/series/job-interview/) | 다른 직무와 설계의 협업 접점 |

### 1-2. HBM (Q5, Q46)

| 자료 | 볼 포인트 |
|---|---|
| [HBM 개발 주역 박명재 부사장 인터뷰](https://news.skhynix.co.kr/hbm_interview_2024/) | TSV 기반 1세대 HBM(2013)부터의 설계 관점 스토리 |
| [이규제 부사장 — 차세대 패키징 기술로 HBM 1등](https://news.skhynix.co.kr/hbm_pakage_interview_2024/) | **MR-MUF**, 적층·방열 이슈 |
| [2024 신임임원 권언오 부사장 — 차세대 HBM은 Specialized + Customized](https://news.skhynix.co.kr/2024-new-executive-gwoneono/) | Custom HBM, Base Die 방향성 |
| [2023 신임임원 박명재 부사장 — DRAM 설계](https://news.skhynix.co.kr/2023-new-executive-parkmyungjae/) | DRAM 설계 조직의 시각 |
| [ONE TEAM SPIRIT EP.2 — HBM 1등 스토리](https://news.skhynix.co.kr/one-team-spirit-ep2/) | 지원동기·인재상 답변 소재 |
| [발열 잡는 메모리 설루션 'iHBM'](https://news.skhynix.co.kr/ihbm-solution/) | 최신 HBM 발열 대응 → Q42·Q46 시나리오 답변 소재 |

### 1-3. NAND (Q3, Q4)

| 자료 | 볼 포인트 |
|---|---|
| [Pathfinder 3편 — 4D 낸드 기술 소개](https://news.skhynix.co.kr/pathfinder-3-4d-nand) (2023.11) | **PUC**(Peri Under Cell)를 아파트 지하주차장에 비유. Peri 회로 = 설계 영역 |
| [321단 NAND 보도자료](https://news.skhynix.co.kr/presscenter/worlds-highest-321-nand) | 최신 적층 수 |
| [Expert Insights — DRAM·NAND 전망 2편](https://news.skhynix.co.kr/expert-insights-dram-nand-prospect-2/) | DRAM·NAND 기술 방향 |

### 1-4. DRAM 제품·저전력 (Q8, Q9, Q43)

| 자료 | 볼 포인트 |
|---|---|
| [LPDDR5X 개발 스토리 — 모바일 D램 최초 HKMG](https://news.skhynix.co.kr/lpddr5x-developer-interview/) | 저전력 DRAM에서 공정(HKMG)과 설계의 협업. 설계품질혁신 조직 언급 |

### 1-5. AI 메모리 (Q27)

| 자료 | 볼 포인트 |
|---|---|
| [SK하이닉스 AI 메모리 2023 (HBM·PIM·CXL)](https://news.skhynix.co.kr/skhynix-ai-memory-2023/) | "HBM은 학습, PIM은 저전력 추론, CXL은 확장" 정리 |
| [PIM 태그 모음 (미래인재 CLASS 제2강 포함)](https://news.skhynix.co.kr/tag/pim) | GDDR6-AiM, AiMX |
| [FMS 2026 — 차세대 메모리 아키텍처 방향](https://news.skhynix.co.kr/fms-2026/) | **최신 방향성**. 면접 직전에 다시 확인 |
| [샌디스크와 HBF 첫 표준 규격 공개](https://news.skhynix.co.kr/hbf-at-fms-2026/) | HBF(고대역폭 플래시). 신기술 질문 대비 |

### 1-6. 입문·가볍게

| 자료 | 볼 포인트 |
|---|---|
| [방구석 반도체 EP1 — AI 시대의 진짜 주인공, 메모리](https://news.skhynix.co.kr/banggu-seok-semiconductor_ep1/) | 영상. DRAM·NAND·HBM 전체 지도 |
| [hy-school](https://news.skhynix.co.kr/post/hy-school) | 미래인재 CLASS 계열 강의 (제1강: TSV·MR-MUF) |
| [뉴스룸 시리즈 전체 목록](https://news.skhynix.co.kr/series) | 위에 없는 기술 해설 시리즈 탐색용 |

---

## 2. 원리 깊이 채우기 — 강의·교재

| 자료 | 용도 | 관련 문항 |
|---|---|---|
| [Razavi — Design of Analog CMOS IC 강의 (YouTube)](https://www.youtube.com/playlist?list=PLxWY2Q1tvbBua1l-fk2n9YSzZJNbUJfet) | 아날로그 표준 강의. **단일단 증폭기, 차동쌍, Current Mirror, 주파수 응답, 피드백·안정도** 챕터만 우선 | Q31~Q39 |
| Razavi, *Design of Analog CMOS Integrated Circuits* (한글 번역판 있음) | 위 강의 교재. 학부 때 쓴 전자회로 교재로 대체 가능 | Q31~Q39 |
| [Keeth·Baker 외, *DRAM Circuit Design* (Wiley/IEEE Press)](https://www.wiley-vch.de/en/areas-interest/engineering/dram-circuit-design-978-0-470-18475-2) | **DRAM 회로설계 유일한 표준 교재**. Array, Sense Amp, Peri, 내부 전압 변환기, DLL, Data Path, Power Delivery. 도서관에서 1~2장(Array)과 전압 변환기 장만 발췌 | Q1, Q6, Q13, Q16, Q40 |
| [Onur Mutlu 강의 채널 (YouTube)](https://www.youtube.com/onurmutlulectures) | 컴퓨터구조 관점의 **DRAM 동작, Refresh, RowHammer, PIM** | Q2, Q7, Q27 |
| Weste & Harris, *CMOS VLSI Design* | 디지털 Timing, 전력, 저전력 기법 | Q17~Q25 |
| [삼성반도체 뉴스룸 반도체 용어사전 (RAM)](https://news.samsungsemiconductor.com/kr/%EB%B0%98%EB%8F%84%EC%B2%B4-%EC%9A%A9%EC%96%B4-%EC%82%AC%EC%A0%84-%EB%9E%A8ram/) | 용어 정의 빠른 확인용 보조 자료. 답변에서 경쟁사 표현을 쓰지 않도록 주의 | 전반 |

---

## 3. 전형·채용 공식 자료

| 자료 | 용도 |
|---|---|
| [SK Careers 2026 하반기 공고](https://www.skcareers.com/Recruit/Detail/R261762) | Half-Day 구성, **Job Description PDF 다운로드** (설계 직무 세부 Task 확인 필수) |
| [Talent Hub — Half-Day 소개](https://talent.skhynix.com/hub/ko/company/story/217) | 문제해결 PT, GD, A!SK 공식 설명 |

---

## 4. 추천 읽기 순서 (공부 계획과 맞춤)

1. **오늘**: 1-1 설계 직무 이해 4편 → 출제자가 생각하는 "설계"의 범위 잡기
2. **1주차 (메모리)**: 방구석 반도체 EP1 → HBM 인터뷰 2편(박명재, 이규제) → Pathfinder 4D 낸드 → Mutlu DRAM 기초 강의 1편
3. **2주차 (아날로그)**: Razavi 강의(증폭기 → 차동쌍 → Mirror → 안정도) + *DRAM Circuit Design* 전압 변환기 장
4. **3주차 (시나리오)**: iHBM, LPDDR5X, 권언오 부사장 인터뷰 → Q42~Q47 답변 소재
5. **면접 1주 전**: FMS 2026, HBF 기사와 뉴스룸 최신 기사 → 최신 키워드 업데이트

---

## 5. 주의

- 링크는 2026-10-07 검색 기준이다. 뉴스룸 URL 구조가 바뀌면 제목으로 검색한다.
- 뉴스룸 기사는 홍보 성격이 있다. **수치(적층 수, 속도)는 기사 날짜와 함께 기억**하고, 답변에서는 "○년 기준"을 붙인다.
- 비공식 PDF(교재 스캔본 등)는 사용하지 않는다.
