class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def set_title(self, title: str):
        self.__title = title

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self) -> int:
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages: int):
        if number_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = number_pages

    def display_info(self):
        super().display_info()
        if hasattr(self, '_Book__number_of_pages'):
            print(f"Number of pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self) -> int:
        return self.__issue_number

    def set_issue_number(self, issue_number: int):
        if issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        super().display_info()
        if hasattr(self, '_Magazine__issue_number'):
            print(f"Issue number: {self.__issue_number}")


# ==========================================
# Testing with Sample Code from Assessment
# ==========================================

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  # setting invalid value on attribute
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
