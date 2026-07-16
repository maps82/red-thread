from __future__ import annotations

from collections import defaultdict
from uuid import UUID

from red_thread.domain import Memory, Person, Project, Source, TimelineEvent


class InMemoryStorage:
    """Temporary bootstrap storage.

    Replace this with SQLAlchemy-backed persistence in the first implementation milestone.
    """

    def __init__(self) -> None:
        self.projects: dict[UUID, Project] = {}
        self.people: dict[UUID, Person] = {}
        self.sources: dict[UUID, Source] = {}
        self.memories: dict[UUID, Memory] = {}
        self.timeline: dict[UUID, TimelineEvent] = {}
        self.project_memories: dict[UUID, list[UUID]] = defaultdict(list)

    def add_project(self, project: Project) -> Project:
        self.projects[project.id] = project
        return project

    def add_person(self, person: Person) -> Person:
        self.people[person.id] = person
        return person

    def add_source(self, source: Source) -> Source:
        self.sources[source.id] = source
        return source

    def add_memory(self, memory: Memory) -> Memory:
        self.memories[memory.id] = memory
        self.project_memories[memory.project_id].append(memory.id)
        return memory

    def add_timeline_event(self, event: TimelineEvent) -> TimelineEvent:
        self.timeline[event.id] = event
        return event

    def search_memories(self, project_id: UUID, query: str, limit: int = 10) -> list[Memory]:
        terms = {term.casefold() for term in query.split() if term.strip()}
        candidates = [
            self.memories[memory_id]
            for memory_id in self.project_memories.get(project_id, [])
        ]

        def score(memory: Memory) -> tuple[float, float, float]:
            haystack = " ".join(
                [memory.title, memory.concise_summary, memory.full_text, *memory.tags]
            ).casefold()
            text_score = sum(1.0 for term in terms if term in haystack)
            return (text_score, memory.importance, memory.emotional_weight)

        return sorted(candidates, key=score, reverse=True)[:limit]
