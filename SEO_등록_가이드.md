# 검색엔진 등록 가이드

> **사이트**: https://youngsampk.github.io/labor_stat/  
> **GitHub**: https://github.com/youngsampk/labor_stat.git  
> **작성일**: 2026-03-06

---

## 완료된 기술적 SEO 작업

### 1. robots.txt 개선
- `Crawl-delay: 10` 추가 (과도한 크롤링 방지)
- Sitemap 경로 명시
- Daum 검색등록 인증코드 포함

### 2. sitemap.xml 정비
- 루트의 오래된 수동 sitemap.xml 삭제
- Quarto 자동 생성 sitemap.xml 사용 (67개 URL, 최신 날짜 반영)
- 경로: https://youngsampk.github.io/labor_stat/sitemap.xml

### 3. JSON-LD 구조화 데이터 추가
- `includes/jsonld.html` 신규 생성
  - **WebSite** 스키마: 사이트명, 저자, 설명, 검색액션
  - **BreadcrumbList** 스키마: 주요 네비게이션 경로 (홈 → 뉴스칼럼 → 노트 → 연구)
- `_quarto.yml`의 `include-in-header`에 등록

### 4. description 메타데이터 일괄 추가 (50개 파일)
- 게시글(posts/): `"제목 - 박영삼 노동통계 뉴스칼럼"`
- 노트(notes/): `"제목 - 박영삼 노동통계 노트"`
- 리스팅 페이지: `"제목 - 박영삼 노동통계 홈페이지"`
- about.qmd: `"박영삼(Park Youngsam) 소개 - 노동 경제 사회 통계 연구"`
- research/index.qmd: `"박영삼의 연구 자료 모음 - 노동 경제 통계 분석"`
- thesis/index.qmd: `"한국 취업자의 계층구조와 불평등 변화 - 박영삼 박사학위논문"`

### 5. 기존 설정 (이미 적용되어 있던 항목)
- Google Analytics (G-60S2W83K5X)
- Open Graph 메타태그 (`open-graph: true`)
- Google 사이트 인증 메타태그
- Naver 사이트 인증 메타태그
- Daum 인증코드 (robots.txt)

---

## 검색엔진별 등록 절차 (수동 작업 필요)

> ⚠️ 아래 작업은 **웹 브라우저에서 직접 로그인하여** 수행해야 합니다.

---

### 🔵 Google Search Console

**접속**: https://search.google.com/search-console

#### 단계별 절차

1. **Google 계정으로 로그인**

2. **속성 추가**
   - 좌측 상단 드롭다운 → "속성 추가" 클릭
   - **URL 접두어** 방식 선택
   - `https://youngsampk.github.io/labor_stat/` 입력
   - "계속" 클릭

3. **소유권 확인**
   - "HTML 태그" 방식 선택
   - 이미 `<meta name="google-site-verification" content="...">` 태그가 모든 페이지에 포함되어 있으므로 **바로 확인 가능**
   - "확인" 버튼 클릭

4. **사이트맵 제출**
   - 좌측 메뉴 → **Sitemaps** 클릭
   - "새 사이트맵 추가"에 `sitemap.xml` 입력
   - "제출" 클릭
   - 상태가 "성공"으로 바뀌는지 확인

5. **주요 페이지 색인 요청**
   - 좌측 메뉴 → **URL 검사** 클릭
   - 아래 URL들을 하나씩 입력하고 "색인 생성 요청" 클릭:
     ```
     https://youngsampk.github.io/labor_stat/
     https://youngsampk.github.io/labor_stat/index.html
     https://youngsampk.github.io/labor_stat/notes.html
     https://youngsampk.github.io/labor_stat/about.html
     https://youngsampk.github.io/labor_stat/thesis/
     ```

6. **등록 확인 방법**
   - Google에서 `site:youngsampk.github.io/labor_stat` 검색
   - 색인된 페이지 목록이 나타나면 성공
   - 반영까지 **수일~2주** 소요

