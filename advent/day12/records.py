import logging


class ConditionRecord:
    def __init__(self, damaged_record, verification_format):
        self.damaged_record = damaged_record
        self.verification_format = verification_format

    def __repr__(self):
        return f"{self.damaged_record} <- {self.verification_format}"

    def count_arrangements(self):
        self.reduce()
        match len(self.verification_format):
            case 0:
                return 1
            case _:
                raise NotImplementedError


    def reduce(self):
        """ Simplify current ConditionRecord

        Removes obvious sections of the record that would not impact the overall count of arrangements
        """
        functions = [self.chop, self.fix_range, self.fix_beginning, self.fix_end, self.remove_dots]
        while True:
            changed = False
            for function in functions:
                if not self.done():
                    if function():
                        changed = True
            if not changed:
                break

    # step 2
    def fix_range(self):
        if shortest_sequence(self.verification_format) == len(self.damaged_record):
            self.damaged_record = ""
            self.verification_format = []
            logging.debug(f"Apply fix_range: {self}")
            return True
        return False

    # step 3.a
    def fix_beginning(self):
        first_seq_len = self.verification_format[0]
        if self.damaged_record[0] == "#" or (
            self.damaged_record[first_seq_len] == "."
            and "#" in self.damaged_record[: first_seq_len - 1]
        ):
            self.damaged_record = self.damaged_record[first_seq_len + 1 :]
            self.verification_format = self.verification_format[1:]
            logging.debug(f"Apply fix_beginning: {self}")
            return True
        return False

    # step 3.b
    def fix_end(self):
        last_seq_len = self.verification_format[-1]
        if self.damaged_record[-1] == "#" or (
            "#" in self.damaged_record[-(last_seq_len): ]
            and self.damaged_record[-last_seq_len -1] == "."
        ):
            self.damaged_record = self.damaged_record[: -(last_seq_len + 1)]
            self.verification_format = self.verification_format[:-1]
            logging.debug(f"Apply fix_end: {self}")
            return True
        return False

    def remove_dots(self):
        previous_len = len(self.damaged_record)

        for index, value in enumerate(self.damaged_record):
            if value != ".":
                self.damaged_record = self.damaged_record[index:]
                logging.debug(f"Apply remove_dots: {self}")
                break


        for index in range(len(self.damaged_record) -1, -1, -1):
            if self.damaged_record[index] != ".":
                self.damaged_record = self.damaged_record[:index+1]
                logging.debug(f"Apply remove_dots: {self}")
                break

        return previous_len != len(self.damaged_record)

    def done(self):
        return len(self.verification_format) == 0

    # step 1
    def chop(self):
        chopped = False
        while True:
            index = find_last_dot(self.damaged_record, self.verification_format[0])
            if index is not None:
                self.damaged_record = self.damaged_record[index + 1 :]
                chopped = True
                logging.debug(f"Apply chopping front: {self}")
            else:
                break

        while True:
            index = find_first_dot(self.damaged_record, self.verification_format[-1])
            if index is not None:
                self.damaged_record = self.damaged_record[:index]
                chopped = True
                logging.debug(f"Apply chopping back: {self}")
            else:
                break
        return chopped


def find_last_dot(sentence, first_len):
    for index in range(first_len - 1, -1, -1):
        if sentence[index] == ".":
            return index
    return None


def find_first_dot(sentence, last_len):
    for index in range(len(sentence) - last_len, len(sentence)):
        if sentence[index] == ".":
            return index
    return None


def shortest_sequence(verification_format):
    minimum_spaces = len(verification_format) - 1
    return sum(verification_format) + minimum_spaces
