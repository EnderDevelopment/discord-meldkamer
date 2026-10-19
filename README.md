# Discord Meldkamer

Discord Meldkamer is a Discord bot designed to facilitate reporting systems within Discord servers. It allows users to submit reports that are then forwarded to a designated police channel. This bot is ideal for communities that need an efficient way to manage and track user reports.

## Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/discord-meldkamer.git
   cd discord-meldkamer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

## Use

1. Invite the bot to your Discord server using the Discord Developer Portal.

2. Create a text channel named `politie` where reports will be forwarded.

3. Users can submit reports using the `!melding` command followed by their report:
   ```bash
   !melding This is a sample report.
   ```

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/f873d85e-a96c-41dc-9893-df667ffe3138?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=f873d85e-a96c-41dc-9893-df667ffe3138
