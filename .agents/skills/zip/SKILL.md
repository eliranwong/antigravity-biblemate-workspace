---
name: zip
description: Create manual_setup.zip containing .agents/ and preferences/ folders for manual repository setup.
---

# Zip Archive Skill

## Overview
This skill packages the `.agents/` configuration and `preferences/` directories into a single `manual_setup.zip` file at the repository root. This archive provides users with a convenient way to manually import the customized AI team personas, skills, workflows, and database preferences into their own new repositories.

## Guidelines & Objectives
When executing this skill:
1. **Remove Existing Archive**: Before creating a new zip file, always check for the existence of `manual_setup.zip` in the root of the repository. If it exists, delete it first to ensure the archive is built fresh.
2. **Execute Python Helper**: Run the zip creator script located at `.agents/skills/zip/zip_creator.py` by calling:
   ```bash
   python3 .agents/skills/zip/zip_creator.py
   ```
3. **Report Status**: Once the zip is created successfully, output a clear summary to the user confirming the location and contents of `manual_setup.zip`.
