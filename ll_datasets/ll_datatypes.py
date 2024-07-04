from dataclasses import dataclass


@dataclass(frozen=True)
class Text:
    text_id: int = None
    text: str = None
    text_metadata: dict = None

    def __post_init__(self):
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
             raise ValueError(f'missing {field_key} config property')

@dataclass(frozen=True)
class TokenizedText:
    text_id: int = None
    text: str = None
    text_metadata: dict = None
    sentences: list[dict] = None
    tokens: list[dict] = None

    def __post_init__(self):
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
             raise ValueError(f'missing {field_key} config property')

@dataclass(frozen=True)
class MaskedSentenceStr:
    idx: str = None
    text: str = None

    def __post_init__(self):
        for field_key in self.__dataclass_fields__.keys():
            if self.__getattribute__(field_key) is None:
                 raise ValueError(f'missing {field_key} config property')
