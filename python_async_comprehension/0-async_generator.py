#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random


async def async_generator():
    """Generate 10 random numbers with a 1 second delay"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
