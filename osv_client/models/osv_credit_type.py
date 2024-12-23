from enum import Enum


class OsvCreditType(str, Enum):
    ANALYST = "ANALYST"
    COORDINATOR = "COORDINATOR"
    FINDER = "FINDER"
    OTHER = "OTHER"
    REMEDIATION_DEVELOPER = "REMEDIATION_DEVELOPER"
    REMEDIATION_REVIEWER = "REMEDIATION_REVIEWER"
    REMEDIATION_VERIFIER = "REMEDIATION_VERIFIER"
    REPORTER = "REPORTER"
    SPONSOR = "SPONSOR"
    TOOL = "TOOL"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
