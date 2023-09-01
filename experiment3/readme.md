# experiment 3

- even after rotations and darkening of the image no changes to the final result,
is the validation data set correctly set?

- make image darker with PIL was super easy, no need to convert the image to [0..1]

```python
enhancer = ImageEnhance.Brightness(image)
darker_image = enhancer.enhance(0.5)  # Darken the image by setting the brightness to 50%
```

see https://pillow.readthedocs.io/en/stable/handbook/index.html

