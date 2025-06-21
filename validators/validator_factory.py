from guardrails.hub import CompetitorCheck, RegexMatch, DetectPII, ToxicLanguage
from guardrails.types import OnFailAction

class ValidatorFactory:
    def __init__(self, config):
        self.config = config

    def competitor_check(self):
        return CompetitorCheck(
            self.config.get("competitors", []),
            on_fail=OnFailAction.EXCEPTION
        )

    def detect_pii(self):
        return DetectPII(on_fail=OnFailAction.EXCEPTION)

    def toxic_language(self):
        return ToxicLanguage(
            threshold=self.config.get("toxicity_threshold", 0.5),
            validation_method=self.config.get("toxicity_method", "sentence"),
            on_fail=OnFailAction.EXCEPTION
        )

    def regex_match(self):
        return RegexMatch(
            regex=self.config.get("regex_pattern"),
            on_fail=OnFailAction.EXCEPTION
        )
