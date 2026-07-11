---
name: morphology
description: Retrieve bible morphology data from the local morphology database for verse references or specific word/phrase queries. Use when the user runs /morphology or requests this BibleMate workflow.
---

# Bible Morphology Retrieval Skill

## Overview
This standalone skill enables any agent to retrieve word-by-word morphology details from the local SQLite database `~/biblemate/data/morphology.sqlite`.

## Guidelines & Objectives
When executing this skill:
- Always run the python retriever script located at `.grok/skills/morphology/morphology_retriever.py`.
- Execute the script using: `python3 .grok/skills/morphology/morphology_retriever.py "<query>"` where `<query>` is the user input.
- Present the exact output of the script to the user, maintaining formatting.
