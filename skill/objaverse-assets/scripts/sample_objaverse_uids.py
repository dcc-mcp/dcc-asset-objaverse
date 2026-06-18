from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _objaverse_assets import LICENSE_NOTICE, sample_uids


@skill_entry
def main(limit: int = 20, seed: int | None = None, **_: Any) -> dict[str, Any]:
    try:
        uids = sample_uids(limit, seed)
        return skill_success("Objaverse UIDs sampled", uids=uids, count=len(uids), license=LICENSE_NOTICE)
    except Exception as exc:
        return skill_exception(exc, message="Failed to sample Objaverse UIDs")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
