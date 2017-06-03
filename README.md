# LaTeX table printer

This simple script is intended to ease writing tables in LaTeX. Given a table 
file, the script prints out the corresponding LaTeX tabular environment 
containing the data.

## Usage

The script can be executed in two different ways: directly from the command 
line or as a python function which can be imported by other programs/scripts or 
inside a Python shell. In any case, the script works using three arguments:

* The file name or path.
* Separator between elements of a row.
* Whether or not the row names are included in the printing.

#### Running the script from the command line:

The script can be called as a normal Python script followed by the file name or 
path as:

```bash
$ python latex_table_printer.py [FILE] [OPTIONS]
```

* Options:

    - **-s, --sep**

        If passed, the program requires the user to input the separator, 
        otherwise tab is assumed by default.

    - **-r, --rownames**

        If passed, the row names (first column) is ommited when printing the 
        table.

#### Using as a Python function

From a Python shell or inside another Python script, import the module and 
calling the corresponding function with the desired arguments:

```python
from latex_table_printer import *

print_latex_table(filename, sep = '\t', rownames = True)
```

* Arguments:

    - **filename** [*str*]

        The file name or path where the data is stored. It is supposed that 
        each line corresponds to a row of the table.

    - **sep** [*str*]

        Optional, `'\t'` (tab) by default. Separator between entries/cells of 
        the table. For instance, if the file is in *.csv* format, the separator 
        should be a comma (`','`).

    - **rownames** [*bool*]

        Optional, `True` by default. Determines if the first column (typically, 
        where the row names are) of the table should be included.

## Example

The file `example.csv` contains the following table in *.csv* format:

|   | x | y |
|---|---|---|
| A | 1 | 2 |
| B | 3 | 4 |
| C | 5 | 6 |

If the user runs the script on this file, should obtain the following:

```bash
$ python latex_table_printer.py example.csv -s
Specify the separator character: ,


\begin{tabular}{|c|c|c|}
\hline
&x&y\\
\hline
A&1&2\\
\hline
B&3&4\\
\hline
C&5&6\\
\hline
\end{tabular}
```
