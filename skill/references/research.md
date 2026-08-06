# Research

Phase 2, Step 3. Keywords pointed outward: in Read they were extracted, here they are what
we go searching with.

---

## What we search for

| Target | What we are actually after |
|--------|----------------------------|
| Company name | Is it taken · who else uses it · trademark exposure · **visual collisions** |
| Naming reason and meaning | Metaphors the word already carries |
| Why the company exists | Category conventions to sit inside or deliberately break |
| The area or industry | What this whole category looks like |
| Customers | What they already respond to, what reads as credible to them |
| **Competitors** | **What is taken — the colours and forms we cannot have** |

Competitors is the differentiation input, not an inspiration board. If every brand in the
category is black and steel, that is occupied territory.

---

## ⛔ Before you open anything: screen the URL

**A protected site does not fail politely. It takes the application down.**

Learned on a real run, twice, before the cause was isolated. Pointing the browser pane at
`voix-du-nucleaire.org` — a Cloudflare-protected site — crashed the user's app. The second
crash cost the run's dispatch and a round of confusion in which the search itself was
blamed, because the user had separately run agents and subagents doing searches with no
problem at all. **The crash correlates with the browser pane meeting a challenge page, not
with searching, not with fan-out.**

Screen every URL before it touches a browser. No browser involved, so it cannot crash:

```bash
curl -s -I -m 12 -A "Mozilla/5.0" "$url" | grep -iE "^(http/|server:|cf-ray)"
```

| Result | Route |
|--------|-------|
| `server: cloudflare`, or a `cf-ray` header, or **403** | **Never open in the browser.** Use `curl` or WebFetch — both often succeed where the pane dies |
| Ordinary server, 200 | Safe for the browser pane |

Screening a batch before a collection run costs seconds:

```bash
for u in "${urls[@]}"; do
  h=$(curl -s -I -m 12 -A "Mozilla/5.0" "$u")
  printf "%-45s %s %s\n" "$u" \
    "$(printf '%s' "$h" | grep -i '^HTTP/' | tail -1 | awk '{print $2}')" \
    "$(printf '%s' "$h" | grep -ic cloudflare)"
done
```

**Note that a 200 to `curl` does not mean the pane is safe** — `voix-du-nucleaire.org`
returns 200 to curl and still crashes the browser. The `server:` header is the signal, not
the status code.

### Subagents must be denied browser tools outright

**Do not tell a collector to screen its own URLs. Tell it that browser tools do not exist.**

An agent given both a rule and a browser will eventually navigate to something unscreened,
and the crash lands on the user, not on the agent. State it as a prohibition with the
consequence attached, near the top of the prompt where it will not be skimmed past:

> ⛔ **CRITICAL TOOL RULE — VIOLATING THIS CRASHES THE USER'S APPLICATION.**
> Do NOT use any browser tools. Use ONLY: Bash (curl), WebFetch, WebSearch, Read, Write.

This costs nothing. `curl` plus WebFetch outperformed the browser for every research task on
that run: palettes came from grepping linked CSS, logos came from downloading the SVG, and
typefaces came from `@font-face` rules — none of which needs a rendered page.

**There is a second reason, independent of crashing.** Collectors share one browser pane. Six
agents navigating it at once collide. Denying them the browser removes the contention as
well as the risk, and leaves the main thread free to screenshot the handful of sites where
composition and register genuinely need to be *seen* — which greps cannot give you.

---

## Sources

**Never collect from a single source.** On a real run the boards were built entirely from
Unsplash for a direction called *The Seal* — hallmarks, stamped marks, manuscripts, archives.
Unsplash returned modern brass wax stamps with Latin monograms. One call to the Met's open
access API returned a **10th–11th century Islamic seal stone with Kufic Arabic carved into
it**, public domain and free. The right century and the right alphabet, from a source that
was never opened.

**Match the source to the direction.** A documentary or heritage direction lives in
archives; a lifestyle direction lives in stock. Using stock for an archival brief produces
a board that is competent and about the wrong thing.

