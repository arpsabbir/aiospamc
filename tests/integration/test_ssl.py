#!/usr/bin/env python3

import pytest

import aiospamc


@pytest.mark.integration
@pytest.mark.asyncio
async def test_verify_false(spamd):
    result = await aiospamc.ping(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_check(spamd, spam):
    result = await aiospamc.check(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_headers(spamd, spam):
    result = await aiospamc.headers(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ping(spamd):
    result = await aiospamc.ping(host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=spamd['ssl']['cert'])

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_process(spamd, spam):
    result = await aiospamc.process(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_report(spamd, spam):
    result = await aiospamc.report(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_report_if_spam(spamd, spam):
    result = await aiospamc.report_if_spam(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_symbols(spamd, spam):
    result = await aiospamc.symbols(spam, host=spamd['ssl']['host'], port=spamd['ssl']['port'], verify=False)

    assert result


@pytest.mark.integration
@pytest.mark.asyncio
async def test_tell(spamd, spam):
    result = await aiospamc.tell(
        message=spam,
        message_class='spam',
        host=spamd['ssl']['host'],
        port=spamd['ssl']['port'],
        verify=False
    )

    assert result
