# Antigravity Bible Study Agents

Welcome to the **Antigravity Bible Study Agents** ecosystem. This repository is configured specifically as a local workspace extension for the **Google Antigravity** agentic development platform, featuring an integrated team of 9 customized agent personas, 110 standalone exegesis/theology skills, and 110 custom slash commands.

This repository works with all antigravity platform, Antigravity, Antigravity IDE, Antigravity CLI. Official downloads at: https://antigravity.google/download

---

## Directory Structure

All agentic configurations are self-contained under the `.agents/` folder at the root:

```
.agents/
├── agents.md             # Custom AI team personas and guidelines
├── skills/               # Standalone, modular exegesis and study skills
│   ├── outline/
│   ├── sermon/
│   ├── translate_greek/
│   └── ... (110 total skills)
└── workflows/            # Parameterized slash command workflows
    ├── outline.md
    ├── sermon.md
    └── ... (110 total slash commands)
```

---

## Quick Start & Auto-Discovery

Because this repository is already configured with the standard Antigravity workspace schema, there is **zero manual configuration or agent registration required** to load the custom personas, skills, and workflows when you open this project folder in your IDE.

1. **Open Workspace**: Open the workspace root directory in your Antigravity-integrated IDE (such as Cursor or VS Code configured with the Antigravity extension) or run the CLI inside this directory:
   ```bash
   agy
   ```
2. **Auto-Discovery**: Antigravity automatically detects the `.agents/` directory at the project root. It will:
   - Load the 9 custom personas from `agents.md` into the agent selection registry.
   - Register the 110 skills in `.agents/skills/` for progressive disclosure.
   - Expose the 110 workflow files in `.agents/workflows/` as native slash commands.

3. **Meet System Prerequisites**: To run local Scripture database lookups and document conversions, please make sure the [System Prerequisites](#system-prerequisites) are installed on your machine.

4. **Running Slash Commands**: In the Antigravity chat input, type `/` to bring up the commands menu, followed by arguments (e.g. references, topics, or words):
   - `/outline Ephesians 1`
   - `/sermon Romans 8:28`
   - `/translate_greek John 1:1`

For a full reference of all available slash commands and usage examples, see the [Slash Commands Reference Guide](docs/slash_commands.md).

---

## System Prerequisites

To utilize the core capabilities of the local Bible study tools (such as database lookups and document exports), you must ensure the following dependencies are installed on your system:

1. **Local Bible Databases (`biblematedata`)**:  
   To enable local Scripture database lookups, you need to install the `biblematedata` package and initialize it:
   ```bash
   pip install --upgrade biblematedata
   biblematedata
   ```
   *Note: For more details on configuring database files, refer to the official [biblemate repository](https://github.com/eliranwong/biblemate).*

2. **Document Converter (`pandoc`)**:  
   To convert your study guides, outlines, and sermons into formats like Microsoft Word (`.docx`), ensure `pandoc` is installed on your system:
   - **macOS**: `brew install pandoc`
   - **Windows**: `winget install JohnMacFarlane.Pandoc` (or download the setup installer)
   - **Linux**: `sudo apt install pandoc` (or equivalent package manager command)

---

## Setting Up a New Repository

If you wish to bring these custom Bible study agents and tools into a **different, brand-new repository** of your own, follow these steps:

1. **Copy Configuration & Preferences (Choose one method)**:
   - **Method A - Git users (Recommended)**: **Fork** this repository on GitHub and `git clone` it. This is highly recommended because when you write your own studies, generate exports, and run the `/sync` command, all changes will be synchronized cleanly to your own personal remote repository.
   - **Method B - Manual Copy**: Manually copy the `.agents/` and `preferences/` folders from the root of this repository into the root of your new project. Google Antigravity will automatically discover the custom personas, skills, and workflows, while the `preferences/` folder preserves your default database preferences.

2. **Install System Prerequisites**: Ensure you have configured the [System Prerequisites](#system-prerequisites) on your system.

---

## Preferences & Customization

You can easily configure your preferred default versions for Bible translation, commentary, and lexicon lookups without modifying any code. To do this, edit the plain text files under the `preferences/` folder at the root of the repository:

- **Bible Default Version**: Set your preference (e.g. `NET`, `KJV`, `ESV2016`) in [preferences/bible.md](file:///Users/admin/dev/antigravity_bible_agents/preferences/bible.md).
- **Commentary Default Version**: Set your preference (e.g. `AIC`, `BI`, `BARNES`) in [preferences/commentary.md](file:///Users/admin/dev/antigravity_bible_agents/preferences/commentary.md).
- **Lexicon Default Version**: Set your preference (e.g. `SECE`, `BDB`, `Thayer`) in [preferences/lexicon.md](file:///Users/admin/dev/antigravity_bible_agents/preferences/lexicon.md).

These files are dynamically read by the respective retrievers on every execution.

---

## Documentation

For in-depth details about the workflows, slash commands, and team structure, please refer to the files under the [docs/](file:///Users/admin/dev/antigravity_bible_agents/docs) directory:

- **[ai_team_personas.md](file:///Users/admin/dev/antigravity_bible_agents/docs/ai_team_personas.md)**: Detailed profiles, guidelines, and expertise profiles for each of the 9 custom AI study personas.
- **[slash_commands.md](file:///Users/admin/dev/antigravity_bible_agents/docs/slash_commands.md)**: A complete reference guide for all 110 custom slash commands (workflows), organized by study category with syntax examples.
- **[README.md (Documentation Index)](file:///Users/admin/dev/antigravity_bible_agents/docs/README.md)**: Index and overview of repository documentation.
