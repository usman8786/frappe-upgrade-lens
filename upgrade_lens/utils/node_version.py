"""Resolve Node.js version without spawning subprocess (Frappe Cloud marketplace audit)."""

from __future__ import annotations

import os
import re
from pathlib import Path

_VERSION_FILE_NAMES = (".nvmrc", ".node-version")
_VERSION_PATTERN = re.compile(r"^v?(\d+(?:\.\d+)*)$")


def get_node_version() -> str | None:
	"""Return the bench Node version from env or version files, if available."""
	import frappe

	for candidate in (
		os.environ.get("NODE_VERSION"),
		_read_version_file(Path(frappe.get_site_path("..", ".."))),
	):
		if normalized := _normalize_version(candidate):
			return normalized
	return None


def _read_version_file(bench_path: Path) -> str | None:
	for name in _VERSION_FILE_NAMES:
		version_file = bench_path / name
		if not version_file.is_file():
			continue
		try:
			content = version_file.read_text(encoding="utf-8").strip()
		except OSError:
			continue
		if content:
			return content
	return None


def _normalize_version(version: str | None) -> str | None:
	if not version:
		return None

	version = version.strip()
	if version.lower().startswith("v"):
		version = version[1:]

	if not _VERSION_PATTERN.match(version):
		return None

	parts = version.split(".")
	if len(parts) == 1:
		return f"v{parts[0]}.0.0"
	if len(parts) == 2:
		return f"v{parts[0]}.{parts[1]}.0"
	return f"v{version}"
