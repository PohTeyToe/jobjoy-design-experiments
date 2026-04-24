# Post-decision cleanup

After George (or Abdallah) picks a winner, run these manually. Nothing below executes automatically.

## Remove global skill installs

```bash
npx skills remove pbakaus/impeccable -g
npx skills remove leonxlnx/taste-skill -g
```

## Clean local caches and dev artifacts

```bash
rm -rf design-experiments/_digests
rm -rf design-experiments/fonts
rm -rf design-experiments/_source
rm -rf design-experiments/*/.playwright
rm -rf .claude/skills/huashu
```

## Archive the decision

```bash
# replace <winner> with the picked variant (faithful, recommended, impeccable, taste-frontend, huashu, baseline)
cp design-experiments/<winner>/final/rationale.md \
   Project_Docs/DESIGN_DECISION_<winner>.md
cp design-experiments/<winner>/final/critic-report.md \
   Project_Docs/DESIGN_DECISION_<winner>_critic.md
```

## Keep for SvelteKit port reference

Keep the winner's `final/index.html` and `final/preview.pdf` as reference while porting to SvelteKit + Paged.js. Delete the other variant directories:

```bash
# list surviving dir, then delete everything else under design-experiments/
```

Do not delete until SvelteKit port is complete.
