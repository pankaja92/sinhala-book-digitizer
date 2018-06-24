
def startUI(text,patterns):
    from PyQt5.QtWidgets import QApplication
    from testing import DisplayTheBook
    if __name__ == "__main__":
        import sys
        a = QApplication(sys.argv)
        t = DisplayTheBook(text, patterns)
        t.show()
        sys.exit(a.exec_())


startUI("වමේ කවියත් ගන ඇති සැටයි.නයම ඉස බුදු සමය.",{'ගන': ['ගන', 'ගත', 'ගහ', 'ගණ', 'කන', 'කහ', 'කණ', 'හන', 'හත', 'ශතන', 'වන', 'ගී', 'ගත', 'ගෙ', 'ගණ', 'ඌන', 'හන', 'එන', 'ඕන', 'ඝන', 'ගඳ'], 'සැටයි': ['යැමයි', 'යාමයි', 'පාමසිසැටි', 'තැටි', 'සිටි', 'සෙයි', 'ගැටය', 'සැලි', 'ජැටි', 'මැයි', 'සායි', 'සැළය', 'යැයි', 'දැයි'], 'නයම': ['කයට', 'ගසට', 'ණයටනය', 'නම', 'නාම', 'එයම', 'නිම', 'නයන', 'තම', 'එය', 'නෑ', 'යූ', 'නො', 'ණය']})