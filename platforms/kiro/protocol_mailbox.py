"""Kiro 协议邮箱注册 worker — usa Playwright (v11)."""
from __future__ import annotations

from typing import Callable

from platforms.kiro.core import KiroRegister


class KiroProtocolMailboxWorker:
    def __init__(
        self,
        *,
        proxy: str | None = None,
        tag: str = "KIRO",
        log_fn: Callable[[str], None] = print,
    ):
        self.proxy = proxy
        self.tag = tag
        self.log_fn = log_fn

    def run(
        self,
        *,
        email: str,
        password: str | None = None,
        name: str = "Kiro User",
        mail_token: str | None = None,
        otp_timeout: int = 120,
        otp_callback=None,
    ) -> dict:
        client = KiroRegister(proxy=self.proxy, tag=self.tag)
        client.log_fn = self.log_fn

        ok, result = client.register(
            email=email,
            pwd=password or None,
            name=name,
            otp_callback=otp_callback,
            otp_timeout=otp_timeout,
        )
        if not ok:
            raise RuntimeError(result.get("error", "Kiro registration failed"))
        return result
