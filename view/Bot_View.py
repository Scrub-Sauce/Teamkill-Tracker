import os
import discord

import random
from controller.Bot_Controller import *
from model.Teamkill import Teamkill
from dotenv import load_dotenv
from discord.ext import commands


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    # Loads the Discord token from .env
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # Creates the discord Client
    bot = commands.Bot(command_prefix='#', intents=intents, help_command=None)

    # Informs the user when running
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    @bot.command()
    async def test(ctx):
        records = fetch_user(123456)
        print(records)
        await ctx.send(f'{records}')

    @bot.command()
    async def help(ctx):
        await ctx.send(
            'Available commands: ```/help - List all commands\n/tk <@killer> <@victim> - Adds a TK to the tracker.\n/tk_remove\n/score - Produces the teamkill scoreboard.\n/history <@killer> - Produces a history of player\'s teamkills.\n/info - Provides information on the author.```')

    @bot.command()
    async def tk(ctx, killer: discord.Member, victim: discord.Member):
        tk_messages = [
            [f'{killer.mention} delivers a surprise performance, starring {victim.mention} as the unexpected guest star. The act for the night: Death by firing squad.', "https://media1.tenor.com/m/tYguIlmfrcoAAAAC/surprise-gifkaro.gif"],
            [f'{killer.mention} and {victim.mention} - redefining teamwork, one unexpected kill at a time.',"https://media1.tenor.com/m/4Puijom5EmAAAAAC/trust-fail-fall.gif"],
            [f'In the game of life, {killer.mention} just played the "unintentional takedown" card on {victim.mention}.',"https://media1.tenor.com/m/KVwKOENJzpQAAAAd/fedor-emelianenko-kevin-randleman.gif"],
            [f'Friendly fire: the secret weapon of {killer.mention}\'s strategic masterplan against {victim.mention}.',"https://media1.tenor.com/m/uUV4KxpD7jcAAAAd/plan-conspiracy.gif"],
            [f'{killer.mention} and {victim.mention} - proving that teamwork makes the dream work, even if it\'s a nightmare.',"https://media1.tenor.com/m/k0e1MR9Ra8IAAAAd/survivor-rowing.gif"],
            [f'Congratulations, {killer.mention}! You just earned the "Worst Wingman" award by taking down {victim.mention}.',"https://media1.tenor.com/m/ViRu1oYgODMAAAAC/south-park-cartman.gif"],
            [f'Is it a bird? Is it a plane? No, it\'s just {killer.mention} unintentionally wrecking {victim.mention}\'s day.',"https://media1.tenor.com/m/Bm87ctQSQBEAAAAC/birb-fly.gif"],
            [f'{killer.mention} takes the lead in the "Oops, I Did It Again" competition with {victim.mention} as a reluctant co-star.',"https://media1.tenor.com/m/OoFDdPceaQEAAAAd/oops-i-did-it-again.gif"],
            [f'Who needs enemies when you have allies like {killer.mention}? Poor {victim.mention}.',"https://media1.tenor.com/m/U7gBj-PISdgAAAAd/jump-fail-prank.gif"],
            [f'{killer.mention} just proved that when in doubt, shoot everything. Including {victim.mention}. Don\'t forget to check his body for snacks!',"https://media1.tenor.com/m/9mjeGBGkFZYAAAAC/guns-shooting.gif"],
            [f'Warning: {killer.mention} may cause sudden drops in team morale by taking out {victim.mention} at the worst times.',"https://media1.tenor.com/m/o-kpBv0RkcEAAAAC/soul-in-danger.gif"],
            [f'Did {killer.mention} just perform a magic trick? Poof! {victim.mention} disappears in a cloud of bullets.',"https://media1.tenor.com/m/beImWqThNaMAAAAd/gun-shooting.gif"],
            [f'Friendly fire: {killer.mention}\'s unique strategy to keep {victim.mention} on their toes.',"https://media1.tenor.com/m/TikTdDzl4zAAAAAC/magic-confetti.gif"],
            [f'In the grand saga of {killer.mention} versus {victim.mention}, today\'s chapter ends with an unexpected twist.',"https://media1.tenor.com/m/JBmnjSa2LJkAAAAC/plot-twist.gif"],
            [f'Brace yourselves for the {killer.mention} and {victim.mention} show - where every kill is an accidental masterpiece.',"https://media1.tenor.com/m/ASZh9wrkwv0AAAAC/aleph-zero-alephzero.gif"],
            [f'Hold onto your hats, folks! {killer.mention} just turned {victim.mention} into an unintentional food critic with only lead on the menu.',"https://media1.tenor.com/m/mXxNnrR5n4QAAAAd/good-great.gif"],
            [f'Move over, strategists! {killer.mention} just introduced the revolutionary "unintentional flanking" technique on {victim.mention}.',"https://media1.tenor.com/m/v6jejtzA8HAAAAAC/we-attack-their-weak-spot-eric-cartman.gif"],
            [f'{killer.mention} just demonstrated to {victim.mention} why warning labels exist.',"https://media1.tenor.com/m/Z0bIoPRxc2gAAAAC/fall-trip.gif"],
            [f'{killer.mention} and {victim.mention} - the pioneers of tactical chaos, bringing a whole new meaning to "friendly" competition.',"https://media1.tenor.com/m/TX8jMsh0EfAAAAAC/buggy-horse-and-buggy.gif"],
            [f'{killer.mention} and {victim.mention} - proving that sometimes the best strategy is no strategy at all.',"https://media.tenor.com/evpSQei_eb4AAAAM/plan-star-lord.gif"],
            [f'{victim.mention}, pleading won\'t save you. {killer.mention} Flux Pavilion just dropped the bass... "I CANT STOP, OP, OP..."',"https://media1.tenor.com/m/p460mRpZFKAAAAAC/dubstep-virtual.gif"],
            [f'Presenting the {killer.mention} and {victim.mention} circus - where every match is a tightrope walk of accidental takedowns.',"https://media1.tenor.com/m/H_0snmBb6ooAAAAd/i-love-lucy-shookt.gif"],
            [f'Is it strategy or is it chaos? {killer.mention} blurs the lines with {victim.mention} caught in the crossfire.',"https://media1.tenor.com/m/tTEkzwUcCI4AAAAC/homer-simpson-caught-in-the-crossfire-crossfire.gif"],
            [f'In the world of accidental eliminations, {killer.mention} channels their inner Private Pile on {victim.mention}',"https://media1.tenor.com/m/1If7h96cEwMAAAAd/full-metal-jacket-vincent.gif"],
            [f'{killer.mention} gave {victim.mention} a warriors death.',"https://media1.tenor.com/m/E_Vj-xkWCe4AAAAd/never-give-up-monty.gif"],
            [f'{killer.mention}, you killed {victim.mention}! Oh my god, you bastard!',"https://media1.tenor.com/m/6ll-AoP1rbkAAAAC/oh-my-god-they-killed-kenny-you-bastards.gif"],
            [f'{killer.mention} ait {victim.mention}\'s lunch.',"https://media1.tenor.com/m/exg-5PtJsxsAAAAC/ronswanson-parksandrec.gif"],
            [f'{killer.mention} had a Nam flashback and {victim.mention} looked like the charlie.',"https://media.tenor.com/9DlIOu67gyQAAAAM/vietnam-cats.gif"],
            [f'{killer.mention} just bulldozed {victim.mention} in true Jibby fashion. He would be so proud.',"https://media1.tenor.com/m/z2YFVt1kZPgAAAAd/killdozer-granby.gif"],
            [f'{killer.mention} gave {victim.mention} the Old Yeller treatment.',"https://media1.tenor.com/m/SQjR-ybf24EAAAAC/eat-shit-robot-chicken.gif"]
        ]

        rng = random.randint(0, (len(tk_messages) - 1))
        status_add_kill, tk_object = add_teamkill(killer, victim, ctx.guild)
        tk_occurence = tk_object.get_datetime().strftime("%m/%d/%y @ %I:%M %p")

        if status_add_kill:
            card = discord.Embed(title='Teamkill Logged!', color=discord.Color.dark_red() ,description=tk_messages[rng][0])
            card.add_field(name='Teamkill ID', value=tk_object.get_auto_id(), inline=True)
            card.add_field(name="Killer", value=killer.mention, inline=True)
            card.add_field(name="Victim", value=victim.mention, inline=True)
            card.set_image(url=tk_messages[rng][1])
            card.set_footer(text=f'Reported by {ctx.author.display_name} - {tk_occurence}',icon_url=ctx.author.avatar)
            await ctx.send(embed=card)
        else:
            await ctx.send(f"There was an error adding the TK please contact the TK Bot Administrator.")

    # async def tk_remove(ctx, killer, victim, kill_id):
    #
    # async def score(ctx):
    #
    # async def history(ctx):

    # Runs the discord client
    bot.run(TOKEN)