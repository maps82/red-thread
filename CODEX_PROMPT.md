# Suggested Codex Prompt

Continue bootstrapping Project Red Thread from this repository.

First read:

- `vision.md`
- `README.md`
- `docs/architecture.md`
- `docs/threat-model.md`

Then:

1. Inspect the current code and write a concise implementation plan.
2. Replace `InMemoryStorage` with SQLAlchemy 2 and SQLite.
3. Add Alembic migrations.
4. Add entities for Project, Person, Source, Memory, TimelineEvent, Tag, Summary, and MemoryLink.
5. Add SQLite FTS5 indexing for memory title, summary, full text, and tags.
6. Implement deterministic hybrid ranking using:
   - FTS score
   - tag overlap
   - people overlap
   - recency
   - importance
   - emotional weight
7. Implement MCP tools:
   - project_create
   - project_get
   - memory_add
   - memory_get
   - memory_search
   - memory_update
   - memory_delete
   - timeline_add
   - timeline_query
   - person_upsert
   - summary_get
   - summary_rebuild
   - context_bundle
   - export_project
   - delete_project
8. Preserve source text and epistemic status.
9. Add comprehensive tests.
10. Run pytest, Ruff, and mypy.
11. Summarize limitations and recommend the next milestone.

Keep the system local-first. Do not add cloud services or real personal data.
