from dataclasses import dataclass, field


@dataclass
class QuestionItem:
    category: str
    question: str
    answer: str
    answer_format: str


@dataclass
class UserSession:
    selected_categories: set[str] = field(default_factory=set)
    remaining_indices: list[int] = field(default_factory=list)
    current_question_index: int | None = None
    awaiting_answer: bool = False
    answered_count: int = 0
