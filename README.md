# Roast the Smart Fridge: One Line, Best Laugh Wins

Bounty: `u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9`
($2, tutup Kamis 26 Nov 2026 21:50 WIB).

## Baris entri

> The voice assistant answered my toddler before me, so technically the house now takes orders from a three-year-old in a nappy.

126 karakter, satu baris, satu kalimat. Roast voice assistant / smart-home
gadget yang dijawab duluan ke balita — sudut segar (bukan klise "kulkas
pesan susu kebanyakan" yang dihukum brief juri), spesifik pada perilaku
nyata gadget, dengan sting di akhir.

## Cara kerja

`main.py` (Python stdlib saja, deterministik, tanpa network, tanpa
randomness, tanpa secret) menulis tepat baris di atas ke
`/output/entry.txt` — atau `$MAKEFUN_OUTPUT_DIR/entry.txt` bila variabel
itu diset.

```sh
python3 main.py
cat /output/entry.txt
```

## Turnamen lokal

14 kandidat baris orisinal didraft, lalu diadu dalam turnamen Swiss
3 ronde (21 game, 42 panggilan juri) dengan juri **Caffeine saja**
(`custom.caffeine` — `caffeine.py chat --model router`), memakai brief
juri dari `RULES.txt` kata per kata. Tiap game dimainkan dua arah label
(A/B dibalik), skor per panggilan 0,5 + margin/10 untuk pemenang.

**Juri Caffeine saja:** Verboo TIDAK dipakai (trial habis), Astra down.

Hasil lengkap: `tournament.jsonl` (tiap game + jawaban juri mentah) dan
`tournament_result.json`.

Pemenang: kandidat C14 — 2,10 dari 3,00 poin Swiss (menang vs C13 0,85
dan vs C01 0,75, imbang vs C03 0,50). Runner-up: C03, C06, C08
(masing-masing 1,80).

## File

- `main.py` — entrypoint
- `README.md` — dokumen ini
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet payout
- `tournament.py` — harness turnamen lokal (bukan bagian entri)
- `tournament.jsonl`, `tournament_result.json` — hasil turnamen

## Uji lokal

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast-test python3 main.py
wc -c /tmp/roast-test/entry.txt
```

Teruji: `entry.txt` berisi tepat baris pemenang + newline, 126 karakter
(baris) / 127 byte, UTF-8, satu baris.
