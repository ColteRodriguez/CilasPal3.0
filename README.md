# INSTRUCTIONS FOR INSTALLING CILASPAL 3.0 AND TROUBLESHOOTING

To start, you must ensure that you have the latest version of Python installed on your computer. You can download or upgrade to the current version at https://www.python.org/downloads/

In order to import the necessary modules for this project, you will need to have pip installed to your computer.

    2a. Navigate to the terminal (or command prompt for widows) of your computer 

    2b. Paste the following, pressing enter after each line: 

        i. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ii. python3 get-pip.py
        iii. pip install --upgrade pip
        vi. pip install git                 *you will need this later*

    2c. Because we want pip to be able to import Python packages, 
        both pip and Python must have the same path on your device. 
        If you installed Python with the default settings, this shouldn't 
        be a problem, but if you are having trouble using pip, it may be because 
        Python and pip do not have the same path. 
Now that your computer is able to read python code, and import packages, you need to download CilasPal to your computer. To do this, simply navigate to the project page here: https://github.com/ColteRodriguez/CilasPal-3.0-

    3a. Click on the green "<> Code" button -> HTTPS -> copy the link

    3b. Navigate to your computers terminal (or command propt for widows OS)

    3c. Now you must cd (change directory) to the location where you want CilasPal Installed. 
        The default directory of the terminal is Home. If you want to import CilasPal to your 
        Desktop, type cd Desktop

    3d. Finally type: git clone (the HTTPS link from earlier)
    
Great! You should see the CilasPal repository on your Desktop. Now you must install the necessary packages

    4a. Again, navigate to the terminal and cd into the location of the CilasPal
        repository by typing: cd Desktop (if you used desktop above)

    4b. Paste the following, pressing enter after each line:
    
        i. pip install pypdf
        ii. pip install xlsxwriter
        iii. pip install tkinter
        iv. pip install auto-py-to-exe
        
You are almost done. To transform the CilasPal repository into an application, we will be using Auto PY to EXE

    5a. cd into the location of CilasPal like before (e.g. cd Desktop) and type:

        i. pyinstaller --onefile (the name of the .py file in the CilasPal repository.
            for version 3.0 it should be CilasPal3.py)
            
Now you should see a .exe desktop which will run CilasPal
