import numpy as np
import matplotlib.pyplot as plt
import math
import statistics


# question 1
# data_1 = np.array([19, 24, 12, 19, 18, 24, 8, 5, 9, 20, 13, 11, 1,
#                    12, 11, 10, 22, 21, 7, 16, 15, 15, 26, 16, 1, 13, 21, 21, 20, 19])

# data_2 = np.array([17, 24, 21, 22, 26, 22, 19, 21, 23, 11, 19, 14, 23,
#                    25, 26, 15, 17, 26, 21, 18, 19, 21, 24, 18, 16, 20, 21, 20, 23, 33])

# data_3 = np.array([56, 52, 13, 34, 33, 18, 44, 41, 48, 75, 24, 19, 35,
#                    27, 46, 62, 71, 24, 66, 94, 40, 18, 15, 39, 53, 23, 41, 78, 15, 35])

# fig, axs = plt.subplots(1, 3, sharey=True)

# axs[0].hist(data_1)
# axs[1].hist(data_2)
# axs[2].hist(data_3)


# #graph1 = left-skewed
# #graph2 = semetric
# #graph3 = right-skewed

# mean_1 = np.mean(data_1)
# mean_2 = np.mean(data_2)
# mean_3 = np.mean(data_3)
# print("Mean for data set 1 = ", mean_1)
# print("Mean for data set 2 = ", mean_2)
# print("Mean for data set 3 = ", mean_3)

# median_1 = np.median(data_1)
# median_2 = np.median(data_2)
# median_3 = np.median(data_3)

# print("Median for data set 1 = ", median_1)
# print("Median for data set 2 = ", median_2)
# print("Median for data set 3 = ", median_3)


# question 2

# def checklowerOutlier(data_set, IQR, Q1):
#     for data in data_set:
#         if(data <= (Q1 - (1.5*IQR))):
#             data_set = np.delete(data_set, np.where(data_set == data))

#     return data_set


# def checkupperOutlier(data_set, IQR, Q3):
#     for data in data_set:
#         if(data >= (Q3 + (1.5*IQR))):
#             data_set = np.delete(data_set, np.where(data_set == data))

#     return data_set


# data_set = np.array([43, 37, 50, 51, 58, 105, 52, 45, 45, 10])
# mean = round(np.mean(data_set), 2)
# median = round(np.median(data_set), 2)
# sd = round(np.std(data_set), 2)
# firstquartile = np.percentile(data_set, 25, interpolation='lower')
# thirdquartile = np.percentile(data_set, 75, interpolation='higher')
# # secondquartile = np.percentile(data_set, 50, interpolation='midpoint')
# IQR = thirdquartile-firstquartile

# print("mean =", mean)
# print("median =", median)
# print("standard deviation =", sd)
# print("first quartile =", firstquartile)
# print("third quartile =", thirdquartile)
# # print("second quartile =", secondquartile)
# print("Interquartile range =", IQR)

# data_set = checklowerOutlier(data_set, IQR, firstquartile)
# data_set = checkupperOutlier(data_set, IQR, thirdquartile)
# print(data_set)  # after remove outlier

# mean_2 = round(np.mean(data_set), 2)
# median_2 = round(np.median(data_set), 2)
# sd_2 = round(np.std(data_set), 2)
# firstquartile_2 = np.percentile(data_set, 25, interpolation='lower')
# thirdquartile_2 = np.percentile(data_set, 75, interpolation='higher')

# print("mean =", mean_2)
# print("median =", median_2)
# print("standard deviation =", sd_2)
# print("first quartile =", firstquartile_2)
# print("third quartile =", thirdquartile_2)

# # conclusion: mean and standard deviation affected


# question 3
