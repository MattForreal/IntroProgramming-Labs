# Program to calculate how long it takes a photo from Curiosity to reach Nasa
# Speed of light = 186,000 miles per second
# Mars distance from earth = 34,000,000 miles

s = 186000
m = 34000000

t = int(m/s)

print("It would take roughly " + str(t) + " seconds for a photo to reach",
      "NASA from Mars at its closest orbit to Earth.")
