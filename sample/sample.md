This folder contains sample images of laundry symbols, that we took from the T-shirts we had on hand.  We used these images as test cases when implementing the API.

To test these yourself, enter the virtualenv and run `python predictions.py [image name in sample folder]`, i.e. `python predictions.py sample1-1.jpg`.

You can test multiple images at once by separating the image names with a space:
`python predictions.py sample1-1.jpg sample 1-2.png sample1-3.png`.

The output will be in the form of the image path, followed by the predicted laundry instruction, such as:
```
sample/sample1-1.jpg
Do not dry clean
```
