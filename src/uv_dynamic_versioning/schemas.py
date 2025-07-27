from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional
from dunamai import Style, Vcs


def _filter_dict(cls, data: dict):
    valid_fields = {f.name for f in cls.__dataclass_fields__.values()}
    
    result = {}
    for k, v in data.items():
        key = k.replace("-", "_")
        if key in valid_fields:
            result[key] = v
    return result


@dataclass
class BumpConfig:
    enable: bool = False
    index: int = -1

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**_filter_dict(cls, data or {}))


@dataclass
class UvDynamicVersioning:
    vcs: Vcs = Vcs.Any
    metadata: Optional[bool] = None
    tagged_metadata: bool = False
    dirty: bool = False
    pattern: str = "default"
    pattern_prefix: Optional[str] = None
    format: Optional[str] = None
    format_jinja: Optional[str] = None
    style: Optional[Style] = None
    latest_tag: bool = False
    strict: bool = False
    tag_dir: str = "tags"
    tag_branch: Optional[str] = None
    full_commit: bool = False
    ignore_untracked: bool = False
    commit_length: Optional[int] = None
    bump: Optional[bool] = False
    fallback_version: Optional[str] = None

    @cached_property
    def bump_config(self) -> BumpConfig:
        if self.bump is False:
            return BumpConfig()
        if self.bump is True:
            return BumpConfig(enable=True)
        return self.bump

    @classmethod
    def from_dict(cls, data: dict):
        data = _filter_dict(cls, data or {})
        if "vcs" in data and isinstance(data["vcs"], str):
            data["vcs"] = Vcs(data["vcs"])
        if "style" in data and isinstance(data["style"], str):
            try:
                data["style"] = Style(data["style"])
            except ValueError:
                data["style"] = None
        return cls(**data)


@dataclass
class Tool:
    uv_dynamic_versioning: Optional[UvDynamicVersioning] = None

    @classmethod
    def from_dict(cls, data: dict):
        data = _filter_dict(cls, data or {})
        if "uv_dynamic_versioning" in data and isinstance(data["uv_dynamic_versioning"], dict):
            data["uv_dynamic_versioning"] = UvDynamicVersioning.from_dict(data["uv_dynamic_versioning"])
        return cls(**data)


@dataclass
class Project:
    tool: Tool

    @classmethod
    def from_dict(cls, data: dict):
        data = _filter_dict(cls, data or {})
        if "tool" in data and isinstance(data["tool"], dict):
            data["tool"] = Tool.from_dict(data["tool"])
        return cls(**data)


@dataclass
class MetadataHookConfig:
    dependencies: Optional[list[str]] = None
    optional_dependencies: Optional[dict[str, list[str]]] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**_filter_dict(cls, data or {}))
