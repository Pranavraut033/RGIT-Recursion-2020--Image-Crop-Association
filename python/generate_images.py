import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import os
import json

data = {"NA": []}
i = 1
j = 1
total = len(os.listdir("./test/images")) * \
    len(os.listdir("./test/crops"))

for template_image in os.listdir("./test/crops"):
    added = False
    for main_image in os.listdir("./test/images"):
        img2 = cv.imread('./test/images/' + main_image)
        img1 = cv.imread('./test/crops/' + template_image)

        # Initiate SIFT detector
        sift = cv.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
        # BFMatcher with default params
        bf = cv.BFMatcher(cv.NORM_L1, crossCheck=False)
        matches = bf.knnMatch(des1, des2, k=2)
        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.40*n.distance:
                good.append([m])

        print(str(i+j) + "/" + str(total),
              template_image, main_image, len(good))

        if len(good) != 0:
            list_kp1 = [kp1[mat[0].queryIdx].pt for mat in good]
            list_kp2 = [kp2[mat[0].trainIdx].pt for mat in good]
            w, h, _ = img1.shape
            min_x = int((min([i[0] for i in list_kp2]) +
                         max([i[0] for i in list_kp2]))/2 - w/2)
            min_y = int((min([i[1] for i in list_kp2]) +
                         max([i[1] for i in list_kp2]))/2 - h/2)
            max_x = min_x+w
            max_y = min_y+h

            n_img = cv.rectangle(img2, (min_x, min_y),
                                 (max_x, max_y), (255, 0, 0))
            img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good,
                                     None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            cv.imwrite("results/im-" + str(i) + ".jpg", img3)

            # if main_image in data:
            #     data[main_image].append(
            #         [template_image, [min_x, min_y, max_x, max_y]])
            # else:
            #     data[main_image] = [
            #         [template_image, [min_x, min_y, max_x, max_y]]]
            # added = True

            # with open("result.json", "w") as write_file:
            #     json.dump(data, write_file)
        i += 1
    # if not added:
    #     data['NA'].append([template_image, []])

    # with open("result.json", "w") as write_file:
    #     json.dump(data, write_file)
    # j += 1
    # cv.imwrite("results/" + str(i) + ".jpg", n_img)

    # os.rename('./dataset/crops/' + template_image,
    #           './matches/' + template_image)
    # os.rename('./dataset/images/' + main_image,
    #           './matches/' + main_image)
    # i += 1
    # cv.waitKey(0)
    # cv.drawMatchesKnn expects list of lists as matches.
    # img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good,
    #                          None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    # cv.imwrite("results/im-" + str(i) + ".jpg", img3)
    # os.remove('./dataset/crops/' + template_image)
    # plt.imshow(img3), plt.show()
