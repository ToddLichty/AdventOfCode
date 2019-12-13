
# Return codes
R_OK = 0
R_HALT = 1
R_INPUT = 2
R_OUTPUT = 3
R_INVALID = 99


class IntCode:
  def __init__(self, codes):
    self.code = {i: x for i, x in enumerate(codes)}
    self.pointer = 0
    self.relative_base = 0
    self.modes = [0, 0, 0]
    self.inputs = []
    self.outputs = []


  def inspect(self, pos):
    return self.code[pos]


  def edit(self, pos, val):
    self.code[pos] = val
    return self


  def write(self, input):
    self.inputs.append(input)
    return self


  def read(self):
    return self.outputs.pop(0)


  def run(self):
    result = R_OK

    while result == R_OK:
      result = self._step()

    return result


  def _step(self):
    mode, op = divmod(self.code.get(self.pointer, 0), 100)
    self.pointer += 1
    self.modes = [int(x) for x in reversed(str(mode))] + [0, 0, 0]

    if op == 1:
      arg1 = self._get_next_value()
      arg2 = self._get_next_value()
      pos = self._get_next_instruction()

      self.code[pos] = arg1 + arg2
      result = R_OK

    elif op == 2:
      arg1 = self._get_next_value()
      arg2 = self._get_next_value()
      pos = self._get_next_instruction()

      self.code[pos] = arg1 * arg2
      result = R_OK

    elif op == 3:
      if len(self.inputs) == 0:
        self.pointer -= 1
        result = R_INPUT
      else:
        pos = self._get_next_instruction()
        self.code[pos] = self.inputs.pop(0)
        result = R_OK

    elif op == 4:
      value = self._get_next_value()
      self.outputs.append(value)
      result = R_OUTPUT

    elif op == 5:
      value = self._get_next_value()
      pos = self._get_next_value()

      if value != 0:
        self.pointer = pos

      result = R_OK

    elif op == 6:
      value = self._get_next_value()
      pos = self._get_next_value()

      if value == 0:
        self.pointer = pos

      result = R_OK

    elif op == 7:
      arg1 = self._get_next_value()
      arg2 = self._get_next_value()
      pos = self._get_next_instruction()

      self.code[pos] = 1 if arg1 < arg2 else 0
      result = R_OK

    elif op == 8:
      arg1 = self._get_next_value()
      arg2 = self._get_next_value()
      pos = self._get_next_instruction()

      self.code[pos] = 1 if arg1 == arg2 else 0
      result = R_OK

    elif op == 9:
      self.relative_base += self._get_next_value()
      result = R_OK

    elif op == 99:
      result = R_HALT

    else:
      print(f"Invalid opcode {op}")
      result = R_INVALID

    return result


  def _get_next_value(self):
    return self._get_next_instruction() if self.modes[0] == 1 else self.code.get(self._get_next_instruction(), 0)

  
  def _get_next_instruction(self):
    instruction = self.code.get(self.pointer, 0)

    if self.modes.pop(0) == 2:
      instruction += self.relative_base

    self.pointer += 1
    return instruction
