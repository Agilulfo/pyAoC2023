from advent import utils
import re


def parse_input():
    workflows = []
    parts = []

    with open(utils.input_path(__file__)) as input:
        for line in input:
            parsed_line = parse_line(line)
            if not parsed_line:
                continue

            if len(parsed_line) == 3:
                workflows.append(parsed_line)
            else:
                parts.append(parsed_line)

    return workflows, parts


def parse_line(line):
    if line[0] == "{":
        # part
        match = re.match("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line)
        return match.group(1, 2, 3, 4)

    if line != "\n":
        # workflow
        match = re.match(
            "(?P<workflow>[a-z]+){(?P<rules>.*,)+(?P<default>[a-z]+|[AR])}", line
        )
        workflow, rules, default = match.group("workflow", "rules", "default")
        rules = [parse_rule(rule) for rule in rules[:-1].split(",")]
        return (workflow, rules, default)
    return None


def parse_rule(rule):
    return re.match("([xmas])([<>])(\d+):(.*)", rule).group(1, 2, 3, 4)
