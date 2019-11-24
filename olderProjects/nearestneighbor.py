
# Author: Matthew Jacobsen
# Date Developed: 4/18/2015
# Purpose: The purpose of this nearest neighbor program is to parse a list
# of cartesian coordinates (x, y, and z) and sort them in "relative" order. 
# First a reference point is established (the point furthest from 0,0,0). 
# Second, a maximum distance from the reference point to the farthest neighbor
# is established. A loop is initiated, comparing each point in the list to 
# the reference point - if the point is closer to the reference point than 
# the previous point compared, it is considered the next closest point. Once 
# the absolute closest point is established, it is added to the sorted dataset
# and set as the next reference point. This continues until the entire list 
# has been sorted. 
import math as m
import pandas
import matplotlib.pyplot as mp
import numpy as np

class NearestNeighbor:
	#Read in the target data set of unordered coordinates
	def __init__(self):
		self.data = pandas.read_csv(
		'C:\Users\Matt\Google Drive\pythonstuff\Test3Ddata.csv', header=None) 
		#Convert the dataframe to matrix for ease of operation.
		self.newdata = self.data.as_matrix()
		#Create empty dictionary to add sorted entries to.
		self.sorteddata={}
	#Establish newpoint(scoping prevents initializing in the loop).
	newpoint = 0

	def referencePoint(self):
		#Find the point farthest from 0,0,0 to use as starting/reference point.
		#Set the greatest distance from 0,0,0 to 0 so that the loop will check 
		##all other points.
		farthestdistance = 0
		#Loop through the entire data set to find the point farthest from 0,0,0.
		for i in self.newdata:
			#Use Euclidean distance formula to calculate the distance between 
			##the current point(i) and 0,0,0.
			distance = m.sqrt(m.pow(abs(i[1]), 2) + m.pow(abs(i[2]), 2) + 
			m.pow(abs(i[3]), 2))
			#Check the distance of i against the current farthest point - if 
			##greater, reset the farthest point to i.
			if distance > farthestdistance:
				farthestdistance = distance
				farthestpoint = i
		#Update the sorted dictionary of points with the farthest point - this 
		##is the starting point for the remainder of this program.
		self.sorteddata[1]=[farthestpoint[0],farthestpoint[1],farthestpoint[2],
		farthestpoint[3]]
		return farthestpoint
		
	def farthestNeighbor(self):
		#Find the point farthest from the starting point to compare to all other 
		##points to determine the next closest neighbor.
		startingpoint = self.referencePoint()
		#Set initial farthest distance to 0, so that all other points will be
		##compared.
		farthestdistance = 0
		#Loop through all points to find the farthest point from the starting/
		##reference point.
		for i in self.newdata:
			#Ensure the starting point is not compared to itself.
			if i[0] != startingpoint[0]:
				#More Euclidian distance...
				distance = m.sqrt(m.pow(abs(i[1]-startingpoint[1]), 2) + m.pow(
				abs(i[2]-startingpoint[2]), 2) + m.pow(abs(i[3]-
				startingpoint[3]), 2))
				#Check the distance of the current point, if it is further from 
				##the starting point than the current farthest distance, then 
				##reset the farthest distance.
				if distance > farthestdistance:
					farthestdistance = distance
					farthestpoint = i
		#return both the coordinates of the farthest point, and the distance 
		##from the point of reference.
		return (farthestpoint, farthestdistance)

	def nearestSorter(self):
		#Determine the starting point to begin comparisons.
		currentpoint = self.referencePoint()
		#Initialize a counter variable.
		a=1
		#The loop needs to run n (n=length of the matrix) number of times to 
		##ensure each point is compared and placed.
		while a < (len(self.newdata)+1):
			#Establish the farthest point and distance to compare all other 
			##points against.
			farthestpoint, nearestdistance = self.farthestNeighbor()
			#Loop through all points and find the one nearest the current point.
			for i in self.newdata:
				#Ensure that i is not the current point and hasn't already been
				##sorted.
				if i[0] != currentpoint[0] and i[0] not in self.sorteddata:
					#More Euclidian distance...
					distance = m.sqrt(m.pow(abs(i[1]-currentpoint[1]), 2) + 
					m.pow(abs(i[2]-currentpoint[2]), 2) + m.pow(abs(i[3]-
					currentpoint[3]), 2))
					#If the distance of i is less than the current closest 
					##point, reset the closet point to i and set the closest 
					##distance to that between i and current point.
					if distance < nearestdistance:
						nearestdistance = distance
						nearestpoint = i
			#After the closest point has been determined, add it to the sorted
			##dictionary.
			self.sorteddata[a+1]=[nearestpoint[0],nearestpoint[1],
			nearestpoint[2],nearestpoint[3]]
			#Set the current point to the point that was closest to the previous
			##current point.
			currentpoint=nearestpoint
			#Increment the counter.
			a+=1
	def printPoints(self):
		print(self.sorteddata)

newsort = NearestNeighbor()	
newsort.nearestSorter()
newsort.printPoints()