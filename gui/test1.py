
from PyQt5.QtWidgets import QApplication

text = "විජය ගේ සහචර පාණ්ඩ්‍ය දේශයෙන් භාර්යාවන් ගත් නමුත් ඔවුන්ගෙන්."

patterns = {"භාර්යාවන්": ["word", "this"], "පාණ්ඩ්‍ය": ["to", "highlight"]}

from testing import MyHighlighter

if __name__ == "__main__":
    import sys
    a = QApplication(sys.argv)
    t = MyHighlighter(text, patterns)
    t.show()
    sys.exit(a.exec_())

