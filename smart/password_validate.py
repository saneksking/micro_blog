import re


class PasswordValidator:
    pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&-])[A-Za-z\d@$!%*#?&-]{8,}$'

    @classmethod
    def check(cls, password):
        status = bool(re.match(cls.pattern1, password))
        return status
