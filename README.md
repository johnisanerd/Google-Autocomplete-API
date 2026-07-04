# 🔎 Google Autocomplete API: search and place suggestions as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Autocomplete API.

**Actor page:** [apify.com/johnvc/google-autocomplete-api](https://apify.com/johnvc/google-autocomplete-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-autocomplete-api/input-schema](https://apify.com/johnvc/google-autocomplete-api/input-schema?fpr=9n7kx3)

Get the autocomplete suggestions Google shows as you type, for any query, as clean structured JSON. Pass one or many partial queries and get the ranked suggestion list for each. For location and place queries, these act as fast place suggestions you can pipe straight into a Maps or Places lookup. It is the lightweight front-end for query expansion, keyword research, and resolving partial searches.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Google-Autocomplete-API.git
   cd Google-Autocomplete-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-autocomplete-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-autocomplete-api-example.py
```

## Why Use This Google Autocomplete API?

Real suggestions, not guesses. These are the exact phrases Google offers in its type-ahead box, ranked by likelihood.

Clean, structured output. Every suggestion is one row with its source query and rank, ready to load into a dataframe, a keyword tool, or an AI pipeline.

Built for batch work. Pass many seed queries and expand them all in one run.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server to resolve a vague user request into concrete queries.

## Features

### Core Capabilities
- Autocomplete suggestions for one or many queries
- About ten ranked suggestions per query
- Localized by country and language
- A fast front-end for place queries before a Maps or Places lookup

### Data Quality
- One clean row per suggestion, tagged with its source query and rank
- Stable JSON shape, easy to load anywhere

## Usage Examples

### Basic Example
```json
{
  "queries": ["coffee near"]
}
```

### Advanced Example
```json
{
  "queries": ["coffee near", "best pizza in", "things to do in"],
  "gl": "us",
  "hl": "en"
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `queries` | `list[str]` | YES | - | One or more partial queries, e.g. `coffee near`. Each is completed independently. |
| `gl` | `str` | no | `"us"` | Two-letter country code, e.g. `us`, `gb`, `de`. |
| `hl` | `str` | no | `"en"` | Two-letter language code, e.g. `en`, `es`, `de`. |

## Output Format

Each item in the dataset is one suggestion:

```json
{
  "query": "coffee near",
  "position": 1,
  "value": "coffee near me"
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Autocomplete API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Autocomplete API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Autocomplete API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-autocomplete-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api`, using OAuth when prompted.
5. Ask Claude to run the Google Autocomplete API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Autocomplete API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-autocomplete-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Autocomplete API to expand queries and power suggestions in your product or AI agent.*

## Featured Tasks

Ready-to-run examples on the Apify Store, each targeting one keyword-research use case:

- [Get Long-Tail Keyword Ideas From Google Autocomplete](https://apify.com/johnvc/google-autocomplete-api/examples/get-long-tail-keyword-ideas-from-google-autocomplete?fpr=9n7kx3)
- [Get Question Keywords From Google Autocomplete](https://apify.com/johnvc/google-autocomplete-api/examples/get-question-keywords-from-google-autocomplete?fpr=9n7kx3)
- [Get Keyword Research Data as JSON From Google](https://apify.com/johnvc/google-autocomplete-api/examples/get-keyword-research-data-as-json-from-google?fpr=9n7kx3)
- [Find Negative Keywords for Google Ads](https://apify.com/johnvc/google-autocomplete-api/examples/find-negative-keywords-for-google-ads?fpr=9n7kx3)
- [Get Google Search Suggestions for Any Keyword](https://apify.com/johnvc/google-autocomplete-api/examples/get-google-search-suggestions-for-any-keyword?fpr=9n7kx3)

Last Updated: 2026.07.04
