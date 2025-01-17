

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        line = ''.join(char for char in line if char not in [',', '.', '=', '!', '?', ';', ':', '-'])
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except UnicodeDecodeError:
                print(f"Проблемы с кодировкой в файле {file_name}.")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word_lower = word.lower()
            if word_lower in words:
                position = words.index(word_lower)
                result[file_name] = position + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2)
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))