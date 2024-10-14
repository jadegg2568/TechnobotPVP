from javascript import require, On
import asyncio
import config

mineflayer = require("mineflayer")
pathfinder = require("mineflayer-pathfinder").pathfinder
pvp = require("mineflayer-pvp").plugin


async def console_input():
    global bot
    loop = asyncio.get_event_loop()
    while True:
        label = await loop.run_in_executor(None, input, "TECHNO-DDOS > ")
        split = label.split(" ")
        name = split[0]
        args = split[1:]

        if name == ".end":
            exit()

        elif name == ".pvp":
            if len(args) < 1:
                continue
            try:
                username = args[0]

                if username == "stop":
                    bot.pvp.stop()
                    print("Stopped attacking.")
                else:
                    player = bots[0].players[username]
                    if player == None:
                        print(f"Player {username} wasn\'t found.")
                    else:
                        bot.pvp.attack(player.entity)
                        print(f"Attacking {username}.")

            except Exception as e:
                print(e)

        elif name.startswith("."):
            print("Command wasn\"t found.")

        else:
            try:
                bot.chat(label)
            except:
                pass


async def setup():
    global bot
    bot = mineflayer.createBot({
        "host": config.host,
        "port": config.port,
        "username": config.username,
    })
    bot.loadPlugin(pathfinder)
    bot.loadPlugin(pvp)


async def main():
    bot_task = asyncio.create_task(setup())
    input_task = asyncio.create_task(console_input())
    await asyncio.gather(bot_task, input_task)


if __name__ == "__main__":
    asyncio.run(main())