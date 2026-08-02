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

## Sources — tested, with what each is for

| Source | Finds images? | Downloads? | Role |
|--------|---------------|------------|------|
| **Behance** | Yes — no login. 29 CDN images and 48 gallery links off one search, titles in `alt` | Yes | **Research only.** Never reaches the client |
| **Unsplash** | Yes — 32 photo URLs off one search page, no login | Yes | **Boards.** Free for commercial use |
| **Pexels** | Untested | Yes | Boards. Same licence position |
| **Pinterest** | **No.** Auth-walled — ships ~1MB of app shell with `login required` and renders zero pins | Yes, via direct `i.pinimg.com` URLs | User-supplied, see below |
| **The named brands' own sites** | Yes, via browser screenshot | n/a | Category conventions, first-party |
| **Trademark registers** | Yes | n/a | Name clearance — search only, never claim cleared |

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
