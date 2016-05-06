from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

class NlogoStyle(Style):
    """
    A NetLogo style, according to the NetLogo Editor Highlighting.
    """

    default_style = ""

    styles = {
        Whitespace:                "#ffffff",

        Comment:                   "#5a5a5a",

        Operator:                  "#660096",

        Keyword:                   "#007f69",

        Name:                      "#090909",
        Name.Function:             "#660096",
        Name.Namespace:            "#090909",
        Name.Constant:             "#963700",        
        Name.Tag:                  "#0000aa",

        Number:                    "#963700",

        String:                    "#963700",

        Error:                     "#F00 bg:#FAA"
    }
