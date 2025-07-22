"""
Basic smoke tests for Delpha MCP package.
"""

import os

os.environ["DELPHA_CLIENT_ID"] = "fake-client-id"
os.environ["DELPHA_CLIENT_SECRET"] = "fake-client-secret"


def test_import_package():
    import delpha_mcp

    assert delpha_mcp is not None


def test_main_entrypoint():
    from delpha_mcp import __main__

    assert hasattr(__main__, "main")
