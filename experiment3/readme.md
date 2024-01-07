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