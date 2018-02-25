# Cleano v1.0

A Py3-package to clean your desktop. 
Once the script is run, it alerts the user once in 5 hours to clean the desktop if more than 5 files are present.


### Key features
* The script auto runs and alerts **only** when the number of files exceeds limit.
* Alerts user every 5 hours (default).
* Function to determine top 10 large files in a given directory (default: home) (recursively traverses the directory).
* Classifies files without extensions.

### Other features
* Can be run as an autostart application in ubunutu.
* Configurable (limit on number of files, time before alert)

***Caveats***
  * Works only for Linux
  * Only a prototype (functional but yet to be refined)

### Prerequisites

You will need the following additional packages to run the code.
Python >= 3
```
adscheduler
os
sys
platform
re (regular expressions)
```

### Installing

Create a folder called 'Cleano' in home directory.
Copy the files in the repo into 'Cleano'.

With the root as 'Cleano', execute the following line (including paranthesis and ampersand)
```
....~/home/your-name/Cleano$ (python3 cleano.py &)
```
That's it. This produces periodic alerts to clean your desktop and also does it for you.

Your result will be ....

<a href="https://imgflip.com/gif/2597x6"><img src="https://i.imgflip.com/2597x6.gif" title="made at imgflip.com"/></a>


### To autostart script
Add the same line as above (with complete paths) to Startup Applications.

[How to launch script at startup](https://itsfoss.com/manage-startup-applications-ubuntu/)


After adding it will look like this:

<a href="https://ibb.co/gYfr5x"><img src="https://preview.ibb.co/f8nFXc/Screenshot_from_2018_02_25_14_10_14.png" alt="Screenshot_from_2018_02_25_14_10_14" border="0"></a><br />

Now, the process will run automatically on start up.

Note: If the process is autorun, the locations of the files should not be changed.

## Authors

**Rajalakshmi.V**  [git repo](https://github.com/rajalakshmi-v15)



## Acknowledgments

* I have used Fleep tool (to determine the files without extensions) [fleep](https://github.com/floyernick/fleep/tree/master/fleep)


  
    
