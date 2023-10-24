
# EC-551-Program-1
# Logic Synthesis Engine


## **Description**

This project is designed to perform a logic synthesis calculation. It will prompt the user to enter the Boolean algebraic function(s) as strings, and then the function will be optmized via a variety of objective functions. This programming will ouput the result on the screen.

This Logic synthesis Engine is designed to perform the following tasks:

a. It will ask the user to enter the boolean Equation.
b. It accepts the boolean equation as strings
c. Once the boolean equation is sent to the tool, it asks the user for what they want to do with the boolean equation.
d. The following are the menu of this program:
e. For instance, typing the following numbers will perform the following tasks:

    1.  Return the design as a canonical SOP
    2.  Return the design as a canonical POS
    3.  Return the design INVERSE as a canonical SOP
    4.  Return the design INVERSE as a canonical POS
    5.  Return a minimized number of literals representation in SOP
        a. Report on the number of saved literals vs. the canonical version
    6.  Return a minimized number of literals representation in POS
        a. Report on the number of saved literals vs. the canonical version
    7.  Report the number of Prime Implicants
    8.  Report the number of Essential Prime Implicants
    9.  Report the number of ON-Set minterms
    10. Report the number of ON-Set maxterms
    11. report all variables in entry
    12. Exit the program

This program uses SymPY library for further simplifcation of the variables, minterms, and dontcares from the truth table.
The rest of the code are performed by the functions that we built.


## **Installation**

In order for this program to work, you will need to install either one of the following packages:

    Step1:
        navigate to the Anaconda url: https://www.anaconda.com/download and follow instructions there depending on your operating system. Anaconda is a free python distribution that comes with the SymPy library.

    Step2:

        or navigate to the Sympy library [https://docs.sympy.org/latest/install.html#installation](https://) and follow the instructions there.

once the package is downloaded and is working; import the following from the SymPy library:
        ```console
        ```python
        from sympy.logic import SOPform
        from sympy.logic import POSform
        ```
        ```
in your file. or simple download our program1.py file.

To use this program, download the file program1.py and run it in your operating system using any test editor. subjective to copyrights.


## **Authors:**

This project is completed as part of the Advanced Digital Design with Verilog and FPGA(EC 551) class at Boston university. Class is taugh by professor Douglas Densmore.

This project is completed by the following students(authors)

    copyright   Evan  Lang      evanlang@bu.edu
    copyright   Mayra Texeira   msteixei@bu.edu  
