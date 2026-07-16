from __future__ import annotations

from datetime import date, datetime, timezone
from enum import StrEnum
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class FactStatus(StrEnum):
    USER_REPORTED = "user_reported"
    SOURCE_DOCUMENT = "source_document"
    ASSISTANT_INFERENCE = "assistant_inference"
    USER_THEORY = "user_theory"
    UNKNOWN = "unknown"


class DatePrecision(StrEnum):
    EXACT = "exact"
    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    APPROXIMATE = "approximate"
    UNKNOWN = "unknown"


class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str = ""
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


class Person(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    name: str
    aliases: list[str] = Field(default_factory=list)
    description: str = ""


class Source(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    source_type: Literal["chat", "image", "document", "manual_note"]
    title: str
    original_text: str = ""
    attachment_path: str | None = None
    created_at: datetime = Field(default_factory=utc_now)


class Memory(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    title: str
    full_text: str
    concise_summary: str
    fact_status: FactStatus
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    event_date: date | None = None
    date_precision: DatePrecision = DatePrecision.UNKNOWN
    people: list[UUID] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    source_ids: list[UUID] = Field(default_factory=list)
    emotional_weight: float = Field(default=0.5, ge=0.0, le=1.0)
    importance: float = Field(default=0.5, ge=0.0, le=1.0)
    unresolved: bool = False
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


class TimelineEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    title: str
    description: str
    event_date: date | None = None
    date_precision: DatePrecision = DatePrecision.UNKNOWN
    memory_ids: list[UUID] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)


class ContextBundleRequest(BaseModel):
    project_id: UUID
    current_query: str
    token_budget: int = Field(default=4000, ge=500, le=50000)
    people: list[UUID] = Field(default_factory=list)
    date_from: date | None = None
    date_to: date | None = None


class ContextBundle(BaseModel):
    project_overview: str
    relevant_timeline: list[TimelineEvent] = Field(default_factory=list)
    relevant_memories: list[Memory] = Field(default_factory=list)
    unresolved_questions: list[str] = Field(default_factory=list)
    contradictions: list[str] = Field(default_factory=list)
    recent_developments: list[str] = Field(default_factory=list)
    source_references: list[Source] = Field(default_factory=list)
