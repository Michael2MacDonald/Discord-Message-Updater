# Discord Message Updater
A quick tool for updating a message sent by a bot on Discord.

Servers like to have information posts, however due to (reasonable) restrictions by
discord, these posts have to be edited by their original author. This makes updating "Rules" or "README" messages sent by bots hard. You have to use long commands that you forget all the time and it is a pain.

This project solves that by storing the posts as markdown on GitHub so you can easily edit them and then automaticly updating them in
Discord throught the bot.

This project is originally by [hreeder](https://github.com/hreeder/) but he seams to have stopped supporting it and the github action no longer worked so I created a clone. Here is the original repo: [github.com/hreeder/discord-post-updater](https://github.com/hreeder/discord-post-updater) 

## Usage

Supply the following environment variables:
* `DISCORD_TOKEN` - Your discord bot token
* `DISCORD_CHANNEL` - Discord Channel ID in which to make the post

Optionally supply:
* `MESSAGE_FILE` - A path to the file containing the post content. Defaults to
  `/etc/discord-message-updater/post` if not supplied.
* `DISCORD_MESSAGE` - ID of the message. `new` will make a new post. Message ID it will update the specified message. If not supplied, the bot will update the last message in the channel.

You have to add `uses: actions/checkout@v2` to the yml file or the path to the message file will not work

Example:
```yaml
- uses: actions/checkout@v2
- uses: michael2macdonald/discord-message-updater
  with:
    discord_token: ${{ secrets.DISCORD_BOT_TOKEN }}
    message_file: /messages/Rules.md
    discord_channel: '1234567890' # The quote marks here are required
    discord_message: new # Optional, use quotes if specifying an ID
```

My Working Example From One Of My Personal Projects:
```yaml
name: Discord Messages
on: workflow_dispatch

jobs:
 discord-messages:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
    - name: readme
      uses: michael2macdonald/discord-message-updater@v1.1.1
      with:
        discord_token: ${{ secrets.DISCORD_BOT_TOKEN }}
        post_file: /github/workspace/Discord-Posts/readme.md
        discord_channel: '829005760359825429'
        discord_message: '849769031313522731'
```
