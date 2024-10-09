from dataclasses import dataclass, field
import discord
from dataclasses_json import dataclass_json
from dataclasses import asdict

@dataclass
class Character:
    display_name: str = ""
    trigger_name: str = ""
    persona_desc: str = ""
    persona_exmp: list[str] = field(default_factory=list)
    system_prompt: str = ""

@dataclass
class Message:
    author_name: str = ""
    author_id: str = ""
    is_bot: bool = True
    content: str = ""
    media: str = ""



