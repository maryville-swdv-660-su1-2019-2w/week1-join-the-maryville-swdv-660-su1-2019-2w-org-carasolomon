# Tacara Solomon - SWDV 660 Week 1 Assignment
# Philosophy Quote Generator

# import dependencies
import clrc 
from colorama import init, Back, Fore
import random

init()
# main function
def main():
     quotes = [
'The unexamined life is not worth living – Socrates',
'Entities should not be multiplied unnecessarily – William of Ockham',
'He who thinks great thoughts, often makes great errors – Martin Heidegger',
'We live in the best of all possible worlds – Gottfried Wilhelm Leibniz',
'What is rational is actual and what is actual is rational – G.W.Fy. Hegel',
'God is dead! He remains dead! And we have killed him. – Friedrich Nietzsche',
'There is but one truly serious philosophical problem, and that is suicide – Albert Camus',
'Happiness is not an ideal of reason but of imagination – Immanuel Kant',
'There is only one good, knowledge, and one evil, ignorance – Socrates',
'He who is unable to live in society, or who has no need because he is sufficient for himself, must be either a beast or a god – Aristotle',
'We are too weak to discover the truth by reason alone – St. Augustine'
]
     # Selects random quote
     randomQuote = random.choice(quotes)

     print(Back.BLACK + Fore.CYAN + 'This program generates a random quote from a philosoher.')

     choice = input(Back.BLACK + Fore.MAGENTA + 'Would you like to get a quote? y/n: ' )
 

     if choice == 'y':
         clrc.success('Quote: ', randomQuote)
     elif choice == 'n':
         clrc.warn('Maybe another time!')
     else: 
         clrc.error('Input Error: Please try again.') 
 



main()