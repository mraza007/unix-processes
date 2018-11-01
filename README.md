# unix-processes
A simple script that allows you to see unix/linux/mac processes with the name and their cpu usage

### Installion
- `git clone repo` and `cd repo/`.
- Make sure you have pipenv installed if you do then activate using `pipenv shell`
- Install dependencies using `pipenv install`
- Add the script to your path

##### Usage 
- It's really simple to use this script `process --list` to list the current processes
- To look up a process `process look <pid>` and this will print specific details of the process.
- To generate the cpu_usage bar graph of specific `pid` use this command `graph <pid>`

**Note**:In order to generate a cpu usage graph install `pip3 install termgraph ` and add to the path.

##### Terminal Cast