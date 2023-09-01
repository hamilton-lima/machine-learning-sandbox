# experiment 2
split the process in smaller scripts

bash to run one after the other 

main.py 
```
/input > resize.py > /resized 
/resized > rotate8.py > /rotated
/rotated > train.py > /saved-network
/saved-network + /test-data > validate.py > /results
/results > report.py > /reports
```

## executing a custom set of scripts 

create a new json file representing the steps that should be executed
```
python3 main.py start-with-validate.json
```


Image after rotation 

```
 [[0.02352941 0.01568628 0.02352941 1.        ]
  [0.01960784 0.01176471 0.01568628 1.        ]
  [0.08627451 0.08627451 0.07058824 1.        ]
  ...
  [0.76862746 0.7372549  0.67058825 1.        ]
  [0.78431374 0.74509805 0.6784314  1.        ]
  [0.8        0.75686276 0.6862745  1.        ]]]
  ```
