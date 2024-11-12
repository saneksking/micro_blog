import subprocess
from dateutil import parser


class GitInfo:
    def __init__(self):
        self._weekdays = {
            0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'
        }

        self._months = {
            1: 'января',
            2: 'февраля',
            3: 'марта',
            4: 'апреля',
            5: 'мая',
            6: 'июня',
            7: 'июля',
            8: 'августа',
            9: 'сентября',
            10: 'октября',
            11: 'ноября',
            12: 'декабря'
        }

    def _get_russian_weekday(self, weekday):
        return self._weekdays.get(weekday, '')

    def _get_russian_month(self, month):
        return self._months.get(month, '')

    def get_last_commit_info(self):
        command = ['git', 'log', '-n', '1', '--format=%cd | %an', '--date=iso']
        result = subprocess.check_output(command, universal_newlines=True).strip()

        commit_date, commit_author = result.split(' | ')
        commit_date = parser.parse(commit_date)

        russian_weekday = self._get_russian_weekday(commit_date.weekday())
        russian_month = self._get_russian_month(commit_date.month)

        formatted_date = commit_date.strftime(f"{russian_weekday}, %d {russian_month} %Y, %H:%M:%S")

        return formatted_date, commit_author

    def get_info(self):
        last_commit_date, commit_author = self.get_last_commit_info()
        return f"Дата последнего коммита: {last_commit_date}. Автор: {commit_author}."
