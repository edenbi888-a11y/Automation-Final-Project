


class AIUtils:
    @staticmethod
    def analyze_test_result(prompt):
        """
        מנתח את נתוני הטסט ומחזיר החלטה אם מדובר בבאג
        """
        prompt_lower = prompt.lower()
        
        # זיהוי באג של מחרוזת ארוכה (שבירת UI)
        if "aaaaa" in prompt_lower or "long string" in prompt_lower:
            return "DECISION: BUG. Reason: UI Overflow. Long strings break the table layout and push buttons off-screen."

        # זיהוי באג של רווחים (בעיה לוגית)
        if "'    '" in prompt or "only spaces" in prompt_lower:
            return "DECISION: BUG. Reason: Validation Error. The system should not accept spaces as a valid name."

        # התנהגות תקינה
        return "DECISION: PASSED. The system behaved as expected or showed a correct alert."