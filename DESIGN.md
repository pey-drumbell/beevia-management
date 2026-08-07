---
name: Beevia Project Status
description: A black-and-white datamatics reading surface for dated project-status reports, built as plain HTML that opens from a double-click.
colors:
  ground: "#000"
  ink: "#fff"
typography:
  display:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "clamp(2.25rem, 7.5vw, 5.25rem)"
    fontWeight: 700
    lineHeight: 0.86
    letterSpacing: "-0.05em"
    fontVariation: "'wdth' 112.5, 'wght' 700"
  headline:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "clamp(1.125rem, 2.4vw, 1.625rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.04em"
    fontVariation: "'wdth' 112.5, 'wght' 700"
  lede:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "clamp(1rem, 2.1vw, 1.375rem)"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "-0.025em"
    fontVariation: "'wdth' 75, 'wght' 500"
  title:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.8125rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.08em"
    fontVariation: "'wdth' 100, 'wght' 700"
  body:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.9375rem"
    fontWeight: 300
    lineHeight: 1.75
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 75, 'wght' 300"
  data:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
    fontVariation: "'wdth' 100, 'wght' 400"
    fontFeature: "tabular-nums"
  label:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.625rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.16em"
    fontVariation: "'wdth' 100, 'wght' 600"
  micro:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.5625rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.16em"
    fontVariation: "'wdth' 100, 'wght' 600"
  numeral:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0"
    fontVariation: "'wdth' 112.5, 'wght' 700"
  frameDate:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "clamp(1.125rem, 3vw, 1.75rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.04em"
    fontVariation: "'wdth' 112.5, 'wght' 700"
  bodyPhone:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.875rem"
    fontWeight: 300
    lineHeight: 1.75
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 75, 'wght' 300"
  dataPhone:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.6875rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
    fontVariation: "'wdth' 100, 'wght' 400"
    fontFeature: "tabular-nums"
  labelPhone:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.5rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.1em"
    fontVariation: "'wdth' 100, 'wght' 600"
rounded:
  none: "0"
spacing:
  s-1: "0.25rem"
  s-2: "0.5rem"
  s-3: "0.75rem"
  s-4: "1rem"
  s-5: "1.5rem"
  s-6: "2rem"
  s-7: "3rem"
  s-8: "4.5rem"
  s-9: "7rem"
components:
  topbar:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    height: "3rem"
  topbar-link-hover:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
  masthead-rail:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    typography: "{typography.data}"
    padding: "{spacing.s-4}"
    width: "13.5rem"
  invert:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
    rounded: "{rounded.none}"
    padding: "{spacing.s-5}"
  table-row:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    typography: "{typography.data}"
    padding: "0.5rem 0.75rem"
  table-row-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
  section-heading:
    typography: "{typography.headline}"
    textColor: "{colors.ink}"
    padding: "0.75rem 0 0"
  archive-frame:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.5rem 2rem"
  archive-frame-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
---

# Design System: Beevia Project Status

## Overview

**Creative North Star: "The Datamatics Print"**

This is a report about disagreement between measuring instruments, and it is drawn the way an instrument draws: pure black ground, pure white ink, hairline rules, tabular columns, and figures set at a width that lets them stack. There is no grey and no colour anywhere in the system. Every tone the page appears to have is produced by *coverage* — hairlines at 0.5px, hatched bar fills, the varying width of a single type face — never by tinting the ink. The world is Ryoji Ikeda datamatics: a page that looks measured rather than styled.

The surface refuses the project-management dashboard on purpose. No donuts, no RAG status pills, no burndown, no avatars, no progress rings. A generic dashboard reports the board; this report reconciles the Zoho board, the commit history of five repositories, and the diffed API surface *against each other*, and the design exists to let that disagreement land rather than average it into a tidy metric. Where the board and the code contradict one another, the two figures sit side by side in the masthead rails and the reader draws the conclusion.

Density is high and deliberate. The reader is the project owner, minutes before standup, on a phone. The overview block, its deltas, and the three things worth knowing must resolve before any scrolling — so nothing decorative is allowed to occupy the first screen. A masthead data-field graphic was built here and then removed at the user's request; the masthead is now type and numeric rails on clean ground, and the rails carry real figures (queue counts, median age, API surface, board-moves-vs-commits) instead of annotating a picture. Nothing on the site animates on entry.

