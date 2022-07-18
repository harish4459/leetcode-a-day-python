An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About



Solution -

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        #change the adjacent pixel that have the same color as starting pixel
        R, C = len(image), len(image[0])
        color = image[sr][sc] #old color 
        
        if color == newcolor:
            return image
        
        
        def dfs(r, c):

            
            if image[r][c] != color or image[r][c] == newcolor: 
            #case when the adjacent pixel doesnt have the same color as starting pixel or adjacent pixel is already of the new color, no change
                return
            image[r][c] = newcolor #
            
            if r >= 1: dfs(r-1,c)
            if r+1 < R: dfs(r+1,c)
            if c >= 1: dfs(r,c-1)
            if c+1 < C: dfs(r,c+1)
        dfs(sr,sc)
        return image
        
#time complexity - O(n) #worst case we change the color of all the pixels adjacent
#space complexity - O(n) #the size of the implicit call stack when calling dfs.
