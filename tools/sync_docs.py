"""공유 폴더의 원본 md를 docs/로 복사하면서 개인 경력 연결 문장을 뺀다. 실행: python3 tools/sync_docs.py"""
import re, pathlib
P = pathlib.Path('/mnt/project-files')
SRC = {
    'qbank': 'claude-skh/A!SK_설계_전공문항은행.md',
    'summary': 'claude-skh/설계직무_면접_핵심총정리_v1.md',
    'mosfet': 'claude-skh/MOSFET_구조와_작동원리_처음부터.md',
    'mosfet-bjt': 'claude-skh/ASK_3분답변_MOSFET_vs_BJT.md',
    'links': 'claude-skh/참고자료_링크모음.md',
    'plan-v1': 'claude-skh/Half-Day_학습계획_v1.md',
    'basics': 'codex-skh/설계/AISK_설계_기초지식_v1.md',
    'keywords': 'codex-skh/설계/AISK_설계_예상문항_키워드_3분답변_v1.md',
    'nand': 'codex-skh/이전지원/2026-06_PE/pe/NAND_Flash_회로설계자_관점_정리.md',
}
PERSONAL = re.compile(r'노트북|KAIST|HD현대|KIST 8층|현직 Power|경험 사실표|VLSI 프로젝트 합성')
out_dir = pathlib.Path(__file__).resolve().parent.parent / 'docs'
for key, rel in SRC.items():
    s = (P / rel).read_text(encoding='utf-8')
    if key == 'qbank':
        s = re.sub(r'\n## 8\. 내 경험 연결 지도.*?(?=\n## 9\.)', '\n', s, flags=re.S)
    lines = [l for l in s.split('\n') if not (PERSONAL.search(l) and 'samsungsemiconductor' not in l)]
    (out_dir / f'{key}.md').write_text('\n'.join(lines), encoding='utf-8')
    print('ok', key)
