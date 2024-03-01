class ConditionRecord:
    def __init__(self, damaged_record, other_format):
        self.damaged_record = damaged_record
        self.other_format = other_format

    def __repr__(self):
        expansion = "~".join(["#" * count for count in self.other_format])
        return f"{self.damaged_record} <- {expansion}"

    def count_arrangements(self):
        return 1
