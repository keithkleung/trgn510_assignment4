# trgn_assignment4

**The following explains the content of this homework assignment for TRGN 510**

**About the program:**
- *This program will take a csv file as an argument and a column number as an input, and then print a file where the Ensembl gene name becomes replaced with its respective HUGO gene name.*

**Installation and Usage:**
- *Use the linux command "git clone" to extract a copy of this repository onto your server.*
- *You will find a file named as "ensg2hugo.py". This file contains the script that makes this program work.*
- *The script is created to be compatible with a gtf file named "Homo_sapiens.GRCh37.75.gtf". This file can be downloaded onto your server and within your working directory by using the "curl" command. Use the following to obtain the file: 'curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz'. The gtf file will then need to be unzipped, which can be done using the gunzip command. This gtf file will be used to create the dictionary needed to replace the HUGO name within a given csv file.*
- *Within your directory that contains both the "ensg2hugo.py" file and the gtf file, you must also provide a unit test file for the script to run with. The unit test file may be downloaded from the following link: https://github.com/davcraig75/unit. The file should be a csv file named "expres.anal.csv". Alternatively, the unit test csv file may also be found in the cloned repository already.*
- *Specific python packages will also be needed to ensure the program can be run. The needed packages will be listed below under "Dependencies".*
- *To run the script and create the file, run the following on your command line: ./ensg2hugo.py -f2 expres.anal.csv >expres.anal.hugo.csv*
- *Note that not all Ensembl gene names will be replaced with HUGO names within the generated csv file. This is due to the dictionary key created by reading the gtf file not having all the matches.* 

**Dependencies:**
- *sys python package*
- *re python package*
- *git*
- *csv python package*
- *fileinput python package*
- *pandas python package*

**Contact**
- *keithleu@usc.edu*

