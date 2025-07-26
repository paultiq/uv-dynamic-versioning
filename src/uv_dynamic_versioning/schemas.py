from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

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
    metadata: Optional[bool] = None
    tagged_metadata: bool = field(
        default=False, metadata=config(field_name="tagged-metadata")
    )
    dirty: bool = False
    pattern: str = "default"
    pattern_prefix: Optional[str] = field(
        default=None, metadata=config(field_name="pattern-prefix")
    )
    format: Optional[str] = None
    format_jinja: Optional[str] = field(
        default=None, metadata=config(field_name="format-jinja")
    )
    style: Optional[Style] = None
    latest_tag: bool = False
    strict: bool = False
    tag_dir: str = field(default="tags", metadata=config(field_name="tag-dir"))
    tag_branch: Optional[str] = field(
        default=None, metadata=config(field_name="tag-branch")
    )
    full_commit: bool = field(default=False, metadata=config(field_name="full-commit"))
    ignore_untracked: bool = field(
        default=False, metadata=config(field_name="ignore-untracked")
    )
    commit_length: Optional[int] = field(
        default=None, metadata=config(field_name="commit-length")
    )
    bump: Optional[bool] = False
    fallback_version: Optional[str] = field(
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
    uv_dynamic_versioning: Optional[UvDynamicVersioning] = field(
        default=None, metadata=config(field_name="uv-dynamic-versioning")
    )


@dataclass_json
@dataclass
class Project:
    tool: Tool


@dataclass_json
@dataclass
class MetadataHookConfig:
    dependencies: Optional[list[str]] = None
    optional_dependencies: Optional[dict[str, list[str]]] = field(
        default=None, metadata=config(field_name="optional-dependencies")
    )
