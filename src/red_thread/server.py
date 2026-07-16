from __future__ import annotations

from typing import Any
from uuid import UUID

from mcp.server.fastmcp import FastMCP

from red_thread.domain import (
    ContextBundle,
    ContextBundleRequest,
    FactStatus,
    Memory,
    Project,
)
from red_thread.storage import InMemoryStorage

mcp = FastMCP("Project Red Thread")
storage = InMemoryStorage()


@mcp.tool()
def project_create(name: str, description: str = "") -> dict[str, Any]:
    project = storage.add_project(Project(name=name, description=description))
    return project.model_dump(mode="json")


@mcp.tool()
def memory_add(
    project_id: str,
    title: str,
    full_text: str,
    concise_summary: str,
    fact_status: str = FactStatus.USER_REPORTED.value,
    tags: list[str] | None = None,
    importance: float = 0.5,
    emotional_weight: float = 0.5,
) -> dict[str, Any]:
    project_uuid = UUID(project_id)
    if project_uuid not in storage.projects:
        raise ValueError(f"Unknown project_id: {project_id}")

    memory = Memory(
        project_id=project_uuid,
        title=title,
        full_text=full_text,
        concise_summary=concise_summary,
        fact_status=FactStatus(fact_status),
        tags=tags or [],
        importance=importance,
        emotional_weight=emotional_weight,
    )
    storage.add_memory(memory)
    return memory.model_dump(mode="json")


@mcp.tool()
def memory_search(project_id: str, query: str, limit: int = 10) -> list[dict[str, Any]]:
    memories = storage.search_memories(UUID(project_id), query, limit)
    return [memory.model_dump(mode="json") for memory in memories]


@mcp.tool()
def context_bundle(
    project_id: str,
    current_query: str,
    token_budget: int = 4000,
) -> dict[str, Any]:
    request = ContextBundleRequest(
        project_id=UUID(project_id),
        current_query=current_query,
        token_budget=token_budget,
    )
    project = storage.projects.get(request.project_id)
    if project is None:
        raise ValueError(f"Unknown project_id: {project_id}")

    memories = storage.search_memories(request.project_id, current_query, limit=12)
    bundle = ContextBundle(
        project_overview=project.description or project.name,
        relevant_memories=memories,
    )
    return bundle.model_dump(mode="json")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
