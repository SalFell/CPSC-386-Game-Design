![Header](../../actions/workflows/py-header.yml/badge.svg)
![Lint](../../actions/workflows/py-lint.yml/badge.svg)
![Format](../../actions/workflows/py-format.yml/badge.svg)

# Instructions

This is an exercise to ensure that you have Git, GitHub, a text editor, and Python setup on your computer. 

An outline of the steps you must follow is:

1. From a command shell, use `git` to clone your repository
1. From a command shell, navigate the filesystem to where your repository has been cloned
1. Edit the file `hello.py` to include a header
1. Change `hello.py` to have executable permission
1. Run the `hello.py` command.
1. Use `pylint` to lint `hello.py`; use the output of `pylint` to make changes to `hello.py`
1. Use `pycodestyle` to lint `hello.py`; use the output of `pylint` to make changes to `hello.py`
1. Use `black` to format `hello.py`

Remember to commit your work as you go along. Better yet, use git's branch-and-merge workflow to work on this project in small stages.

Whatever you push to your GitHub repository is what is graded. You can get a pretty good idea if your project is passing muster if it passes the automated tests.

## Tips

First, use `git` to clone your repository onto your Linux computer. If you are new to using `git` or need a quick refresher, please review the [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit). Specifically, the book [Pro Git by Scott Chacon](https://git-scm.com/book/en/v2) is a good starting point.

Once you have cloned your repository to your computer, execute the `hello.py` program. You can do this by navigating to your repository's directory using the command shell.

If you are not familiar with how to use a shell or are a little rusty, the [recommended reading](https://docs.google.com/document/d/184U-IQ0DrmlVlPMySjKaYxq2M-ScNvgX8NRa1Kkuk9Q/edit) has [The Linux Command Line by William Shotts](http://linuxcommand.org/tlcl.php) as a reference.

The next step is to edit the program `hello.py` and add a header using your favorite text editor. If you do not have a favorite, you are recommended to use [Microsoft Visual Studio Code](https://code.visualstudio.com/).

Open the file `hello.py` in your text editor and add a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) and a header identifying you, your contact information, and the course's information. In this course, you are required to follow [PEP-8](https://www.python.org/dev/peps/pep-0008/), the official Python coding style and add a header to each Python source file you submit. The header is not a requirement of PEP-8. It is a requirement for this course.

The [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) should only be added to files which you intend on running or executing from the command prompt. In our case, `hello.py` will be so please include it. In the future, you may write a project across multiple files and including a shebang is not recommended for library files.

The version of Python that we are using in this course is version 3. It is important that you write all your code using Python version 3 and not any earlier versions.

To illustrate, let us imagine we have a hello world program written in Python saved in a file named `hello.py`.

```python
""" This is the file hello.py and it is a hello world program. """
def main():
    print("Hello World!")

if __name__ == '__main__':
    main()

```

To add a shebang, we need to add `#!/usr/bin/env python3` to the very first line. A shebang is _always_ the first line of a file. The file `hello.py` will contain:
```python
#!/usr/bin/env python3
def main():
    print("Hello World!")

if __name__ == '__main__':
    main()

```

Let us add our header to the file. In this example, we will imagine the author's name is Tuffy Titan who has an email address tuffy.titan@csu.fullerton.edu, and Tuffy's GitHub login is `tuffytitan`.

```python
#!/usr/bin/env python3
# Tuffy Titan
# CPSC 120-01
# 2050-01-01
# tuffy.titan@csu.fullerton.edu
# @tuffytitan
#
# Lab 00-00
#

def main():
    print("Hello World!")

if __name__ == '__main__':
    main()

```

Once all the changes are saved, our next step is to change the `hello.py` to have executable permission.

From the command prompt, use the command `chmod` to add the execute bit. For example:

```bash
$ chmod u+x pycheck.py
```

Next, run the `hello.py` program from the command prompt. For example:

```bash
$ ./hello.py 
Hello World!
```

To use tools such as `pylint`, `pycodestyle`, and `black`, you'll need to install them using `pip` or `apt`. On a Debian-style system like Ubuntu, you can install the necessary software with the following command:

```bash
$ sudo apt install flake8 pylint pycodestyle black
```

To use `pylint`, the command is:

```bash
$ pylint hello.py
```

The output may appear cryptic. With practice it will make more sense. If there is anything you don't understand, write it down and ask about it in class.

To use `pycodestyle`, the command is very similar to `pylint`.
```bash
$ pycodestyle hello.py
```

Please read [the documentation on `black`](https://black.readthedocs.io/en/stable/) because it is a very powerful tool which will modify your code. Before you use it, make sure you understand what it does.

# Rubric

This exercise is worth 5 points. Submissions that do not execute (syntax or semantic error; uncaught exception) shall be assigned a zero grade. Submissions that have made no change substantive change from the template repository shall be assied a zero grade.

* Formatting & Readability (4 points): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is. Failure to include a header forfeits all marks. 

* Execution (1 point): Does it print 'Hello World!' or not?