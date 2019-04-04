# Template Repo

This repo serves as a template for research project conducted by student interns.
The general structure of the repo is inspired by the paper,
[Good enough practices in scientific computing](pcbi.1005510.pdf). We recommend
you read through the paper as it provides good information about conducting
computational research. This repo also serves as a guide for references to tutorials for NERSC's
computing resources at the lab, where to store your project material, and expectations
about documentation to ensure that we promote reproducibility in research!

For those of you who have not much experience working with Github projects,
here is a link to a great quick [tutorial](http://rogerdudler.github.io/git-guide/).

## Repo layout
Here are some of the highlights from the paper:

### Data Management
- Data should be stored separately from your code (i.e within a `data/` folder)
- Make sure to save your raw data! Have one static copy among your group.
- Use file types to your advantage!
  - Tabular? -> .csv
  - Not Tabular? -> .yaml, .json, .xml
  - Working with IO heavy work? Try HDF5
- Make sure headers and labels are easily understood
  - DO: patient_height
  - DON'T: var_12, feature_6
- Document your data processing steps in a README

### Software
- Keep uncompiled source code in one place (i.e. within a `src/` folder)
- Provide a description of a program at the start of its code.
- Decompose your program into functions!
  - Functional programming is very useful and languages like Julia take advantage of this for use in
    scientific computing.
  - Don't copy and paste code if you can write a function instead!
- Give functions and variables meaningful names
  - Rule of thumb? The greater the scope, the more descriptive the name should be.
- DONT! Control how your program behaves by commenting and uncommenting blocks of code.
- Always provide a dummy dataset for testing
- Program outputs should be stored in one place i.e. within an `output/` folder)

### Documentation
- Use Jupyter notebooks for tutorials, and to showcase results!
- Have a good project README with information about setting up the project and how to run it.
- File names should work as documentation too!

### Codebase Management
- Take full advantage of all the features of Git!
- Remember: Small commit with descriptive push messages make version control easier!
- Communicate with team when changes are made to keep everyone up-to-date.

## Getting Started on NERSC's CORI
After getting access to NERSC, take some time to read through NERSC's documentation
on their site [here](https://www.nersc.gov/users/computational-systems/cori/getting-started/).
There you'll learn how to navigate Cori and how to submit your first job!

The [run.sbatch](run.sbatch) in this repo serves as an example of a CORI batch job file.

It is also highly recommended for you to try out the interactive session on CORI
where you can allocate up to 64 nodes at once for 4 hours! The link to how to request
a interactive session is [here](https://docs.nersc.gov/jobs/interactive/).

## Where to store code and data
There is a shared project drive on Cori under: `/project/projectdirs/m1532`
Here is where you can share and store large files between members of your team.

Since the repository is shared with the WeFold project, we've made two directories
for ongoing work for protein-related and MVP-related projects respectively.
These two directories are named: `Projects_Proteins/` and `Projects_MVP/`

Within these folders feel free to make directories for your own use. There is also
three special directories we are maintaining as a way of archiving final versions
of projects. The follow explains the purpose of each:

- `_datasets/` : contains final versions of datasets created during your project
which can be later used by future researchers.
- `_models/` : contains final versions of models which can be easily executed or imported
by future researchers.
- `_repo/` :  contains an archived versions of your final project codebases.

## Where to save project deliverables
During your time at the lab, depending on your program, you will be required to
write presentations and papers for deliverables. We want to be able to show the
next years interns your amazing work, and have something for them to reference when working
on their own projects.

We have created shared folders on Google Drive where you will be able to save copies
of your work. Links to these folders will be provided when you arrive.

## Working with Jupyter
One of the recently added features to Cori include support for running JupyterLab
on shared nodes for small-scale data analysis and visualizations. Juypter is a great
way of building reproducible projects thanks to its ability to embed documentation
using git-flavored markdown. Its highly recommended (cough cough please do it!)
that you have a Jupyter notebook for your project to provide a tour of your work.
The more the merrier!

For more information on how to use Jupyter and notebooks, we recommend looking through
one of our previous student's presentation on using [Jupyter on Cori](https://github.com/shahzeb1/jupyter-talk).
