    
    
    circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, 1, minDist=40, param1=50, param2=30, minRadius=0, maxRadius=0)
    with no parameters at min/max takes forever

    