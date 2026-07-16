from red_thread.domain import FactStatus, Memory, Project
from red_thread.storage import InMemoryStorage


def test_memory_search_prefers_text_match() -> None:
    storage = InMemoryStorage()
    project = storage.add_project(Project(name="Fictional Project"))

    matching = storage.add_memory(
        Memory(
            project_id=project.id,
            title="Balcony scene",
            full_text="A quiet evening on the balcony.",
            concise_summary="A remembered balcony evening.",
            fact_status=FactStatus.USER_REPORTED,
            tags=["balcony", "summer"],
            importance=0.8,
        )
    )
    storage.add_memory(
        Memory(
            project_id=project.id,
            title="Unrelated scene",
            full_text="A train ride.",
            concise_summary="A train ride.",
            fact_status=FactStatus.USER_REPORTED,
            tags=["travel"],
            importance=1.0,
        )
    )

    results = storage.search_memories(project.id, "balcony")
    assert results[0].id == matching.id
