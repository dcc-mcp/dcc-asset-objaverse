from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _objaverse_assets import LICENSE_NOTICE, annotations_for


@skill_entry
def main(uids: list[str], **_: Any) -> dict[str, Any]:
    try:
        annotations = annotations_for(uids)
        return skill_success(
            "Objaverse annotations loaded",
            annotations=annotations,
            count=len(annotations),
            license=LICENSE_NOTICE,
        )
    except Exception as exc:
        return skill_exception(exc, message="Failed to load Objaverse annotations")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
