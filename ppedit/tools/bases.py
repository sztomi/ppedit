import io

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

  def process_text(self, text: str, flags_fmt: str = None) -> str:
    """
    Runs the executable of this TextProcessor on the text provided and returns
    the processed output as string.
    :param text: The text to process.
    :param flags_fmt: The flags as a format string. Must contain {input_file}.
    :return: The processed text as string.
    """
    with io.BytesIO(text.encode("utf-8")) as f:
      flags = flags_fmt.split(" ") if flags_fmt else []
      proc = run([self.executable, *flags], stdout=PIPE, input=f.read())
      return proc.stdout.decode("utf-8")
