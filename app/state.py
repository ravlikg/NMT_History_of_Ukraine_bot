from app.models import UserSession


class AppState:
    def __init__(self, questions, categories) -> None:
        self.questions = questions
        self.categories = categories
        self.user_sessions: dict[int, UserSession] = {}

    def get_session(self, user_id: int) -> UserSession:
        if user_id not in self.user_sessions:
            self.user_sessions[user_id] = UserSession()
        return self.user_sessions[user_id]
