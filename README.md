# RADAN55.github.io

EL Publishing — free English learner teaching resources by Richard A. Daniel, M.Ed.,
ENL/EL Specialist, Laurel High School.

Live at **https://radan55.github.io/**

## The one rule that keeps this working

**Every file sits at the root of the repo. There are no folders.**

That is deliberate. GitHub's web uploader only preserves folders when you drag a folder into the
drop zone; if you pick files through the file dialog, it flattens them and every link that points
into a folder breaks. Keeping everything flat makes that impossible.

Each HTML file is also fully self-contained — images are embedded inside the file rather than
linked from an images folder — so a page can never lose its pictures no matter how it is uploaded.

## Files

| File | What it is | URL |
| --- | --- | --- |
| `index.html` | The hub page that links to everything | `radan55.github.io/` |
| `hispanic-heritage.html` | 30 bilingual biography profiles, all illustrations embedded (3.8 MB) | `radan55.github.io/hispanic-heritage.html` |
| `language-bridge-2026-09.html` | Faculty bulletin, September 2026, cover embedded | `radan55.github.io/language-bridge-2026-09.html` |
| `elpa21-practice-student.pdf` | Student practice packet, 16 pages | `radan55.github.io/elpa21-practice-student.pdf` |
| `elpa21-practice-teacher.pdf` | Teacher edition, 13 pages | `radan55.github.io/elpa21-practice-teacher.pdf` |
| `.nojekyll` | Empty file that turns off the Jekyll build | — |

## First-time setup

1. Create a new **public** repository named exactly `RADAN55.github.io`. The name has to match the
   account name — that is what makes it a user site served from the root of the domain.
2. Add file → Upload files. Drag in every file listed above, including `.nojekyll`. Commit to
   `main`.
3. Settings → Pages. Source should read *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. Wait for the status dot next to the commit to turn green, then open `radan55.github.io`.

If `.nojekyll` is invisible after unzipping, your computer is hiding dot-files. Windows: View →
Show → Hidden items. Mac: Cmd+Shift+period. Or create it in GitHub: Add file → Create new file,
name it `.nojekyll`, leave it empty, commit.

## Adding the next resource

1. Name the file for what it is, in lowercase with hyphens: `language-bridge-2026-10.html`,
   `newcomer-survival-guide.pdf`. Dates go as `YYYY-MM` so files sort in order.
2. Upload it to the root alongside everything else.
3. Add a card to `index.html`. Copy an existing `<a class="card">` block, change the `href`, the
   `kind` label, the heading, the description and the three `meta` tags.
4. Commit both files in the same upload so the hub never links to something that isn't there yet.

Keep new HTML self-contained. If a page needs images, embed them as base64 data URIs rather than
adding an images folder.

## The old repositories

The earlier project repos still work at their own addresses — `radan55.github.io/<repo-name>/` —
and nothing here breaks them. As you move a resource into this site, either delete the old repo or
replace its `index.html` with a one-line redirect:

```html
<meta http-equiv="refresh" content="0; url=https://radan55.github.io/hispanic-heritage.html">
```

Worth cleaning up eventually: `hispanicheritagemonth` and `hispanicheritagemonth2026` hold the same
project, and there are four variations on the Language Bridge name.

## Reuse

Other educators are welcome to adapt these for their own buildings. Compliance content is written
to Mississippi requirements and should be checked against your own state's before republishing.

Contact: richard.spanishteacher@gmail.com

## Adding or changing a resource

Everything on the hub comes from one file: `tools/catalog.py`. Add the entry
there — href, title, group, format, size and one line of description — then run

    python3 tools/build.py

That writes the home page's four doors and Now Showing band, every row of
`all.html`, the Hub Guide's catalog, `catalog.json` (which the personal site
reads), the resource counts and the full-text search index. Nothing about a
resource is typed in two places, and every count is written into the HTML
itself rather than calculated by a browser, so a search engine or a link
preview sees the right number too.

Mark a resource `core=True` to star it in the index and put it on the home
page. Add its release date to `NEW` to make it the Now Showing hero for three
weeks, and a date in `PIN` to make it the resource of the week until then.
