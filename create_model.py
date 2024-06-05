import os
import tensorflow as tf

# define cnn model
def define_model():
    # load model
    model = tf.keras.applications.vgg16.VGG16(include_top=False, input_shape=(224, 224, 3))
    # mark loaded layers as not trainable
    for layer in model.layers:
        layer.trainable = False
    # add new classifier layers
    flat1 = tf.keras.layers.Flatten()(model.layers[-1].output)
    class1 = tf.keras.layers.Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(class1)
    #define new model
    model = tf.keras.models.Model(inputs=model.inputs, outputs=output)
    # compile model
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model


def run_test_harness():
    # define model
    model = define_model()
    # create data generator
    
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(featurewise_center=True, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')
    # specify imagenet mean values for centering
    datagen.mean = [123.68, 116.779, 103.939]
    # prepare iterators
    base_dir = os.path.abspath(os.path.dirname(__file__))
    train_it = datagen.flow_from_directory(os.path.join(base_dir, 'finalize_dogs_vs_cats/'), class_mode='binary', batch_size=64, target_size=(224,224), shuffle=True)

    # if no images found
    if len(train_it) == 0:
        print("No images found. Please check the directory structure and paths.")
        return
    
    # fit model
    steps_per_epoch = train_it.samples // train_it.batch_size
    model.fit(train_it, steps_per_epoch=steps_per_epoch, epochs=10, verbose=0)
    # save model
    model.save(os.path.join(base_dir, 'final_model.h5'))

# run the test harness
run_test_harness()