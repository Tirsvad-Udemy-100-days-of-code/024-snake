# RC-016: Review of DICT-001 (screenshot)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [988ebba] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. One row was added. Earlier record: [RC-003].
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also drafted the change)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All 29 rows have a PO term, `en`, an IT term and a definition; the new row `screenshot` is complete. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | `screenshot` maps to one IT term, the file `docs/images/snake-score-5.png`, and no other row uses that file. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists in this project. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists in this project. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | The new definition is one sentence in English. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | BC, SA, PP and MIL exist; the IT column says `none` because no source code uses the term. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | `Language` is `en` and `Domain` is `it`; every row is `en`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells of DICT-001, including the new and changed text and the new Version History row, are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is the one the registry gives for the type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001], including the new row `screenshot`, which is the word of S01's request and names the one file `docs/images/snake-score-5.png`. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The assistant, as stand-in for S01, reads English and knows the IT domain and checked the terms against [DICT-001]. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | No new abbreviation is introduced; PNG and HTTP are standard names. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that drafted the change, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. S01 accepted the plan that contains this change in chat on 2026-10-13; the verdict can be challenged in the run summary or on the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-20 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[988ebba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/988ebba060c1ec69728a7fa36b24bc70737096d8
