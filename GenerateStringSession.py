#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os
import asyncio
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", input("Enter API_ID: ")))
API_HASH = os.environ.get("API_HASH", input("Enter API_HASH: "))


async def main(api_id, api_hash):
    """generate StringSession for the current MemorySession"""
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(API_ID, API_HASH))
