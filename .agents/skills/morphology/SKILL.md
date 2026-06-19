---
name: morphology
description: Retrieve bible morphology data from the local morphology database for verse references or specific word/phrase queries.
---

# Bible Morphology Retrieval Skill

## Overview
This standalone skill enables any agent to retrieve word-by-word morphology details from the local SQLite database `/Users/admin/biblemate/data/morphology.sqlite`.

## Guidelines & Objectives
When executing this skill:
- Always run the python retriever script located at `.agents/skills/morphology/morphology_retriever.py`.
- Execute the script using: `python3 .agents/skills/morphology/morphology_retriever.py "<query>"` where `<query>` is the user input.
- Present the exact output of the script to the user, maintaining formatting.
