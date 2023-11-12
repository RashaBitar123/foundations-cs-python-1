
class Browser:
    def __init__(self):
        self.tabs = []

    def open_tab(self, title, url):
        tab = {'title': title, 'url': url, 'nested_tabs': []}
        self.tabs.append(tab)

    def close_tab(self, index=None):
        if not self.tabs:
            print("No tabs to close.")
        else:
            if index is None:
                index = -1 
            if 0 <= index < len(self.tabs):
                closed_tab = self.tabs.pop(index)
                print(f"Closed tab: {closed_tab['title']}")
            else:
                print("Invalid tab index.")

    def switch_tab(self, index):
        if 0 <= index < len(self.tabs):
            print(f"Switched to tab: {self.tabs[index]['title']}")
        else:
            print("Invalid tab index.")

    def display_tabs(self):
        if not self.tabs:
            print("No tabs open.")
        else:
            print("Open Tabs:")
            for i, tab in enumerate(self.tabs):
                print(f"{i}. {tab['title']}")

def main():
    browser = Browser()

    while True:
        print("\nMenu:")
        print("1. Open Tab")
        print("2. Close Tab")
        print("3. Switch Tab")
        print("4. Display All Tabs")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter tab title: ")
            url = input("Enter tab URL: ")
            browser.open_tab(title, url)
        elif choice == '2':
            index = int(input("Enter tab index to close (or press Enter to close the last opened tab): ") or -1)
            browser.close_tab(index)
        elif choice == '3':
            index = int(input("Enter tab index to switch to: "))
            browser.switch_tab(index)
        elif choice == '4':
            browser.display_tabs()
        elif choice == '5':
            print("Exiting the browser.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()