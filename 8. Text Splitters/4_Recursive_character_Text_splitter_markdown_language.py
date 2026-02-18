from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_summary(self):
        return f"'{self.title}' by {self.author}, published in {self.year}. Contains {len(self.chapters)} chapters."

    def get_total_pages(self):
        return sum(ch.pages for ch in self.chapters)


class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def get_outline(self):
        outline = f"Chapter: {self.title} ({self.pages} pages)\n"
        for sec in self.sections:
            outline += f"  - {sec.title}\n"
        return outline


class Section:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def summarize(self):
        words = self.content.split()
        return " ".join(words[:20]) + "..." if len(words) > 20 else self.content


def create_sample_book():
    book = Book("The Art of Recursive Thinking", "S. Ray", 2025)

    chapter1 = Chapter("Introduction to Recursion", 15)
    chapter1.add_section(Section("What is Recursion?", "Recursion is a method of solving a problem where the solution depends on smaller instances of the same problem."))
    chapter1.add_section(Section("Why Recursion Matters", "It helps simplify complex problems by breaking them into smaller, more manageable parts."))

    chapter2 = Chapter("Recursive Patterns", 22)
    chapter2.add_section(Section("Divide and Conquer", "This pattern involves dividing a problem into subproblems, solving them recursively, and combining the results."))
    chapter2.add_section(Section("Backtracking", "A technique used for solving constraint satisfaction problems, such as puzzles or mazes."))

    book.add_chapter(chapter1)
    book.add_chapter(chapter2)
    return book
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))

print("================== 1 =====================")
print(chunks[0])

print("================== 2 =====================")
print(chunks[1])