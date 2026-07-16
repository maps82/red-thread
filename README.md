# Project Red Thread

A private, local-first narrative-memory system for long-running AI conversations.

This repository is an initial bootstrap. It intentionally starts small:

- a clear product vision
- a proposed domain model
- a minimal MCP server skeleton
- a local SQLite database
- deterministic retrieval foundations
- tests and development tooling

## Status

Very early prototype.

Nothing here should yet be trusted with irreplaceable data without backups.

## Goals for Milestone 1

- Store projects, people, memories, scenes, timeline events, tags, and sources.
- Keep reported facts separate from interpretations.
- Preserve source text.
- Search with SQLite FTS5 and structured filters.
- Produce a compact context bundle for an AI client.
- Export and delete a complete project.
- Run fully locally.

## Non-goals for Milestone 1

- Automatic ingestion of an entire ChatGPT export.
- Embeddings or vector databases.
- Remote hosting.
- Multi-user authentication.
- Fully autonomous memory writing.

## Quick start

Requires Python 3.12+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m red_thread.server
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
python -m red_thread.server
```

## Suggested next steps in Codex

1. Review `vision.md`.
2. Review `docs/architecture.md`.
3. Replace the placeholder in-memory tool implementations with SQLAlchemy models.
4. Add Alembic migrations.
5. Add SQLite FTS5.
6. Implement deterministic `context_bundle` ranking.
7. Add import support for exported chat transcripts.
8. Add encryption and a threat model review before storing sensitive attachments.

## Repository layout

```text
project-red-thread/
├── vision.md
├── README.md
├── pyproject.toml
├── .gitignore
├── docs/
│   ├── architecture.md
│   └── threat-model.md
├── src/red_thread/
│   ├── __init__.py
│   ├── domain.py
│   ├── server.py
│   └── storage.py
├── tests/
│   └── test_domain.py
└── data/
    └── attachments/
```

## Privacy

This project is intended to be local-first.

Do not commit real conversation exports, screenshots, API keys, or the SQLite database.
