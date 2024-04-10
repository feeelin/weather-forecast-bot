import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher
from config import Settings
from handlers import basic as basic_router