Sample tutorial for MNIST dataset.

Before you start make sure to check requirements.txt to make sure you have all
of those packages installed. (Anaconda should take care of this for you)

## Usage
First generate the model ('`model.pkl`'):
```bash
$ python classify.py
```
This creates a 'model.pkl' file, which predict.py will open in order to predict
user-drawn inputs.  Run `python predict.py` and draw a digit in the input window and
press enter. Your drawing will be scaled and normalized to conform (more or less)
to the format of the training data, and plugged into the function that
scikit-learn learned. The predicted digit will be printed to the screen in square
brackets.

You can also run `python draw.py` and draw a digit into the output window, then
open up the `img.png` file to see what the scaled and normalized output looks
like. This image is what's being flattened into a vector and fed into the scikit
learn model.

##Tutorial
You should start your jupyter-notebook service and then open classify.ipynb in your web browser. 
You can then run the code and see some sweet graphs to visualize the process.
