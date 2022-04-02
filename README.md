# website-code-guesser
Python script that guess the codes on website using configurable code format.

In config.py needs to be defined targetet website and chrome driver. 

Basically, it finds the search bar on the site, following by guessing random codes (e.g. ABC123) trying to find correct combinations, if generated code fails, than it is added to tries.txt that is evaluated next time guess is made, so no two same guesses exist. If, however, guess is correct it adds to correct_guesses.txt. Of course, one can make only few guesses, so script is enrich by threads and if site reach maximum requests limit, script ends. 

Disclaimer: This code was written only for educational purposes. I'm not responsible for any illegal use of this tool. Usage of brute force to get to any targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. I assume no liability and I'm not responsible for any misuse or damage caused by this tool. Use it at YOUR OWN RISK.


