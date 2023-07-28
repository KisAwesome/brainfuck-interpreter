
# Brainfuck Interpreter

Brainfuck is an esoteric programming language created in 1993 by Urban Müller. It is famously known for its minimalistic design, consisting of just eight commands, and its Turing-completeness, meaning it can perform any computation that can be done by a computer. The language is deliberately difficult to write and read, making it more of a fun challenge and a demonstration of computational principles than a practical programming tool.

## Language reference
The eight commands in Brainfuck are as follows:

\>: Increment the data pointer. Move the pointer to the right.

<: Decrement the data pointer. Move the pointer to the left.

+: Increment the byte at the data pointer. Increase the value stored in the current cell.

-: Decrement the byte at the data pointer. Decrease the value stored in the current cell.

[: Jump past the matching ] if the byte at the data pointer is 0 (start of loop).

]: Jump back to the matching [ if the byte at the data pointer is nonzero (end of loop).

.: Output the byte at the data pointer as a character (ASCII value).

,: Input a character and store its ASCII value in the byte at the data pointer.


Brainfuck operates on an array of memory cells, known as the "data tape." Each cell initially contains a value of 0. The data pointer is a special pointer that points to one of the memory cells on the data tape. The pointer can be moved left or right, allowing access to different memory cells.

## How to Use
Clone the repository or download the Python script to your local machine.



Make sure you have Python 3 installed on your system.

Run the Brainfuck interpreter by executing the following command in your terminal or command prompt:

```bash
python3 main.py <file_path> [--debug] [--array-size <size>]
```
Replace <file_path> with the path to the Brainfuck code file you want to execute.

### Optional arguments:

--debug: Enable debug mode. This will display the current command, pointer position, and array contents at each step of execution.
--array-size <size>: Specify the size of the array used by the program (default is 30000).

## Brainfuck Code File
Create a text file containing the Brainfuck code you want to execute. Save it with a .bf extension.

## Example
Let's say you have a file named hello_world.bf with the following Brainfuck code:
```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.

```

To execute this Brainfuck code, run the following command in your terminal:

```shell
python3 main.py hello_world.bf
```
