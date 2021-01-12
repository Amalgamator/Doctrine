# Refactoring and optimization, uniformity and a e s t h e t i c s.
*
* Decide on a help message format (look at how other bots do it)
* Manage help messages through file / db instead of in code. (embeds using strings from db / file)
* Have a look at send_help() https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context.send_help
* Make sure invocation is done correctly where applicable https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context.send_help
*

# Implement Features

## Main Features
```
d!help : pretty much this overview here, but prettier, more clear, useful and per command as well.
d!about : [alias = d!doctrine] provides more contextual information about the bot, our community, etc.
d!invite : [alies = d!discord] provides the permanent invite link to the discord
d!yt [alias = youtube, tube] provides the link to the youtube channel
d!
d!report : any argument passed will be sent to the git board. Intended as a bug/issue report feature. Reviewed before submitted as issue.
```
## Engine Features
```

d!tech ["tech"] : gives you in-depth information about a technology ["tech"] and ANY object it applies to
d!unit ["unit"] : gives you in-depth information about a unit ["unit"], best/worst counters, techs that apply to it
d!hasunit ["unit"] : shows all civs that have [unit]
d!hastech ["tech"] : shows all civs that have [tech]
d!cbonus [civ] : shows all civ bonuses and unique units / techs for [civ].
d!randmap [label] ([label] .... ) : selects a random map from the standard map pool, [label] constrains the pool by types.
                                    [label] can be (in no particular order):
                                        open/restricted (how wallable & bottlenecked the map is),
                                        land/hybrid/water (water: fully disconnected opponents by water),
                                        tc/-tc (false/true nomadic types),
                                        elev/-elev (true/false elevation),
                                        ponds/-ponds (true/false ponds in map, doesn't necessarily mean fish!)
d!randciv ["label"] (["label"] .... ) : selects a random civ from the civ pool,
                                    ["label"] can be a unit or tech (use "" or '' to avoid whitespace issues)
d!elo [playername/steamnumber] : gives you the 1v1 RM elo and TG RM elo of a player
d!welo [playername/steamnumber] : gives a weighted average of a player's 1v1 RM / 1v1 DM / TG RM / TG DM and custom games.
d!morelo [playername/steamnumber] : Shows an in-depth analysis of a player's ratings in all gametypes.
                                     (1) Preferred maps, preferred civs. (find preferences)
                                     (2) A map*civ matrix of winrates. (find weaknesses)
                                     (3) Smurfness estimator & Rating history.
                                     (4) Recordings link & Average game time.
d!hint : gives a random (obscure) fact about the game.
d!map ["mapname"] : tells you everything you need to know about a map.
                    - The spawning distances of starting resources
                    - A total average % breakdown of terrain by type (land, non-buildable land, water, shallow, forest, ...)
                    - A total resource breakdown by type and placement
                                   (start/neutral)
                                   (deepfish, fish, shorefish, hunt, herd, prey, trees, berries, gold, stone)
d!bo [civ] ["unit"*n,] ["building"*n,] ["tech,tech"] ( [teamciv,teamciv,teamciv] ) ( ["map"] ) ( ["name"] ) :
                                   generates a time-optimised build order based
                                   on an idealised simulation.
                                   ["map"] is optional, however, if no map is given, simulator will assume Arabia resources.
                                   ["name"] is required to save to web and share (2,3). alphanumeric, hyphen, dot and spaces only. 80chars.
                                   ["unit"*n] --> "unit name" times n, n the amount you want.
                                   the same for building. ["tech"] or a list of techs can be included.
                                   To add multiple unit types, separate them by comma only.
                                   [teamciv] applies the teambonus from that/those civ/civs if applicable
                     - Will respond with:
                             (1) A build order overlay txt file (for use in game)
                             (2) A link to the online version (web UI to share/edit/save and see more stats)
                             (3) BO: "Name" in MM:SS, (sharecode: ###########).
d!bo [code] : shows the response tied to that code
d!bo list : gives a list of the most popular BOs as logged by d!bo usage
d!bo web : responds with the link to the web version
```
### Misc features.
```
d!activity : shows a table for AoE2DE activity last 4 hours, 12 hours, day, week, month (steamapi, aoe2.net api)

d!rumpel : "What is a Rumpel?" -- Debbie, Wife of the Snek
d!thanks : a list of community members that have inspired or helped me.
d!donate : responds with a patreon / paypool link or something, to support development, server costs and Dev coffee/tea
d!tools : list of aoe2 tools
d!servers : list of important aoe2 discords
d!streams : list of noteworthy twitch streams
```
### Unsure Features
```
d!twitch : twitch integration, will check functionality later
d!twitch list : list of aoe2 twitch streamers
d!sustain [civ] ["unit"*n] (["unit"*n]) : shows you how much vils on each res you need for sustained production
                                          For example, [franks] [knight*10] [monk] --> 60f, 100g.
d!duel ["unit"] ["unit"] : simulates a number of 1v1 fights between two opposing player-controlled units, to see who comes out on top.
d!instahit ["unit"] ["unit"] ["tech"] ["tech"] : how many units, with perfect micro, does it take to insta-kill an opponent unit.
                                                 In other words, how many units in a control group.
d!members : number of discord servers using Doctrine bot
d!premium [code] : enables premium features for non-Doctrine guilds, they'll get a code after payment
d!premium members : number of discord servers using Doctrine bot premium features
```
