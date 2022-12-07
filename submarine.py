"""
Description: Class for submarine object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class submarine(ship):
    def __init__(self, name:str = "submarine", length:int = 3,  horizontal:bool = True) -> None:
        super.__init__(length, horizontal)
        self.name = name

