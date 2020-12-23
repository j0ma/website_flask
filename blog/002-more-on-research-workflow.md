---
title: More on Research Workflow
author: Jonne Saleva
date: 2020-12-22
---

I'm now a semester into my Ph.D. at Brandeis, and after a couple of projects, I've now refined some of the ideas from the previous post and have some additional thoughts on what works (for me) and what doesn't.

### What was worth it

- Experiment management software -- [Guild.AI](https://guild.ai)
  - The TUI for `guild compare` is great, for example
- Scripts with _verbose_ arguments
  - Do: `--input`, `--output`, `--mode`
  - Don't: `-i`, `-o`, `-m`
- Use [`click`](https://click.palletsprojects.com/en/7.x/) for creating CLIs
- Coreutils + command line tools like `grep`, `sed`, `awk`, `cut`, `paste`, `...`
- In particular, the above tools are very, very useful inside little shell scripts
- Infrastructure-as-code is suprisingly worthwhile (e.g. `guild.yml`)
- Symlinking is also very worthwhile
  - Create an `experiments` folder that is the sole entry point for data on that experiment
  - Inside each experiment folder, simply symlink to data / checkpoints etc.
  - This way, any script only needs to navigate to the folder of that particular experiment

### What I never found the use case for

- A lot of examples seem to have train & evaluation done in the same script
- This is often not true when you train with one metric & evaluate using another.
- Case in point: evaluating MT / seq2seq outputs decoded using beam search
- I also haven't yet felt the need for `cookiecutter` or similar tools that produce boilerplate code.
