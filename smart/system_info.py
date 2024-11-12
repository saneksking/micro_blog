import datetime
import psutil


class SystemInfoMasterBase:
    @staticmethod
    def make_string(n):
        symbols = ('kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%s" % n

    @staticmethod
    def make_string_percent(number):
        return f'{number}%'


class DiskInfoMaster(SystemInfoMasterBase):

    @staticmethod
    def _get_data(path):
        return psutil.disk_usage(path)

    @property
    def system_usage(self):
        d = self._get_data('/')
        return {
            'total': self.make_string(d.total),
            'percent': self.make_string_percent(d.percent),
            'free': self.make_string(d.free),
            'used': self.make_string(d.used)
        }


class InfoMaster(SystemInfoMasterBase):
    @property
    def boot_time(self):
        """Возвращает время загрузки системы, выраженное в секундах с начала эпохи."""
        return psutil.boot_time()

    @property
    def boot_time_str(self):
        return datetime.datetime.fromtimestamp(self.boot_time).strftime("%d.%m.%Y %H:%M:%S")


class CPUInfoMaster(SystemInfoMasterBase):

    @property
    def count(self):
        """Возвращает количество логических ядер ЦП.
        «логические процессоры» означают количество физических ядер,
        умноженное на количество потоков, которые могут выполняться на каждом ядре"""
        return psutil.cpu_count()

    @property
    def count_real(self):
        return psutil.cpu_count(logical=False)

    @property
    def percent(self):
        """Возвращает число с плавающей запятой, представляющее текущую
        загрузку ЦП в масштабе всей системы в процентах."""
        return psutil.cpu_percent(interval=1)

    @property
    def percent_str(self):
        return self.make_string_percent(self.percent)


class MemoryInfoMaster(SystemInfoMasterBase):

    @property
    def virtual(self):
        return psutil.virtual_memory()

    @property
    def total(self):
        """Общая физическая память"""
        return self.virtual.total

    @property
    def total_str(self):
        return self.make_string(self.total)

    @property
    def available(self):
        """память, которая может быть немедленно предоставлена процессам без перехода системы в своп."""
        return self.virtual.available

    @property
    def available_str(self):
        return self.make_string(self.available)

    @property
    def percent(self):
        """Процент использования"""
        return self.virtual.percent

    @property
    def percent_str(self):
        return self.make_string_percent(self.percent)

    @property
    def used(self):
        return self.virtual.used

    @property
    def used_str(self):
        return self.make_string(self.used)

    @property
    def free(self):
        return self.virtual.free

    @property
    def free_str(self):
        return self.make_string(self.free)

    @property
    def free_real(self):
        return self.free + self.available

    @property
    def free_real_str(self):
        return self.make_string(self.free_real)

    @property
    def active(self):
        return self.virtual.active

    @property
    def active_str(self):
        return self.make_string(self.active)

    @property
    def inactive(self):
        return self.virtual.inactive

    @property
    def inactive_str(self):
        return self.make_string(self.inactive)

    @property
    def buffers(self):
        return self.virtual.buffers

    @property
    def buffers_str(self):
        return self.make_string(self.buffers)

    @property
    def cached(self):
        return self.virtual.cached

    @property
    def cached_str(self):
        return self.make_string(self.cached)

    @property
    def shared(self):
        return self.virtual.shared

    @property
    def shared_str(self):
        return self.make_string(self.shared)

    @property
    def slab(self):
        return self.virtual.slab

    @property
    def slab_str(self):
        return self.make_string(self.slab)

    @property
    def wired(self):
        return self.virtual.wired

    @property
    def wired_str(self):
        return self.make_string(self.wired)


class SystemInfoMaster:
    memory = MemoryInfoMaster()
    cpu = CPUInfoMaster()
    info = InfoMaster()
    disk = DiskInfoMaster()
