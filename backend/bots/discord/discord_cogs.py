import discord
from discord.ext import commands
import logging
from app.core.orchestration.queue_manager import AsyncQueueManager, QueuePriority
from app.db.supabase.auth import login_with_github
from bots.discord.discord_bot import DiscordBot
from bots.discord.discord_views import OAuthView

logger = logging.getLogger(__name__)

class DevRelCommands(commands.Cog):
    def __init__(self, bot: DiscordBot, queue_manager: AsyncQueueManager):
        self.bot = bot
        self.queue = queue_manager

    @commands.command(name="reset")
    async def reset_thread(self, ctx: commands.Context):
        """Reset your DevRel thread and memory."""
        user_id = str(ctx.author.id)
        cleanup = {
            "type": "clear_thread_memory",
            "memory_thread_id": user_id,
            "user_id": user_id,
            "cleanup_reason": "manual_reset"
        }
        await self.queue.enqueue(cleanup, QueuePriority.HIGH)
        self.bot.active_threads.pop(user_id, None)
        await ctx.send("Your DevRel thread & memory have been reset! Send another message to start fresh.")

    @commands.command(name="help_devrel")
    async def help_devrel(self, ctx: commands.Context):
        """Show DevRel assistant help."""
        embed = discord.Embed(
            title="DevRel Assistant Help",
            description="I can help you with Devr.AI related questions!"
        )
        embed.add_field(
            name="Commands",
            value=(
                "• `!reset` – Reset your DevRel thread and memory\n"
                "• `!help_devrel` – Show this help message\n"
                "• `!verify_github` – Link your GitHub account\n"
            ),
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command(name="verify_github")
    async def verify_github(self, ctx: commands.Context):
        """Get GitHub verification link."""
        try:
            logger.info(f"User {ctx.author.name}({ctx.author.id}) has requested for GitHub verification")

            oauth_result = await login_with_github()
            logger.info(f"OAuth result: {oauth_result}")
            oauth_url = oauth_result["url"]

            embed = discord.Embed(
                title="🔗 Verify GitHub Account",
                description="Click the button below to link your GitHub account \nAfter authorization, you'll be redirected to your GitHub profile.",
            )
            embed.add_field(
                name="ℹ️ Note:",
                value="The link expires in 5 minutes for security purposes.",
                inline=False
            )

            view = OAuthView(oauth_url, "GitHub")
            await ctx.send(embed=embed, view=view)

        except Exception as e:
            logger.error(f"Error in verify_github: {str(e)}")
            await ctx.send("Error generating GitHub verification link. Please try again.")
