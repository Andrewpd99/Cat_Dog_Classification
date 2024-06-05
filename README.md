# Cat and Dog Classification through CNN

This project demonstrates a Cat and Dog Binary Classification algorithm using a Convolutional Neural Network (CNN) to classify images as either a cat or a dog. The dataset consists of 25,000 images from the Kaggle Dogs vs. Cats competition, which were used during the training process. The dataset can be found in the 'train' folder.

## Dataset

The dataset is available at [Kaggle Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data).

## Steps Taken

1. **Gathered Data**: Collected images of cats and dogs.
2. **Preprocessed Data**: Preprocessed data for faster processing within the algorithm (`preprocess_data.py`).
3. **Created Directories**: Created train/test directories and organized data accordingly.
4. **Initial Model**: Developed a Three Block VGG Model with an accuracy of approximately 79%.
5. **Improved Model**: Switched to a VGG16 model, achieving an accuracy of approximately 97%.
6. **Final Directories**: Organized final train/test directories.
7. **Model Creation**: Ran `create_model.py` to create a VGG16 model and saved the results as `final_model.h5`.
8. **Prediction**: Used `make_prediction.py` to load the saved model (`final_model.h5`) and predict whether an input image contains a cat or a dog.
9. **Accuracy**: Achieved a 98% accuracy rating on the sample image using `make_prediction.py`. To test the model, change the `image_file` variable to the name of the image file you want to test.
10. **Explore**: Have fun with this cat and dog binary classification algorithm!

## Installation:
1. Clone the repository
2. Install dependecies
3. Run the program and/or reproduce it in your own way

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.



