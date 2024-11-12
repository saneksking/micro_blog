class SliceMaster:

    @classmethod
    def divide_into_slices(cls, number):
        result = {}

        start_index = 0
        slice_size = number // 31
        remainder = number % 31

        for day in range(1, 32):
            if remainder > 0:
                end_index = start_index + slice_size + 1
                remainder -= 1
            else:
                end_index = start_index + slice_size

            result[day] = slice(start_index, end_index)
            start_index = end_index

        return result

    @classmethod
    def get_slice(cls, number, day):
        return cls.divide_into_slices(number)[day]
