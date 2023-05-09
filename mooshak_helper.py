#Author: Andre Costa

def replace_last(string, old, new):
    return new.join(string.rsplit(old, 1))

class MooshakHelper():

    def __init__(self, input_lines, activate=True):
        self.active = activate
        if activate:
            self.curr_line = 0
            self.input_lines = input_lines.copy()

    def input(self, *args, **kwargs):
        toPrint = " ".join(args)

        if(self.active):
            if toPrint != "":
                print(toPrint, end="")
            ret = replace_last(self.input_lines[self.curr_line], "\n", "")
            self.curr_line = self.curr_line + 1
        else:
            ret = input(toPrint)

        return ret

    def get_last_cmmnd(self):
        last_line = self.curr_line - 1
        return (last_line + 1, self.input_lines[last_line])

