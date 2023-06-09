# chaos_based_cryptography
<br>
It's an cryptographic technique for surely transfering images over internet or storing images on clouds etc.
<br>
<br>
Its an 3-steps procedure to encrypt your image :<br>
1. selecting a chaotic map <br>
2. confusion of image <br>
3. diffusion of image <br>
<br>
first we select the chaotic map & generate a key-array which is equal to the total number of pixels we have in the image. Now keep it aside.
<br><br>
move to the second-step which is shuffling the image. since we are using an RGB-image, therefore it has 3D-matrix. so we first convert the 3D-matrix into 1D. Now apply the python function to randomize the indices of the 1D-array. Due to which the image get shuffled. then bring back to 3D-matrix & print it out
<br><br>
move to the third-step which is diffusion. For diffusion do XOR operation with key-array elements & pixels of the image. Due to which the pixel-intensity spread across the image. nobody can guess the real image.
<br><br>
for decryption again do XOR with the encrypted image and then convert to 1D-array & sort the indices. covert 1D-array to 3D-matrix.
<br>
> here matrix == array
<br><br>

https://github.com/parth721/visual_cryptography/assets/112557191/d019b4ea-033a-47cf-b98d-c27d395a1b2e

