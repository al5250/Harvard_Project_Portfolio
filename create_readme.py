import pandas as pd
import numpy as np

header_file = 'header.md'
ms_file = 'math-and-sciences.csv'
hu_file = 'humanities.csv'
output_file = 'README.md'

# Read in header
with open(header_file, 'r') as f_head:
  header = f_head.read()

# Read in data
ms_df = pd.read_csv(ms_file)
hu_df = pd.read_csv(hu_file)

with open(output_file, 'wb') as f_out:
  
  # Write header
  f_out.write(header + '\n\n')

  # Write math and sciences section
  f_out.write('## Math and Sciences\n\n')
  for idx, vals in enumerate(ms_df.values[::-1]):
    title, year, term, link, course, num, collabs, tools, acks = vals
    
    # Write project information
    f_out.write(str(idx + 1) + '. ')
    f_out.write('**' + title.strip() + '** ')
    f_out.write('(' + term.strip() + ' ' + str(year))
    if link is not np.nan:
      f_out.write(', [Link](' + link.strip() + ')')
    f_out.write(')  \n')
    
    # Write course information
    f_out.write('*Course Title*: ' + course.strip() + ' (' + num.strip() + ')  \n')

    # Write collaborator information
    if collabs is not np.nan:
      f_out.write('*Collaborator(s)*: ' + collabs.strip() + '  \n')
    if acks is not np.nan:
      f_out.write('*Acknolwedgements*: ' + acks.strip() + '  \n')

    # Write tools information
    f_out.write('*Tools*: ' + tools + '  \n\n')

  # Write humanities section
  f_out.write('## Humanities\n\n')
  for idx, vals in enumerate(hu_df.values[::-1]):
    title, year, term, course, num, paper = vals

    # Write project information
    f_out.write(str(idx + 1) + '. ')
    f_out.write('**' + title.strip() + '**  \n')

    # Write course information
    f_out.write('*Course Title*: ' + course.strip() + ' (' + num.strip() + ')  \n')

    # Write paper title
    f_out.write('*Paper Title*: ' + paper.strip() + '  \n\n')
