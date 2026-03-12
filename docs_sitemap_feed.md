# sitemap.xml / feed.xml 자동 생성 작업 정리

## 1. 개요

GitHub Pages로 배포되는 Quarto 블로그(`youngsampk/labor_stat`)에 대해,
`main` 브랜치에 push할 때마다 **sitemap.xml**과 **feed.xml(RSS 2.0)**을 자동으로 생성·커밋하는 파이프라인을 구성했습니다.

---

## 2. 추가된 파일

| 파일 | 역할 |
|---|---|
| `scripts/generate_sitemap.py` | `docs/` 폴더의 HTML 파일을 스캔하여 `docs/sitemap.xml` 생성 |
| `scripts/generate_feed.py` | `docs/posts/` 하위 `index.html`을 스캔하여 `docs/feed.xml` (RSS 2.0) 생성 |
| `.github/workflows/build-site.yml` | GitHub Actions 워크플로 — Quarto 렌더 후 위 스크립트 실행, 결과 자동 커밋 |

---

## 3. 각 파일 상세

### 3.1 `scripts/generate_sitemap.py`

- `docs/` 디렉터리를 재귀 탐색하여 `.html` 파일 목록을 수집
- 각 파일의 마지막 수정일(`mtime`)을 `<lastmod>`로 기록
- 결과를 `docs/sitemap.xml`에 표준 Sitemap XML 형식으로 출력

**실행 예시:**
```powershell
python scripts/generate_sitemap.py --site-url https://youngsampk.github.io/labor_stat --input-dir docs --output docs/sitemap.xml
```

### 3.2 `scripts/generate_feed.py`

- `docs/posts/` 하위 폴더의 `index.html`을 탐색
- `<title>`, `<meta name="description">`, 첫 번째 `<p>` 등에서 제목과 설명을 추출
- 파일 수정일 기준으로 최신순 정렬, 최대 N개 항목을 RSS 2.0 형식으로 출력
- 결과를 `docs/feed.xml`에 저장

**실행 예시:**
```powershell
python scripts/generate_feed.py --site-url https://youngsampk.github.io/labor_stat --input-dir docs/posts --output docs/feed.xml --max-items 30
```

### 3.3 `.github/workflows/build-site.yml`

```yaml
name: Build site and generate sitemap/feed

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      SITE_URL: https://youngsampk.github.io/labor_stat
    steps:
      - Checkout (actions/checkout@v4)
      - Setup Quarto (quarto-dev/quarto-actions/setup@v2)
      - Setup Python (actions/setup-python@v5)
      - Render site (quarto-dev/quarto-actions/render@v2)
      - Generate sitemap (python scripts/generate_sitemap.py ...)
      - Generate RSS feed (python scripts/generate_feed.py ...)
      - Commit & push (docs/sitemap.xml, docs/feed.xml)
```

**동작 흐름:**
1. `main`에 push 이벤트 발생
2. Ubuntu 러너에서 Quarto + Python 환경 세팅
3. `quarto render`로 사이트 빌드 → `docs/` 폴더에 HTML 생성
4. Python 스크립트로 `docs/sitemap.xml`, `docs/feed.xml` 생성
5. 변경 사항이 있으면 자동 커밋 및 push

---

## 4. 생성 파일 위치

| 생성 파일 | 경로 | 접속 URL |
|---|---|---|
| Sitemap | `docs/sitemap.xml` | https://youngsampk.github.io/labor_stat/sitemap.xml |
| RSS Feed | `docs/feed.xml` | https://youngsampk.github.io/labor_stat/feed.xml |

---

## 5. 수행한 커밋 이력

| 커밋 | 내용 |
|---|---|
| `cddf550` | `chore(ci): add sitemap and RSS generation workflow and scripts` — 스크립트 2개 + 워크플로 최초 추가 |
| `3a8e1ca` | `fix(ci): set SITE_URL to actual GitHub Pages domain` — SITE_URL을 실제 도메인으로 변경 |
| `db01ba7` | `fix(ci): use correct quarto-actions/setup@v2 and render@v2` — GitHub Actions 오류 수정 (올바른 action 경로·버전 사용) |

---

## 6. 확인 방법

1. **GitHub Actions 탭**: https://github.com/youngsampk/labor_stat/actions
   - "Build site and generate sitemap/feed" 워크플로 실행 상태 확인 (✅ 성공 / ❌ 실패)
2. **생성된 파일 직접 확인**:
   - https://youngsampk.github.io/labor_stat/sitemap.xml
   - https://youngsampk.github.io/labor_stat/feed.xml
3. **로컬 테스트** (선택):
   ```powershell
   python scripts/generate_sitemap.py --site-url https://youngsampk.github.io/labor_stat --input-dir docs --output docs/sitemap.xml
   python scripts/generate_feed.py --site-url https://youngsampk.github.io/labor_stat --input-dir docs/posts --output docs/feed.xml
   ```

---

## 7. 트러블슈팅 기록

| 문제 | 원인 | 해결 |
|---|---|---|
| Actions Run #1~#3 실패 | `quarto-dev/quarto-actions/setup-quarto@v1` 경로가 존재하지 않음 | `quarto-dev/quarto-actions/setup@v2`로 변경 |
| `actions/setup-python@v4` 경고 | deprecated 버전 | `actions/setup-python@v5`로 업그레이드 |
| `run: quarto render` 단독 실행 | 공식 action 활용이 더 안정적 | `quarto-dev/quarto-actions/render@v2`로 교체 |
