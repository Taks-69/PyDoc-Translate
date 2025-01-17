# PyDoc Translate

Automatically translate comments and docstrings in a Python project, without touching regular strings.

---

## Features

- **Docstrings & Comments**: Translate `""" ... """`, `''' ... '''`, and `# ...` comments into the language of your choice.  
- **Graphical User Interface (GUI)**: Easily switch to GUI mode using the `Pydoc-Translate` command.  
- **Command-Line Interface (CLI)**: Automate translation using the `Pydoc-Translate-CLI` command, perfect for integration into other scripts.  
- **Output Folder**: Translated files are stored in an `output` folder, created automatically.  
- **Cyberpunk Style**: Minimalistic, dark-themed interface for an immersive experience.

---

## Installation

1. **Clone** this repository:  
    ```bash
    git clone https://github.com/Taks-69/PyDoc-Translate
    ```
2. **Navigate** to the project directory:  
    ```bash
    cd PyDoc-Translate
    ```
3. **Install** the module (build the distributions, then install them):  
    ```bash
    python setup.py sdist bdist_wheel
    pip install dist\pydoc_translate-1.0.0-py3-none-any.whl
    ```

---

## Usage (GUI)

1. **Navigate** to the directory where you want the `output` folder to be created.  
2. **Launch** the GUI:  
    ```bash
    Pydoc-Translate
    ```
3. **Select** a `.py` file or a folder containing `.py` files.  
4. **Enter** the target language (e.g., `en`, `fr`, `es`, etc.).  
5. **Click** "Start Translation".  
6. Translated files will appear in the `output` folder at the same location where the command was run.

---

## Usage (CLI)

1. **Run** the following command:  
    ```bash
    Pydoc-Translate-CLI --path="my_file.py" --lang=es --output="output_es"
    ```
    - `--path`: Path to a `.py` file or a folder containing `.py` files.  
    - `--lang`: Target language (default: `en`).  
    - `--output`: Name of the output folder (default: `output`).  

2. Translated files will be saved in the specified folder (`output_es` in the example).

---

## Example Input File

```python
""" Hello everyone, test 01 Display hello """
print("hello")

""" Another docstring """
# Hello everyone, test 02 Display hello

" Simple string, not translated "
```

## Output Example (e.g., in `fr`)
```py
""" Bonjour tout le monde, test 01 Afficher bonjour """
print("hello")

""" Un autre docstring """
# Bonjour tout le monde, test 02 Afficher bonjour

" Simple string, not translated "

```

---

## Disclaimer
> For educational use only.
> Any misuse or inappropriate use of this program is solely the responsibility of the user.

---

## Technologies Used

- Python 3
- Googletrans (Unofficial API)
- Tkinter for the GUI (included in most Python distributions)
- argparse for the CLI

---

## License
This project is licensed under the GNU General Public License v3.0.

---

**⭐ Feel free to leave a star if you find this project useful!**