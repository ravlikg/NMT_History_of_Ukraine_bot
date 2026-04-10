import json

from app.models import QuestionItem


def load_questions(path: str) -> tuple[list[QuestionItem], list[str]]:
    with open(path, "r", encoding="utf-8") as file:
        raw_items = json.load(file)

    questions: list[QuestionItem] = []
    categories: list[str] = []
    seen_categories: set[str] = set()

    for item in raw_items:
        question = QuestionItem(
            category=item["category"],
            question=item["question"],
            answer=item["answer"],
            answer_format=item["format"],
        )
        questions.append(question)
        if question.category not in seen_categories:
            seen_categories.add(question.category)
            categories.append(question.category)

    return questions, categories
