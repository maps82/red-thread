# Threat Model

## Protected data

Potentially sensitive data may include:

- personal histories
- health information
- relationship details
- private messages
- screenshots
- names and contact information
- inferred psychological interpretations

## Main risks

### Accidental source control exposure

Real data, screenshots, SQLite files, and exports must not be committed.

### Over-collection

The system should not automatically store every sentence.

### Hallucinated memory

Assistant-generated interpretations must never be stored as confirmed facts without user approval.

### Silent mutation

Summaries must not overwrite original source material.

### Local machine compromise

Local-first is not equivalent to encrypted.

Disk encryption and encrypted backups are recommended.

### Remote MCP exposure

A future remote server would require:

- TLS
- strong authentication
- per-user authorization
- audit logging
- rate limiting
- encrypted backups
- strict attachment access controls

## Initial safeguards

- local-only operation
- explicit user confirmation
- append-only source records
- export and deletion tools
- no secrets in repository
- no real personal seed data
