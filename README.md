
# EC-551-Program-1
# Logic Synthesis Engine and virtual FPGA


## **Description**

This project is divided into two mains: the first main named as program1.py performs logic synthesis calculation and the second main named as Evan_Mayra_Program2_final.py creates a virtual FPGA that connects to the prgram1.py. In details, the Evan_Mayra_Program2_final.py assigns logic function to "LUTs" on the FPGA and make interconnection between LUTs.

**First lets start explaining program1.py** :

This program is designed to perform a logic synthesis calculation. It will prompt the user to enter the Boolean algebraic function(s) as strings, and then the function will be optmized via a variety of objective functions. This programming will ouput the result on the screen.

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


**The following are Evan_Mayra_Program2_final.py explanation:**

This program is designed to create a virtual FPGA that assigns logic function to "LUTs" on the FPGA and make interconnection between LUTs. This program creates an internal representation of the FPGA and assigns the functionality for the logic expressions to those resoruces. this program runs as follows

    a. first welcomes the users to the FPGA resource Allocation program
    b. asks the users to set the limits for the FPGA
    c. asks the users to enter the maximum number of the Luts
    d. asks the users to enter the maximum number of outputs
    d. then asks the users to please select an option 
    The options are printed on the terminal to provide information about which perform which tasks.
    For instance

        1. type 1 on the prompt, then enter the boolean equation. The users can enter any equations. or Follow our Tests to see how to properly enter the equations. once the user types 1, the users will be prompted with " what is the Lut size". Please enter 4 or 6. Then, the users will be prompted with what do you like to do. The users can type 1 again to enter the boolean equation and follow steps 1 or type any of the option bellow.
        2. type 2 to save the bistream. the bistream are saved as json files
        3. type 3 to load the bistream. Note the bistream is designed such that users shouldnt worry about overwrite
        4. type 4 to display the calculated FPGA resource usage
        5. Type 5 to display a visual representation of FPGA. The visual representation is a GUI. Note, there is also two buttons with color magenta. click on master_luct_dict to display the master luct dictionary. Like the json files, it also shows the interconnections between the variables to luts, and luts to luts. To exit the GUI, click on exit. 
        6. type 6 to view Lut connections and LUT details. the users will be asked to type the lut name.
        7. type 7 to view bitstream/current FPGA state.
        or type 12 to exit the program


    

## ** Tests**

    Please enter the boolean equation such as 
        m=a&b, 
        s= (a&b)|(c&d)|m
        luta= (a&b)|(f&g)|(r&g)|s
        lutb=(a&b)|(f&g)|(n&g)|luta|m
        lutc=(a&b)|(f&g)|(n&g)|luta|lutb
        please do not enter h, e, and i. Since we are using symPY, the program will crash. We assume that h, e, and i must be some "math" symbols used by sYmPy library. 
    
    Please note that the GUI constraints depends on the geometry set for the GUI,the canvas, and buttons as defined in the code. Look at the dimensions and see how many interconnections can be displayed in the screen. The screen is big enough, so the users have a larger GUi to display a lots of interconnections.



## **Installation**

In order for this program to work, you will need to install either one of the following packages:

Step1: navigate to the Anaconda url and follow instructions there depending on your operating system. Anaconda is a free python distribution that comes with the SymPy library.
        https://www.anaconda.com/download 


Step2:or navigate to the Sympy library url and follow the instructions there.
            [https://docs.sympy.org/latest/install.html#installation] 

once the package is downloaded and is working; import the following from the SymPy library:
        
        
        from sympy.logic import SOPform
        from sympy.logic import POSform
        
        
in your file. or simple download our program1.py file.

To use this program, download the file program1.py and run it in your operating system using any test editor. subjective to copyrights.

## Contributing

we welcome any Feedbacks and contributions.
If you want to contribute to this project, follow these steps:

Fork this repository.
Create a new branch: git checkout -b new-feature
Make your changes and commit them: git commit -am 'Add new feature'
Push to the branch: git push origin new-feature
Submit a pull request.

Alternatively see this webiste on how to pull request:

    https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request



## **Authors:**

This project is completed as part of the Advanced Digital Design with Verilog and FPGA(EC 551) class at Boston university. Class is taught by professor Douglas Densmore.

This project is completed by the following students(authors)

    copyright   Evan  Lang      evanlang@bu.edu
    copyright   Mayra Texeira   msteixei@bu.edu  

