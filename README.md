# netlogo_latex_minted
Nlogo.py is the style file, you can change the name, but the class name must be <name>Style
netlogo.py is the lexer name
These two files are created from 
"https://sourceforge.net/projects/netlogo-pygment/", with very few changes. 
Thanks to Jchiele

Installation method (tested on Ubuntu 16.04)
First you must have python installed, if not, install by
>sudo apt-get install python
Then you must have pygments installed, if not, install by
>sudo apt-get install python-pygments

pygment will probably installed in /usr/bin or /usr/local/bin, test that by
>which pygmentize
suppose it is installed in /usr/bin, copy the lexer file to the corresponding libary
>sudo cp netlogo.py /usr/lib/python2.7/dist-packages/pygments/lexers/
Then go to the lexer directory and run the mapping 
>sudo cd /usr/lib/python2.7/dist-packages/pygments/lexers
>sudo python _mapping.py

Now add the style file to style directory:
sudo cp Nlogo.py /usr/lib/python2.7/dist-packages/pygments/styles/
Now the configuration is ready!

"if it is installed in /usr/local/bin, change the directories /usr/lib/* to /usr/local/lib*"

Here is an example latex file
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

save this file to "try.tex"
>pdfLatex -shell-escape try.tex
if you are using IDE like texMaker, configure the editor to add -shell-escape after pdfLatex

