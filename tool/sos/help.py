import asyncio

from prettytable import PrettyTable
from pyrogram import filters, Client
from pyrogram.types import Message

from tool.main import CMD_HELP
from tool.sos.utility import split_list

heading = "──「 **{0}** 」──\n"
