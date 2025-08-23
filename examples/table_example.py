from pyglow.views.table import Table


def main():
 table = Table(
        border_color="#44E80E",
        header_color="#0E19E8",
    )
 table.set_title("Students Info Table")

 table.add_column("ID")
 table.add_column("NAME")
 table.add_column("DEPARTMENT")

 table.add_row(["001", "Alice", "Marketing"])
 table.add_row(["002", "Biruk", "CS"])
 table.add_row(["003", "Bob", "CS"])
 table.add_row(["004", "Charlie", "Finance"])

 table.show()

if __name__ == "__main__":
    main()
