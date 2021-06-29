from src.do_substitute import do_substitute, subs as subs_dict
from src.detection import MatchList, detectslash
import discord
from discord.ext import commands
import json
import os

bot = commands.Bot(command_prefix="$", help_command=None)

@bot.event
async def on_ready():
    print("Bot successfully run")

@bot.command()
async def help(ctx):
    await ctx.send("""
This is an ipa discord bot!
Tired of having to go to an ipa keyboard website?
Use the `$ipa` command and the text after it will look for any // and do a substitution

For example,
`$ipa i think its spelled /[epsilon][hit]/ rather than /[epsilon]j/`
will be returned as
`i think its spelled /ɛɪ/ rather than /ɛj/`

See `$subs` to see all the substitutions
    """)

@bot.command()
async def ipa(ctx, *, text: str):
    print(text)

    matches: MatchList = detectslash(text)

    for m in matches: print(matches)

    if matches is not []:
        substituted = do_substitute(text, matches)

        await ctx.reply(substituted)

@bot.command()
async def subs(ctx):
    await ctx.reply(f"```json\n{json.dumps(subs_dict, ensure_ascii=False, indent=4)}```")

if __name__ == '__main__':
    bot.run(os.environ.get("DISCORD_KEY")) # heroku env var