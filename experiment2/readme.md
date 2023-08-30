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