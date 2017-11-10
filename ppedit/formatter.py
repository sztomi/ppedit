from ppedit.tools.bases import TextProcessor


class ClangFormatter(TextProcessor):
  config_file = None
  def process_text(self, text: str, flags_fmt: str = None) -> str:
    if self.config_file:
      flags_fmt += " -style='{0}'".format(self.config_file)
    return super().process_text(text, flags_fmt)
