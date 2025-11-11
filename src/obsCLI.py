# main.py
import asyncio
from twitchController import TwitchChatBot
from obsController import ObsController

async def main():
    # ONE ObsController, created once at startup
    obsctl = ObsController()
    print(obsctl.get_version())
    print(f"Scenes found: {obsctl.get_scenes()}")
    print(f"Video Sources found: {obsctl.get_sources()}")
    print(f"Audio Sources found: {obsctl.get_input_names()}")

    # Pass it into the bot so the bot can use it
    bot = TwitchChatBot(obs_controller=obsctl)

    # Run the bot (and anything else you want in this loop)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
