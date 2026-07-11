---
name: objaverse-assets
description: Search Objaverse annotations and download Creative Commons GLB objects.
license: MIT
compatibility: "dcc-mcp-core 0.18+, optional Python package: objaverse"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - asset
      - objaverse
      - huggingface
      - creative-commons
      - glb
      - download
    search-hint: "objaverse, creative commons 3d dataset, hugging face 3d objects, glb download"
    tools: tools.yaml
    runtimes: runtimes.yaml
---

# Objaverse Assets

Use this skill to sample Objaverse UIDs, inspect annotations, and download GLB
objects. Preserve returned license and attribution metadata with downloaded
files.
