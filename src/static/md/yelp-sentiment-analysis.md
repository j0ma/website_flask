# yelp review sentiment analysis

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

*Overall, the goal was to gauge the sentiment of yelp reviews as being positive or negative, using a maximum entropy classifier and stochastic gradient descent optimizer implemented from scratch. I enjoyed this project a lot and had a good time implementing things with only numpy.*

*For more information about the files referenced in the writeup below, see the [project repository](https://gitlab.com/jonnesaleva/maxent-sgd-from-scratch) on Gitlab.*

---

### Code Structure

The code is centered around `maxent.py` which contains the logic to fit the MaxEnt model and classify examples. The experiments are located in `exp1_exp2_grid.py` as well as `exp3.py`. Feature extraction is done in `extract_features.py` and leverages the `sklearn` library. To run the code, see instructions in `README.md`. The instructions have been tested in a clean Python 3.7 environment with Miniconda. After running the code, the results of individual experiments will be saved in the `results` folder.

### Experimental Settings

Our model is trained on data $\mathbb{D} = \{(\mathbf{\phi(x)}_i, y_i)\}_{i=1}^n$ where each observation consists of a vector of "feature counts" $\mathbf{\phi(x)} \in \mathbb{R}^D$ and a label $y$, represented either as an integer or a one-hot vector $\mathbf{y} \in \{0,1\}^K$, where $K$ is the number of classes.

We transform $\mathbf{\phi}(x)$ into a K-dimensional probability vector $\mathbf{\pi}$ via the $\text{softmax}$ function and a dot product between the feature count vector and class-specific parameter vector $\theta_k$: $P(y_i = k) = \pi_k(\mathbf{\phi(x)}_i) = \frac{\text{exp}(\mathbf{\theta_k} \cdot \mathbf{\phi}(x)_i)}{\sum_{j=1}^K \text{exp}(\mathbf{\theta_j} \cdot \mathbf{\phi}(x_i))}$

The "feature counts" in our case correspond to a "bag of words" counts, so the dimensionality $D$ is in fact equal to the size of the vocabulary, $|V|$. We stack the class-specific parameter vectors into a parameter matrix $\Theta \in \mathbb{R}^{K \times D}$.

The loss function, ie. the averaged negative log likelihood, is computed in matrix form as $\lambda ||\Theta||_F^2 - \frac{1}{N}\mathbf{1}^\top(\mathbf{Y}\otimes\log\mathbf{\Pi})\mathbf{1} = \lambda ||\Theta||_F^2 - \frac{1}{N} \sum_{i=1}^N \sum_{k=1}^K \mathbf{1}\{y_i = k\} \log P(y_i = k)$ where $\otimes$ denotes the elementwise matrix product. $\mathbf{Y}$ and $\mathbf{\Pi}$ are the K-by-N matrices of observed labels and softmax probabilities.

The gradient is computed as $\nabla L = \lambda\Theta - \frac{1}{M} \sum_i (\mathbf{1}\{y_i\} - \pi(\phi(x_i)))\odot\Phi_i$ where $\Phi_i$ is K-by-D matrix consisting of stacking the feature vector $\phi(x_i)$ on top of itself K times and $\odot$ denotes the row-wise vector-matrix product. $M$ denotes the minibatch size.

### Experiments 1 & 2

We run these together as a grid and work through the various values for the training set size $N$ and minibatch size $M$. 

<center>

![Training set size vs accuracy](../static/img/training_set_size_vs_accuracy.png){height=20%}

![Minibatch size vs accuracy](../static/img/minibatch_size_vs_accuracy.png){height=20%}

![Heatmap & L2 penalty vs accuracy](../static/img/heatmap_l2_combined.png)

</center>

Overall, it seems like as long as the minibatch is not too small, and we take a large enough set as our training set (say, 1000 to 10000 samples), we gain all the accuracy we can, at least as measured on the development set. Beyond that, larger minibatches simply cause a lot of computational overhead without much gain. It would most likely have been useful to run the experiments several times and plot several curves for each experimental condition, in order to get an idea of the variance in the outcome. Based on the heatmap on the last page, we adopt $N=50000$ and $M=100$ as our settings for training set size and minibatch size for Experiment 3.

### Experiment 3

For experiment 3, we simply note that increasing the regularization penalty only seems to harm our results. In fact, this seemed rather surprising, given the large dimensionality of our features. In `maxent_test.py`, we only apply $\lambda = 0.01$ as our regularization penalty for this reason.

---

<tfoot>

<tr>

  <td>© Jonne Sälevä, 2020</td>

</tr>

</tfoot>