# experiment 1 
When adding adaptative way too many false positives
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

[INFO]: RETR_EXTERNAL: 60 bubbles found, took 32.03463554382324 miliseconds
[INFO]: RETR_LIST: 21083 bubbles found, took 237.6091480255127 miliseconds
[INFO]: RETR_CCOMP: 21083 bubbles found, took 1352.4339199066162 miliseconds
[INFO]: RETR_TREE: 21083 bubbles found, took 1399.1053104400635 miliseconds

# experiment 2 

gray = cv2.GaussianBlur(gray, (5, 5), 0)

2023-09-04 20:49:11,450 [INFO]: RETR_EXTERNAL: 1456 bubbles found, took 22.045135498046875 miliseconds
2023-09-04 20:49:11,450 [INFO]: RETR_LIST: 1566 bubbles found, took 20.229578018188477 miliseconds
2023-09-04 20:49:11,450 [INFO]: RETR_CCOMP: 1566 bubbles found, took 14.773368835449219 miliseconds
2023-09-04 20:49:11,450 [INFO]: RETR_TREE: 1566 bubbles found, took 14.022111892700195 miliseconds

without the gaussianblur 

2023-09-04 20:51:26,206 [INFO]: RETR_EXTERNAL: 1468 bubbles found, took 23.671865463256836 miliseconds
2023-09-04 20:51:26,206 [INFO]: RETR_LIST: 1589 bubbles found, took 30.69162368774414 miliseconds
2023-09-04 20:51:26,206 [INFO]: RETR_CCOMP: 1589 bubbles found, took 18.80812644958496 miliseconds
2023-09-04 20:51:26,206 [INFO]: RETR_TREE: 1589 bubbles found, took 15.835762023925781 miliseconds

reduce around 1% the number of bubbles detected.

# experiment 3

change aproximation parameter in the findCountour
no visible results, the number of detected bubbles are the same and visually the results are the same
no check done to confirm is the bubbles are the same.

2023-09-04 20:56:32,749 [INFO]: RETR_EXTERNAL: 1468 bubbles found, took 24.694442749023438 miliseconds
2023-09-04 20:56:32,749 [INFO]: RETR_LIST: 1589 bubbles found, took 28.215885162353516 miliseconds
2023-09-04 20:56:32,749 [INFO]: RETR_CCOMP: 1589 bubbles found, took 20.11275291442871 miliseconds
2023-09-04 20:56:32,749 [INFO]: RETR_TREE: 1589 bubbles found, took 17.678499221801758 miliseconds

