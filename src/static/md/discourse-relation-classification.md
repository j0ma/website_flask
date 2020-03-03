# discourse relation classification

</div>

<thead>

<tr>

  <td>[Home](/)</td>

  <td>[Research](/research)</td>

  <td>[Portfolio](/portfolio)</td>
<td>[Resume](/resume)</td>

</tr>

</thead>

---

*Quick note from Jonne, march 2020: This page is a HTML version of my writeup for this project.*

*Overall, the goal was to classify text into one of several different discourse relation classes, and the task was based on the [CoNLL 2016 Shallow Discourse Parsing Task](https://www.cs.brandeis.edu/~clp/conll16st/). *

*For more information about the files referenced in the writeup below, see the [project repository](https://gitlab.com/jonnesaleva/discourse-relation-classification) on Gitlab.*

---

### Code Structure

Overall, the main workhorse of the code is the `experiment.py` file which contains all classes required to run experiments. To run the code, follow instructions in `README.md`. Everything should be properly automated, and can be executed using various `make` commands. The experiments are run using `run_ff.py` and `run_cnn.py` which instantiate several `Experiment`s corresponding to the various hyperparameters that get executed.

In addition to the `.py` files there are also two Jupyter Notebooks, containing _extensive_ visualizations and tabular analyses. We wholeheartedly encourage the grader to peek at those in order to get a full idea beyond the 3 pages of this report.

### Experimental Settings

#### Feature representations and other design desicions
For word vectors, we opted to use 300-dimensional `FastText` vectors since they are trained to handle subword representations. To further avoid OOV issues, we vectorized all my sentences using `pymagnitude` package, which auto-handles subword representations, so there was no need to perform lemmatization or stemming of any kind.

To construct the feature representations, we first pick 25 tokens from Arg1 and Arg2, but in such a way that Arg1 tokens get extracted in reverse order, so that the argument tokens form a "window" around the connective. This was an approach suggested by `<REDACTED>`. For the connective, we simply pick 2 tokens. These numbers are justified by looking at the empirical distribution of token counts in Arg1, Arg2 and the connective, and picking values that cover over 90% of the input sentences. This analysis can be reproduced using `make explore` after feature extraction has been performed.

In line with what was discussed by the teaching staff, we first stack the vectors of tokens in a sentence together verticall, forming a N-b-300 representation. We call this condition the `stacked` condition. In addition, we experiment with **averaging** the rows of said matrix, to obtain a **single** 300 dimensional vector for the sentence. Two averaging conditions are introduced: either we average the word vectors for the entire sentence, or simpl the 52 tokens discussed previously. These form the `average_entire` and `average_padded` conditions.

#### Hyperparameter configurations
For feedforward networks, we first project the input to 512 hidden units (arbitrarily), and then follow with several layers according to three "layer conditions", or shapes: `funnel`, `bottleneck` and `double bottleneck`. In the `funnel` condition the layer sizes simply decrease, e.g. 512, 128, 64. In `bottleneck`, there is a small layer in between two larger ones, e.g. 512, 256, 64, 128. In `double bottleneck` we simply repeat a bottleneck twice. Finall, there is a softmax layer of 21 units. We also run feedforward networks using all three feature representations, `stacked`, `average_entire` and `average_padded`. Further, we experiment with whether including dropout after each full connected layer helps or not. In case dropout is used, its probability is kept constant at 0.5. 

For convolutional networks, we need an input matrix so we only use the `stacked` condition. In terms of parameters, we vary the number of convolutional layers, filters used, the kernel size, the inclusion of dropout after convolutional layers (fully connected layers always have dropout).

### Experiments

For both feedforward and convolutional networks, we run a grid of all hyperparameters for 50 epochs. Overall, this probably took around 12-15 hours to run. There are a total of 78 experiments for feedforward and 54 for convolutional networks.

### Results & discussion

After running the experiments, it is fairly clear that we could have managed with running the training for fewer epochs. Looking at the validation accuracy vs epochs, it is obvious that by 20 epochs, everything has already plateaued. 

<center>

![Validation accuracy vs epoch](../static/img/val_acc_vs_epoch.png){ height=256px }

</center>

In terms of what conditions outperform others, there are a few points to make but the results are not entirely clear. Features in the `stacked` condition do seem to be top performers for feedforward networks, with only stacked features present in the top 10 conditions.

Dropout also seems to help a great deal for feedforward networks, yielding on average about 0.1 absolute improvement in accuracy. This can as can be seen from the picture below:

<center>

![Effect of dropout on validation accuracy](../static/img/dropout_validation_treatment_effect_feedforward.png){ height=256px }

</center>

However, for convolutional networks it is not the case; in fact it seems to hurt performance. 

<center>

![Effect of convolutional dropout on validation accuracy](../static/img/dropout_validation_treatment_effect_val_conv.png){ height=256px }

</center>

Across all conditions, the best accuracy we see on the validation set is in the high 80s.

#### Test set
Overall the out-of-domain test scores are much lower. The best values for F1 seem to be around 0.5. Recall is definitely the weakest metric, especially in implicit cases

Overall we can see that the evaluation metrics produce similar distributions for convolutional networks and feedforward ones, as long as `stacked` features are used:

<center>

![Evaluation metric distribution for feedforward networks](../static/img/evaluation_metrics_feedforward_stacked.png){ height=256px }

![Evaluation metric distribution for convolutional networks](../static/img/evaluation_metrics_convolutional.png)

</center>

Therefore, overall there is no clear conclusion to things. Dropout helps, stacking helps, but personally I would still opt for feedforward over convolutional networks, given the ease of implementation. 

Please see the [Gitlab repository](https://gitlab.com/jonnesaleva/discourse-relation-classification) for more analysis!

---

<tfoot>

<tr>

  <td>© Jonne Sälevä, 2020</td>

</tr>

</tfoot>