# pynum2words-language-packs

Language Packs For [pynum2words](https://github.com/BirukBelihu/pynum2words) Python Library

# How To Create A Language Dictionary

Creating a language dictionary for `pynum2words` python library is very easy. all you need to do is to create a dedicated text file with .n2w extension and define the basic number that subsequent numbers will be derived from it. here is an example of a language dictionary for the English language:

```text
# English Language Dictionary

0 = Zero
1 = One
2 = Two
3 = Three
4 = Four
5 = Five
6 = Six
7 = Seven
8 = Eight
9 = Nine
10 = Ten
11 = Eleven
12 = Twelve
13 = Thirteen
14 = Fourteen
15 = Fifteen
16 = Sixteen
17 = Seventeen
18 = Eighteen
19 = Nineteen
20 = Twenty
30 = Thirty
40 = Forty
50 = Fifty
60 = Sixty
70 = Seventy
80 = Eighty
90 = Ninety
100 = Hundred
1000 = Thousand
1000000 = Million
1000000000 = Billion
```

```pynum2words``` Library also supports comments in the dictionary file, so you can add comments to explain the numbers or any other information you want like this.

```text

# Here I define the basic numbers in Amharic language from 0 to 10
0 = ዜሮ
1 = አንድ
2 = ሁለት
3 = ሶስት
4 = አራት
5 = አምስት
6 = ስድስት
7 = ሰባት
8 = ስምንት
9 = ዘጠኝ
10 = አስር
```

```text
Supported Comments ``#, //, /* */``
```

The ```pynum2words``` library will also show errors & warnings if there are any issues with the dictionary file. For example, if your definition have a syntax error, it will show a warning like this:

```text
0 = Zero
1One # Invalid pyum2words dictionary entry, it should be like this: 1 = One
2 = Two
3 = Three
```

```text
Line 2 Invalid Format: 1One — expected 'number = word'
```
# How To Use The Language Dictionary

To use the language dictionary you created, you need to save it with a `.n2w` extension and place it in the current or any other directory you want(Note that you should use the absolute path if it's in another folder). After that, you can use it in your Python code like this:

```python
from pynum2words.builtin_dictionaries import amharic_dictionary, english_dictionary
from pynum2words.pynum2words import PyNum2Words

amharic = PyNum2Words("amharic.n2w")

# Number to words

print(amharic.number_to_words(1995))  # Output: አንድ ሺህ ዘጠኝ መቶ ዘጠና አምስት
# Words to number

print(amharic.words_to_number("ሁለት ሺህ አምስት"))  # Output: 2005
```
# How To Contribute
If you want to contribute a language dictionary, you can create a pull request with your language dictionary file. Make sure to follow the format mentioned above and test it with the `pyn2wc` tool before submitting the pull request.

You can download pyn2wc tool from the [pynum2words-language-packs](https://github.com/birukbelihu/pynum2words-language-packs/releases) releases page for your operating system. currently prebuilt binaries are available only for Windows & Linux. If you want to build it from source, you can follow this simple steps:
1. Clone the repository
```bash
git clone https://github.com/birukbelihu/pynum2words-language-packs
```

2. Navigate to the cloned directory
```bash
cd pynum2words-language-packs
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Build the tool using PyInstaller
```
pyinstaller --onefile pyn2wc.py
```
