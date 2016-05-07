# netlogo_latex_minted
Nlogo.py is the **style** file, you can change the name of this file, but you must change the class name in this file to **\<name\>Style**.

netlogo.py is the **lexer** file.

These two files are created from 
"https://sourceforge.net/projects/netlogo-pygment/", with very few changes. 
Thanks to Jchiele

###Installation method (tested on Ubuntu 16.04 and Mac OS X EI Capitan)
First you must have python installed, if not, install by (on Ubuntu)
```
sudo apt-get install python
```
Then you must have pygments installed, if not, install by (on Ubuntu)
```
sudo apt-get install python-pygments
```
**or**
```
sudo pip install pygments
```
Then find the pygment library:

pygment will probably installed in /usr/bin or /usr/local/bin, test that by
```
which pygmentize
```
_On Ubuntu, if pygments is installed in /usr/local/bin, the library is in/usr/local/lib. If it is installed in /usr/bin, the library is in /usr/lib/_

copy the **lexer** file to the the **lexer** library
```
sudo cp netlogo.py /usr/lib/python2.7/dist-packages/pygments/lexers/
```
Then go to the lexer directory and run the mapping 
```
sudo cd /usr/lib/python2.7/dist-packages/pygments/lexers
sudo python _mapping.py
```
Now add the **style** file to **style** library
```shell
sudo cp Nlogo.py /usr/lib/python2.7/dist-packages/pygments/styles/
```
Congratulations! Now the configuration is ready!

Here is an example latex file
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel} 
\usepackage{minted}
\usemintedstyle[netlogo]{Nlogo}
\begin{document}
\begin{minted}{netlogo}
to test-setup
   clear-all
   create-turtles 100[
      setxy random-xcor random-ycor
   ]
   reset-ticks
end
\end{minted}
\end{document}
```
save this file to "try.tex"
```
pdfLatex -shell-escape try.tex
```
If you are using IDE like texMaker, configure the editor to add -shell-escape after pdfLatex

Then you can view the "try.pdf" file!


