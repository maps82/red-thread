# Architecture

## Design intent

Project Red Thread is a narrative-memory system, not a generic document-search application.

Its primary job is to preserve continuity across long-running conversations while keeping facts, interpretations, chronology, and sources distinguishable.

## Core layers

### 1. Source layer

Immutable or append-only material:

- chat excerpts
- screenshots
- imported transcripts
- manual notes
- structured user confirmations

A source may be referenced by multiple memories.

### 2. Narrative layer

Structured objects derived from or linked to sources:

- Project
- Person
- Relationship
- Memory
- Scene
- TimelineEvent
- Place
- Object
- Tag
- Question
- Contradiction
- Summary
- MemoryLink

### 3. Retrieval layer

Milestone 1 ranking should combine:

- full-text score
- explicit people overlap
- explicit tag overlap
- chronology proximity
- recency
- importance
- emotional weight
- unresolved-question relevance

The ranking must be deterministic and testable.

### 4. Context assembly layer

`context_bundle` should return a compact package containing:

1. project overview
2. relevant timeline
3. relevant detailed memories
4. unresolved questions
5. contradictions
6. recent developments
7. source references

The bundle must stay within a caller-provided token budget.

## Fact status

Every memory-like object must declare its epistemic status:

- `user_reported`
- `source_document`
- `assistant_inference`
- `user_theory`
- `unknown`

Confidence must not be used to disguise the difference between a report and an inference.

## Versioning

Updates should create a new version or preserve an audit trail.

Original source text must never be overwritten by a summary rebuild.

Useful link types include:

- `supersedes`
- `contradicts`
- `supports`
- `clarifies`
- `same_scene`
- `caused_by`
- `related_to`

## Storage

Milestone 1:

- SQLite
- SQLAlchemy 2
- FTS5
- filesystem attachments outside the database

Later:

- optional embeddings
- hybrid retrieval
- encrypted attachment storage
- remote MCP deployment
- per-project keys

## MCP tool surface

Initial target:

- `project_create`
- `project_get`
- `memory_add`
- `memory_get`
- `memory_search`
- `memory_update`
- `memory_delete`
- `timeline_add`
- `timeline_query`
- `person_upsert`
- `summary_get`
- `summary_rebuild`
- `context_bundle`
- `export_project`
- `delete_project`

## Ingestion philosophy

Do not silently ingest everything.

Preferred workflow:

1. AI proposes candidate memories.
2. User confirms, edits, or rejects them.
3. Confirmed records are stored with source references.
4. Summaries are rebuilt without replacing originals.
