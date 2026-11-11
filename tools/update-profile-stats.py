"""Regenerate the profile cards from GitHub's public pages. Python 3, no token needed."""

import argparse
from collections import defaultdict
from datetime import date, timedelta
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
USER = "brunoo-code"


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.tooltips = {}
        self.active = None

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if tag == "td" and "data-date" in fields and "id" in fields:
            self.dates[fields["id"]] = date.fromisoformat(fields["data-date"])
        if tag == "tool-tip" and fields.get("for", "").startswith("contribution-day-"):
            self.active = fields["for"]
            self.tooltips[self.active] = ""

    def handle_data(self, data):
        if self.active:
            self.tooltips[self.active] += data

    def handle_endtag(self, tag):
        if tag == "tool-tip":
            self.active = None

    def counts(self):
        result = {}
        for key, day in self.dates.items():
            label = self.tooltips.get(key, "").strip()
            match = re.match(r"^(No|[\d,]+) contributions? on\b", label)
            if not match or day in result:
                raise ValueError(f"Unexpected contribution cell on {day}")
            count = match[1]
            result[day] = 0 if count == "No" else int(count.replace(",", ""))
        if len(result) < 350:
            raise ValueError("GitHub did not return a full contribution calendar")
        return result


def fetch(url):
    request = Request(url, headers={"User-Agent": "BNQQ-profile-stats", "Accept-Language": "en-US"})
    with urlopen(request, timeout=25) as response:
        return response.read().decode("utf-8")


def public_repositories():
    result = []
    page = 1
    while True:
        batch = json.loads(fetch(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}"))
        result.extend(repo for repo in batch if not repo["private"])
        if len(batch) < 100:
            return result
        page += 1


def svg(title, description, height, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="{height}" viewBox="0 0 920 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <defs>
    <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0d1928"/><stop offset="1" stop-color="#17152e"/></linearGradient>
    <linearGradient id="line"><stop stop-color="#6ff0db"/><stop offset="1" stop-color="#a395ff"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="918" height="{height - 2}" rx="18" fill="url(#bg)" stroke="#465479"/>
  <g font-family="Segoe UI, Arial, sans-serif">
{body}
  </g>
</svg>
"""


def cards(repos, languages, total, latest):
    entries = [(repos, "Repositórios públicos"), (languages, "Linguagens principais"), (total, "Contribuições no último ano")]
    body = ['    <text x="30" y="36" fill="#f0f5ff" font-size="22" font-weight="700">GitHub em números</text>']
    for i, (number, label) in enumerate(entries):
        x = 30 + i * 290
        color = "#a395ff" if i == 1 else "#6ff0db"
        body.extend([
            f'    <rect x="{x}" y="56" width="280" height="100" rx="11" fill="#152239" stroke="#344668"/>',
            f'    <text x="{x + 16}" y="106" fill="{color}" font-size="38" font-weight="700">{number}</text>',
            f'    <text x="{x + 16}" y="134" fill="#cedaf4" font-size="16">{label}</text>',
        ])
    body.append(f'    <text x="30" y="181" fill="#aabbd9" font-size="13">Fonte: perfil público do GitHub · até {latest:%d/%m/%Y}</text>')
    return svg("GitHub em números", f"{repos} repositórios públicos, {languages} linguagens principais e {total} contribuições no último ano.", 199, "\n".join(body))


def chart(counts, latest):
    weekly = defaultdict(int)
    for day, count in counts.items():
        sunday = day - timedelta(days=(day.weekday() + 1) % 7)
        weekly[sunday] += count
    end = latest - timedelta(days=(latest.weekday() + 1) % 7)
    dates = [end - timedelta(weeks=i) for i in reversed(range(16))]
    values = [weekly[day] for day in dates]
    top = max(4, ((max(values) + 39) // 40) * 40)
    points = [(67 + i * (812 / 15), 222 - 136 * value / top) for i, value in enumerate(values)]
    coordinates = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    body = [
        '    <text x="30" y="37" fill="#f0f5ff" font-size="22" font-weight="700">Atividade no GitHub</text>',
        '    <text x="30" y="60" fill="#aabbd9" font-size="15">Contribuições por semana · últimas 16 semanas</text>',
    ]
    for i in range(5):
        y = 222 - 34 * i
        body.extend([
            f'    <path d="M67 {y}H879" stroke="#344668"/>',
            f'    <text x="54" y="{y + 5}" fill="#aabbd9" text-anchor="end" font-size="13">{top * i // 4}</text>',
        ])
    body.extend([
        f'    <polygon points="67,222 {coordinates} 879,222" fill="#6ff0db" opacity=".10"/>',
        f'    <polyline points="{coordinates}" fill="none" stroke="url(#line)" stroke-width="3" stroke-linejoin="round"/>',
    ])
    for i, (x, y) in enumerate(points):
        body.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#a2ede3"><title>{dates[i]:%d/%m/%Y}: {values[i]} contribuições</title></circle>')
        if i % 3 == 0:
            body.append(f'    <text x="{x:.1f}" y="245" fill="#aabbd9" text-anchor="middle" font-size="13">{dates[i]:%d/%m}</text>')
    note = " · semana atual parcial" if latest != end + timedelta(days=6) else ""
    body.append(f'    <text x="30" y="276" fill="#aabbd9" font-size="13">Fonte: calendário público do GitHub · até {latest:%d/%m/%Y}{note}</text>')
    description = "Contagens semanais: " + ", ".join(f"{day:%d/%m}: {value}" for day, value in zip(dates, values)) + "."
    return svg("Atividade no GitHub", description, 294, "\n".join(body))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calendar", type=Path, help="use a previously fetched public calendar HTML")
    args = parser.parse_args()
    calendar = Calendar()
    calendar.feed(args.calendar.read_text(encoding="utf-8") if args.calendar else
                  fetch(f"https://github.com/users/{USER}/contributions"))
    counts = calendar.counts()
    latest = max(counts)
    total = sum(counts.values())
    repos = public_repositories()
    languages = {repo["language"] for repo in repos if repo["language"]}
    (ROOT / "assets/github-stats.svg").write_text(cards(len(repos), len(languages), total, latest), encoding="utf-8")
    (ROOT / "assets/github-activity.svg").write_text(chart(counts, latest), encoding="utf-8")
    print(f"{len(repos)} public repositories, {len(languages)} primary languages, {total} contributions through {latest}")


if __name__ == "__main__":
    main()
