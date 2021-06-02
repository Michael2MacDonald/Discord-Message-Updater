# Discord Message Updater
A quick tool for updating a message sent by a bot on Discord.

Servers like to have information posts, however due to (reasonable) restrictions by
discord, these posts have to be edited by their original author.

This project solves that by storing the posts as markdown, and updating them in
Discord by a bot.

This project is originally by [hreeder](https://github.com/hreeder/) but he seams to have stopped supporting it and the github action no longer worked so I created a clone.

## Usage

Supply the following environment variables:
* `DISCORD_TOKEN` - Your discord bot token
* `DISCORD_CHANNEL` - Discord Channel ID in which to make the post

Optionally supply:
* `POST_FILE` - A path to the file containing the post content. Defaults to
  `/etc/discord-message-updater/post`.
* `DISCORD_MESSAGE` - If not supplied, the bot will update the last message in the
  channel. If supplied as `new` the bot will make a new post, and if supplied as a
  message ID, it will update the specified message.

```yaml
- uses: michael2macdonald/discord-message-updater
  with:
    discord_token: ${{ secrets.discord_bot_token }}
    post_file: README.md
    discord_channel: '1234567890' # N.B. The quote marks here are required
    discord_message: new # Optional, use quotes if specifying an ID
```
