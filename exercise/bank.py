class SetFull(Exception):
    pass


class MemoryBank:
    def __init__(self):
        self.members = []

    def add_problem(self, problem_id):
        # TODO: refuse the 11th problem. Raise SetFull. Change nothing else.
        if len(self.members) >= 10:
            raise SetFull
        if problem_id not in self.members:
            self.members.append(problem_id)
