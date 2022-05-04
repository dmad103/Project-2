# The librararies are imported
import dog_names
import re

# The variable holds the data for all of the female dog names
femaledognames = dog_names.all(gender='female')

# The names are printed
print(femaledognames)

# Female dog names are filtered for a name that starts with the letter G
lettername = re.findall(r'[G]\w+', femaledognames)

# The female dog names that start with the letter G are printed out
print(lettername)


