from subprocess import run, PIPE
from os import remove


class TextProcessor(object):
  """
    This class provides a generic implementation for invoking a
    program that expects a text file as input and produces another
    as its output.
    """

  def __init__(self, executable: str):
    self.executable = executable

  def process_text(self, text: str, flags_fmt: str) -> str:
    """
        Runs the executable of this TextProcessor on the text provided and returns
        the processed output as string.
        :param text: The text to process.
        :param flags_fmt: The flags as a format string. Must contain {input_file}.
        :return: The processed text as string.
        """
    input_file = '__textproc_in.tmp'
    flags = flags_fmt.format(input_file=input_file).split(' ')
    with open(input_file, 'w') as f:
      f.write(text)
    proc = run([self.executable, *flags], stdout=PIPE)
    remove(input_file)
    return proc.stdout.decode('utf-8')
