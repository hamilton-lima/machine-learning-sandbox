# %%
import tensorflow as tf 
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np 

from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop

# %%
img = image.load_img('images-experiment1/train/hamilton/Screenshot_8.png')
plt.imshow(img)

# %%
cv2.imread('images-experiment1/train/hamilton/Screenshot_8.png').shape

# %%
train = ImageDataGenerator(rescale=1/255)
validation = ImageDataGenerator(rescale=1/255)

# %%
train_dataset = train.flow_from_directory('images-experiment1/train/', 
                                          target_size=(200,200), 
                                          batch_size=3, 
                                          class_mode = 'binary')

validation_dataset = train.flow_from_directory('images-experiment1/validate/', 
                                          target_size=(200,200), 
                                          batch_size=3, 
                                          class_mode = 'binary')

# %%
train_dataset.class_indices

# %%
train_dataset.classes

# %%
model = tf.keras.models.Sequential( [ 
    tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape= (200,200,3)), 
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'), 
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'), 
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation = 'relu'), 
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

# %%
model.compile(loss= 'binary_crossentropy', optimizer = RMSprop(lr=0.001), metrics=['accuracy'])

# %%
model_fit = model.fit( train_dataset, 
                      steps_per_epoch = 3, 
                      epochs = 20, 
                      validation_data = validation_dataset)

# %%
def show_prediction_from_folder(dir_path):
    result = []
    for i in os.listdir(dir_path):
        name = dir_path +'//'+ i
        img = image.load_img(name, target_size=(200,200))
        # plt.imshow(img)
        # plt.show()
        
        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        images = np.vstack([X])
        
        # The result is a matrix!!!
        prediction = model.predict(images)
        
        print(">> prediction of {} is {}".format(name,prediction[0][0]))
        result.append( prediction[0][0] )
        if prediction == 0:
            print('It\'s Hamilton')
        else:
            print('Not him.') 
            
    return result 

# %%
def array2string(array_of_integers):
    inner = ", ".join(["{:.0f}".format(num) for num in array_of_integers])
    return f"[{inner}]"

folder_not_hamilton_results = show_prediction_from_folder('images-experiment1/validate/not-hamilton/')
folder_hamilton_results = show_prediction_from_folder('images-experiment1/validate/hamilton/')


# %%
accuracy_not_hamilton = sum(folder_not_hamilton_results) / len(folder_not_hamilton_results) * 100
accuracy_hamilton = (len(folder_hamilton_results) - sum(folder_hamilton_results)) / len(folder_hamilton_results) * 100

message = f"---RESULTS\n \
    not hamilton folder = {array2string(folder_not_hamilton_results)} {accuracy_not_hamilton}%\n \
    hamilton     folder = {array2string(folder_hamilton_results)} {accuracy_hamilton}%"
print(message)


