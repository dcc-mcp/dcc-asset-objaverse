from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _objaverse_assets import download_glbs


@skill_entry
def main(uids: list[str], output_dir: str, download_processes: int = 1, **_: Any) -> dict[str, Any]:
    try:
        result = download_glbs(uids, output_dir, download_processes)
        return skill_success("Objaverse objects downloaded", **result)
    except Exception as exc:
        return skill_exception(exc, message="Failed to download Objaverse objects")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
