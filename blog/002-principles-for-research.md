---
title: Research principles for a replicable workflow
author: Jonne Saleva
---

This fall, I will begin my Ph.D. in Computer Science at Brandeis, where I'll be working on low-resource and multilingual applications of NLP and machine learning. Obviously, I am very excited, but based on my first year of research experience during my M.S., I've recently started to feel that it would be beneficial to establish a set of **research principles** that can help avoid noob-level pitfalls and make the research more replicable.

With that in mind, here are some I came up with:

- Use `cookiecutter` to have a common directory structure
- Use modular scripts. For example:
    - downloading training data
    - preprocessing (tokenization etc)
    - featurization & binarizing
    - training
    - tuning hyperparameters
    - post-processing
    - evaluation
- All scripts should use *command line options*. Some typical ones I've needed:
    - `--input`: input folder/file
    - `--output`: output folder/file
    - `--model-name / --arch`: name of model to run / eval / use as prefix
    - `--model-bin`: path to model binary
    - `--seeds`: (comma-separated) list of seeds to run
- All scripts consume input from a file, and write output to a file
    - This way, the stages of data processing remain transparent
    - Respecting the UNIX philosophy
- Do not forget common sense testing
    - All unfiltered outputs should contain a similar number of lines
- For experiment management, use something like `runx` which uses YAML
- Use a Makefile to document & reliably execute experiments
- Define a wiki for the project, and document the following:
    - Overall documentation for the codebase
    - Instructions for running experiments
    - Environment information
    - Experimental results
- Use `tensorboard` for logging

Some of these I've already incorporated into my workflow, while some of these are still a work in progress. I think my next big push will be to get myself used to using `runx` and `tensorboard`
