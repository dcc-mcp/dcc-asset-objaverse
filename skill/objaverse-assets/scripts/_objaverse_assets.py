from __future__ import annotations

import importlib
import random
import shutil
from pathlib import Path
from typing import Any


LICENSE_NOTICE = {
    "dataset": "Objaverse",
    "dataset_license": "ODC-By v1.0",
    "asset_license_notice": "Individual objects use Creative Commons licenses; keep per-object license and attribution metadata with downloaded files.",
    "docs": "https://objaverse.allenai.org/docs/objaverse-1.0/",
}


def objaverse_module():
    try:
        return importlib.import_module("objaverse")
    except ImportError as exc:
        raise RuntimeError("Install the optional dependency first: python -m pip install objaverse") from exc


def clean_uids(uids: list[str]) -> list[str]:
    out = []
    for uid in uids:
        uid = str(uid).strip()
        if uid:
            out.append(uid)
    if not out:
        raise ValueError("At least one UID is required")
    return out


def sample_uids(limit: int, seed: int | None = None) -> list[str]:
    objaverse = objaverse_module()
    uids = objaverse.load_uids()
    limit = max(1, min(int(limit), len(uids)))
    if seed is None:
        return uids[:limit]
    rng = random.Random(seed)
    return rng.sample(uids, limit)


def annotations_for(uids: list[str]) -> dict[str, Any]:
    objaverse = objaverse_module()
    return objaverse.load_annotations(clean_uids(uids))


def download_glbs(uids: list[str], output_dir: str, download_processes: int = 1) -> dict[str, Any]:
    objaverse = objaverse_module()
    wanted = clean_uids(uids)
    cached = objaverse.load_objects(uids=wanted, download_processes=max(1, int(download_processes)))
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    copied = {}
    for uid, source in cached.items():
        source_path = Path(source)
        target = target_dir / source_path.name
        shutil.copy2(source_path, target)
        copied[uid] = str(target)
    return {"cached_files": cached, "files": copied, **LICENSE_NOTICE}