### Stock — client-facing boards

| Source | Status | Notes |
|--------|--------|-------|
| **Unsplash** | ✅ tested | 32 URLs off one search page, no login. Free for commercial use |
| **Pexels** | ✅ downloads verified | Same licence position |
| **Openverse** | untested | Aggregates CC-licensed media across many sources — `openverse.org` |

### Archive and museum open access — the source most often missed

Public domain, high resolution, free, and **the only place historical material exists**.
Essential for any direction involving heritage, craft, documentation, seals, manuscripts,
tools, or regional history.

| Source | Access | Notes |
|--------|--------|-------|
| **The Met** | ✅ tested — clean JSON API, no key | `collectionapi.metmuseum.org` · 490k+ public domain objects · strong Islamic art holdings |
| **Wikimedia Commons** | ✅ tested — MediaWiki API, no key | Vast, uneven quality, excellent for objects and processes |
| **Rijksmuseum** | untested | Very high resolution, needs a free API key |
| **Smithsonian Open Access** | untested | 4.5M+ CC0 items |
| **Library of Congress** | untested | `loc.gov` JSON, strong on documents and photography |
| **Europeana** | untested | Aggregates European institutions |
| **NYPL Digital Collections** | untested | Strong on ephemera and print |

**Met pattern, verified:**

```
search  → collectionapi.metmuseum.org/public/collection/v1/search?q=<term>&hasImages=true
object  → collectionapi.metmuseum.org/public/collection/v1/objects/<id>
fields  → title · objectDate · culture · isPublicDomain · primaryImage · primaryImageSmall
```

Check `isPublicDomain` before using anything. Record the object title and date in
`FINDINGS.md` — provenance is part of the value.

### Design work — research only, never client-facing

| Source | Status | Notes |
|--------|--------|-------|
| **Behance** | ✅ tested — no login | 29 CDN images and 48 gallery links off one search, titles in `alt`. **The strongest source for finished identity systems** |
| **Dribbble** | untested | Shots rather than systems; shallower than Behance |
| **Fonts In Use** | untested | Typefaces shown in real context, with the faces named |

These are other designers' copyrighted portfolio work. **They stay in `research/`
permanently.**

### First-party and clearance

| Source | Role |
|--------|------|
| **The named brands' own sites** | Category conventions, via browser screenshot |
| **Trademark registers** | Name clearance — search only, never claim cleared |
| **Regional foundries and type specimens** | Essential for a bilingual brand; Arabic type needs its own reference |

### User-supplied

| Source | Status |
|--------|--------|
| **Pinterest** | **Renders nothing anonymously** — ships ~1MB of app shell with `login required` and zero pins. Direct `i.pinimg.com` URLs download fine. See the three routes below |

### Behance is the strongest source, and the most restricted

It holds finished brand identities, logos and brand books rather than stock photography.
Nothing else surfaces what an actual competitor's identity system looks like. One search
for `knife brand identity` returned *"Nesal"* — a published knife identity under a
near-identical name — alongside *"SKIF Knives Brand Identity"*. A name collision and a
direct category reference from a single query.

**It never reaches a client-facing board.** That is other designers' copyrighted portfolio
work, and putting it in a mood board is presenting their work as our direction. Behance
stays in `research/`, permanently. Thumbnails run 444×347; full resolution needs the project
page.

### Unsplash and Pexels are the workhorses for boards

Verified end to end: navigate the search page, extract image URLs from the DOM, download,
save. The licence permits commercial use, so these carry no cleanup burden if they outlive
the board.

### Pinterest needs a session — three routes, ranked

1. **User-assisted login.** Open Pinterest in the browser pane and ask the user to sign in
   themselves. The normal pipeline then works.
2. **User-supplied links.** They browse, they paste board or pin URLs, we fetch the
   originals. Costs nothing, needs no session.
3. **Their own logged-in Chrome**, where a session may already exist.

