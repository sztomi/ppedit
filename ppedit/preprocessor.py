from abc import ABCMeta, abstractmethod
from typing import List

from ppedit.tools.bases import TextProcessor


class Preprocessor(object, metaclass=ABCMeta):
  @abstractmethod
  def get_preprocessed_contents(self, filename: str, input_file: str,
                                scratch: str, flags: List[str]) -> str:
    pass


class ClangPreprocessor(Preprocessor):
  marker = "PPEDIT_MARK_SCRATCH"

  def get_preprocessed_contents(self, filename: str, input_text: str,
                                scratch: str, flags: List[str]) -> str:
    text = "{input}\n{marker}\n{scratch}".format(
      input=input_text, marker=self.marker, scratch=scratch)
    pp = TextProcessor("clang++")
    assembled_flags = "-E {flags} -x c++ -D{marker}={marker} -".format(
      flags=" ".join(flags), marker=self.marker)
    processed = pp.process_text(text, assembled_flags)
    clang_format = TextProcessor("clang-format")
    lines = clang_format.process_text(processed)
    marker_idx = lines.find(self.marker)
    return "".join(lines[marker_idx + len(self.marker) + 1:])
