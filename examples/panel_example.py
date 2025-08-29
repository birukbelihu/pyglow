from pyglow.styles.border import Border
from pyglow.views.panel import Panel

def main():
 panel = Panel("pyglow",
           "Console output formatter library",
         "#09ED1C",
      "#E9ED09",
      "#ED093F",
              Border.ROUNDED
             )
 panel.show()

if __name__ == "__main__":
    main()
