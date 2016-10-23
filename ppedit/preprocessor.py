from abc import ABCMeta, abstractmethod
from typing import List
from subprocess import run, PIPE
from os import remove


class Preprocessor(object, metaclass=ABCMeta):
    @abstractmethod
    def get_preprocessed_contents(self, filename: str, input_file: str, sketch: str, flags: List[str]) -> str:
        pass


class ClangPreprocessor(Preprocessor):
    def get_preprocessed_contents(self, filename: str, input_file: str, sketch: str, flags: List[str]) -> str:
        sketch_name = '{}.sketch.h'.format(filename)
        marker = 'PPEDIT_MARK_SKETCH'
        with open(sketch_name, 'w') as sketch_file:
            print(input_file, file=sketch_file)
            print(marker, file=sketch_file)
            print(sketch, file=sketch_file)

        complete_flags = ['-E', *flags, '-x', 'c++', '-D{}={}'.format(marker, marker), sketch_name]
        command = ['clang++', *complete_flags]
        clang = run(command, stdout=PIPE)
        preprocessed_name = '{}.preprocessed.h'.format(sketch_name)
        with open(preprocessed_name, 'w') as f:
            f.write(clang.stdout.decode('utf-8'))
        command = ['clang-format', preprocessed_name]
        clang_format = run(command, stdout=PIPE)
        lines = clang_format.stdout.decode('utf-8')
        marker_idx = lines.find(marker)
        remove(sketch_name)
        remove(preprocessed_name)
        return ''.join(lines[marker_idx + len(marker):])
