# sitemap.xml / feed.xml ?먮룞 ?앹꽦 ?묒뾽 ?뺣━

## 1. 媛쒖슂

GitHub Pages濡?諛고룷?섎뒗 Quarto 釉붾줈洹?`youngsampk/labor_stat`)?????
`main` 釉뚮옖移섏뿉 push???뚮쭏??**sitemap.xml**怨?**feed.xml(RSS 2.0)**???먮룞?쇰줈 ?앹꽦쨌而ㅻ컠?섎뒗 ?뚯씠?꾨씪?몄쓣 援ъ꽦?덉뒿?덈떎.

---

## 2. 異붽????뚯씪

| ?뚯씪 | ??븷 |
|---|---|
| `scripts/generate_sitemap.py` | `docs/` ?대뜑??HTML ?뚯씪???ㅼ틪?섏뿬 `docs/sitemap.xml` ?앹꽦 |
| `scripts/generate_feed.py` | `docs/posts/` ?섏쐞 `index.html`???ㅼ틪?섏뿬 `docs/feed.xml` (RSS 2.0) ?앹꽦 |
| `.github/workflows/build-site.yml` | GitHub Actions ?뚰겕?뚮줈 ??Quarto ?뚮뜑 ?????ㅽ겕由쏀듃 ?ㅽ뻾, 寃곌낵 ?먮룞 而ㅻ컠 |

---

## 3. 媛??뚯씪 ?곸꽭

### 3.1 `scripts/generate_sitemap.py`

- `docs/` ?붾젆?곕━瑜??ш? ?먯깋?섏뿬 `.html` ?뚯씪 紐⑸줉???섏쭛
- 媛??뚯씪??留덉?留??섏젙??`mtime`)??`<lastmod>`濡?湲곕줉
- 寃곌낵瑜?`docs/sitemap.xml`???쒖? Sitemap XML ?뺤떇?쇰줈 異쒕젰

**?ㅽ뻾 ?덉떆:**
```powershell
python scripts/generate_sitemap.py --site-url https://youngsampk.github.io --input-dir docs --output docs/sitemap.xml
```

### 3.2 `scripts/generate_feed.py`

- `docs/posts/` ?섏쐞 ?대뜑??`index.html`???먯깋
- `<title>`, `<meta name="description">`, 泥?踰덉㎏ `<p>` ?깆뿉???쒕ぉ怨??ㅻ챸??異붿텧
- ?뚯씪 ?섏젙??湲곗??쇰줈 理쒖떊???뺣젹, 理쒕? N媛???ぉ??RSS 2.0 ?뺤떇?쇰줈 異쒕젰
- 寃곌낵瑜?`docs/feed.xml`?????

**?ㅽ뻾 ?덉떆:**
```powershell
python scripts/generate_feed.py --site-url https://youngsampk.github.io --input-dir docs/posts --output docs/feed.xml --max-items 30
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
      SITE_URL: https://youngsampk.github.io
    steps:
      - Checkout (actions/checkout@v4)
      - Setup Quarto (quarto-dev/quarto-actions/setup@v2)
      - Setup Python (actions/setup-python@v5)
      - Render site (quarto-dev/quarto-actions/render@v2)
      - Generate sitemap (python scripts/generate_sitemap.py ...)
      - Generate RSS feed (python scripts/generate_feed.py ...)
      - Commit & push (docs/sitemap.xml, docs/feed.xml)
```

**?숈옉 ?먮쫫:**
1. `main`??push ?대깽??諛쒖깮
2. Ubuntu ?щ꼫?먯꽌 Quarto + Python ?섍꼍 ?명똿
3. `quarto render`濡??ъ씠??鍮뚮뱶 ??`docs/` ?대뜑??HTML ?앹꽦
4. Python ?ㅽ겕由쏀듃濡?`docs/sitemap.xml`, `docs/feed.xml` ?앹꽦
5. 蹂寃??ы빆???덉쑝硫??먮룞 而ㅻ컠 諛?push

---

## 4. ?앹꽦 ?뚯씪 ?꾩튂

| ?앹꽦 ?뚯씪 | 寃쎈줈 | ?묒냽 URL |
|---|---|---|
| Sitemap | `docs/sitemap.xml` | https://youngsampk.github.io/sitemap.xml |
| RSS Feed | `docs/feed.xml` | https://youngsampk.github.io/feed.xml |

---

## 5. ?섑뻾??而ㅻ컠 ?대젰

| 而ㅻ컠 | ?댁슜 |
|---|---|
| `cddf550` | `chore(ci): add sitemap and RSS generation workflow and scripts` ???ㅽ겕由쏀듃 2媛?+ ?뚰겕?뚮줈 理쒖큹 異붽? |
| `3a8e1ca` | `fix(ci): set SITE_URL to actual GitHub Pages domain` ??SITE_URL???ㅼ젣 ?꾨찓?몄쑝濡?蹂寃?|
| `db01ba7` | `fix(ci): use correct quarto-actions/setup@v2 and render@v2` ??GitHub Actions ?ㅻ쪟 ?섏젙 (?щ컮瑜?action 寃쎈줈쨌踰꾩쟾 ?ъ슜) |

---

## 6. ?뺤씤 諛⑸쾿

1. **GitHub Actions ??*: https://github.com/youngsampk/labor_stat/actions
   - "Build site and generate sitemap/feed" ?뚰겕?뚮줈 ?ㅽ뻾 ?곹깭 ?뺤씤 (???깃났 / ???ㅽ뙣)
2. **?앹꽦???뚯씪 吏곸젒 ?뺤씤**:
   - https://youngsampk.github.io/sitemap.xml
   - https://youngsampk.github.io/feed.xml
3. **濡쒖뺄 ?뚯뒪??* (?좏깮):
   ```powershell
   python scripts/generate_sitemap.py --site-url https://youngsampk.github.io --input-dir docs --output docs/sitemap.xml
   python scripts/generate_feed.py --site-url https://youngsampk.github.io --input-dir docs/posts --output docs/feed.xml
   ```

---

## 7. ?몃윭釉붿뒋??湲곕줉

| 臾몄젣 | ?먯씤 | ?닿껐 |
|---|---|---|
| Actions Run #1~#3 ?ㅽ뙣 | `quarto-dev/quarto-actions/setup-quarto@v1` 寃쎈줈媛 議댁옱?섏? ?딆쓬 | `quarto-dev/quarto-actions/setup@v2`濡?蹂寃?|
| `actions/setup-python@v4` 寃쎄퀬 | deprecated 踰꾩쟾 | `actions/setup-python@v5`濡??낃렇?덉씠??|
| `run: quarto render` ?⑤룆 ?ㅽ뻾 | 怨듭떇 action ?쒖슜?????덉젙??| `quarto-dev/quarto-actions/render@v2`濡?援먯껜 |

