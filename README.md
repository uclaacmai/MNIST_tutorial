Sample tutorial for MNIST dataset.

Before you start make sure to check requirements.txt to make sure you have all
of those packages installed.

## Usage
First generate the model:
```bash
$ ./classify.py
```
This creates a 'model.pkl' file, which predict.py will open in order to predict
user-drawn inputs.  Run `./predict.py` and draw a digit in the input window,
which will then be scaled and normalized to conform (more or less) to the format
of the training data.  The predicted digit will be printed to the screen.
