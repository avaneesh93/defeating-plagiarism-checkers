The Google WSD Dataset needs to be downloaded from:
https://research.googleblog.com/2017/01/a-large-corpus-for-supervised-word.html

Files and folders: "masc", "semcor", "manual_map.txt"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The WordNet data in the form of the file "index.sense" needs to be downloaded from:
https://wordnet.princeton.edu/wordnet/download/current-version/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project requires some model files to be either downloaded or generated,
and some model files to downloaded.

For Logistic Regression, the files needed are "model.pkl" and "vectorizer.pkl".
These files need to be placed in "<Project Code Root Directory>/datasets".
You may download it from here:

model.pkl:
https://drive.google.com/file/d/1qOTapymRf_zl8n1sZQrEaezgrT9scIV8/view

vectorizer.pkl:
https://drive.google.com/file/d/1lN8-yaDLG3d-xPTrMg1fTajei_1StI0u/view

You can also generate these files by running the project for the first time.
However, it will take about 3 hours to do so.

P.S.:
model.pkl is a 3.25 GB file which needs to be *loaded onto RAM*! You may want to use a higher-specced
workstation to execute the project.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Language Modeling using Facebook's Word Vectors. the file needed is "wiki.en.vec".
This file needs to also be placed in "<Project Code Root Directory>/datasets".

You can download the file from here:
https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.en.vec

If in case the above link becomes dead, the GitHub link for the project is:
https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md

P.S.:
This is a 6.14 GB file which needs to be *loaded onto RAM*! You may want to use a higher-specced
workstation to execute the project.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to download the required Python packages that this project depends upon.

Please note that this project uses Python 3.x

For installing all packages, "cd" to <Project Code Root Directory>, and execute:
pip3 install -r requirements.txt

P.S.:
The package "language-check" needs Java to be installed in the operating  system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To execute the project, please paste your text (whose plagiarism needs to be possibly reduced)
in "<Project Code Root Directory>/datasets/input_text.txt"

Then, execute "<Project Code Root Directory>/src/algorithm.py"

Please note that while executing the Python file, you may need to add the "src" folder to your
PYTHONPATH. This can be done by "cd"ing to "src" and then executing the following command:
export PYTHONPATH=`pwd`