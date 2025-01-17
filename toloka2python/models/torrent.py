from dataclasses import dataclass
from typing import Any, List


@dataclass
class Torrent:
    """Датаклас, який містить інформацію про торрент"""

    forum: str = ""
    forum_url: str = ""
    url: str = ""
    name: str = ""
    author: str = ""
    img: str = ""
    thumbnail: str = ""
    torrent_name: str = ""
    date: str = ""
    size: str = ""
    thanks: int = ""
    rating: int = ""
    torrent_url: str = ""
    files: List[Any] = None
    description: str = ""


@dataclass
class TorrentFile:
    """Датаклас, який містить інформацію про Список файлів завантаження"""

    folder_name: str = ""
    file_name: str = ""
    size: str = ""


@dataclass
class TorrentElement:
    """Датаклас, що містить інформацію про торрент зі списку торрентів під час пошуку"""

    forum: str
    forum_url: str
    url: str
    name: str
    author: str
    verify: bool
    torrent_url: str
    size: str
    status: str
    seeders: int
    leechers: int
    answers: int
    date: str


@dataclass
class TorrentAccount:
    """Датаклас, що містить інформацію про торрент зі списку торрентів з акаунта користувача"""

    forum: str
    forum_url: str
    name: str
    seeders: int
    leechers: int
    url: str