**Never type their credentials**, and **collect modestly** — a few dozen references for one
project is ordinary use; bulk harvesting is what the terms exist to stop.

### Search in the market's own language

A brand operating in Iraq or the Gulf loses sales to local competitors, not to the global
category leader. **Search in Arabic as well as English**, and search the local market by
name. A local rival's palette is far more likely to be genuinely occupied where it counts.

---

## How to build a search query

**Both of these were learned by getting them wrong on a real brief.**

A query has three parts. Missing either of the last two wastes the collection.

```
[ subject ]  +  [ register ]  +  [ exclusion built in ]
```

### 1 · The forbidden list goes IN the query, not on a checklist beside it

Searching `wax seal` for a brand that forbids red returns **red wax**, because that is what
the phrase means to a search engine. The constraint was recorded, but it was only applied
at review — after eight unusable images had been downloaded.

**An agent told "avoid red" still types "wax seal" and still gets red.** The exclusion has
to change the words.

| Constraint | Wrong query | Right query |
|------------|-------------|-------------|
| No red | `wax seal document` | `brass stamp embossed paper` |
| No faces | `chef kitchen` | `chef hands preparation close` |
| No weapons framing | `knife` | `blade craftsmanship workshop` |

Most search engines have no reliable negative operator, so **name the thing you want
instead of the thing you don't.** Brass instead of not-red. Hands instead of not-faces.

### 2 · The register goes in the query too

Subject alone returns stock photography. `date palm frond desert` returned tourism —
bright blue skies, wide postcard shots, nothing resembling an art direction.
`palm frond texture macro` returned the same subject in the right world.

Register words that actually change results:

**texture · macro · close · detail · monochrome · low light · overhead · minimal ·
studio · natural light · dark · muted · film**

| Direction | Subject only | Subject + register |
|-----------|--------------|--------------------|
| Craft workshop | `workshop tools` → teal toolrolls, yellow benches | `craftsman hands workshop monochrome` |
| Place | `date palm desert` → postcards | `palm frond texture macro` |
| Documentation | `document` → office stock | `archive paper embossed detail` |

### 3 · Write the queries before collecting, and check them against the brief

For each direction, write the query list first and read it against the forbidden list and
the intended register. **A wrong query costs a whole collection run** — the most expensive
step in the process — so the minute spent checking is free by comparison.

---

## The folder

```
<company-name>/research/
  admired-brands/     named by the user in the questionnaire
  competitors/        direct rivals, including the local market
  category/           wider conventions
  name/               meaning, existing uses, trademark, visual collisions
  audience/           where they already are
  FINDINGS.md         what we saw, and what it means
```

**`FINDINGS.md` is the deliverable of this step.** A folder of screenshots nobody wrote
about is dead weight. Every saved reference gets a line: what it is, why it was saved, what
it implies for us.

---

## Running it with subagents

**One agent per direction or target. Sonnet.** The work is largely mechanical — search,
extract, download, write a manifest line — but not purely: the agent must apply the brief's
forbidden list and hold one mood while filtering, and adapt when a page does not match the
expected shape. Weaker models drift on both. Opus is wasted on downloading files.

Each agent receives the direction or target, the forbidden list, the audience, its own
folder, and seed terms. **Agents share no context** — every prompt must be complete.

**Agents over-collect; the main thread curates.** If each agent decides for itself what
cohesive means, the result is one taste per agent. Gather roughly three times the target,
then curate with a single judgement.

**Monitoring is reading the manifests and the folders** before anything reaches the user —
not watching progress.

**Say the cost before running it.** Directions × oversampling × searches per agent makes
this the most expensive step in the process by a wide margin.

---

## The line that governs all of it

**Reference versus shipped asset.** Found images are legitimate as reference — that is what
research and mood boards are made of. What they never become is the brand's own
photography. Anything that ships as a brand asset is original or licensed.

And: **gather inspiration, do not be moved by it.** A palette that looks good on Behance was
derived from someone else's brief. Ours governs.
