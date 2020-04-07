import sys

class Noise:
    def __init__(self, x, y):

        # The below array holds values from 0 - 255 (inclusively) randomly scattered about
        # However, there are 510 elements in total with each value from 0 - 255 being repeated twice
        # Note that there will be a slightly biased output since the max index possible to reach is 510 and not 511 (Meaning that 1 value from 0 - 255 is not "reapeated twice")
        # This bias is really just negligible
        p = [151, 160, 137, 91, 90, 15,
             131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23,
             190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33,
             88, 237, 149, 56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166,
             77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244,
             102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196,
             135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123,
             5, 202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
             223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9,
             129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228,
             251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249, 14, 239, 107,
             49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254,
             138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180,
             51, 160, 137, 91, 90, 15,
             131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23,
             190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33,
             88, 237, 149, 56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166,
             77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244,
             102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196,
             135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123,
             5, 202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
             223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9,
             129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228,
             251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249, 14, 239, 107,
             49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254,
             138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180
]
        vectors = [[1,1],[-1,1],[-1,-1],[1,-1]]  # All possible gradient vector options

        # Note that:
        # 1 = Top-left
        # 2 = Top-right
        # 3 = Bottom-left
        # 4 = Bottom-right

        # Find the top-left coordinate of the unit square
        xi = int(x) & 255
        yi = int(y) & 255

        # Generate a pseudo-random values for each of the 4 points of the unit square
        # (Used later to find the gradient vectors of the 4 points)
        # Note that generating these values do not require a set formula
        # However, the formula must account for the 4 points on the unit square
        # NOTE THAT INDEXING RANGE FOR "p" array RANGES FROM 0 - 510 (Not 511)
        q1 = p[p[xi] + p[yi]]
        q2 = p[p[xi + 1] + p[yi]]
        q3 = p[p[xi] + p[yi + 1]]
        q4 = p[p[xi + 1] + p[yi + 1]]

        '''
        There are examples of cases with wrong formulas. The below example is one of those since it forms symmetry along
        y = -x. 
                
        q1 = p[xi + yi]
        q2 = p[xi + 1 + yi]
        q3 = p[xi + yi + 1]
        q4 = p[xi + 1 + yi + 1]
        
        ############### The reason can be explained by: #####################
        Let "q" be the sum of xi + yi
        Say "q" = 10 
        There are "symmetrical" answers to get to "q" with:
            xi, yi = 1, 9
            xy, yi = 9, 1
            xi, yi = 3, 7
            xi, yi = 7, 3
            xi, yi = 5, 5
        
        These symmetrical solutions are responsible for creating symmetrical and geometric shape (Both of which are undesirable) of the noise
        '''

        # Find the gradient vector using the "q" values
        # In this case, we use the "vectors" array and just index from it
        g1 = vectors[q1 % len(vectors)]
        g2 = vectors[q2 % len(vectors)]
        g3 = vectors[q3 % len(vectors)]
        g4 = vectors[q4 % len(vectors)]

        # Find the distance vectors from the 4 points on the unit square to the input coordinate
        d1 = x % 1, y % 1
        d2 = x % 1 - 1, y % 1
        d3 = x % 1, y % 1 - 1
        d4 = x % 1 - 1, y % 1 - 1

        # Calculate the dot product between the distance and gradient vectors of each point on the unit square
        dx = x - int(x)  # Find the displacement from top left corner of unit circle to the input coordinate (x)
        dy = y - int(y)  # Find the displacement from top left corner of unit circle to the input coordinate (y)
        v1 = self.dot_product(g1[0], g1[1], d1[0], d1[1])
        v2 = self.dot_product(g2[0], g2[1], d2[0], d2[1])
        v3 = self.dot_product(g3[0], g3[1], d3[0], d3[1])
        v4 = self.dot_product(g4[0], g4[1], d4[0], d4[1])

        # Interpolate/predict the value of the input co-ordinate (from -1 to 1)
        # Also perform the fade function
        # The reason we perform fade on dx and dy is due to the inaccuracies of linear interpolation
        # This inaccuracy forms rigidness in the output
        # A fade function clumps up inputs to be closer towards the midpoint
        # This way, we bascially are cheesing the inaccuracy of linear interpolation by squeezing all of the inputs closer to one another
        # So, while the outputs might be inaccurate, all of the outputs are more packed to give off the illusion of smoothness
        dx = self.fade(dx)
        dy = self.fade(dy)
        final_val_x1 = self.lerp(dx, v1, v2)
        final_val_x2 = self.lerp(dx, v3, v4)
        final_val_y = self.lerp(dy, final_val_x1, final_val_x2)
        self.final_val = final_val_y

    def return_val(self):
        return self.final_val

    def dot_product(self, x1, y1, x2, y2):  # Output between -1 to 1
        # The dot product is used to connect the gradient and distance vectors
        # It conveniently return a single value which is later used to find the color of the input coordinate
        return x1 * x2 + y1 * y2

    def lerp(self, amt, left, right):  # A.K.A Interpolate
        # The interpolation is needed to find the final output of the value for the input coordinate
        # "Interpolation" in other words, is an "averaging" technique since all we know is the values for the 4 points on
        # Quick bu inaccurate
        return (right - left) * amt + left

    def fade(self, t):  # Fade function to smooth out rigidness
        return 6 * t ** 5-15 * t ** 4+10 * t ** 3
