## CookieCutterExample

*[ TODO Add project description]*

## How to Run

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project.

```shell
mkvirtualenv CookieCutterExample
pip install -e 'git+https://github.com/mcpad/Springboard/CookieCutterExample.git#egg=CookieCutter_Example_Datascience'
```

> For a private repository accessible only through an SSH authentication, substitute `git+https://github.com` with `git+ssh://git@github.com`.

*[ TODO Add instructions to run package scritps ]*

## How to Contribute

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project in development mode.

```shell
mkvirtualenv CookieCutterExample
git clone https://github.com/mcpad/Springboard/CookieCutterExample.git
cd CookieCutterExample
pip install -r requirements.txt
pip install -e .
pip freeze | grep -v CookieCutter_Example_Datascience > requirements.txt
```

> For a private repository accessible only through an SSH authentication, substitute `https://github.com/` with `git@github.com:`.

Then, create or select a GitHub branch and have fun... 

Tutorial found at https://github.com/Satalia/production-data-science/tree/master/template
Explanations at https://github.com/Satalia/production-data-science
