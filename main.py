import tkinter as tk

class RecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Словарь терминов по информатике")

        self.records = []

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Добавить термин", command=self.add_record)
        self.add_button.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Поиск", command=self.search_record)
        self.search_button.pack()

    def add_record(self):
        record = self.entry.get()
        self.records.append(record)
        self.entry.delete(0, tk.END)
        print("Термин добавлен:", record)

    def search_record(self):
        keyword = self.search_entry.get()
        results = [record for record in self.records if keyword in record]
        print("Результат по запросу '{}':".format(keyword))
        for result in results:
            print(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecordsApp(root)
    root.mainloop()