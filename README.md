# QETool_pip

## TODO:

- [ ] Update example text file
- [ ] Finish README
- [ ] Installation with `scl enable rh-python34 bash`
- [ ] Add check to make sure user is running Python 3.X

### About

Along with the website `netqe-infra01.knqe.lab.eng.bos.redhat.com:8009` this tool was made to view network test data for the Red Hat Network QE team.  It uses matplotlib in order to create the graphs which are present in the output PDF.  Uses website API calls to access and write to the mongodb.

This tool will create two new commands:
* `fileMaker [-o (<output file name>]`
    * -o &nbsp; --output &nbsp; [default: out.txt]
* `graphGen -f <input file name>`

### Installation

This tool requires Python version 3.X

1. First install matplotlib on your system through pip:
    ```
    sudo (pip|pip3) install matplotlib
    ```
1. If you are using a virtualenv use the flag `--system-site-packages` so that system wide packages are available to the virtual environment.

1. If your system does not come preinstalled with Tkinter for python3 run one of the following commands based on your system.
  * `sudo yum install python3-tk`
  * `sudo apt-get install python3-tk`

1. Finally:
    ```
    (pip|pip3) install qeGraphMaker
    ```

### Input text file
The input text for the graph generator is a well structured file as defined in the [example file](/graphMaker/multiGraphFileExample).

### Input file generator
For a user friendly process when creating the input file use the `fileMaker` command.  This will walk you through the process of creating a file that can the be passed into `graphGen`

### The graph generator
