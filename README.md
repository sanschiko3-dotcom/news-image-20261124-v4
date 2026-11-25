# news-image-20261124-v4

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/sanschiko3-dotcom/news-image-20261124-v4/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/sanschiko3-dotcom/news-image-20261124-v4/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the [make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124).

## What it is

A newspaper front page, **"THE WORLD TODAY — Tuesday, 24 November 2026"**, drawn with Pillow at build time (`render.py`) and shipped as `entry.png`. The entry program `main.py` (Python 3.13, standard library only) copies that image to `/output/entry.png` — no network, fully deterministic.

36 dated stories across 9 regions:

- **LEAD** — Ukraine sea drones sink the Russian corvette Merkury off Benghazi, Libya, with a schematic Mediterranean map and a stat strip (7 drones, 1 corvette sunk, 1 Ka-27 destroyed, 1 cargo ship hit).
- **HORMUZ STRIP** — Three tankers ablaze after hitting mines in the Strait of Hormuz.
- **GRID (12 panels)** — COP31 collapses in Antalya; Shanghai chief Chen Jining probed; Dow tops 50,000 first time; Russian strike hits Zaporizhzhia; Hasina plans 16 Dec return; Sarkozy to stand trial in 2027; Indonesia factory fire toll 26; Israeli strike kills Hamas chief; Huawei convicted in US trial; Sanofi buys Insmed for $41bn; NATO counts 25 airspace violations; Tiangong welcomes its first foreign astronaut. Each panel carries a region tag, a date tag, a drawn pictogram, a headline and a fact deck.
- **FULL-WIDTH** — States sue SpaceX over Grok abuse images (Oregon + Virginia, CCDH study figures).
- **ALSO TODAY** — 21 numbered one-line briefs, all dated: Huang returns as NVIDIA CEO, Sparta II ablaze in the Baltic, no Ukraine deal at Shenzhen, 14 states back the Rohingya case at the ICJ, US sanctions on Iran, Nepal 5.6 quake, measles ninth death in Pennsylvania, Villavicencio car bomb, Tripoli asks Kyiv about the Libya attack, Guterres AI-risk framework, Tedros on the Cuba fuel blockade, Microsoft Code Red, Houthis 60 km from Aden, Senegal regain the AFCON title, Tesla–SpaceX merger talks, CIA hack, Seoul scrambles jets, US drones aid Mexico's El Chapo Isidro arrest, MSCI Indonesia downgrade talks, Solomons–Australia security pact, Malaysia repatriates 6,803 Myanmar nationals.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, under 1 MiB, byte-identical on every run
```

Rebuild the image from scratch:

```sh
python3 render.py
# writes entry.png next to render.py
```

## License

MIT — see [LICENSE](LICENSE).
