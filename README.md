# UCI-Beall-Matching
MUST HAVE PYTHON 3.7-3.9 FOR TENSOR_FLOW TO RUN AND INSTALL PROPERLY

MUST HAVE PIP INSTALLED

RUN THESE COMMANDS IN THE TERMINAL ONCE YOU HAVE PYTHON INSTALLED TO GET THE PROPER LIBRARIES FOR THE PROGRAM

################################################################

python get-pip.py

python -m pip install requests

python -m pip install scipy

pip install "tensorflow>=2.0.0"

pip install --upgrade tensorflow-hub

pip install PyQt5

################################################################

### WARNING

CSVs must be formatted in the same way as the example CSVs that were provided by UCI Beall Applied Innovations

If there are any changes to the columns in the CSVs, it could result in the program crashing or not working as intended

A Valid API Key must be put into the PATH of the system in the form of a .txt file

The results from the Matching are suggestions, and should be used with the user's discretion

################################################################

### HOW TO USE

Create a .txt file named APIKey.txt with the APIKey for Insightly written in it in one line.

Run the launch.py file to open up the main window

From there, press UPLOAD button to upload a CSV file that has been imported from Qualtrics that has the contents of potential projects

Press the Check Projects button to see all the projects that the program has detected

Press the Start Matching button to generate a .txt file of all the matches as well as preview a sample of the matches.

Press Back at any point to return back to the file upload window

Press Exit or the X button to exit the window

#################################################################

### ADDING INDUSTRIES AND SKILLSETS

Find the .txt files named skillSets.txt or Industries.txt

Add your skill or industry to the text file with '' surrounding the skill or industry and fitting the format.

Make sure that the industry or skillset that you want to add is spelt the same way in both the Insightly database as well as in the txt files
