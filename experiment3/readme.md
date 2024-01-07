# experiment 3

- even after rotations and darkening of the image no changes to the final result,
is the validation data set correctly set?

- make image darker with PIL was super easy, no need to convert the image to [0..1]

```python
enhancer = ImageEnhance.Brightness(image)
darker_image = enhancer.enhance(0.5)  # Darken the image by setting the brightness to 50%
```

see https://pillow.readthedocs.io/en/stable/handbook/index.html

## update on 06-Jan-2024 
- Add images from real bubbles to folder: `bubbles-jan-2024/input` in two separated folders boa-espumacao and ma-espumacao
- Created scripts definition with the `bubbles-jan-2024` folder as parent
- copy `bubbles-jan-2024/input` to `bubbles-jan-2024/test-data`

Execute the experiment 
```
python3 main.py full-process-input-bubbles-jan-2024.json
```

found error
```
2024-01-06 19:05:44,462 - INFO - CLASS INDICES ={}
2024-01-06 19:05:44.763860: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] could not open file to read NUMA node: /sys/bus/pci/devices/0000:01:00.0/numa_node
Your kernel may have been built without NUMA support.
2024-01-06 19:05:44.764713: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1960] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-01-06 19:05:45,414 - WARNING - `lr` is deprecated in Keras optimizer, please use `learning_rate` or use the legacy optimizer, e.g.,tf.keras.optimizers.legacy.RMSprop.
Traceback (most recent call last):
  File "main.py", line 72, in <module>
    main()
  File "main.py", line 69, in main
    run_script(script_name, input_folder, output_folder, model_folder)
  File "main.py", line 46, in run_script
    module.run()
  File "/home/ubuntu/source/machine-learning-sandbox/experiment3/./scripts/train.py", line 75, in run
    train_model(input,output)
  File "/home/ubuntu/source/machine-learning-sandbox/experiment3/./scripts/train.py", line 62, in train_model
    model_fit = model.fit( train_dataset,
  File "/home/ubuntu/.local/lib/python3.8/site-packages/keras/src/utils/traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "/home/ubuntu/.local/lib/python3.8/site-packages/keras/src/preprocessing/image.py", line 103, in __getitem__
    raise ValueError(
ValueError: Asked to retrieve element 0, but the Sequence has length 0
```

Tried to reinstall all dependencies `pip3 install -r ../requirements.txt`

WRONG FOLDER NAMES!!!!

### First result 50% accuracy but inverted
- all good were classified as bad
- all bad were classified as good

### Changed input data to 'espumacao' e 'not-espumacao' 
copied 'espumacao' e 'not-espumacao' to `test-data` folder as the images is hardcoded in reports.py

result 60% 
with good matching for good bubbles 

### ERROR uploading trained model for bubbles - will remove it.
remote: error: File experiment3/bubbles-jan-2024-saved-network/trained_model.h5 is 132.48 MB; this exceeds GitHub's file size limit of 100.00 MB        

