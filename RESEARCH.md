# User brief and comparison

**User:** Maintainer distributing a repository or asset bundle between Linux, Windows and macOS.

**Pain:** Distinct Linux filenames can collapse after case and Unicode normalization; some cannot be checked out on Windows.

**Need:** Inferred from cross-platform filesystem constraints, not a verified request for this tool.

**Capability:** Read-only recursive sibling collision report with explicit Windows rules and Unicode normalization.

**Acceptance:** Detect case and NFC collisions, reserved basenames, nested non-collisions, invalid roots, and symlink cycles.

**Discovery:** Python tooling and cross-platform release checklists.

**Portfolio:** syncplan compares directory snapshots; pathmask matches patterns. Neither new product is copied or subdivided; this tool audits checkout portability.


## Search coverage

GitHub query `filename sanitize in:description`, sorted by stars descending; observation 2026-10-04T12:43:43.465081+00:00. The top ten search results were screened for relevance. Search is not an exhaustive global ranking. Established comparables outside that query were also inspected; highest-star relevant comparable found among this researched set is identified below. Stars are research context, not technical performance.

Highest-star relevant comparable found: [dharple/detox](https://github.com/dharple/detox), 447 stars.

| Comparable | Stars | Last push UTC | License | Workflow and tradeoff |
| --- | ---: | --- | --- | --- |
| [dharple/detox](https://github.com/dharple/detox) | 447 | 2026-07-12T02:21:55Z | BSD-3-Clause | Filename renaming utility; README states development is on hold. This MVP is read-only and reports sibling normalization collisions. |
| [parshap/node-sanitize-filename](https://github.com/parshap/node-sanitize-filename) | 372 | 2026-03-20T22:17:25Z | NOASSERTION | npm string sanitizer with documented reserved-character rules; issue 84 concerns superscript device names. |
| [thombashi/pathvalidate](https://github.com/thombashi/pathvalidate) | 296 | 2026-05-10T10:35:35Z | MIT | Python validation/sanitization library with multiple-platform CI; an established alternative for individual path validation. |

README installation and example workflows and available recent issues were inspected. Push time does not prove active support, and mature alternatives cover broader domains. No competitor installations or equivalent performance workloads were measured. Time to first result and runtime performance comparisons are unmeasured. Tests prove only this implementation. Demand is inferred unless an issue is linked explicitly; no users, adoption or results are fabricated.

Related public report: [superscript Windows device names](https://github.com/parshap/node-sanitize-filename/issues/84). This MVP recognizes COM/LPT superscripts as well as ordinary digits; it does not claim complete Windows compatibility.