**Key Characteristics:**
- Two ink values only: pure black ground (#000), pure white ink (#fff). No grey, no colour, no alpha — including hover.
- One self-hosted variable mono face at three widths: 75 for prose, 100 for data and labels, 112.5 for display.
- Tone from coverage: sub-pixel hairlines, bar-pattern fills, type weight and width.
- Full-frame inversion (white ground, black type) reserved for the lede, the standing question, and the close.
- Flat by construction — no shadow, no radius, no gradient except as a literal bar pattern.
- Static HTML with one classic script; opens by double-click from `file://`.

## Colors

A two-value palette. Everything else on the page is an arrangement of these two.

### Primary
- **Signal White** (`#fff`): all ink — type, hairline rules, bar fills, barcode strokes, focus outline. Also the *ground* of any inverted block, where the type turns black. This is the only mark-making colour the system has.

### Neutral
- **Absolute Ground** (`#000`): the page background, the topbar background, and the type colour inside inverted blocks. It is never softened toward charcoal.

### Named Rules

**The Two-Value Rule.** The palette is `#000` and `#fff`. No grey, no colour, no `rgba()`, no `opacity` below 1 anywhere in the system — including hover, focus and disabled states. If a value looks like it needs to be quieter, change its *coverage*, its hairline weight, or its type weight and width. A hex that is not `#000` or `#fff` is a defect.

**The Coverage-Not-Alpha Rule.** Apparent grey is produced by pure-white geometry at low density. The canonical instance is the archive frame's proportional bar: the share sitting in review is a solid white run, and the remainder is a hairline box filled with a 1px-on-4px-off hatch. Both marks are `#fff`; only how much of the surface the ink covers changes, and the difference in coverage *is* the datum.

An earlier instance — an ambient 0.5px/7px hatch painted across every non-hovered row while a table was hovered — was removed at the user's request. Do not reintroduce a whole-table ambient state; row sampling is the solid inversion alone.

**The Inversion Rule.** Full-frame inversion (white ground, black type) is the loudest device in the system and is spent only on the lede, a standing question, and the close of a report. If a third inverted block appears on a screen, one of them is not load-bearing. Inverted blocks re-derive their own `::selection` and their own barcode so no white-on-white gap opens.

**The Print Exception.** `@media print` is the single place the ink values invert to `#fff` ground / `#000` type. That is a substrate change, not a palette change; nothing else may take that exemption.

## Typography

**Display Font:** Martian Mono — self-hosted variable WOFF2 at `fonts/martian-mono-latin.woff2`, `font-weight: 300 700`, `font-stretch: 75% 112.5%`, `font-display: swap`
**Body Font:** Martian Mono (same file, condensed register)
**Label/Mono Font:** Martian Mono (same file, normal register)
**Fallback stack:** `ui-monospace, 'SF Mono', Menlo, Consolas, monospace`

**Character:** One face doing three jobs. Monospace throughout, so every column of figures aligns without being asked; the variation axes do the work a second and third family would normally do. Extended and heavy reads as engineered signage; normal reads as instrument output; condensed and light reads as running prose that stays comfortable at 68ch despite being a mono.

### Hierarchy

- **Display** (`wdth` 112.5 / `wght` 700, `clamp(2.25rem, 7.5vw, 5.25rem)`, line-height 0.86, tracking −0.05em, uppercase): the masthead `h1` only — "PROJECT STATUS", "FRAMES". Set on clean ground with nothing behind it.
- **Headline** (`wdth` 112.5 / `wght` 700, `clamp(1.125rem, 2.4vw, 1.625rem)`, line-height 1.05, tracking −0.04em, uppercase): numbered section headings and the archive frame's date.
- **Title** (`wdth` 100 / `wght` 700, 0.8125rem, tracking 0.08em, uppercase): `h3` sub-headings inside a section.
- **Lede** (`wdth` 75 / `wght` 500, `clamp(1rem, 2.1vw, 1.375rem)`, line-height 1.5, tracking −0.025em, max 46ch): the one-paragraph statement inside an inverted block.
- **Body** (`wdth` 75 / `wght` 300, 0.9375rem → 0.875rem below 40rem, line-height 1.75, tracking −0.01em, measure 68ch): all running prose.
- **Data** (`wdth` 100 / `wght` 400, tabular figures, tracking 0): table cells (0.75rem), bar rows (0.6875rem), masthead rails (0.625rem), frame stats (0.625rem). Never tracked out; the tabular figures are the alignment mechanism.
- **Label** (`wdth` 100 / `wght` 600, 0.625rem — 0.5625rem inside rails, table heads and bar rows — tracking 0.16em, uppercase): eyebrow-free field names, table column heads, rail terms, nav.

### Named Rules

**The One-Face Rule.** The system has exactly one typeface. New weight or emphasis is bought on the `wght` and `wdth` axes of Martian Mono, never by importing a second family and never by falling back to a system display face. Emphasis inside prose stays in the condensed register: `strong` is `wdth` 75 / `wght` 700; `em` is `wdth` 75 / `wght` 300 with a 0.5px hairline underline rather than an italic.

**The Register Rule.** Width encodes what a thing *is*, not how important it is. 75 is prose, 100 is data and labels, 112.5 is display. A number typeset in the prose register or a sentence typeset in the data register is a category error, and it shows immediately because the columns stop lining up.

**The Tabular Rule.** Every quantity carries `font-variant-numeric: tabular-nums` — table cells, rails, bar rows, section numbers, finding numbers, frame indices. Figures that change between dated reports must not shift the layout under them.

## Layout

**Grid.** Two related grids share one rail token (`--rail`, 13.5rem desktop / 11rem below 78rem).

- The **masthead** (`.field`) is `rail | 1fr | rail`: a left numeric rail, the title stage, a right numeric rail.
- The **document shell** (`.shell`) is `rail | 1fr`: a sticky contents rail beside the report body.

Above them both, `.topbar` is sticky at `top: 0` and lives *outside* `.masthead` so it survives the scroll. The contents rail sticks at `top: 3rem` (clearing the topbar) with `max-height: calc(100vh - 3rem)` and its own overflow.

**Spacing rhythm.** A nine-step scale from 0.25rem to 7rem, roughly ×1.5 with flat runs where the build needed them (0.25 / 0.5 / 0.75 / 1 / 1.5 / 2 / 3 / 4.5 / 7rem). Sections are separated by 4.5rem, the document body is padded 3rem / 2rem / 7rem, and internal component padding lives between 0.5rem and 1.5rem.

**Measure.** Prose, sub-headings, findings and notes are capped at 68ch (`--measure`). Data is deliberately *not* capped to the reading measure — tables, bar fields and inverted blocks run to 62rem, because crushing a column to fit a text measure destroys the thing the reader came for.

**Responsive.** Columns thin and drop from the edges inward:

- **≤78rem** — the rail token narrows to 11rem and the masthead's right rail is dropped; the field becomes `rail | 1fr`.
- **≤60rem** — both masthead rails are gone and the field is a single column; the shell collapses to one column and **the contents rail is hidden entirely**, so the lede reaches the phone's first screen. The topbar's jump links are the only navigation that survives, which is why it is sticky at every width. Archive frames stack to a single column and their stat block gains a 0.5px top rule.
- **≤40rem** — body type drops to 0.875rem; the topbar shortens to 2.75rem and its nav becomes one horizontally scrolling row (never two rows that eat the viewport), scrollbar hidden; the masthead stage loses its 14rem minimum. Narrow tables release their 34rem `min-width` and are allowed to wrap and collapse to fit; only `table.wide` keeps its columns and scrolls inside its frame.

**Motion.** State transitions only, 0.12s–0.15s on `cubic-bezier(0.16, 1, 0.3, 1)`: table row 0.12s, archive frame 0.14s, topbar link underline 0.15s. There is **no entrance animation anywhere on the site** — no reveal, no stagger, no load sequence. A `prefers-reduced-motion` block collapses all durations to 0.001ms.

### Named Rules

**The Data-Escapes-The-Measure Rule.** Prose holds 68ch; tables and bar fields take the width they need up to 62rem. A number pushed off-screen or wrapped into a two-line cell to satisfy a text measure is a worse outcome than a wide block.

**The One-Row Topbar Rule.** The sticky bar is a single row at every width. Below 40rem its links scroll horizontally rather than wrapping, because on the phone read a second bar row costs the reader the only screen that matters.

## Elevation & Depth

**There are no shadows in this system, and there is no elevation.** Nothing is lifted, floated, blurred or layered. Depth does not exist as a metaphor here; the page is a printed sheet.

What separates one region from another is a **hairline rule** and a **change of ground**. Two rule weights carry the whole structure:

- **Full hairline** (`1px solid #fff`) — structural division: masthead bottom, topbar bottom, rail edges, section top rules, table outer frame, table head underline, note top and bottom, archive frame separators, footer top.
- **Half hairline** (`0.5px solid #fff`) — subordinate division inside an already-framed region: table body row separators, bar-field row separators, `code` outline, `em` underline, footer link underline. At 0.5px the browser antialiases it toward optical grey while the ink itself stays `#fff` — which is exactly the print behaviour the world is imitating.

Emphasis that a shadow would carry elsewhere is carried by **inversion** instead: a block or row swaps ground and ink outright.

### Named Rules

**The No-Depth Rule.** No `box-shadow`, no `filter`, no `backdrop-filter`, no gradient used as shading. The only `linear-gradient` permitted is a `repeating-linear-gradient` producing a literal bar pattern at full opacity.

**The Two-Weights Rule.** Rules come in exactly two weights, 1px and 0.5px, and the choice is structural: 1px frames a region, 0.5px divides inside one. A third weight is not available.

## Shapes

**Every corner is square.** No `border-radius` appears anywhere in the stylesheet — not on frames, tables, inverted blocks, bars, or the focus outline. The form language is orthogonal: rectangles, rules, and columns.

Recurring geometry:

- **The barcode mark** — the project's only mark, drawn as a `repeating-linear-gradient` of uneven vertical strokes (1px, 1px, 2px runs at 3/4/7/9/11px offsets) at three sizes: 1.5×0.75rem small, 2.25×1.125rem default, 4×1.5rem large. It is generated geometry, never an icon font, never an emoji, never an image file. It re-declares itself in `#000` inside any inverted or hovered surface.
- **The bar** — quantities drawn as a run of 3px-wide solid white ticks with 2px gaps, 0.75rem tall (`.bar i`), width set inline from the real figure. Never a sparkline, never a curve.
- **The proportion bar** — the archive variant, where a solid run (`i`) sits beside a hatched run (`u`, a 1px-on-4px pattern inside a 0.5px border). How much of the bar is solid is how much of the sprint is stuck in review.
- **The dashed edge** — the only broken border in the world, used exclusively to say "this scrolls further right".

**Focus** is a 2px solid white outline at 3px offset, square, applied via `:focus-visible` and never removed.

### Named Rules

**The Square-Corner Rule.** `border-radius: 0` everywhere, implicitly — the property is simply never written. A rounded corner is off-world.

**The Dashed-Edge Rule.** A dashed border means one thing and only one thing: content continues past this edge. It is never decorative and never used for emphasis.

## Components

### Topbar

Sticky at `top: 0`, `z-index: 20`, minimum 3rem tall (2.75rem below 40rem), black ground with a full hairline beneath. Left cell (`.topbar__mark`) holds the small barcode and the wordmark (`wdth` 112.5 / `wght` 700, 0.9375rem, tracking 0.1em, uppercase) behind a right hairline. Jump links sit right, in label type, underlined on hover by a `border-bottom` that transitions from transparent over 0.15s. It sits **outside** `.masthead` deliberately: below 60rem it is the only route to the section the reader opened the report for.

### Masthead

`.field` — a three-column band, full hairline below, no graphic and no background of any kind.

- `.field__stage` — the centre column, `min-height: 14rem`, contents pushed to the bottom (`justify-content: flex-end`) so the title sits on the baseline of the band.
- `.field__title` — the display `h1`, hard-broken across lines in the markup.
- `.field__meta` — a wrapping row of tabular facts beneath the title: date, sprint id, sprint window, and where the sprint stands.
- `.field__rail--l` / `--r` — definition lists of real measurements, label-cased terms over data-register values. Left rail carries the queue (in review, median age, done); right rail carries the counter-evidence (consumer API surface with delta, admin API surface, board moves in 48h, commits in 48h, repos at origin/main). The right rail drops at 78rem, the left at 60rem, and no figure is duplicated in the rails alone — losing them loses no unique content.

### MVP Readiness Strip

`.mvp` — the one sanctioned page-top graphic, requested by the user on 2026-08-07, sitting directly under the masthead with a full hairline below. A head row (`.label` title, a large tabular percentage at `wdth` 112.5/700, and right-aligned meta carrying the target date marked *provisional* and days remaining), then `.mvp__bar`: a 1.375rem flex row (1rem below 40rem) of hairline-outlined segments, one per rubric capability, `flex` = frozen weight, containing an absolute solid-ink `<i>` whose width is the evidence score. A zero-score capability is an **empty outline** — absence is drawn, never omitted. `.mvp__read` beneath states the encoding in one line, names the empty segments, and links to the method table in the appendix.

Rules the component must keep: the percentage is always written with `≈` and the word "estimate"; fill measures build evidence, never board acceptance; the capability names live in the appendix table, not crammed into the strip; and the strip stays pure data — no icons, no colour, no motion. Weights come from the rubric in the refresh skill and are frozen across editions so the strip is comparable date to date.

**Lives on two pages, not one** (owner, 2026-08-07): the dated report carries the full strip with its method paragraph; `index.html` carries the identical markup and fill values directly under its own masthead, so the archive shows MVP status without a click. Both are written from the same edition's numbers and must never disagree. `index.html`'s reading line links to the dated report's `#mvp-method` anchor rather than duplicating the capability table a third time.

### Inverted Block

`.invert` — white ground, black type, full hairline border, 1.5rem padding (1rem below 40rem). Carries the lede, a standing question, or a closing statement. It re-declares `::selection` inverted and re-draws any contained barcode in black.

### Contents Rail

Sticky beside the document at `top: 3rem`, right hairline, label-cased heading, an unstyled ordered list of jump links each prefixed by a fixed 1.25rem tabular number column so titles left-align regardless of index. Hover does not change colour — it thickens the link from `wght` 400 to 700 within the condensed register. Hidden entirely below 60rem.

### Section Header

`.sec__h` — a full hairline across the top of the section, then a baseline-aligned row of a two-digit section number (`wdth` 100 / `wght` 700, 0.75rem, tracking 0.1em) and the headline `h2`. The number is data, the title is display; the appendix uses an em-dash where a number would be. Section headers escape the prose measure (`max-width: none`) so the rule spans the column.

### Tables

The system's core component. Collapsed borders, 100% width, 34rem minimum (released below 40rem), data register throughout with tabular figures.

- **Frame:** `.tbl-wrap` carries the full hairline border *and* the `overflow-x: auto`, so the frame stays put while columns move under it.
- **Head:** label register, 0.5625rem, tracking 0.16em, uppercase, left-aligned, bottom-aligned, `white-space: nowrap`, full hairline beneath.
- **Body:** 0.5rem/0.75rem cells separated by half hairlines; the last row's rule is removed so it does not double the frame. Row-header cells (`tbody th`) go `wght` 600 and never wrap. `.r` right-aligns a numeric column; `.hi` promotes a cell to `wght` 700.
- **Hover:** the sampled row inverts to solid white ground with black type over 0.12s. Sibling rows are untouched — there is no ambient whole-table state. Contained `code` borders and bar fills restate themselves in black so nothing disappears.
- **Overflow marks:** `.scrolls` is the static no-JS default and errs toward telling the reader there is more; `ui.js` adds `.measured` (which restores a solid edge) and toggles `.is-clipped` from a real `scrollWidth − clientWidth − scrollLeft > 2` measurement on load, on scroll, and on a 120ms-debounced resize. The dashed right edge therefore clears the moment the reader reaches the end. `.wide` marks a table whose columns must survive at phone width and scroll rather than collapse.

### Bar Fields

`.bars` — a hairline-framed stack of rows, each `label | count | bar` (7.5rem / 3.25rem / 1fr), half hairline between rows. `.bars--share` adds a fourth column (7.5rem / 3.25rem / 3.25rem / 1fr) so a percentage printed by the source report is not dropped in translation. Bars are `aria-hidden`; the figure beside them is the accessible value. Below 40rem the columns tighten to 5.5rem-based tracks.

### Note

`.note` — full hairline above and below, no side borders, 1rem vertical padding, opened by a block label. This is where the report's caveats and measurement gaps live; the treatment is intentionally as prominent as a finding, because those caveats are content, not fine print.

### Findings

`.stack` is a 1rem-gapped grid of `.finding` rows. Each finding is a 2rem number column beside its prose, opened by a full hairline. The number is display register at 1.5rem, line-height 1, tabular — deliberately larger than the body it labels.

### Archive Frame

`.frame` — a whole-row link in the index: index number (4.5rem) | date and summary (1fr) | stats and proportion bar (12rem), 1.5rem/2rem padding, full hairline beneath. Hover **and** `:focus-visible` invert the entire row to white ground over 0.14s, with the barcode, the solid bar run and the hatched run all restating in black. Collapses to a single stacked column below 60rem, where the stats block gains a half-hairline top rule to keep the separation.

### Footer

`.foot` — full hairline above, 2rem padding, a wrapping space-between row of the large barcode, an identity line, and a link back to the archive. Links are underlined with a half hairline rather than `text-decoration`.

## Do's and Don'ts

### Do:

- **Do** keep the entire surface to `#000` and `#fff`. If something needs to recede, reduce its coverage (hairline weight, bar density) or its type weight and width.
- **Do** buy emphasis on the type axes: `wdth` 75 for prose, 100 for data and labels, 112.5 for display; `wght` 300–700 within a register.
- **Do** put `font-variant-numeric: tabular-nums` on every quantity, in every component.
- **Do** frame regions with the 1px hairline and divide inside them with the 0.5px hairline — those two weights only.
- **Do** let data escape the 68ch prose measure. Tables and bar fields run to 62rem.
- **Do** render whatever section structure the report actually has. The 05 Aug frame has five numbered sections; the 07 Aug frame has seven with sub-sections; only `#overview` and `#method` are stable across every date. Section titles are authored per report.
- **Do** show only real, measured quantities. Every figure on these pages comes from the Zoho board, the five repositories, or the four OpenAPI specs, and the reports name real colleagues — invented people, metrics or dates are out of bounds even in a mockup.
- **Do** state a frame's own measurement weakness on the page when it has one. The 05 Aug left rail says its queue age was measured from `Last Modified`, a reading the next frame corrects; that admission is content and keeps its position in the rail.
- **Do** measure overflow before marking it. `.scrolls` is the no-JS default; `.measured` / `.is-clipped` come from real geometry and clear when the reader reaches the end.
- **Do** keep the topbar sticky and one row tall at every width — below 60rem it is the only navigation left.
- **Do** ship every page as a self-contained static file with one classic `<script src>` at the end of `<body>`. It must open by double-click from `file://`.

### Don't:

- **Don't** reintroduce a decorative masthead graphic, canvas field, hero chart, or generative background. One was built here and removed at the user's explicit request; the masthead is type and rails on clean ground. The one sanctioned page-top graphic is the `.mvp` readiness strip, which the user requested on 2026-08-07 — it is pure data and stays that way.
- **Don't** add an entrance animation, load reveal, stagger, or scroll-triggered transition. Motion is state-change only, 0.12s–0.15s. There is currently none on load anywhere, and that is the state to preserve.
- **Don't** introduce grey, colour, `rgba()`, or any `opacity` below 1 — including on hover, focus, and disabled states. `@media print` is the only permitted departure.
- **Don't** use a second typeface, an icon font, an emoji, an SVG icon set, or a raster image. The barcode is the only mark, and it is drawn with a gradient.
- **Don't** round a corner, cast a shadow, or apply a blur or backdrop-filter. The only gradients allowed are `repeating-linear-gradient` bar patterns at full opacity.
- **Don't** use a dashed border for anything except "content continues past this edge".
- **Don't** spend full-frame inversion on more than the lede, a standing question, and the close. Its scarcity is what makes it land.
- **Don't** assume a fixed section schema, and never bend a report's structure to fit the template. If a layout only works when the prose is trimmed, the layout is wrong.
- **Don't** demote a report's caveats or measurement gaps into fine print. They are set at the same weight as findings on purpose.
- **Don't** add a framework, build step, bundler, npm dependency, or backend, and never write `type="module"` — module scripts are blocked by CORS on `file://` and would break the double-click open. Nothing may be fetched at runtime.
- **Don't** cross-reference dates in the chrome (trend charts, two-date comparison, follow-through tracking). Each frame stands alone; the archive is navigation only.
- **Don't** write anything into the five sub-repositories (`beevia-admin`, `beevia-admin-api`, `beevia-api`, `beevia-db-schema`, `beevia-mobile`) — a hard rule in `.claude/rules.md`.