---

### 🟢 Naver Search Advisor

**접속**: https://searchadvisor.naver.com/

#### 단계별 절차

1. **네이버 계정으로 로그인**

2. **사이트 등록**
   - 상단 메뉴 → "웹마스터 도구" 클릭
   - "사이트 관리" → "사이트 등록"
   - `https://youngsampk.github.io/labor_stat/` 입력
   - "등록" 클릭

3. **소유권 확인**
   - "HTML 태그" 방식 선택
   - 이미 `<meta name="naver-site-verification" content="...">` 태그가 포함되어 있으므로 **바로 확인 가능**
   - "소유확인" 버튼 클릭

4. **사이트맵 제출**
   - 좌측 메뉴 → **요청** → **사이트맵 제출**
   - `https://youngsampk.github.io/labor_stat/sitemap.xml` 입력
   - "확인" 클릭

5. **웹 페이지 수집 요청**
   - 좌측 메뉴 → **요청** → **웹 페이지 수집**
   - `https://youngsampk.github.io/labor_stat/` 입력
   - "확인" 클릭
   - 주요 페이지도 추가로 요청

6. **RSS 제출 (선택)**
   - Quarto 블로그가 RSS를 생성하는 경우:
   - 좌측 메뉴 → **요청** → **RSS 제출**
   - `https://youngsampk.github.io/labor_stat/index.xml` 입력

7. **등록 확인 방법**
   - 네이버에서 `site:youngsampk.github.io/labor_stat` 검색
   - 반영까지 **수일~수주** 소요

---

### 🟡 Daum 검색등록

**접속**: https://register.search.daum.net/index.daum

#### 단계별 절차

1. **카카오 계정으로 로그인**

2. **신규 등록**
   - "신규 등록하기" 클릭
   - URL: `https://youngsampk.github.io/labor_stat/`
   - 사이트 이름: `노동통계 - 박영삼`
   - 사이트 설명: `노동 경제 사회 통계 분석, 뉴스칼럼, 연구자료`

3. **소유권 확인**
   - `robots.txt` 방식 선택
   - 이미 Daum 인증코드가 `robots.txt`에 포함되어 있으므로 **바로 확인 가능**

4. **등록 확인 방법**
   - Daum에서 `site:youngsampk.github.io` 검색
   - 반영까지 **1~4주** 소요

---

## 등록 후 모니터링

### 정기 확인 사항

| 항목 | 주기 | 도구 |
|------|------|------|
| 색인 현황 | 주 1회 | Google Search Console |
| 크롤링 오류 | 주 1회 | Google Search Console > 페이지 |
| 검색 노출 순위 | 월 1회 | Google Search Console > 실적 |
| Naver 수집 현황 | 월 1회 | Naver Search Advisor |
| 사이트맵 상태 | 월 1회 | 각 웹마스터 도구 |

### 검색어 확인

등록 후 아래 검색어로 노출 여부를 확인하세요:

```
Google: site:youngsampk.github.io/labor_stat
Naver:  site:youngsampk.github.io/labor_stat
Daum:   site:youngsampk.github.io
```

### 새 글 작성 시

새로운 `.qmd` 파일을 작성할 때 반드시 YAML 헤더에 `description`을 포함하세요:

```yaml
---
title: "글 제목"
description: "이 글에 대한 간단한 설명 (150자 이내 권장)"
---
```

---

## 참고 링크

- [Google Search Console 도움말](https://support.google.com/webmasters)
- [Naver Search Advisor 도움말](https://searchadvisor.naver.com/guide)
- [Daum 검색등록 도움말](https://register.search.daum.net/searchGuide.daum)
- [Quarto SEO 설정](https://quarto.org/docs/websites/website-tools.html)
- [Google 구조화된 데이터 테스트](https://search.google.com/test/rich-results)
