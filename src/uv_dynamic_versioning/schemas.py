from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property

from dataclasses_json import config, dataclass_json
from dunamai import Style, Vcs

@dataclass_json
@dataclass
class BumpConfig:
    enable: bool = False
    index: int = -1


@dataclass_json
@dataclass
class UvDynamicVersioning:
    vcs: Vcs = Vcs.Any
    metadata: bool | None = None
    tagged_metadata: bool = field(
        default=False, metadata=config(field_name="tagged-metadata")
    )
    dirty: bool = False
    pattern: str = "default"
    pattern_prefix: str | None = field(
        default=None, metadata=config(field_name="pattern-prefix")
    )
    format: str | None = None
    format_jinja: str | None = field(
        default=None, metadata=config(field_name="format-jinja")
    )
    style: Style | None = None
    latest_tag: bool = False
    strict: bool = False
    tag_dir: str = field(default="tags", metadata=config(field_name="tag-dir"))
    tag_branch: str | None = field(
        default=None, metadata=config(field_name="tag-branch")
    )
    full_commit: bool = field(default=False, metadata=config(field_name="full-commit"))
    ignore_untracked: bool = field(
        default=False, metadata=config(field_name="ignore-untracked")
    )
    commit_length: int | None = field(
        default=None, metadata=config(field_name="commit-length")
    )
    bump: bool | BumpConfig = False
    fallback_version: str | None = field(
        default=None, metadata=config(field_name="fallback-version")
    )

    @cached_property
    def bump_config(self) -> BumpConfig:
        if self.bump is False:
            return BumpConfig()

        if self.bump is True:
            return BumpConfig(enable=self.bump)

        return self.bump


@dataclass_json
@dataclass
class Tool:
    uv_dynamic_versioning: UvDynamicVersioning | None = field(
        default=None, metadata=config(field_name="uv-dynamic-versioning")
    )


@dataclass_json
@dataclass
class Project:
    tool: Tool


@dataclass_json
@dataclass
class MetadataHookConfig:
    dependencies: list[str] | None = None
    optional_dependencies: dict[str, list[str]] | None = field(
        default=None, metadata=config(field_name="optional-dependencies")
    )
