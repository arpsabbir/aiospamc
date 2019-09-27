#!/usr/bin/env python3

import pytest

from aiospamc import Client
from aiospamc.options import MessageClassOption


@pytest.mark.integration
@pytest.mark.asyncio
async def test_verify_false(spamd):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)
    result = await c.ping()

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_check(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.check(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_headers(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.headers(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ping(spamd):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.ping()

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_process(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.process(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_report(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.report(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_report_if_spam(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.report_if_spam(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_symbols(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.symbols(spam)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_tell(spamd, spam):
    c = Client(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])
    result = await c.tell(message_class=MessageClassOption.spam, message=spam)

    assert result
